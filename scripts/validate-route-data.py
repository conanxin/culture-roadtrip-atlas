#!/usr/bin/env python3
"""
validate-route-data.py · 行旅图谱 · 路线数据校验脚本

校验 data/routes/<route-slug>.{csv,geojson,gpx} 三种数据格式的一致性与字段完整性。
只用 Python 标准库。支持任意路线 slug,以及 --all 遍历 manifest 全部路线。

Usage:
    python3 scripts/validate-route-data.py                 # 默认校验 OEDW
    python3 scripts/validate-route-data.py <route-slug>   # 自定义 slug
    python3 scripts/validate-route-data.py --all          # 遍历 manifest 所有路线
    python3 scripts/validate-route-data.py --help

退出码:
    0  PASS / ALL PASS
    1  FAIL

校验内容:
    CSV: 行数 / 必需字段 / segment_id 覆盖 / 经纬度可解析 / 字段取值合法
    GeoJSON: FeatureCollection / is_original_gps_track=false / Point 数量 = CSV 行数 /
             LineString 数量 >= 1 / disclaimer 文本包含 "not for navigation"
    GPX: 标准 XML / root 是 gpx / 文本包含必要声明 / waypoint 数量 == CSV 行数（粗略）

路线级别阈值:
    OEDW (out-of-eden-walk-china): CSV >= 35 行 / S01-S10 覆盖 / GeoJSON lines >= 11
    liao-tower-roadtrip:           CSV >= 15 行 / S01-S09 覆盖 / GeoJSON lines >= 1
    其他路线:                      CSV >= 5 行  / 至少一个 Sxx 段    / GeoJSON lines >= 1

历史:
    v1.1 · 2026-07-05 · Phase 7 · 增强 --all / 路线级别阈值 / 通用化校验
    v1.0 · 2026-07-04 · Phase 5 · 固化 Phase 5 临时校验逻辑
"""

import argparse
import csv
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


# ---------- 字段取值合法集合 ----------

ALLOWED_SOURCE_LEVEL = {
    "A_official_oedw",
    "B_partner_or_education",
    "C_chinese_media",
    "D_reconstructed_for_travel",
    "E_project_internal",
}

ALLOWED_REPLICATION_FEASIBILITY = {
    "high",
    "medium",
    "low",
    "not_recommended",
    "reading_only",
}

ALLOWED_COORDINATE_PRECISION = {
    "city",
    "landmark",
    "region",
    "approximate",
    "unknown",
}

ALLOWED_DIFFICULTY = {
    "easy",
    "medium",
    "hard",
    "extreme",
    "mixed",
    "n/a",
}

REQUIRED_CSV_FIELDS = {
    "id",
    "sequence",
    "segment_id",
    "segment_name",
    "point_name",
    "province",
    "city_or_area",
    "latitude",
    "longitude",
    "coordinate_precision",
    "source_level",
    "replication_feasibility",
    "difficulty",
    "best_season",
    "transport_hint",
    "risk_note",
    "source_note",
    "url",
}


# ---------- 路线级别阈值 ----------

ROUTE_THRESHOLDS = {
    "out-of-eden-walk-china": {
        "min_csv_rows": 35,
        "min_segments": 10,
        "max_segments": 10,
        "segment_pattern": "S{:02d}",
        "min_geojson_lines": 11,
    },
    "liao-tower-roadtrip": {
        "min_csv_rows": 15,
        "min_segments": 9,
        "max_segments": 9,
        "segment_pattern": "S{:02d}",
        "min_geojson_lines": 1,
    },
}

DEFAULT_THRESHOLDS = {
    "min_csv_rows": 5,
    "min_segments": 1,
    "max_segments": 99,
    "segment_pattern": "S{:02d}",
    "min_geojson_lines": 1,
}


def get_thresholds(slug: str) -> dict:
    """根据 slug 返回校验阈值,未知路线使用 default。"""
    return ROUTE_THRESHOLDS.get(slug, DEFAULT_THRESHOLDS)


# ---------- 校验函数 ----------


def validate_csv(csv_path: Path, thresholds: dict) -> tuple[bool, list[str], list[dict]]:
    """校验 CSV 文件。返回 (passed, errors, rows)."""
    errors: list[str] = []
    rows: list[dict] = []

    if not csv_path.exists():
        errors.append(f"CSV 文件不存在: {csv_path}")
        return False, errors, rows

    with csv_path.open(newline="", encoding="utf-8") as f:
        try:
            rows = list(csv.DictReader(f))
        except Exception as e:
            errors.append(f"CSV 解析失败: {e}")
            return False, errors, rows

    if len(rows) < thresholds["min_csv_rows"]:
        errors.append(f"CSV 行数过少: {len(rows)} (要求 ≥ {thresholds['min_csv_rows']})")

    if rows:
        missing = REQUIRED_CSV_FIELDS - set(rows[0].keys())
        if missing:
            errors.append(f"CSV 缺少必需字段: {missing}")

        for i, r in enumerate(rows, start=1):
            # segment_id 必须以 S 开头
            if not r.get("segment_id", "").startswith("S"):
                errors.append(f"行 {i} segment_id 不合法: {r.get('segment_id')!r}")
            # 经纬度必须可解析
            try:
                float(r.get("latitude", ""))
                float(r.get("longitude", ""))
            except (ValueError, TypeError):
                errors.append(f"行 {i} 经纬度无法解析: {r.get('latitude')}, {r.get('longitude')}")
            # 字段取值合法性
            sl = r.get("source_level", "")
            if sl and sl not in ALLOWED_SOURCE_LEVEL:
                errors.append(f"行 {i} source_level 非法: {sl!r}")
            rf = r.get("replication_feasibility", "")
            if rf and rf not in ALLOWED_REPLICATION_FEASIBILITY:
                errors.append(f"行 {i} replication_feasibility 非法: {rf!r}")
            cp = r.get("coordinate_precision", "")
            if cp and cp not in ALLOWED_COORDINATE_PRECISION:
                errors.append(f"行 {i} coordinate_precision 非法: {cp!r}")
            diff = r.get("difficulty", "")
            if diff and diff not in ALLOWED_DIFFICULTY:
                errors.append(f"行 {i} difficulty 非法: {diff!r}")

    # 段覆盖检查
    seg_ids = sorted({r.get("segment_id", "") for r in rows if r.get("segment_id")})
    if seg_ids:
        try:
            seg_nums = sorted({int(s[1:]) for s in seg_ids if s[1:].isdigit()})
        except Exception:
            seg_nums = []
        if thresholds["min_segments"] == thresholds["max_segments"]:
            expected = list(range(1, thresholds["min_segments"] + 1))
            missing_segs = [n for n in expected if n not in seg_nums]
            if missing_segs:
                seg_pattern = thresholds["segment_pattern"]
                seg_names = [seg_pattern.format(n) for n in missing_segs]
                errors.append(
                    f"段覆盖不完整: 缺少 {seg_names} (现有: {seg_ids})"
                )

    passed = len(errors) == 0
    return passed, errors, rows


def validate_geojson(geo_path: Path, csv_rows: list[dict], thresholds: dict) -> tuple[bool, list[str], dict]:
    """校验 GeoJSON 文件。返回 (passed, errors, geojson)."""
    errors: list[str] = []
    geo: dict = {}

    if not geo_path.exists():
        errors.append(f"GeoJSON 文件不存在: {geo_path}")
        return False, errors, geo

    try:
        geo = json.loads(geo_path.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"GeoJSON 解析失败: {e}")
        return False, errors, geo

    if geo.get("type") != "FeatureCollection":
        errors.append(f"GeoJSON 顶层 type 必须为 FeatureCollection,实际为 {geo.get('type')!r}")

    metadata = geo.get("metadata", {})
    if metadata.get("is_original_gps_track") is not False:
        errors.append(f"GeoJSON metadata.is_original_gps_track 必须为 false,实际为 {metadata.get('is_original_gps_track')!r}")

    features = geo.get("features", [])
    points = [f for f in features if f.get("geometry", {}).get("type") == "Point"]
    lines = [f for f in features if f.get("geometry", {}).get("type") == "LineString"]

    if len(points) != len(csv_rows):
        errors.append(f"GeoJSON Point 数量 ({len(points)}) 与 CSV 行数 ({len(csv_rows)}) 不一致")

    if len(lines) < thresholds["min_geojson_lines"]:
        errors.append(
            f"GeoJSON LineString 数量 < {thresholds['min_geojson_lines']},实际为 {len(lines)}"
        )

    # LineString properties 应包含 is_original_gps_track: false 和 "not for navigation"
    has_navigation_warning = any(
        "not for navigation" in str(f.get("properties", {})).lower() for f in lines
    )
    if not has_navigation_warning:
        errors.append("GeoJSON LineString properties 缺少 'not for navigation' 警告")

    # Point id 校验
    csv_ids = {r["id"] for r in csv_rows if r.get("id")}
    geo_ids = {f.get("properties", {}).get("id") for f in points}
    missing_ids = csv_ids - geo_ids
    if missing_ids:
        errors.append(
            f"GeoJSON Point 缺少 CSV 中的 id: {sorted(missing_ids)[:5]}"
            f"{'...' if len(missing_ids) > 5 else ''}"
        )

    passed = len(errors) == 0
    return passed, errors, geo


def validate_gpx(gpx_path: Path, csv_rows: list[dict]) -> tuple[bool, list[str], int]:
    """校验 GPX 文件。返回 (passed, errors, waypoint_count)."""
    errors: list[str] = []
    waypoint_count = 0

    if not gpx_path.exists():
        errors.append(f"GPX 文件不存在: {gpx_path}")
        return False, errors, waypoint_count

    try:
        root = ET.parse(gpx_path).getroot()
    except ET.ParseError as e:
        errors.append(f"GPX XML 解析失败: {e}")
        return False, errors, waypoint_count

    if not root.tag.endswith("gpx"):
        errors.append(f"GPX root 标签必须是 gpx,实际为 {root.tag!r}")

    # waypoint 数量粗略匹配（wpt element）
    ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
    wpts = root.findall(".//gpx:wpt", ns) or root.findall(".//{http://www.topografix.com/GPX/1/1}wpt")
    if not wpts:
        # 兼容无命名空间
        wpts = [el for el in root.iter() if el.tag.endswith("wpt")]
    waypoint_count = len(wpts)

    if waypoint_count != len(csv_rows):
        errors.append(f"GPX waypoint 数量 ({waypoint_count}) 与 CSV 行数 ({len(csv_rows)}) 不一致")

    # 文本包含必须关键词（路线无关的通用声明）
    text = gpx_path.read_text(encoding="utf-8").lower()
    required_phrases = [
        "not for navigation",
        "cultural replica",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"GPX 文本缺少必要声明: {phrase!r}")

    passed = len(errors) == 0
    return passed, errors, waypoint_count


# ---------- 验证单条路线 ----------


def validate_route(slug: str, data_dir: Path, verbose: bool = True) -> tuple[bool, dict]:
    """校验单条路线。返回 (passed, summary)."""
    csv_path = data_dir / f"{slug}.csv"
    geo_path = data_dir / f"{slug}.geojson"
    gpx_path = data_dir / f"{slug}.gpx"
    thresholds = get_thresholds(slug)

    csv_passed, csv_errors, csv_rows = validate_csv(csv_path, thresholds)
    geo_passed, geo_errors, geo_data = validate_geojson(geo_path, csv_rows, thresholds)
    gpx_passed, gpx_errors, gpx_count = validate_gpx(gpx_path, csv_rows)

    geo_points = sum(1 for f in geo_data.get("features", []) if f.get("geometry", {}).get("type") == "Point")
    geo_lines = sum(1 for f in geo_data.get("features", []) if f.get("geometry", {}).get("type") == "LineString")
    segments = sorted({r.get("segment_id", "") for r in csv_rows if r.get("segment_id")})

    if verbose:
        print(f"route: {slug}")
        print(f"CSV: {csv_path.name} · {len(csv_rows)} 行 · {'PASS' if csv_passed else 'FAIL'}")
        for e in csv_errors[:5]:
            print(f"  ✗ {e}")
        print(f"GeoJSON: {geo_path.name} · {geo_points} points · {geo_lines} lines · {'PASS' if geo_passed else 'FAIL'}")
        for e in geo_errors[:5]:
            print(f"  ✗ {e}")
        print(f"GPX: {gpx_path.name} · {gpx_count} waypoints · {'PASS' if gpx_passed else 'FAIL'}")
        for e in gpx_errors[:5]:
            print(f"  ✗ {e}")
        print("-" * 50)
        print(f"route: {slug}")
        print(f"csv_rows: {len(csv_rows)}")
        print(f"geojson_points: {geo_points}")
        print(f"geojson_lines: {geo_lines}")
        print(f"gpx_waypoints: {gpx_count}")
        print(f"segments: {'-'.join([segments[0], segments[-1]]) if segments else '(none)'}")
        print()

    all_passed = csv_passed and geo_passed and gpx_passed
    summary = {
        "slug": slug,
        "passed": all_passed,
        "csv_rows": len(csv_rows),
        "geojson_points": geo_points,
        "geojson_lines": geo_lines,
        "gpx_waypoints": gpx_count,
        "segments": segments,
        "csv_passed": csv_passed,
        "geo_passed": geo_passed,
        "gpx_passed": gpx_passed,
        "errors": csv_errors + geo_errors + gpx_errors,
    }
    return all_passed, summary


# ---------- 主函数 ----------


def _is_planned_route(entry: dict) -> bool:
    """planned-data 路线判定。"""
    if entry.get("status") == "planned-data":
        return True
    url_fields = ("csv_url", "geojson_url", "gpx_url", "svg_url")
    return all(entry.get(f) is None for f in url_fields)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="行旅图谱 · 路线数据校验脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python3 scripts/validate-route-data.py
    python3 scripts/validate-route-data.py out-of-eden-walk-china
    python3 scripts/validate-route-data.py liao-tower-roadtrip
    python3 scripts/validate-route-data.py --all
        """,
    )
    parser.add_argument(
        "slug",
        nargs="?",
        default=None,
        help="路线 slug(默认: out-of-eden-walk-china,或与 --all 互斥)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="遍历 manifest 中所有 route slug 逐个验证",
    )
    parser.add_argument(
        "--data-dir",
        default="data/routes",
        help="数据目录(默认: data/routes)",
    )
    parser.add_argument(
        "--manifest",
        default="data/routes/routes-manifest.json",
        help="manifest 路径(默认: data/routes/routes-manifest.json)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="严格模式:任何警告都视为失败",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="输出 JSON 格式结果(适合 CI / 脚本解析)",
    )
    parser.add_argument(
        "--manifest-check",
        action="store_true",
        help="校验 manifest 统计字段与实际数据一致(对已存在数据的路线)",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)

    # --all 模式:遍历 manifest
    if args.all:
        manifest_path = Path(args.manifest)
        if not manifest_path.exists():
            print(f"FAIL: manifest 不存在: {manifest_path}")
            return 1
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"FAIL: manifest 解析失败: {e}")
            return 1
        routes = manifest.get("routes", [])
        if not routes:
            print("FAIL: manifest 中没有 routes")
            return 1

        if not args.json:
            print(f"行旅图谱 · 路线数据校验 (--all 模式)")
            print(f"manifest: {manifest_path}")
            print(f"routes: {len(routes)}")
            print("=" * 50)

        all_passed = True
        summaries = []
        for r in routes:
            slug = r.get("slug")
            if not slug:
                print(f"  ✗ manifest 中 route 缺少 slug: {r}")
                all_passed = False
                continue
            # planned-data 路线:跳过文件校验
            if _is_planned_route(r):
                if not args.json:
                    print(f"  · {slug}: planned-data 跳过文件校验")
                continue
            passed, summary = validate_route(slug, data_dir, verbose=not args.json)
            summaries.append(summary)
            if not passed:
                all_passed = False

        # --manifest-check:对照 manifest 统计字段
        manifest_errors: list[str] = []
        if args.manifest_check:
            from collections import defaultdict
            for r in routes:
                slug = r.get("slug")
                if not slug or _is_planned_route(r):
                    continue
                csv_path = data_dir / f"{slug}.csv"
                if not csv_path.exists():
                    continue
                # 重新统计
                with csv_path.open(newline="", encoding="utf-8") as f:
                    rows = list(csv.DictReader(f))
                geo_path = data_dir / f"{slug}.geojson"
                geo_stats = {"features": 0, "points": 0, "lines": 0}
                if geo_path.exists():
                    try:
                        geo = json.loads(geo_path.read_text(encoding="utf-8"))
                        feats = geo.get("features", [])
                        geo_stats["features"] = len(feats)
                        geo_stats["points"] = sum(1 for f in feats if f.get("geometry", {}).get("type") == "Point")
                        geo_stats["lines"] = sum(1 for f in feats if f.get("geometry", {}).get("type") == "LineString")
                    except Exception:
                        pass
                gpx_path = data_dir / f"{slug}.gpx"
                gpx_count = 0
                if gpx_path.exists():
                    try:
                        ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
                        root = ET.parse(gpx_path).getroot()
                        wpts = root.findall(".//gpx:wpt", ns)
                        if not wpts:
                            wpts = [el for el in root.iter() if el.tag.endswith("wpt")]
                        gpx_count = len(wpts)
                    except Exception:
                        pass
                seg_ids = sorted({row.get("segment_id", "") for row in rows if row.get("segment_id")})
                # 校验
                for key, actual in [
                    ("points", len(rows)),
                    ("segments", len(seg_ids)),
                    ("geojson_features", geo_stats["features"]),
                    ("geojson_points", geo_stats["points"]),
                    ("geojson_lines", geo_stats["lines"]),
                    ("gpx_waypoints", gpx_count),
                ]:
                    expected = r.get(key)
                    if expected is None:
                        manifest_errors.append(f"{slug}: manifest 缺少字段 {key}")
                    elif expected != actual:
                        manifest_errors.append(
                            f"{slug}.{key}: manifest={expected} 实际={actual} 不一致"
                        )

        if args.json:
            payload = {
                "status": "PASS" if (all_passed and not manifest_errors) else "FAIL",
                "routes": summaries,
            }
            if args.manifest_check:
                payload["manifest_errors"] = manifest_errors
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 0 if (all_passed and not manifest_errors) else 1

        print("=" * 50)
        if all_passed and not manifest_errors:
            print(f"PASS all route data validation")
            if args.manifest_check:
                print("manifest matches generated statistics")
            print(f"routes: {len(summaries)}")
            return 0
        else:
            print(f"FAIL all route data validation")
            failed = [s["slug"] for s in summaries if not s["passed"]]
            if failed:
                print(f"data failed: {failed}")
            for e in manifest_errors:
                print(f"  ✗ {e}")
            return 1

    # 单路线模式
    slug = args.slug or "out-of-eden-walk-china"

    if not args.json:
        print(f"行旅图谱 · 路线数据校验")
        print(f"route: {slug}")
        print(f"data dir: {data_dir}")
        print("-" * 50)

    passed, summary = validate_route(slug, data_dir, verbose=not args.json)
    if args.json:
        payload = {
            "status": "PASS" if passed else "FAIL",
            "routes": [summary],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0 if passed else 1

    if passed:
        print("PASS route data validation")
        return 0
    else:
        print("FAIL route data validation")
        return 1


if __name__ == "__main__":
    sys.exit(main())
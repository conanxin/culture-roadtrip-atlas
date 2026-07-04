#!/usr/bin/env python3
"""
validate-route-data.py · 行旅图谱 · 路线数据校验脚本

校验 data/routes/<route-slug>.{csv,geojson,gpx} 三种数据格式的一致性与字段完整性。
只用 Python 标准库。可通过命令行参数传入其他 route slug。

Usage:
    python3 scripts/validate-route-data.py                 # 默认校验 OEDW
    python3 scripts/validate-route-data.py <route-slug>   # 自定义 slug
    python3 scripts/validate-route-data.py --help

退出码:
    0  PASS
    1  FAIL

校验内容:
    CSV: 行数 / 必需字段 / segment_id 覆盖 / 经纬度可解析 / 字段取值合法
    GeoJSON: FeatureCollection / is_original_gps_track=false / Point 数量 = CSV 行数 /
             LineString 数量 >= 1 / disclaimer 文本包含 "not for navigation"
    GPX: 标准 XML / root 是 gpx / 文本包含 "not Paul Salopek" + "not for navigation" +
         "cultural replica" / waypoint 数量 == CSV 行数（粗略）

历史:
    v1.0 · 2026-07-04 · 固化 Phase 5 临时校验逻辑
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


# ---------- 校验函数 ----------


def validate_csv(csv_path: Path) -> tuple[bool, list[str], list[dict]]:
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

    if len(rows) < 35:
        errors.append(f"CSV 行数过少: {len(rows)} (要求 ≥ 35)")

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

    passed = len(errors) == 0
    return passed, errors, rows


def validate_geojson(geo_path: Path, csv_rows: list[dict]) -> tuple[bool, list[str], dict]:
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
        errors.append(f"GeoJSON 顶层 type 必须为 FeatureCollection，实际为 {geo.get('type')!r}")

    metadata = geo.get("metadata", {})
    if metadata.get("is_original_gps_track") is not False:
        errors.append(f"GeoJSON metadata.is_original_gps_track 必须为 false，实际为 {metadata.get('is_original_gps_track')!r}")

    features = geo.get("features", [])
    points = [f for f in features if f.get("geometry", {}).get("type") == "Point"]
    lines = [f for f in features if f.get("geometry", {}).get("type") == "LineString"]

    if len(points) != len(csv_rows):
        errors.append(f"GeoJSON Point 数量 ({len(points)}) 与 CSV 行数 ({len(csv_rows)}) 不一致")

    if len(lines) < 1:
        errors.append(f"GeoJSON LineString 数量 < 1，实际为 {len(lines)}")

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
        errors.append(f"GeoJSON Point 缺少 CSV 中的 id: {sorted(missing_ids)[:5]}{'...' if len(missing_ids) > 5 else ''}")

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
        errors.append(f"GPX root 标签必须是 gpx，实际为 {root.tag!r}")

    # waypoint 数量粗略匹配（wpt element）
    ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
    wpts = root.findall(".//gpx:wpt", ns) or root.findall(".//{http://www.topografix.com/GPX/1/1}wpt")
    if not wpts:
        # 兼容无命名空间
        wpts = [el for el in root.iter() if el.tag.endswith("wpt")]
    waypoint_count = len(wpts)

    if waypoint_count != len(csv_rows):
        errors.append(f"GPX waypoint 数量 ({waypoint_count}) 与 CSV 行数 ({len(csv_rows)}) 不一致")

    # 文本包含必须关键词
    text = gpx_path.read_text(encoding="utf-8").lower()
    required_phrases = [
        "not paul salopek",
        "not for navigation",
        "cultural replica",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"GPX 文本缺少必要声明: {phrase!r}")

    passed = len(errors) == 0
    return passed, errors, waypoint_count


# ---------- 主函数 ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="行旅图谱 · 路线数据校验脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python3 scripts/validate-route-data.py
    python3 scripts/validate-route-data.py out-of-eden-walk-china
        """,
    )
    parser.add_argument(
        "slug",
        nargs="?",
        default="out-of-eden-walk-china",
        help="路线 slug（默认: out-of-eden-walk-china）",
    )
    parser.add_argument(
        "--data-dir",
        default="data/routes",
        help="数据目录（默认: data/routes）",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="严格模式：任何警告都视为失败",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    csv_path = data_dir / f"{args.slug}.csv"
    geo_path = data_dir / f"{args.slug}.geojson"
    gpx_path = data_dir / f"{args.slug}.gpx"

    print(f"行旅图谱 · 路线数据校验")
    print(f"route: {args.slug}")
    print(f"data dir: {data_dir}")
    print("-" * 50)

    # CSV
    csv_passed, csv_errors, csv_rows = validate_csv(csv_path)
    print(f"CSV: {csv_path.name} · {len(csv_rows)} 行 · {'PASS' if csv_passed else 'FAIL'}")
    for e in csv_errors[:5]:
        print(f"  ✗ {e}")

    # GeoJSON
    geo_passed, geo_errors, geo_data = validate_geojson(geo_path, csv_rows)
    geo_points = sum(1 for f in geo_data.get("features", []) if f.get("geometry", {}).get("type") == "Point")
    geo_lines = sum(1 for f in geo_data.get("features", []) if f.get("geometry", {}).get("type") == "LineString")
    print(f"GeoJSON: {geo_path.name} · {geo_points} points · {geo_lines} lines · {'PASS' if geo_passed else 'FAIL'}")
    for e in geo_errors[:5]:
        print(f"  ✗ {e}")

    # GPX
    gpx_passed, gpx_errors, gpx_count = validate_gpx(gpx_path, csv_rows)
    print(f"GPX: {gpx_path.name} · {gpx_count} waypoints · {'PASS' if gpx_passed else 'FAIL'}")
    for e in gpx_errors[:5]:
        print(f"  ✗ {e}")

    # 段覆盖统计
    segments = sorted({r.get("segment_id", "") for r in csv_rows if r.get("segment_id")})

    print("-" * 50)
    print(f"route: {args.slug}")
    print(f"csv_rows: {len(csv_rows)}")
    print(f"geojson_points: {geo_points}")
    print(f"geojson_lines: {geo_lines}")
    print(f"gpx_waypoints: {gpx_count}")
    print(f"segments: {', '.join(segments)}")

    all_passed = csv_passed and geo_passed and gpx_passed
    if all_passed:
        print()
        print("PASS route data validation")
        return 0
    else:
        print()
        print("FAIL route data validation")
        return 1


if __name__ == "__main__":
    sys.exit(main())
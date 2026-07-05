#!/usr/bin/env python3
"""
build-route-assets.py · 行旅图谱 · 路线工厂入口

把"路线数据校验 + SVG 生成 + manifest 统计同步"做成一条命令。
只用 Python 标准库。通过 subprocess 复用 validate-route-data.py 与 render-route-map-svg.py 的逻辑,
保持单文件职责清晰、依赖最小。

Usage:
    python3 scripts/build-route-assets.py                  # 同 --all
    python3 scripts/build-route-assets.py --all
    python3 scripts/build-route-assets.py <route-slug>     # 单条路线
    python3 scripts/build-route-assets.py --check          # CI 用 · 不回写不生成

退出码:
    0  PASS / all routes pass
    1  FAIL

输出示例 (build):
    PASS route factory build
    routes: 2
    - out-of-eden-walk-china: 42 points, 53 features, 42 waypoints, 10 segments, svg ok
    - liao-tower-roadtrip: 20 points, 30 features, 20 waypoints, 9 segments, svg ok
    manifest updated: data/routes/routes-manifest.json

输出示例 (--check):
    PASS route factory check
    manifest matches generated statistics
    routes: 2

历史:
    v1.0 · 2026-07-05 · Phase 8 首版 · 路线工厂入口
"""

import argparse
import csv
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Any


# ---------- 数据统计 ----------


def count_csv_points(csv_path: Path) -> int:
    """统计 CSV 数据行数(不含表头)。"""
    if not csv_path.exists():
        return 0
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return sum(1 for _ in reader)


def count_geojson_stats(geo_path: Path) -> dict:
    """统计 GeoJSON features / points / lines / segments。"""
    if not geo_path.exists():
        return {"features": 0, "points": 0, "lines": 0, "segments": 0}
    try:
        geo = json.loads(geo_path.read_text(encoding="utf-8"))
    except Exception:
        return {"features": 0, "points": 0, "lines": 0, "segments": 0}
    features = geo.get("features", [])
    points = sum(1 for f in features if f.get("geometry", {}).get("type") == "Point")
    lines = sum(1 for f in features if f.get("geometry", {}).get("type") == "LineString")
    seg_ids = sorted({
        f.get("properties", {}).get("segment_id", "")
        for f in features
        if f.get("geometry", {}).get("type") == "Point"
        and f.get("properties", {}).get("segment_id")
    })
    return {
        "features": len(features),
        "points": points,
        "lines": lines,
        "segments": len(seg_ids),
    }


def count_gpx_waypoints(gpx_path: Path) -> int:
    """统计 GPX waypoint 数量。"""
    if not gpx_path.exists():
        return 0
    try:
        root = ET.parse(gpx_path).getroot()
    except Exception:
        return 0
    ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
    wpts = root.findall(".//gpx:wpt", ns)
    if not wpts:
        wpts = [el for el in root.iter() if el.tag.endswith("wpt")]
    return len(wpts)


def collect_route_stats(slug: str, data_dir: Path, img_dir: Path) -> dict:
    """为单条路线收集统计信息。"""
    csv_path = data_dir / f"{slug}.csv"
    geo_path = data_dir / f"{slug}.geojson"
    gpx_path = data_dir / f"{slug}.gpx"
    svg_path = img_dir / f"{slug}-map.svg"

    csv_rows = count_csv_points(csv_path)
    geo_stats = count_geojson_stats(geo_path)
    gpx_waypoints = count_gpx_waypoints(gpx_path)
    has_svg = svg_path.exists() and svg_path.stat().st_size > 0

    return {
        "points": csv_rows,
        "geojson_features": geo_stats["features"],
        "geojson_points": geo_stats["points"],
        "geojson_lines": geo_stats["lines"],
        "gpx_waypoints": gpx_waypoints,
        "segments": geo_stats["segments"],
        "has_svg_preview": has_svg,
    }


# ---------- manifest 读写 ----------


MANIFEST_URL_FIELDS = ("csv_url", "geojson_url", "gpx_url", "svg_url")


def is_planned_route(entry: dict) -> bool:
    """planned-data 路线:status=planned-data 且 4 个 URL 全为 null。"""
    if entry.get("status") == "planned-data":
        return True
    return all(entry.get(f) is None for f in MANIFEST_URL_FIELDS)


def update_manifest_entry(entry: dict, stats: dict) -> dict:
    """生成新的 manifest 条目,保留人工字段,刷新统计字段。"""
    new_entry = dict(entry)  # 浅拷贝
    if not is_planned_route(new_entry):
        # 只有非 planned 路线才刷新统计
        new_entry["points"] = stats["points"]
        new_entry["segments"] = stats["segments"]
        new_entry["geojson_features"] = stats["geojson_features"]
        new_entry["geojson_points"] = stats["geojson_points"]
        new_entry["geojson_lines"] = stats["geojson_lines"]
        new_entry["gpx_waypoints"] = stats["gpx_waypoints"]
        new_entry["has_svg_preview"] = stats["has_svg_preview"]
    return new_entry


# ---------- 子命令执行 ----------


def run_subprocess(cmd: list[str], cwd: Path) -> tuple[int, str, str]:
    """运行子命令并返回 (returncode, stdout, stderr)。"""
    try:
        result = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError as e:
        return 127, "", str(e)


# ---------- 主流程 ----------


def build_one(
    slug: str,
    repo_root: Path,
    generate_svg: bool = True,
) -> tuple[bool, dict]:
    """构建单条路线: 校验数据 + 生成 SVG + 收集统计。返回 (passed, stats)."""
    data_dir = repo_root / "data" / "routes"
    img_dir = repo_root / "assets" / "img" / "routes"

    # 1) 校验数据(只对有 CSV 的路线)
    csv_path = data_dir / f"{slug}.csv"
    if csv_path.exists():
        rc, out, err = run_subprocess(
            ["python3", "scripts/validate-route-data.py", slug],
            cwd=repo_root,
        )
        if rc != 0:
            print(f"  ✗ validate-route-data.py {slug} FAILED")
            if out:
                print(out)
            if err:
                print(err, file=sys.stderr)
            return False, {}

    # 2) 生成 SVG(只在 generate_svg=True 时)
    if generate_svg:
        rc, out, err = run_subprocess(
            ["python3", "scripts/render-route-map-svg.py", slug],
            cwd=repo_root,
        )
        if rc != 0:
            print(f"  ✗ render-route-map-svg.py {slug} FAILED")
            if out:
                print(out)
            if err:
                print(err, file=sys.stderr)
            return False, {}

    # 3) 统计
    stats = collect_route_stats(slug, data_dir, img_dir)
    return True, stats
    # 注:失败路径已在上面提前 return False, {}



def check_manifest(repo_root: Path) -> tuple[bool, list[str]]:
    """校验 manifest 统计字段与实际数据一致(不回写)。"""
    manifest_path = repo_root / "data" / "routes" / "routes-manifest.json"
    if not manifest_path.exists():
        return False, [f"manifest 不存在: {manifest_path}"]

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    routes = manifest.get("routes", [])
    errors: list[str] = []

    data_dir = repo_root / "data" / "routes"
    img_dir = repo_root / "assets" / "img" / "routes"

    for entry in routes:
        slug = entry.get("slug")
        if not slug:
            continue
        if is_planned_route(entry):
            # planned-data 路线:不校验统计字段
            continue
        stats = collect_route_stats(slug, data_dir, img_dir)
        for key, actual in stats.items():
            expected = entry.get(key)
            if expected is None:
                errors.append(f"{slug}: manifest 缺少字段 {key}")
                continue
            if expected != actual:
                errors.append(
                    f"{slug}.{key}: manifest={expected} 实际={actual} 不一致"
                )
    return (not errors), errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="行旅图谱 · 路线工厂入口",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python3 scripts/build-route-assets.py
    python3 scripts/build-route-assets.py --all
    python3 scripts/build-route-assets.py out-of-eden-walk-china
    python3 scripts/build-route-assets.py liao-tower-roadtrip
    python3 scripts/build-route-assets.py --check
        """,
    )
    parser.add_argument(
        "slug",
        nargs="?",
        default=None,
        help="路线 slug(默认走 --all)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="构建 manifest 中所有路线",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="CI 模式:校验 manifest 与数据一致性,不回写不生成",
    )
    parser.add_argument(
        "--manifest",
        default="data/routes/routes-manifest.json",
        help="manifest 路径",
    )
    parser.add_argument(
        "--data-dir",
        default="data/routes",
        help="数据目录",
    )
    parser.add_argument(
        "--img-dir",
        default="assets/img/routes",
        help="SVG 输出目录",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    manifest_path = repo_root / args.manifest
    data_dir = repo_root / args.data_dir
    img_dir = repo_root / args.img_dir

    if not manifest_path.exists():
        print(f"FAIL: manifest 不存在: {manifest_path}")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    routes = manifest.get("routes", [])
    if not routes:
        print("FAIL: manifest 中没有 routes")
        return 1

    # 确定要处理的 slug 列表
    if args.slug:
        slugs = [args.slug]
    elif args.all or (not args.slug and not args.check):
        slugs = [r["slug"] for r in routes if r.get("slug")]
    else:
        slugs = [r["slug"] for r in routes if r.get("slug")]

    if args.check:
        print("行旅图谱 · 路线工厂 check")
        print(f"manifest: {manifest_path}")
        print(f"routes: {len(routes)}")
        print("-" * 50)
        passed, errors = check_manifest(repo_root)
        if passed:
            print("PASS route factory check")
            print("manifest matches generated statistics")
            print(f"routes: {len(routes)}")
            return 0
        else:
            print("FAIL route factory check")
            for e in errors:
                print(f"  ✗ {e}")
            return 1

    # build 模式
    print("行旅图谱 · 路线工厂 build")
    print(f"manifest: {manifest_path}")
    print(f"routes: {len(routes)}")
    print("-" * 50)

    all_passed = True
    build_results: list[tuple[str, bool, dict]] = []
    new_routes: list[dict] = []

    for entry in routes:
        slug = entry.get("slug")
        if not slug:
            print(f"  ✗ manifest entry 缺少 slug: {entry}")
            all_passed = False
            continue
        if is_planned_route(entry):
            print(f"  · {slug}: planned-data 跳过构建")
            new_routes.append(entry)
            continue
        if slug not in slugs:
            new_routes.append(entry)
            continue

        print(f"  · 构建 {slug} ...")
        passed, stats = build_one(slug, repo_root, generate_svg=True)
        build_results.append((slug, passed, stats))
        new_entry = update_manifest_entry(entry, stats)
        new_routes.append(new_entry)
        if not passed:
            all_passed = False
            continue
        # 输出统计(必须保证 stats 含有必需字段)
        if not stats or "points" not in stats:
            print(f"    ✗ 统计缺失,跳过 manifest 更新")
            new_routes.append(entry)
            all_passed = False
            continue
        print(
            f"    → {stats['points']} points, "
            f"{stats['geojson_features']} features, "
            f"{stats['gpx_waypoints']} waypoints, "
            f"{stats['segments']} segments, "
            f"svg {'ok' if stats['has_svg_preview'] else 'MISSING'}"
        )

    # 回写 manifest
    if all_passed:
        manifest["routes"] = new_routes
        # 保留 version / updated_at
        manifest["version"] = manifest.get("version", "v1.4.8")
        from datetime import datetime
        manifest["updated_at"] = datetime.utcnow().strftime("%Y-%m-%d")
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print("-" * 50)
        print(f"PASS route factory build")
        print(f"routes: {len(routes)}")
        for slug, ok, stats in build_results:
            if ok:
                print(
                    f"- {slug}: {stats['points']} points, "
                    f"{stats['geojson_features']} features, "
                    f"{stats['gpx_waypoints']} waypoints, "
                    f"{stats['segments']} segments, "
                    f"svg {'ok' if stats['has_svg_preview'] else 'MISSING'}"
                )
        print(f"manifest updated: {manifest_path}")
        return 0
    else:
        print("-" * 50)
        print("FAIL route factory build")
        for slug, ok, stats in build_results:
            if not ok:
                print(f"  ✗ {slug}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
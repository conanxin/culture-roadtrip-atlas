#!/usr/bin/env python3
"""
render-route-map-svg.py · 行旅图谱 · 路线静态 SVG 生成脚本

基于 GeoJSON 数据生成纯静态 SVG 路线示意图（cultural replica generalized map）。
只用 Python 标准库,不使用外部底图或地图 API。支持任意路线 slug 与 --all 批量模式。

Usage:
    python3 scripts/render-route-map-svg.py                      # 默认 OEDW
    python3 scripts/render-route-map-svg.py <route-slug>        # 自定义 slug
    python3 scripts/render-route-map-svg.py --all               # 遍历 manifest
    python3 scripts/render-route-map-svg.py --help

输出:
    assets/img/routes/<route-slug>-map.svg

技术决策:
    * bounding-box equirectangular projection(经纬度等距投影)
    * 简化参考网格(每 5 度)
    * 主路线 + 段分路线 + waypoint + 起点/终点标注
    * <title>/<desc> 与图例文案随 manifest route 动态生成
    * 必须包含 "not for navigation"、"cultural replica"、"not original GPS track"

历史:
    v1.2 · 2026-07-05 · Phase 8 · --check 不生成 / 跳过 planned-data
    v1.1 · 2026-07-05 · Phase 7 · --all / 通用化标题与图例 / 短路线防重叠
    v1.0 · 2026-07-04 · Phase 6 · OEDW 静态 SVG 首版
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any


# ---------- 配色(行旅图谱 · 墨绿/米白/暗金) ----------

COLOR_BG = "#fbf7ec"           # 米白
COLOR_ROUTE_MAIN = "#6b8e23"   # 墨绿
COLOR_ROUTE_SEG = "#9caf6f"    # 墨绿浅
COLOR_POINT = "#b8860b"        # 暗金
COLOR_POINT_START = "#5d8a3a"  # 起点(深墨绿)
COLOR_POINT_END = "#a8423a"    # 终点(暗红)
COLOR_TEXT = "#2a3d1f"         # 深墨绿(文字)
COLOR_TEXT_LIGHT = "#6b7c5f"   # 浅文字
COLOR_BORDER = "#d4c89a"       # 米色边框


# ---------- 投影与坐标 ----------


def project(lon: float, lat: float, bbox: tuple[float, float, float, float],
            w: float, h: float, padding: float = 60) -> tuple[float, float]:
    """equirectangular projection: 经纬度 → SVG x/y 坐标。"""
    min_lon, min_lat, max_lon, max_lat = bbox
    pw = w - 2 * padding
    ph = h - 2 * padding
    x = padding + (lon - min_lon) / (max_lon - min_lon) * pw
    # 注意:SVG y 轴向下,纬度越高 y 越小
    y = padding + (max_lat - lat) / (max_lat - min_lat) * ph
    return x, y


def calculate_bbox(features: list[dict]) -> tuple[float, float, float, float]:
    """从所有 Point + LineString 坐标计算 bounding box。"""
    coords: list[tuple[float, float]] = []
    for f in features:
        geom = f.get("geometry", {})
        gtype = geom.get("type")
        if gtype == "Point":
            coords.append(tuple(geom["coordinates"][:2]))  # (lon, lat)
        elif gtype == "LineString":
            for c in geom.get("coordinates", []):
                coords.append(tuple(c[:2]))
    if not coords:
        return (0, 0, 0, 0)
    lons = [c[0] for c in coords]
    lats = [c[1] for c in coords]
    return (min(lons), min(lats), max(lons), max(lats))


# ---------- 通用文案生成 ----------


def build_route_meta(geojson: dict, slug: str) -> dict:
    """从 GeoJSON metadata + features 提取 SVG 渲染所需元数据。"""
    metadata = geojson.get("metadata", {})
    features = geojson.get("features", [])
    sorted_pts = sorted(
        [f for f in features if f.get("geometry", {}).get("type") == "Point"],
        key=lambda f: f.get("properties", {}).get("sequence", 999),
    )

    # 段列表
    seg_ids = sorted({
        f.get("properties", {}).get("segment_id", "")
        for f in features
        if f.get("geometry", {}).get("type") == "Point"
        and f.get("properties", {}).get("segment_id")
    })
    seg_label = f"{seg_ids[0]}-{seg_ids[-1]}" if seg_ids else ""

    # 起终点
    start_label = ""
    end_label = ""
    if sorted_pts:
        s = sorted_pts[0]
        sp = s.get("properties", {})
        start_label = f"{sp.get('city_or_area', '')} / {sp.get('province', '')}".strip(" /")
        e = sorted_pts[-1]
        ep = e.get("properties", {})
        end_label = f"{ep.get('city_or_area', '')} / {ep.get('province', '')}".strip(" /")

    # 路线类型描述
    route_type = metadata.get("route_type", "cultural_replica")
    route_type_zh = {
        "cultural_replica": "文化复刻",
        "cultural_roadtrip": "文化自驾",
    }.get(route_type, "文化路线")

    # 副标题
    subtitle_parts = []
    if metadata.get("approximate_distance_km"):
        subtitle_parts.append(f"约 {metadata['approximate_distance_km']} 公里")
    if metadata.get("time_span"):
        subtitle_parts.append(metadata["time_span"])
    subtitle_parts.append(f"{len(sorted_pts)} 个粗点")
    if seg_label:
        subtitle_parts.append(f"{len(seg_ids)} 段路线")
    subtitle_parts.append(metadata.get("version", "v1.4.7"))
    subtitle = " · ".join(subtitle_parts)

    # 标题
    title = metadata.get("title", slug)
    if route_type == "cultural_roadtrip":
        title_with_type = f"{title} · 文化自驾静态示意图"
    else:
        title_with_type = f"{title} · 文化复刻静态示意图"

    # <desc> 段(包含必要声明 - 中英文双语)
    desc_en = (
        f"{route_type_zh} waypoints and generalized route only; "
        f"not original GPS track; not for navigation; "
        f"cultural replica. "
        f"Not real-time road conditions; not for safety guidance."
    )
    desc_zh = (
        f"{route_type_zh}粗点 + 概括路线;非原始 GPS 轨迹;非导航;不保证路况与开放状态。"
        f"本数据为研究、写作与旅行规划参考;{metadata.get('disclaimer', '')}"
    )
    desc = f"{desc_en} | {desc_zh}"

    return {
        "slug": slug,
        "title": title,
        "title_with_type": title_with_type,
        "subtitle": subtitle,
        "desc": desc,
        "route_type": route_type,
        "route_type_zh": route_type_zh,
        "seg_label": seg_label,
        "seg_count": len(seg_ids),
        "point_count": len(sorted_pts),
        "start_label": start_label,
        "end_label": end_label,
        "version": metadata.get("version", "v1.4.7"),
        "updated_at": metadata.get("updated_at", "2026-07-05"),
    }


# ---------- SVG 片段生成 ----------


def svg_header(width: int, height: int, meta: dict) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" preserveAspectRatio="xMidYMid meet">
  <title>{meta["title_with_type"]}</title>
  <desc>{meta["desc"]}</desc>
'''


def svg_style() -> str:
    return f'''  <style>
    .bg {{ fill: {COLOR_BG}; }}
    .frame {{ fill: none; stroke: {COLOR_BORDER}; stroke-width: 1; }}
    .route-main {{ fill: none; stroke: {COLOR_ROUTE_MAIN}; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; opacity: 0.85; }}
    .route-seg {{ fill: none; stroke: {COLOR_ROUTE_SEG}; stroke-width: 1.4; stroke-dasharray: 4 3; opacity: 0.7; }}
    .point {{ fill: {COLOR_POINT}; stroke: #fff; stroke-width: 1.2; }}
    .point-start {{ fill: {COLOR_POINT_START}; stroke: #fff; stroke-width: 1.6; }}
    .point-end {{ fill: {COLOR_POINT_END}; stroke: #fff; stroke-width: 1.6; }}
    .seg-label {{ fill: {COLOR_TEXT}; font: 600 11px sans-serif; }}
    .point-label {{ fill: {COLOR_TEXT_LIGHT}; font: 9px sans-serif; }}
    .start-label {{ fill: {COLOR_POINT_START}; font: 700 12px sans-serif; }}
    .end-label {{ fill: {COLOR_POINT_END}; font: 700 12px sans-serif; }}
    .title {{ fill: {COLOR_TEXT}; font: 700 16px sans-serif; }}
    .subtitle {{ fill: {COLOR_TEXT_LIGHT}; font: 11px sans-serif; }}
    .legend-text {{ fill: {COLOR_TEXT}; font: 10px sans-serif; }}
    .disclaimer {{ fill: #c0392b; font: italic 11px sans-serif; }}
  </style>
'''


def svg_background(width: int, height: int) -> str:
    parts = [
        f'  <rect class="bg" x="0" y="0" width="{width}" height="{height}"/>',
        f'  <rect class="frame" x="0.5" y="0.5" width="{width-1}" height="{height-1}" fill="none"/>',
    ]
    return "\n".join(parts) + "\n"


def svg_china_outline(bbox: tuple[float, float, float, float], w: int, h: int) -> str:
    """简化参考网格(每 5 度),不画国境线。"""
    min_lon, min_lat, max_lon, max_lat = bbox
    lines = []
    for lon in range(int(min_lon // 5 * 5), int(max_lon // 5 * 5) + 6, 5):
        if min_lon <= lon <= max_lon:
            x, _ = project(lon, min_lat, bbox, w, h)
            x2, _ = project(lon, max_lat, bbox, w, h)
            lines.append(f'  <line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{h}" stroke="{COLOR_BORDER}" stroke-width="0.5" stroke-dasharray="1 4" opacity="0.4"/>')
    for lat in range(int(min_lat // 5 * 5), int(max_lat // 5 * 5) + 6, 5):
        if min_lat <= lat <= max_lat:
            _, y = project(min_lon, lat, bbox, w, h)
            _, y2 = project(max_lon, lat, bbox, w, h)
            lines.append(f'  <line x1="0" y1="{y:.1f}" x2="{w}" y2="{y:.1f}" stroke="{COLOR_BORDER}" stroke-width="0.5" stroke-dasharray="1 4" opacity="0.4"/>')
    return "\n".join(lines) + "\n"


def svg_route_main(features: list[dict], bbox, w: int, h: int) -> str:
    parts = ["  <g id=\"route-main\">"]
    for f in features:
        if f.get("geometry", {}).get("type") != "LineString":
            continue
        props = f.get("properties", {})
        # 只画主路线(feature_type == generalized_route_line)
        if props.get("feature_type") != "generalized_route_line":
            continue
        coords = f["geometry"]["coordinates"]
        points_str = " ".join(
            f"{project(c[0], c[1], bbox, w, h)[0]:.1f},{project(c[0], c[1], bbox, w, h)[1]:.1f}"
            for c in coords
        )
        parts.append(f'    <polyline class="route-main" points="{points_str}"/>')
    parts.append("  </g>")
    return "\n".join(parts) + "\n"


def svg_route_segments(features: list[dict], bbox, w: int, h: int) -> str:
    parts = ["  <g id=\"route-segments\">"]
    for f in features:
        if f.get("geometry", {}).get("type") != "LineString":
            continue
        props = f.get("properties", {})
        if props.get("feature_type") != "segment_generalized_line":
            continue
        coords = f["geometry"]["coordinates"]
        points_str = " ".join(
            f"{project(c[0], c[1], bbox, w, h)[0]:.1f},{project(c[0], c[1], bbox, w, h)[1]:.1f}"
            for c in coords
        )
        parts.append(f'    <polyline class="route-seg" points="{points_str}"/>')
    parts.append("  </g>")
    return "\n".join(parts) + "\n"


def svg_points(features: list[dict], bbox, w: int, h: int) -> tuple[str, str]:
    """返回 (points_svg, segment_labels_svg)。"""
    points_svg = ["  <g id=\"points\">"]
    labels_svg = ["  <g id=\"segment-labels\">"]
    seg_centers: dict[str, list[tuple[float, float]]] = {}

    sorted_pts = sorted(
        [f for f in features if f.get("geometry", {}).get("type") == "Point"],
        key=lambda f: f.get("properties", {}).get("sequence", 999),
    )

    for idx, f in enumerate(sorted_pts):
        props = f.get("properties", {})
        lon, lat = f["geometry"]["coordinates"][:2]
        x, y = project(lon, lat, bbox, w, h)
        seg_id = props.get("segment_id", "")

        if idx == 0:
            cls = "point-start"
            r = 6
        elif idx == len(sorted_pts) - 1:
            cls = "point-end"
            r = 6
        else:
            cls = "point"
            r = 3.2

        points_svg.append(f'    <circle class="{cls}" cx="{x:.1f}" cy="{y:.1f}" r="{r}"/>')

        if seg_id and seg_id not in seg_centers:
            seg_centers[seg_id] = []
        if seg_id:
            seg_centers[seg_id].append((x, y))

    points_svg.append("  </g>")

    # 段编号放在中心点
    for seg_id, pts in seg_centers.items():
        if not pts:
            continue
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        labels_svg.append(f'    <text class="seg-label" x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle">{seg_id}</text>')

    labels_svg.append("  </g>")
    return "\n".join(points_svg) + "\n", "\n".join(labels_svg) + "\n"


def svg_start_end_labels(features: list[dict], bbox, w: int, h: int, meta: dict) -> str:
    sorted_pts = sorted(
        [f for f in features if f.get("geometry", {}).get("type") == "Point"],
        key=lambda f: f.get("properties", {}).get("sequence", 999),
    )
    if not sorted_pts:
        return ""

    parts = ["  <g id=\"endpoint-labels\">"]

    start_props = sorted_pts[0].get("properties", {})
    start_lon, start_lat = sorted_pts[0]["geometry"]["coordinates"][:2]
    sx, sy = project(start_lon, start_lat, bbox, w, h)
    start_text = f"起点:{start_props.get('point_name', start_props.get('city_or_area', meta.get('start_label', '')))}"
    parts.append(f'    <text class="start-label" x="{sx + 10:.1f}" y="{sy - 8:.1f}">{start_text}</text>')

    end_props = sorted_pts[-1].get("properties", {})
    end_lon, end_lat = sorted_pts[-1]["geometry"]["coordinates"][:2]
    ex, ey = project(end_lon, end_lat, bbox, w, h)
    end_text = f"终点:{end_props.get('point_name', end_props.get('city_or_area', meta.get('end_label', '')))}"
    parts.append(f'    <text class="end-label" x="{ex + 10:.1f}" y="{ey - 8:.1f}">{end_text}</text>')

    parts.append("  </g>")
    return "\n".join(parts) + "\n"


def svg_legend(w: int, h: int, meta: dict) -> str:
    """图例 + 标题 + 免责声明(随路线变化)。"""
    seg_label = meta["seg_label"] or ""
    seg_text = f"分段路线({seg_label})" if seg_label else "分段路线"
    return f'''  <g id="header">
    <text class="title" x="60" y="34">{meta["title_with_type"]}</text>
    <text class="subtitle" x="60" y="52">{meta["subtitle"]}</text>
  </g>
  <g id="legend" transform="translate(60, {h - 80})">
    <rect class="frame" x="0" y="0" width="540" height="64" rx="4" fill="#fff" opacity="0.92"/>
    <circle class="point-start" cx="14" cy="14" r="6"/>
    <text class="legend-text" x="28" y="18">起点</text>
    <circle class="point" cx="120" cy="14" r="3.2"/>
    <text class="legend-text" x="132" y="18">{meta["route_type_zh"]}粗点({meta["point_count"]} 个)</text>
    <circle class="point-end" cx="370" cy="14" r="6"/>
    <text class="legend-text" x="384" y="18">终点</text>
    <line x1="14" y1="38" x2="40" y2="38" class="route-main"/>
    <text class="legend-text" x="50" y="42">主路线(概括连接)</text>
    <line x1="200" y1="38" x2="240" y2="38" class="route-seg"/>
    <text class="legend-text" x="250" y="42">{seg_text}</text>
    <text class="disclaimer" x="0" y="60">⚠ {meta["route_type_zh"]}粗点 · 非原始 GPS 轨迹 / not original GPS · 非导航 / not for navigation · 不保证路况与开放状态</text>
  </g>
  <g id="footer">
    <text class="legend-text" x="{w - 60}" y="{h - 20}" text-anchor="end">Generated by render-route-map-svg.py · 行旅图谱 {meta["version"]} · {meta["updated_at"]}</text>
  </g>
'''


def build_svg(geojson: dict, slug: str, width: int = 1200, height: int = 760) -> str:
    """组装完整 SVG。"""
    features = geojson.get("features", [])
    bbox = calculate_bbox(features)
    pad_lon = (bbox[2] - bbox[0]) * 0.05
    pad_lat = (bbox[3] - bbox[1]) * 0.05
    bbox = (bbox[0] - pad_lon, bbox[1] - pad_lat, bbox[2] + pad_lon, bbox[3] + pad_lat)

    meta = build_route_meta(geojson, slug)

    parts = [svg_header(width, height, meta)]
    parts.append(svg_style())
    parts.append(svg_background(width, height))
    parts.append(svg_china_outline(bbox, width, height))
    parts.append(svg_route_segments(features, bbox, width, height))
    parts.append(svg_route_main(features, bbox, width, height))
    points_svg, labels_svg = svg_points(features, bbox, width, height)
    parts.append(points_svg)
    parts.append(labels_svg)
    parts.append(svg_start_end_labels(features, bbox, width, height, meta))
    parts.append(svg_legend(width, height, meta))
    parts.append("</svg>\n")
    return "".join(parts)


# ---------- 通用声明检查 ----------


def _required_phrases(route_type: str) -> list[str]:
    """根据 route_type 返回必要声明短语。"""
    base = ["not for navigation", "cultural replica", "not original gps"]
    return base


# ---------- 主函数 ----------


def render_one(slug: str, data_dir: Path, output_dir: Path, width: int, height: int) -> tuple[bool, dict]:
    """生成单条路线 SVG。返回 (success, info)."""
    geo_path = data_dir / f"{slug}.geojson"
    output_path = output_dir / f"{slug}-map.svg"

    if not geo_path.exists():
        print(f"  ✗ {slug}: GeoJSON 不存在: {geo_path}")
        return False, {"slug": slug, "passed": False, "error": "GeoJSON not found"}

    geo = json.loads(geo_path.read_text(encoding="utf-8"))
    meta = build_route_meta(geo, slug)

    svg = build_svg(geo, slug, width, height)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg, encoding="utf-8")

    # 必要声明检查
    svg_lower = svg.lower()
    required = _required_phrases(meta["route_type"])
    missing = [p for p in required if p not in svg_lower]

    size = output_path.stat().st_size
    status = "OK" if not missing else "WARN"
    print(f"  {status}: {slug} · {output_path.name} · {size} bytes · title={meta['title_with_type'][:50]}...")
    for p in required:
        present = p in svg_lower
        print(f"    {'✓' if present else '✗'} contains: {p!r}")

    return not missing, {
        "slug": slug,
        "passed": not missing,
        "output": str(output_path),
        "size": size,
        "title": meta["title_with_type"],
        "missing_phrases": missing,
    }


def check_svg(slug: str, output_dir: Path) -> tuple[bool, dict]:
    """只检查 SVG 文件是否存在 + 包含必要声明,不重新生成。"""
    output_path = output_dir / f"{slug}-map.svg"
    fail_reasons: list[str] = []
    info: dict = {"slug": slug, "size": 0, "fail_reasons": fail_reasons}

    if not output_path.exists():
        fail_reasons.append(f"SVG 文件不存在: {output_path}")
        return False, info

    size = output_path.stat().st_size
    if size == 0:
        fail_reasons.append(f"SVG 文件为空: {output_path}")
        return False, info
    info["size"] = size

    svg_text = output_path.read_text(encoding="utf-8").lower()
    required = _required_phrases("cultural_replica")
    missing = [p for p in required if p not in svg_text]
    for p in required:
        present = p in svg_text
        print(f"    {'✓' if present else '✗'} contains: {p!r}")
    if missing:
        for p in missing:
            fail_reasons.append(f"SVG 缺少必要声明: {p!r}")
        return False, info

    print(f"  OK: {slug} · {output_path.name} · {size} bytes")
    return True, info


def main() -> int:
    parser = argparse.ArgumentParser(
        description="行旅图谱 · 路线静态 SVG 生成脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python3 scripts/render-route-map-svg.py
    python3 scripts/render-route-map-svg.py out-of-eden-walk-china
    python3 scripts/render-route-map-svg.py liao-tower-roadtrip
    python3 scripts/render-route-map-svg.py --all
        """,
    )
    parser.add_argument("slug", nargs="?", default=None, help="路线 slug(默认: out-of-eden-walk-china)")
    parser.add_argument("--all", action="store_true", help="遍历 manifest 所有 route slug 批量生成")
    parser.add_argument("--check", action="store_true", help="只检查 SVG 是否存在且包含必要声明,不重新生成")
    parser.add_argument("--data-dir", default="data/routes", help="GeoJSON 目录")
    parser.add_argument("--output-dir", default="assets/img/routes", help="SVG 输出目录")
    parser.add_argument("--manifest", default="data/routes/routes-manifest.json", help="manifest 路径")
    parser.add_argument("--width", type=int, default=1200, help="SVG 宽度")
    parser.add_argument("--height", type=int, default=760, help="SVG 高度")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output_dir)

    # --check 模式:只校验 SVG
    if args.check:
        if args.all:
            manifest_path = Path(args.manifest)
            if not manifest_path.exists():
                print(f"FAIL: manifest 不存在: {manifest_path}")
                return 1
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            routes = manifest.get("routes", [])
            if not routes:
                print("FAIL: manifest 中没有 routes")
                return 1
            print(f"行旅图谱 · 路线 SVG 检查 (--all --check)")
            print(f"manifest: {manifest_path}")
            print(f"routes: {len(routes)}")
            print("=" * 50)
            all_ok = True
            checked = 0
            for r in routes:
                slug = r.get("slug")
                if not slug:
                    continue
                # planned-data 跳过
                if (r.get("status") == "planned-data" or
                        all(r.get(f) is None for f in ("csv_url", "geojson_url", "gpx_url", "svg_url"))):
                    print(f"  · {slug}: planned-data 跳过 SVG 检查")
                    continue
                ok, info = check_svg(slug, output_dir)
                checked += 1
                if not ok:
                    all_ok = False
            print("=" * 50)
            if all_ok:
                print(f"PASS all route SVG check")
                print(f"routes: {checked}")
                return 0
            else:
                print(f"FAIL all route SVG check")
                return 1
        else:
            slug = args.slug or "out-of-eden-walk-china"
            print(f"行旅图谱 · 路线 SVG 检查")
            print(f"slug: {slug}")
            print("-" * 50)
            ok, info = check_svg(slug, output_dir)
            print()
            if ok:
                print(f"PASS route SVG check")
                print(f"  size: {info['size']} bytes")
                return 0
            else:
                print(f"FAIL route SVG check")
                for reason in info.get("fail_reasons", []):
                    print(f"  ✗ {reason}")
                return 1

    # --all 模式
    if args.all:
        manifest_path = Path(args.manifest)
        if not manifest_path.exists():
            print(f"FAIL: manifest 不存在: {manifest_path}")
            return 1
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        routes = manifest.get("routes", [])
        if not routes:
            print("FAIL: manifest 中没有 routes")
            return 1

        print(f"行旅图谱 · 路线 SVG 生成 (--all 模式)")
        print(f"manifest: {manifest_path}")
        print(f"routes: {len(routes)}")
        print("=" * 50)

        all_ok = True
        for r in routes:
            slug = r.get("slug")
            if not slug:
                continue
            # planned-data 跳过
            if (r.get("status") == "planned-data" or
                    all(r.get(f) is None for f in ("csv_url", "geojson_url", "gpx_url", "svg_url"))):
                print(f"  · {slug}: planned-data 跳过生成")
                continue
            ok, _info = render_one(slug, data_dir, output_dir, args.width, args.height)
            if not ok:
                all_ok = False

        print("=" * 50)
        if all_ok:
            print(f"PASS all route SVG generation")
            print(f"routes: {len(routes)}")
            return 0
        else:
            print(f"FAIL all route SVG generation")
            return 1

    # 单路线模式
    slug = args.slug or "out-of-eden-walk-china"
    print(f"行旅图谱 · 路线 SVG 生成")
    print(f"slug: {slug}")
    print("-" * 50)

    ok, info = render_one(slug, data_dir, output_dir, args.width, args.height)
    print()
    if ok:
        print(f"OK: SVG generated · {info['size']} bytes")
        return 0
    else:
        print(f"FAIL: SVG missing required phrases: {info.get('missing_phrases', [])}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

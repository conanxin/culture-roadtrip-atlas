#!/usr/bin/env python3
"""
render-route-map-svg.py · 行旅图谱 · 路线静态 SVG 生成脚本

基于 GeoJSON 数据生成纯静态 SVG 路线示意图（cultural replica generalized map）。
只用 Python 标准库，不使用外部底图或地图 API。

Usage:
    python3 scripts/render-route-map-svg.py
    python3 scripts/render-route-map-svg.py <route-slug>
    python3 scripts/render-route-map-svg.py --output <path>

输出:
    assets/img/routes/<route-slug>-map.svg

技术决策:
    * bounding-box equirectangular projection（经纬度等距投影）
    * 简化中国轮廓（矩形区域近似，不画国境线）
    * 主路线 + 10 段分路线 + 42 waypoint + 起点/终点标注
    * 必须包含 "not Paul Salopek original GPS track"、"not for navigation"、"cultural replica"

历史:
    v1.0 · 2026-07-04 · Phase 6 首版
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any


# ---------- 配色（行旅图谱 · 墨绿/米白/暗金） ----------

COLOR_BG = "#fbf7ec"           # 米白
COLOR_ROUTE_MAIN = "#6b8e23"   # 墨绿
COLOR_ROUTE_SEG = "#9caf6f"    # 墨绿浅
COLOR_POINT = "#b8860b"        # 暗金
COLOR_POINT_START = "#5d8a3a"  # 起点（深墨绿）
COLOR_POINT_END = "#a8423a"    # 终点（暗红）
COLOR_TEXT = "#2a3d1f"         # 深墨绿（文字）
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
    # 注意：SVG y 轴向下，纬度越高 y 越小
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


# ---------- SVG 片段生成 ----------


def svg_header(width: int, height: int) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" preserveAspectRatio="xMidYMid meet">
  <title>Out of Eden Walk 中国段文化复刻路线静态示意图</title>
  <desc>Cultural replica waypoints and generalized route only; not Paul Salopek original GPS track; not for navigation. This is a hand-crafted schematic for research and storytelling purposes, generated from public Out of Eden Walk milestones and dispatches.</desc>
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
    """简化中国轮廓矩形（仅作示意，不画国境线）。"""
    # bbox already roughly covers China, draw a thin reference grid
    min_lon, min_lat, max_lon, max_lat = bbox
    # 经纬度参考线（每 5 度）
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
        # 只画主路线（feature_type == generalized_route_line）
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
    
    # Sort by sequence to identify first/last
    sorted_pts = sorted(
        [f for f in features if f.get("geometry", {}).get("type") == "Point"],
        key=lambda f: f.get("properties", {}).get("sequence", 999),
    )
    
    for idx, f in enumerate(sorted_pts):
        props = f.get("properties", {})
        lon, lat = f["geometry"]["coordinates"][:2]
        x, y = project(lon, lat, bbox, w, h)
        seg_id = props.get("segment_id", "")
        
        # First point = start, last point = end
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
        
        # Track segment center for label placement
        if seg_id and seg_id not in seg_centers:
            seg_centers[seg_id] = []
        if seg_id:
            seg_centers[seg_id].append((x, y))
    
    points_svg.append("  </g>")
    
    # Place segment labels at the centroid of their points
    for seg_id, pts in seg_centers.items():
        if not pts:
            continue
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        labels_svg.append(f'    <text class="seg-label" x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle">{seg_id}</text>')
    
    labels_svg.append("  </g>")
    return "\n".join(points_svg) + "\n", "\n".join(labels_svg) + "\n"


def svg_start_end_labels(features: list[dict], bbox, w: int, h: int) -> str:
    sorted_pts = sorted(
        [f for f in features if f.get("geometry", {}).get("type") == "Point"],
        key=lambda f: f.get("properties", {}).get("sequence", 999),
    )
    if not sorted_pts:
        return ""
    
    parts = ["  <g id=\"endpoint-labels\">"]
    
    # Start
    start_props = sorted_pts[0].get("properties", {})
    start_lon, start_lat = sorted_pts[0]["geometry"]["coordinates"][:2]
    sx, sy = project(start_lon, start_lat, bbox, w, h)
    parts.append(f'    <text class="start-label" x="{sx + 10:.1f}" y="{sy - 8:.1f}">起点：{start_props.get("city_or_area", "云南西部")} / {start_props.get("province", "")}</text>')
    
    # End
    end_props = sorted_pts[-1].get("properties", {})
    end_lon, end_lat = sorted_pts[-1]["geometry"]["coordinates"][:2]
    ex, ey = project(end_lon, end_lat, bbox, w, h)
    parts.append(f'    <text class="end-label" x="{ex + 10:.1f}" y="{ey - 8:.1f}">终点：{end_props.get("city_or_area", "大连")} / 黄海</text>')
    
    parts.append("  </g>")
    return "\n".join(parts) + "\n"


def svg_legend(w: int, h: int) -> str:
    """图例 + 标题 + 免责声明。"""
    return f'''  <g id="header">
    <text class="title" x="60" y="34">Out of Eden Walk 中国段 · 文化复刻静态示意图</text>
    <text class="subtitle" x="60" y="52">约 6,000–6,700 公里 · 两年多 · 42 个文化复刻粗点 · 10 段路线 · v1.4.6</text>
  </g>
  <g id="legend" transform="translate(60, {h - 80})">
    <rect class="frame" x="0" y="0" width="500" height="64" rx="4" fill="#fff" opacity="0.92"/>
    <circle class="point-start" cx="14" cy="14" r="6"/>
    <text class="legend-text" x="28" y="18">起点 · 云南西部边境</text>
    <circle class="point" cx="160" cy="14" r="3.2"/>
    <text class="legend-text" x="172" y="18">文化复刻粗点（42 个）</text>
    <circle class="point-end" cx="350" cy="14" r="6"/>
    <text class="legend-text" x="364" y="18">终点 · 大连黄海</text>
    <line x1="14" y1="38" x2="40" y2="38" class="route-main"/>
    <text class="legend-text" x="50" y="42">主路线（概括连接）</text>
    <line x1="180" y1="38" x2="220" y2="38" class="route-seg"/>
    <text class="legend-text" x="230" y="42">分段路线（S01–S10）</text>
    <text class="disclaimer" x="0" y="60">⚠ 文化复刻粗点 · 非 Paul Salopek 原始 GPS 轨迹 · 非导航</text>
  </g>
  <g id="footer">
    <text class="legend-text" x="{w - 60}" y="{h - 20}" text-anchor="end">Generated by render-route-map-svg.py · 行旅图谱 v1.4.6 · 2026-07-04</text>
  </g>
'''


def build_svg(geojson: dict, width: int = 1200, height: int = 760) -> str:
    """组装完整 SVG。"""
    features = geojson.get("features", [])
    bbox = calculate_bbox(features)
    # Slightly pad bbox
    pad_lon = (bbox[2] - bbox[0]) * 0.05
    pad_lat = (bbox[3] - bbox[1]) * 0.05
    bbox = (bbox[0] - pad_lon, bbox[1] - pad_lat, bbox[2] + pad_lon, bbox[3] + pad_lat)
    
    parts = [svg_header(width, height)]
    parts.append(svg_style())
    parts.append(svg_background(width, height))
    parts.append(svg_china_outline(bbox, width, height))
    parts.append(svg_route_segments(features, bbox, width, height))
    parts.append(svg_route_main(features, bbox, width, height))
    points_svg, labels_svg = svg_points(features, bbox, width, height)
    parts.append(points_svg)
    parts.append(labels_svg)
    parts.append(svg_start_end_labels(features, bbox, width, height))
    parts.append(svg_legend(width, height))
    parts.append("</svg>\n")
    return "".join(parts)


# ---------- 主函数 ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="行旅图谱 · 路线静态 SVG 生成脚本",
    )
    parser.add_argument("slug", nargs="?", default="out-of-eden-walk-china", help="路线 slug")
    parser.add_argument("--data-dir", default="data/routes", help="GeoJSON 目录")
    parser.add_argument("--output-dir", default="assets/img/routes", help="SVG 输出目录")
    parser.add_argument("--width", type=int, default=1200, help="SVG 宽度")
    parser.add_argument("--height", type=int, default=760, help="SVG 高度")
    args = parser.parse_args()

    geo_path = Path(args.data_dir) / f"{args.slug}.geojson"
    output_path = Path(args.output_dir) / f"{args.slug}-map.svg"
    
    if not geo_path.exists():
        print(f"ERROR: GeoJSON not found: {geo_path}", file=sys.stderr)
        return 1
    
    print(f"行旅图谱 · 路线 SVG 生成")
    print(f"input:  {geo_path}")
    print(f"output: {output_path}")
    
    geo = json.loads(geo_path.read_text(encoding="utf-8"))
    svg = build_svg(geo, args.width, args.height)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg, encoding="utf-8")
    
    # 必须包含的关键词检查（不区分大小写）
    required_phrases = [
        "not Paul Salopek",
        "not for navigation",
        "cultural replica",
    ]
    svg_lower = svg.lower()
    print()
    for phrase in required_phrases:
        present = phrase.lower() in svg_lower
        print(f"  {'✓' if present else '✗'} contains: {phrase!r}")
    
    size = output_path.stat().st_size
    print()
    print(f"OK: SVG generated · {size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
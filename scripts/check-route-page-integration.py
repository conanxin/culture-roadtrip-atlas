#!/usr/bin/env python3
"""
check-route-page-integration.py · 行旅图谱 · 路线详情页集成检查

读取 data/routes/routes-manifest.json,对每条有 page_url 的路线:
- 检查页面文件存在
- 检查页面含 data-route-slug="<slug>"
- 检查页面引入 route-page-badges.js
- 检查页面含 route-page-data-panel 容器
- 数据完整路线检查:含"路线数据"或"路线数据状态"
- planned-data 可跳过下载按钮检查

Usage:
    python3 scripts/check-route-page-integration.py

退出码:
    0  PASS
    1  FAIL

历史:
    v1.0 · 2026-07-06 · Phase 11 首版
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser(
        description="行旅图谱 · 路线详情页集成检查",
    )
    parser.add_argument(
        "--manifest",
        default="data/routes/routes-manifest.json",
        help="manifest 路径",
    )
    parser.add_argument(
        "--badges-js",
        default="assets/js/route-page-badges.js",
        help="route-page-badges.js 路径",
    )
    parser.add_argument(
        "--guide",
        default="docs/ROUTE_PAGE_INTEGRATION_GUIDE.md",
        help="路线页面接入指南路径",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    manifest_path = repo_root / args.manifest
    badges_js_path = repo_root / args.badges_js
    guide_path = repo_root / args.guide

    if not manifest_path.exists():
        print(f"FAIL: manifest 不存在: {manifest_path}")
        return 1
    if not badges_js_path.exists():
        print(f"FAIL: route-page-badges.js 不存在: {badges_js_path}")
        return 1
    if not guide_path.exists():
        print(f"FAIL: 路线页面接入指南不存在: {guide_path}")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    routes = manifest.get("routes", [])
    if not routes:
        print("FAIL: manifest 中没有 routes")
        return 1

    print("行旅图谱 · 路线详情页集成检查")
    print(f"manifest: {manifest_path}")
    print(f"badges-js: {badges_js_path}")
    print(f"guide: {guide_path}")
    print(f"routes: {len(routes)}")
    print("-" * 50)

    errors: list[str] = []
    warnings: list[str] = []
    checked = 0

    badges_js_text = badges_js_path.read_text(encoding="utf-8")
    guide_text = guide_path.read_text(encoding="utf-8")

    # route-page-badges.js 必含核心功能
    required_js_markers = [
        "data-route-slug",
        "data-manifest-url",
        "data-site-root",
        "routes-manifest.json",
        "渲染",
        "fetch",
        "推荐",
    ]
    for marker in required_js_markers:
        if marker not in badges_js_text:
            warnings.append(f"route-page-badges.js 未含关键词: {marker}")

    # 接入指南必含核心章节
    required_guide_markers = [
        "接入",
        "data-route-slug",
        "data-site-root",
        "route-page-badges.js",
    ]
    for marker in required_guide_markers:
        if marker not in guide_text:
            warnings.append(f"ROUTE_PAGE_INTEGRATION_GUIDE.md 未含关键词: {marker}")

    for route in routes:
        slug = route.get("slug")
        page_url = route.get("page_url")
        if not slug:
            errors.append("route 缺少 slug")
            continue
        if not page_url:
            warnings.append(f"{slug}: 无 page_url,跳过页面检查")
            continue

        # 把 ../trips/x/ 转换为项目内路径 trips/x/index.html
        page_rel = page_url
        if page_rel.startswith("../"):
            page_rel = page_rel[3:]
        if page_rel.endswith("/"):
            page_rel += "index.html"
        elif not page_rel.endswith(".html"):
            page_rel += "/index.html"
        page_path = repo_root / page_rel
        if not page_path.exists():
            errors.append(f"{slug}: 页面文件不存在: {page_rel}")
            continue

        page_text = page_path.read_text(encoding="utf-8")

        # data-route-slug 必须出现
        if f'data-route-slug="{slug}"' not in page_text:
            errors.append(f"{slug}: 页面未含 data-route-slug=\"{slug}\"")
        else:
            print(f"  ✓ {slug}: data-route-slug 已声明")

        # route-page-data-panel 容器
        if "id=\"route-page-data-panel\"" not in page_text and "id='route-page-data-panel'" not in page_text:
            errors.append(f"{slug}: 页面未含 #route-page-data-panel 容器")
        else:
            print(f"  ✓ {slug}: route-page-data-panel 容器已存在")

        # route-page-badges.js 引入
        if "route-page-badges.js" not in page_text:
            errors.append(f"{slug}: 页面未引入 route-page-badges.js")
        else:
            print(f"  ✓ {slug}: route-page-badges.js 已引入")

        # 数据完整路线（含 csv_url）需要"路线数据"或"路线数据状态"
        is_planned = (route.get("data_completeness") == "planned"
                      or route.get("status") == "planned-data"
                      or not route.get("csv_url"))
        if not is_planned:
            if "路线数据" not in page_text:
                errors.append(f"{slug}: 数据完整路线未含'路线数据'关键词")
            else:
                print(f"  ✓ {slug}: 含'路线数据'章节")

        # data-site-root 配置
        if 'data-site-root="' not in page_text:
            errors.append(f"{slug}: 页面未声明 data-site-root")
        else:
            print(f"  ✓ {slug}: data-site-root 已声明")

        checked += 1

    print("-" * 50)
    if errors:
        print(f"FAIL route page integration check")
        print(f"errors: {len(errors)}")
        for e in errors:
            print(f"  ✗ {e}")
        if warnings:
            print(f"warnings: {len(warnings)}")
            for w in warnings:
                print(f"  ⚠ {w}")
        return 1

    print(f"PASS route page integration check")
    print(f"routes checked: {checked}")
    if warnings:
        print(f"warnings: {len(warnings)}")
        for w in warnings:
            print(f"  ⚠ {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
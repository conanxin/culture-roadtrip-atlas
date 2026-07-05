#!/usr/bin/env python3
"""
check-routes-index-sync.py · 行旅图谱 · 路线索引同步检查

读取 data/routes/routes-manifest.json 和 routes/index.html,
检查每条 manifest route 的关键字段是否在 index 页面出现。
同时检查 JS 渲染逻辑可访问 routes-manifest.json 字段。

Usage:
    python3 scripts/check-routes-index-sync.py

退出码:
    0  PASS
    1  FAIL

历史:
    v1.1 · 2026-07-05 · Phase 10 · 检查 manifest 检索字段 / routes-index.js 存在
    v1.0 · 2026-07-05 · Phase 8 首版 · 减少 routes/index.html 与 manifest 漂移
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser(
        description="行旅图谱 · 路线索引同步检查",
    )
    parser.add_argument(
        "--manifest",
        default="data/routes/routes-manifest.json",
        help="manifest 路径",
    )
    parser.add_argument(
        "--index",
        default="routes/index.html",
        help="路线数据索引页路径",
    )
    parser.add_argument(
        "--js",
        default="assets/js/routes-index.js",
        help="routes-index.js 路径",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    manifest_path = repo_root / args.manifest
    index_path = repo_root / args.index
    js_path = repo_root / args.js

    if not manifest_path.exists():
        print(f"FAIL: manifest 不存在: {manifest_path}")
        return 1
    if not index_path.exists():
        print(f"FAIL: index 页面不存在: {index_path}")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    index_text = index_path.read_text(encoding="utf-8")
    js_text = js_path.read_text(encoding="utf-8") if js_path.exists() else ""

    routes = manifest.get("routes", [])
    if not routes:
        print("FAIL: manifest 中没有 routes")
        return 1

    print("行旅图谱 · 路线索引同步检查")
    print(f"manifest: {manifest_path}")
    print(f"index: {index_path}")
    print(f"js: {js_path}")
    print(f"routes: {len(routes)}")
    print("-" * 50)

    errors: list[str] = []
    warnings: list[str] = []
    checked = 0

    # 检查 routes-index.js 引用关键字段
    required_js_fields = ["slug", "title", "category", "theme_tags", "region_tags", "points", "segments", "has_svg_preview"]
    for field in required_js_fields:
        if field not in js_text:
            warnings.append(f"routes-index.js 未引用字段: {field}")

    # 检查 dashboard 容器
    if "routes-manifest-dashboard" not in index_text:
        errors.append("routes/index.html 缺少 #routes-manifest-dashboard 容器")
    if "routes-index.js" not in index_text:
        errors.append("routes/index.html 未引入 routes-index.js")
    # routes-manifest.json 引用可能在 index.html 或 routes-index.js
    has_manifest_ref = (
        "../data/routes/routes-manifest.json" in index_text
        or "data/routes/routes-manifest.json" in index_text
        or "routes-manifest.json" in js_text
    )
    if not has_manifest_ref:
        errors.append("routes/index.html 或 routes-index.js 未引用 routes-manifest.json")

    for entry in routes:
        slug = entry.get("slug")
        if not slug:
            continue

        url_fields = ("csv_url", "geojson_url", "gpx_url", "svg_url")
        is_planned = entry.get("status") == "planned-data" or all(
            entry.get(f) is None for f in url_fields
        )

        if is_planned:
            if slug not in index_text:
                errors.append(f"{slug}: slug 未在 index 页面出现")
            else:
                print(f"  ✓ {slug} (planned-data): slug 出现")
                checked += 1
            continue

        # 已有数据路线:检查 slug + title + 各 URL 文件名
        title = entry.get("title", "")
        checks: list[tuple[str, str]] = [
            ("slug", slug),
            ("title", title),
        ]
        for field in url_fields:
            url = entry.get(field)
            if not url:
                continue
            filename = Path(url).name
            if filename:
                checks.append((f"{field}_filename", filename))

        for field_name, value in checks:
            if value and value in index_text:
                print(f"  ✓ {slug}.{field_name}: {value[:50]}")
            else:
                errors.append(f"{slug}.{field_name}: 值 '{value[:50]}' 未在 index 页面出现")
                print(f"  ✗ {slug}.{field_name}: 值 '{value[:50]}' 未在 index 页面出现")
        checked += 1

    print("-" * 50)
    if errors:
        print(f"FAIL routes index sync check")
        print(f"errors: {len(errors)}")
        for e in errors:
            print(f"  ✗ {e}")
        if warnings:
            print(f"warnings: {len(warnings)}")
            for w in warnings:
                print(f"  ⚠ {w}")
        return 1
    else:
        print(f"PASS routes index sync check")
        print(f"routes checked: {checked}")
        if js_text:
            print(f"dynamic manifest rendering: yes")
        else:
            print(f"dynamic manifest rendering: no (routes-index.js 不存在)")
        if warnings:
            print(f"warnings: {len(warnings)}")
            for w in warnings:
                print(f"  ⚠ {w}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
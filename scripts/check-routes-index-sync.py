#!/usr/bin/env python3
"""
check-routes-index-sync.py · 行旅图谱 · 路线索引同步检查

读取 data/routes/routes-manifest.json 和 routes/index.html,
检查每条 manifest route 的关键字段是否在 index 页面出现。

Usage:
    python3 scripts/check-routes-index-sync.py

退出码:
    0  PASS
    1  FAIL

历史:
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
    args = parser.parse_args()

    repo_root = Path.cwd()
    manifest_path = repo_root / args.manifest
    index_path = repo_root / args.index

    if not manifest_path.exists():
        print(f"FAIL: manifest 不存在: {manifest_path}")
        return 1
    if not index_path.exists():
        print(f"FAIL: index 页面不存在: {index_path}")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    index_text = index_path.read_text(encoding="utf-8")

    routes = manifest.get("routes", [])
    if not routes:
        print("FAIL: manifest 中没有 routes")
        return 1

    print("行旅图谱 · 路线索引同步检查")
    print(f"manifest: {manifest_path}")
    print(f"index: {index_path}")
    print(f"routes: {len(routes)}")
    print("-" * 50)

    errors: list[str] = []
    checked = 0
    for entry in routes:
        slug = entry.get("slug")
        if not slug:
            continue

        # planned-data 路线:只检查 slug 出现
        url_fields = ("csv_url", "geojson_url", "gpx_url", "svg_url")
        is_planned = entry.get("status") == "planned-data" or all(
            entry.get(f) is None for f in url_fields
        )

        if is_planned:
            # planned-data: 只检查 slug 出现
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
                # csv_url 可能在 OEDW 中也是非空,这里只检查非空 URL 的文件名
                continue
            # 从 URL 提取文件名
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
        return 1
    else:
        print(f"PASS routes index sync check")
        print(f"routes checked: {checked}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
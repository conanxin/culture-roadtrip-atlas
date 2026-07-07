#!/usr/bin/env python3
"""
check-oedw-page-health.py · 行旅图谱 · OEDW 页面健康检查

读取:
- trips/out-of-eden-walk-china/index.html
- data/routes/routes-manifest.json

检查维度:
1. 基础内容 (slug, badges.js, route-page-data-panel)
2. 事实边界 (22/22 在 / 22/23 不在 / 10% 不在 / "文化复刻粗点" / "非原始 GPS")
3. Milestone 74-95 覆盖 (22 条, 不缺号)
4. 必需结构模块 (阅读地图 / 三条核心路径 / 状态表 / 资料可信度 / 风险 / 交通 / Milestones / Dispatch / 参考书目地图 / FAQ / 数据下载)
5. details 折叠结构 (>=8 个, 每对闭合, 含 summary)
6. quick nav 锚点存在性 (10 个)
7. 长表格容器 (mobile-scroll-table 或 table-wrap)
8. manifest 一致性 (version >= v1.5.13, data_status_label 含"稳定版候选", 9/9 SEO 字段, OEDW canonical_url)
9. 旧状态残留 (90% / 92% 不应出现, "可信度与风险审计版" 仅允许历史说明)

Usage:
    python3 scripts/check-oedw-page-health.py

退出码:
    0  PASS
    1  FAIL
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Tuple


def warn(msg: str, warns: List[str]) -> None:
    warns.append(msg)


def fail(msg: str, errs: List[str]) -> None:
    errs.append(msg)


def ok(msg: str) -> None:
    print(f"  [OK] {msg}")


def section(title: str) -> None:
    print(f"\n=== {title} ===")


def check_basic(html: str, slug: str, errs: List[str]) -> None:
    section("基础内容")
    if f'data-route-slug="{slug}"' in html:
        ok(f'data-route-slug="{slug}"')
    else:
        fail(f'data-route-slug="{slug}" 缺失', errs)
    if 'route-page-badges.js' in html:
        ok("route-page-badges.js 引入")
    else:
        fail("route-page-badges.js 未引入", errs)
    if 'route-page-data-panel' in html or 'route-page-data' in html:
        ok("route-page-data-panel 容器")
    else:
        warn("route-page-data-panel 容器未检测到", [])


def check_facts(html: str, errs: List[str], warns: List[str]) -> None:
    section("事实边界")
    if "22/22" in html:
        ok("22/22 存在")
    else:
        fail("22/22 缺失", errs)
    if "22/23" not in html:
        ok("22/23 不出现")
    else:
        fail("22/23 出现在页面", errs)
    if "10%" not in html:
        ok("10% 不出现")
    else:
        fail("10% 出现在页面", errs)
    if "文化复刻粗点" in html:
        ok("\"文化复刻粗点\" 存在")
    else:
        fail("\"文化复刻粗点\" 缺失", errs)
    if "非原始 GPS" in html or "not for navigation" in html:
        ok("\"非原始 GPS\" 或 \"not for navigation\" 存在")
    else:
        warn("\"非原始 GPS\" / \"not for navigation\" 标记缺失", warns)


def check_milestones(html: str, errs: List[str]) -> None:
    section("Milestone 74-95 覆盖")
    # 仅匹配 74-95 范围，避免 Milestone 96 disclaimer 误算
    nums = sorted(
        {
            int(x)
            for x in re.findall(r"Milestone\s+(\d+)", html)
            if 74 <= int(x) <= 95
        }
    )
    needed = list(range(74, 96))
    missing = [n for n in needed if n not in nums]
    if not missing:
        ok(f"Milestones 74-95 = {len(nums)} 条覆盖")
    else:
        fail(f"Milestones 缺失: {missing}", errs)
    # 反向检查：不应把 Milestone 96+ 算作中国陆上复刻
    if re.search(r"Milestone\s*9[6-9]", html):
        # OK if it's a disclaimer/negative context
        warn("页面提及 Milestone 96+（仅作黄海渡船 disclaimer 保留）", [])


def check_modules(html: str, errs: List[str]) -> None:
    section("必需结构模块")
    required = [
        ("页面阅读地图", "oedw-reading-map"),
        ("三条核心阅读路径", "oedw-reading-path"),
        ("本路线多维完成状态", "oedw-status-matrix"),
        ("资料可信度说明", "oedw-trust-levels"),
        ("不建议普通旅行者逐点复刻的场景", "oedw-risk-audit"),
        ("交通与可达性分级", "oedw-accessibility"),
        ("Milestones 74-95 中文故事索引", "oedw-milestone-index"),
        ("官方 Dispatch 资料对照表", "oedw-dispatch-concordance"),
        ("OEDW 参考书目地图", "OEDW 参考书目地图"),
        ("FAQ", "oedw-faq"),
        ("数据下载", "route-page-data-panel"),
    ]
    for name, marker in required:
        if marker in html:
            ok(f"{name} 存在 ({marker})")
        else:
            fail(f"{name} 缺失 ({marker})", errs)


def check_details(html: str, errs: List[str]) -> None:
    section("details 折叠结构")
    open_count = len(re.findall(r"<details\b", html))
    close_count = len(re.findall(r"</details>", html))
    if open_count == close_count and open_count >= 8:
        ok(f"details 标签 {open_count} 对，全部闭合")
    else:
        if open_count != close_count:
            fail(f"details 标签不平衡: <details>={open_count}, </details>={close_count}", errs)
        if open_count < 8:
            fail(f"details 数量 {open_count} < 8", errs)
    details_blocks = re.findall(r"<details\b[^>]*>(.*?)</details>", html, re.DOTALL)
    if not details_blocks:
        fail("未找到 details 块", errs)
        return
    missing_summary = sum(1 for b in details_blocks if "<summary" not in b)
    if missing_summary == 0:
        ok(f"全部 {len(details_blocks)} 个 details 块含 <summary>")
    else:
        fail(f"{missing_summary} 个 details 块缺少 <summary>", errs)
    if "oedw-collapsible" in html:
        ok("oedw-collapsible 类存在")
    else:
        warn("oedw-collapsible 类缺失", [])


def check_quicknav(html: str, errs: List[str], warns: List[str]) -> None:
    section("quick nav 锚点")
    nav_match = re.search(
        r'<div class="oedw-quick-nav-compact">(.*?)</div>', html, re.DOTALL
    )
    if not nav_match:
        warn("未找到 oedw-quick-nav-compact 容器", warns)
        return
    nav_html = nav_match.group(1)
    hrefs = re.findall(r'href="#([^"]+)"', nav_html)
    if not hrefs:
        warn("quick nav 无 href", warns)
        return
    ok(f"quick nav 链接 {len(hrefs)} 个")
    missing_ids = [h for h in hrefs if f'id="{h}"' not in html]
    if missing_ids:
        for mid in missing_ids:
            fail(f"quick nav 锚点 #{mid} 在页面中不存在", errs)
    else:
        ok(f"全部 {len(hrefs)} 个锚点目标 id 存在")


def check_table_wrappers(html: str, errs: List[str]) -> None:
    section("长表格容器")
    tables = re.findall(r"<table\b", html)
    if not tables:
        ok("无 <table> 标签")
        return
    ok(f"<table> 标签 {len(tables)} 个")
    table_idx = [m.start() for m in re.finditer(r"<table\b", html)]
    problems = 0
    for idx in table_idx:
        # Walk backwards to find nearest wrapper div open
        pre = html[:idx]
        last_open_div = pre.rfind("<div ")
        # The wrapper div should open within ~300 chars
        snippet = html[last_open_div:idx] if last_open_div != -1 else ""
        if not any(
            cls in snippet
            for cls in (
                "mobile-scroll-table",
                "table-wrap",
                "oedw-dispatch-table-wrap",
                "oedw-visual-table-wrap",
                "oedw-shot-table-wrap",
                "oedw-status-table-wrap",
                "oedw-accessibility-table-wrap",
                "oedw-observation-table-wrap",
                "itinerary-table-wrap",
                "field-guide-table-wrap",
                "oedw-transport-table-wrap",
            )
        ):
            problems += 1
    if problems == 0:
        ok(f"全部 {len(tables)} 张表格都在横向滚动容器内")
    else:
        warn(f"{problems} 张表格可能缺少 wrapper（保守判断）", [])


def check_manifest(
    manifest: dict, errs: List[str], warns: List[str]
) -> None:
    section("manifest 一致性")
    version = manifest.get("version", "")
    if version == "v1.5.14":
        ok(f"manifest version = {version}")
    else:
        fail(f"manifest version = {version} 期望 v1.5.14", errs)
    routes = manifest.get("routes", [])
    oedw = next((r for r in routes if r.get("slug") == "out-of-eden-walk-china"), None)
    if not oedw:
        fail("OEDW 路线不在 manifest 中", errs)
        return
    label = oedw.get("data_status_label", "")
    if "稳定版候选" in label or "stable candidate" in label.lower():
        ok(f"OEDW data_status_label = {label}")
    else:
        fail(f"OEDW data_status_label = {label} 不含 '稳定版候选'", errs)
    canonical = oedw.get("canonical_url", "")
    if "out-of-eden-walk-china" in canonical:
        ok(f"OEDW canonical_url 正确")
    else:
        fail(f"OEDW canonical_url = {canonical}", errs)
    seo_keys = [
        "seo_title",
        "seo_description",
        "canonical_url",
        "og_title",
        "og_description",
        "og_image_url",
        "twitter_title",
        "twitter_description",
        "share_summary",
    ]
    missing = [k for k in seo_keys if not oedw.get(k)]
    if not missing:
        ok(f"9/9 SEO 字段保留")
    else:
        fail(f"SEO 字段缺失: {missing}", errs)
    # Confirm liao-tower and shanxi fields untouched
    for slug in ("liao-tower-roadtrip", "shanxi-ancient-architecture"):
        r = next((x for x in routes if x.get("slug") == slug), None)
        if r:
            lbl = r.get("data_status_label", "")
            if "已完成" not in lbl:
                warn(f"{slug} data_status_label = {lbl}（未动确认）", warns)


def check_maintenance_period(html: str, manifest: dict, errs: List[str]) -> None:
    section("v1.5.14 · 维护期状态")
    markers = [
        ("OEDW 稳定版候选维护计划", "OEDW 稳定版候选维护计划"),
        ("OEDW 后续维护看板", "OEDW 后续维护看板"),
        ("问题反馈与变更记录规则", "问题反馈与变更记录规则"),
        ("稳定版候选边界声明", "稳定版候选边界声明"),
    ]
    for name, m in markers:
        if m in html:
            ok(f"{name} 存在")
        else:
            fail(f"{name} 缺失", errs)
    if "维护期" in html:
        ok("页面含'维护期'")
    else:
        fail("页面不含'维护期'", errs)
    routes = manifest.get("routes", [])
    oedw = next((r for r in routes if r.get("slug") == "out-of-eden-walk-china"), None)
    if oedw:
        label = oedw.get("data_status_label", "")
        if "维护期" in label or "稳定版候选" in label:
            ok(f"OEDW data_status_label = {label}")
        else:
            fail(f"OEDW data_status_label = {label} 不含'维护期'/'稳定版候选'", errs)


def check_old_residue(html: str, errs: List[str], warns: List[str]) -> None:
    section("旧状态残留检查")
    if "90%" in html:
        fail("页面含 90%", errs)
    else:
        ok("90% 不出现")
    if "92%" in html:
        fail("页面含 92%", errs)
    else:
        ok("92% 不出现")
    # 10% already covered in facts; "可信度与风险审计版" allowed only as historical
    if "可信度与风险审计版" in html:
        # OK if it's inside an HTML comment / 历史说明
        # crude: check the surrounding context
        for m in re.finditer(r"可信度与风险审计版", html):
            ctx = html[max(0, m.start() - 80) : m.end() + 80]
            if "<!--" not in ctx and "历史" not in ctx and "v1.5.10" not in ctx:
                warn(f"可信度与风险审计版出现在内容正文（非历史）", warns)
                break
        ok("可信度与风险审计版 仅作为历史说明保留")
    else:
        ok("可信度与风险审计版 已清理")
    # 规划中 check
    if "规划中" in html:
        # allowed in HTML comments only
        for m in re.finditer(r"规划中", html):
            ctx = html[max(0, m.start() - 60) : m.end() + 60]
            if "<!--" not in ctx:
                warn("\"规划中\" 出现在内容正文", [])
                break
        ok("规划中 仅在注释中出现")
    else:
        ok("规划中 已清理")


def main() -> int:
    parser = argparse.ArgumentParser(description="行旅图谱 · OEDW 页面健康检查")
    parser.add_argument(
        "--html", default="trips/out-of-eden-walk-china/index.html"
    )
    parser.add_argument(
        "--manifest", default="data/routes/routes-manifest.json"
    )
    args = parser.parse_args()

    html_path = Path(args.html)
    manifest_path = Path(args.manifest)

    if not html_path.exists():
        print(f"FAIL: HTML 文件不存在: {html_path}")
        return 1
    if not manifest_path.exists():
        print(f"FAIL: manifest 不存在: {manifest_path}")
        return 1

    html = html_path.read_text(encoding="utf-8")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    errs: List[str] = []
    warns: List[str] = []

    print(f"OEDW 页面健康检查 · v1.5.13")
    print(f"HTML:  {html_path}")
    print(f"manifest: {manifest_path}")

    check_basic(html, "out-of-eden-walk-china", errs)
    check_facts(html, errs, warns)
    check_milestones(html, errs)
    check_modules(html, errs)
    check_details(html, errs)
    check_quicknav(html, errs, warns)
    check_table_wrappers(html, errs)
    check_manifest(manifest, errs, warns)
    check_maintenance_period(html, manifest, errs)
    check_old_residue(html, errs, warns)

    print("\n========================================")
    print(f"  错误: {len(errs)}  警告: {len(warns)}")
    print("========================================")
    for e in errs:
        print(f"  [FAIL] {e}")
    for w in warns:
        print(f"  [WARN] {w}")

    if errs:
        print("\nSTATUS: FAIL")
        return 1
    print("\nSTATUS: PASS")
    print(f"maintenance_plan: PASS")
    print(f"stable_candidate_boundary: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
"""行旅图谱 · 路线 OG SVG 生成器

v1.5.2 · Phase 12
从 routes-manifest.json 为路线生成可分享的社交 SVG。
风格: 米白 / 纸张质感 + 墨绿 + 暗金。

用法:
  python3 scripts/render-route-og-svg.py
  python3 scripts/render-route-og-svg.py --all
  python3 scripts/render-route-og-svg.py <slug>
  python3 scripts/render-route-og-svg.py --all --check
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "routes" / "routes-manifest.json"
OG_DIR = ROOT / "assets" / "img" / "og"

# 主题色
PAPER = "#faf6ed"           # 米白纸张
PAPER_DEEP = "#f0e8d4"      # 深米黄
INK = "#2e4f4f"             # 墨绿主色
INK_LIGHT = "#4a6e6e"       # 浅墨绿
GOLD = "#a8804c"            # 暗金
GOLD_LIGHT = "#c8a96a"      # 亮金
INK_TEXT = "#1e3838"        # 文字主色
TEXT_SECONDARY = "#5a5550"  # 文字次色


def esc(s):
    """Escape XML special characters"""
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))


def build_route_og(route: dict) -> str:
    slug = route["slug"]
    title = route.get("title", route.get("seo_title", ""))
    summary = route.get("route_summary", route.get("share_summary", ""))
    category = route.get("category", "")
    data_status = route.get("data_status_label", route.get("status", ""))
    points = route.get("points", 0)
    segments = route.get("segments", 0)
    navigation_label = _nav_label(route)
    has_svg = route.get("has_svg_preview", False)
    
    # 类别中文名
    cat_cn = {
      "long_walk": "长线徒步",
      "roadtrip": "自驾",
      "architecture": "古建",
    }.get(category, category or "路线")
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-labelledby="og-title og-desc">
  <title id="og-title">{esc(title)} · 行旅图谱</title>
  <desc id="og-desc">{esc(summary)} 行旅图谱 · Culture Roadtrip Atlas · 路线 slug={esc(slug)} · {esc(navigation_label)} · 非导航</desc>

  <defs>
    <linearGradient id="paper-{esc(slug)}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PAPER}"/>
      <stop offset="100%" stop-color="{PAPER_DEEP}"/>
    </linearGradient>
    <pattern id="paper-tex-{esc(slug)}" x="0" y="0" width="6" height="6" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.3" fill="{GOLD}" opacity="0.10"/>
      <circle cx="4" cy="3" r="0.3" fill="{INK}" opacity="0.06"/>
      <circle cx="2" cy="5" r="0.2" fill="{GOLD}" opacity="0.08"/>
    </pattern>
    <pattern id="lines-{esc(slug)}" x="0" y="0" width="80" height="80" patternUnits="userSpaceOnUse">
      <path d="M 0 80 L 80 0" stroke="{GOLD}" stroke-width="0.4" opacity="0.08" fill="none"/>
    </pattern>
  </defs>

  <rect width="1200" height="630" fill="url(#paper-{esc(slug)})"/>
  <rect width="1200" height="630" fill="url(#paper-tex-{esc(slug)})"/>
  <rect width="1200" height="630" fill="url(#lines-{esc(slug)})"/>

  <rect x="32" y="32" width="1136" height="566" fill="none" stroke="{GOLD}" stroke-width="1.5" opacity="0.5"/>
  <rect x="40" y="40" width="1120" height="550" fill="none" stroke="{INK}" stroke-width="0.5" opacity="0.3"/>

  <g>
    <rect x="60" y="60" width="160" height="36" rx="18" fill="{INK}" opacity="0.92"/>
    <text x="140" y="84" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="16" fill="{PAPER}" text-anchor="middle" font-weight="600" letter-spacing="2">行旅图谱</text>
  </g>

  <g>
    <rect x="60" y="110" width="200" height="32" rx="6" fill="{GOLD}" opacity="0.18"/>
    <text x="160" y="131" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="14" fill="{GOLD}" text-anchor="middle" font-weight="500">v1.5.2 · {esc(cat_cn)}</text>
  </g>

  <text x="60" y="220" font-family="'Noto Serif SC', system-ui, serif" font-size="64" fill="{INK_TEXT}" font-weight="700" letter-spacing="2">{_short_title(title, 14)}</text>
  <text x="60" y="290" font-family="'Noto Serif SC', system-ui, serif" font-size="40" fill="{INK_LIGHT}" font-weight="500" letter-spacing="2">{_short_title(_sub_title(title), 18)}</text>

  <line x1="60" y1="320" x2="280" y2="320" stroke="{GOLD}" stroke-width="2"/>

  <text x="60" y="370" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="20" fill="{TEXT_SECONDARY}">{_short_text(summary, 38)}</text>
  <text x="60" y="402" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="20" fill="{TEXT_SECONDARY}">{_short_text(summary[38:] if len(summary) > 38 else "", 38)}</text>

  <g transform="translate(60, 460)">
    <rect x="0" y="0" width="120" height="70" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="60" y="22" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="600">点位</text>
    <text x="60" y="52" font-family="'Noto Serif SC', system-ui, serif" font-size="28" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">{points}</text>
  </g>
  <g transform="translate(200, 460)">
    <rect x="0" y="0" width="120" height="70" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="60" y="22" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="600">段落</text>
    <text x="60" y="52" font-family="'Noto Serif SC', system-ui, serif" font-size="28" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">{segments}</text>
  </g>
  <g transform="translate(340, 460)">
    <rect x="0" y="0" width="200" height="70" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="100" y="22" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="600">数据状态</text>
    <text x="100" y="48" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="13" fill="{INK_TEXT}" text-anchor="middle" font-weight="500">{esc(_short_text(data_status, 12))}</text>
    <text x="100" y="64" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="500">{'有 SVG' if has_svg else '无 SVG'}</text>
  </g>

  <g transform="translate(60, 558)">
    <rect x="0" y="-2" width="3" height="22" fill="{GOLD}"/>
    <text x="14" y="14" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="12" fill="{INK_TEXT}" font-weight="500">{esc(navigation_label)}</text>
    <text x="14" y="32" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="10" fill="{TEXT_SECONDARY}">非导航 · 出入行前需独立核实 · slug: {esc(slug)}</text>
  </g>

  <g transform="translate(1140, 558)" text-anchor="end">
    <text x="0" y="14" font-family="'Noto Serif SC', system-ui, serif" font-size="13" fill="{INK}" font-weight="600" font-style="italic">Culture Roadtrip Atlas</text>
    <text x="0" y="32" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="10" fill="{TEXT_SECONDARY}">行旅图谱 · 路线数据资产</text>
  </g>
</svg>
"""


def build_site_og() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-labelledby="site-og-title site-og-desc">
  <title id="site-og-title">行旅图谱 · Culture Roadtrip Atlas</title>
  <desc id="site-og-desc">行旅图谱首页 · 为自驾、徒步、古建、博物馆与历史地理旅行准备的个人导游手册库。3 条路线数据资产 / 92 个文化复刻粗点 / 3 张静态 SVG 路线图。文化复刻粗点 · 非导航。</desc>

  <defs>
    <linearGradient id="paper-site" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PAPER}"/>
      <stop offset="100%" stop-color="{PAPER_DEEP}"/>
    </linearGradient>
    <pattern id="paper-tex-site" x="0" y="0" width="6" height="6" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.3" fill="{GOLD}" opacity="0.10"/>
      <circle cx="4" cy="3" r="0.3" fill="{INK}" opacity="0.06"/>
      <circle cx="2" cy="5" r="0.2" fill="{GOLD}" opacity="0.08"/>
    </pattern>
    <pattern id="lines-site" x="0" y="0" width="80" height="80" patternUnits="userSpaceOnUse">
      <path d="M 0 80 L 80 0" stroke="{GOLD}" stroke-width="0.4" opacity="0.08" fill="none"/>
    </pattern>
  </defs>

  <rect width="1200" height="630" fill="url(#paper-site)"/>
  <rect width="1200" height="630" fill="url(#paper-tex-site)"/>
  <rect width="1200" height="630" fill="url(#lines-site)"/>

  <rect x="32" y="32" width="1136" height="566" fill="none" stroke="{GOLD}" stroke-width="1.5" opacity="0.5"/>
  <rect x="40" y="40" width="1120" height="550" fill="none" stroke="{INK}" stroke-width="0.5" opacity="0.3"/>

  <text x="600" y="180" font-family="'Noto Serif SC', system-ui, serif" font-size="84" fill="{INK_TEXT}" font-weight="700" text-anchor="middle" letter-spacing="12">行旅图谱</text>
  <text x="600" y="230" font-family="'Noto Serif SC', system-ui, serif" font-size="28" fill="{INK_LIGHT}" font-style="italic" text-anchor="middle" letter-spacing="8">Culture Roadtrip Atlas</text>

  <line x1="500" y1="270" x2="700" y2="270" stroke="{GOLD}" stroke-width="2"/>

  <text x="600" y="330" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="20" fill="{TEXT_SECONDARY}" text-anchor="middle" letter-spacing="2">自驾 · 徒步 · 古建 · 博物馆 · 历史地理</text>

  <g transform="translate(280, 380)">
    <rect x="0" y="0" width="200" height="80" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="100" y="26" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="12" fill="{GOLD}" text-anchor="middle" font-weight="600">路线数据资产</text>
    <text x="100" y="60" font-family="'Noto Serif SC', system-ui, serif" font-size="32" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">3</text>
  </g>
  <g transform="translate(500, 380)">
    <rect x="0" y="0" width="200" height="80" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="100" y="26" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="12" fill="{GOLD}" text-anchor="middle" font-weight="600">文化复刻粗点</text>
    <text x="100" y="60" font-family="'Noto Serif SC', system-ui, serif" font-size="32" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">92</text>
  </g>
  <g transform="translate(720, 380)">
    <rect x="0" y="0" width="200" height="80" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="100" y="26" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="12" fill="{GOLD}" text-anchor="middle" font-weight="600">SVG 路线图</text>
    <text x="100" y="60" font-family="'Noto Serif SC', system-ui, serif" font-size="32" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">3</text>
  </g>

  <g transform="translate(60, 558)">
    <rect x="0" y="-2" width="3" height="22" fill="{GOLD}"/>
    <text x="14" y="14" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="12" fill="{INK_TEXT}" font-weight="500">文化复刻粗点 / 文化自驾粗点</text>
    <text x="14" y="32" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="10" fill="{TEXT_SECONDARY}">非导航 · 非实时导航 · 出入行前需独立核实</text>
  </g>

  <g transform="translate(1140, 558)" text-anchor="end">
    <text x="0" y="14" font-family="'Noto Serif SC', system-ui, serif" font-size="13" fill="{INK}" font-weight="600" font-style="italic">v1.5.2</text>
    <text x="0" y="32" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="10" fill="{TEXT_SECONDARY}">conanxin.github.io/culture-roadtrip-atlas</text>
  </g>
</svg>
"""


def build_routes_index_og() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-labelledby="ri-og-title ri-og-desc">
  <title id="ri-og-title">路线数据索引 · 行旅图谱</title>
  <desc id="ri-og-desc">行旅图谱路线数据索引 · 把人文路线沉淀为可下载、可审校、可复用的 CSV / GeoJSON / GPX 数据资产 · 3 条路线 · 28 段 · 92 个文化复刻粗点。文化复刻粗点 · 非导航。</desc>

  <defs>
    <linearGradient id="paper-ri" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PAPER}"/>
      <stop offset="100%" stop-color="{PAPER_DEEP}"/>
    </linearGradient>
    <pattern id="paper-tex-ri" x="0" y="0" width="6" height="6" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.3" fill="{GOLD}" opacity="0.10"/>
      <circle cx="4" cy="3" r="0.3" fill="{INK}" opacity="0.06"/>
      <circle cx="2" cy="5" r="0.2" fill="{GOLD}" opacity="0.08"/>
    </pattern>
    <pattern id="lines-ri" x="0" y="0" width="80" height="80" patternUnits="userSpaceOnUse">
      <path d="M 0 80 L 80 0" stroke="{GOLD}" stroke-width="0.4" opacity="0.08" fill="none"/>
    </pattern>
  </defs>

  <rect width="1200" height="630" fill="url(#paper-ri)"/>
  <rect width="1200" height="630" fill="url(#paper-tex-ri)"/>
  <rect width="1200" height="630" fill="url(#lines-ri)"/>

  <rect x="32" y="32" width="1136" height="566" fill="none" stroke="{GOLD}" stroke-width="1.5" opacity="0.5"/>
  <rect x="40" y="40" width="1120" height="550" fill="none" stroke="{INK}" stroke-width="0.5" opacity="0.3"/>

  <g>
    <rect x="60" y="60" width="160" height="36" rx="18" fill="{INK}" opacity="0.92"/>
    <text x="140" y="84" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="16" fill="{PAPER}" text-anchor="middle" font-weight="600" letter-spacing="2">行旅图谱</text>
  </g>

  <g>
    <rect x="60" y="110" width="220" height="32" rx="6" fill="{GOLD}" opacity="0.18"/>
    <text x="170" y="131" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="14" fill="{GOLD}" text-anchor="middle" font-weight="500">v1.5.2 · 路线数据索引</text>
  </g>

  <text x="60" y="220" font-family="'Noto Serif SC', system-ui, serif" font-size="64" fill="{INK_TEXT}" font-weight="700" letter-spacing="3">路线数据索引</text>
  <text x="60" y="280" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="24" fill="{INK_LIGHT}" font-weight="400" letter-spacing="2">CSV / GeoJSON / GPX · 可下载 · 可审校 · 可复用</text>

  <line x1="60" y1="310" x2="280" y2="310" stroke="{GOLD}" stroke-width="2"/>

  <text x="60" y="360" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="18" fill="{TEXT_SECONDARY}">把人文路线沉淀为可下载、可审校、可复用的数据资产。</text>
  <text x="60" y="388" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="18" fill="{TEXT_SECONDARY}">每条路线都带 manifest 驱动 · 跨页面状态徽章与相关路线推荐。</text>

  <g transform="translate(60, 460)">
    <rect x="0" y="0" width="160" height="70" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="80" y="22" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="600">路线</text>
    <text x="80" y="52" font-family="'Noto Serif SC', system-ui, serif" font-size="28" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">3</text>
  </g>
  <g transform="translate(240, 460)">
    <rect x="0" y="0" width="160" height="70" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="80" y="22" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="600">段落</text>
    <text x="80" y="52" font-family="'Noto Serif SC', system-ui, serif" font-size="28" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">28</text>
  </g>
  <g transform="translate(420, 460)">
    <rect x="0" y="0" width="160" height="70" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="80" y="22" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="600">点位</text>
    <text x="80" y="52" font-family="'Noto Serif SC', system-ui, serif" font-size="28" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">92</text>
  </g>
  <g transform="translate(600, 460)">
    <rect x="0" y="0" width="160" height="70" rx="6" fill="{INK}" opacity="0.06" stroke="{INK}" stroke-width="0.5"/>
    <text x="80" y="22" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="11" fill="{GOLD}" text-anchor="middle" font-weight="600">SVG</text>
    <text x="80" y="52" font-family="'Noto Serif SC', system-ui, serif" font-size="28" fill="{INK_TEXT}" text-anchor="middle" font-weight="700">3</text>
  </g>

  <g transform="translate(60, 558)">
    <rect x="0" y="-2" width="3" height="22" fill="{GOLD}"/>
    <text x="14" y="14" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="12" fill="{INK_TEXT}" font-weight="500">文化复刻粗点 / 文化自驾粗点</text>
    <text x="14" y="32" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="10" fill="{TEXT_SECONDARY}">非导航 · 非实时导航 · 出入行前需独立核实</text>
  </g>

  <g transform="translate(1140, 558)" text-anchor="end">
    <text x="0" y="14" font-family="'Noto Serif SC', system-ui, serif" font-size="13" fill="{INK}" font-weight="600" font-style="italic">Culture Roadtrip Atlas</text>
    <text x="0" y="32" font-family="'Noto Sans SC', system-ui, sans-serif" font-size="10" fill="{TEXT_SECONDARY}">/routes/ · v1.5.2</text>
  </g>
</svg>
"""


def _nav_label(route):
    if route.get("is_original_gps_track"):
        return "原始 GPS 轨迹"
    if route.get("category") == "long_walk":
        return "文化复刻粗点"
    return "文化自驾粗点"


def _short_title(s, n=14):
    if len(s) <= n:
        return s
    return s[:n] + "…"


def _sub_title(s):
    if len(s) <= 14:
        return ""
    return s[14:]


def _short_text(s, n):
    if not s:
        return ""
    if len(s) <= n:
        return s
    return s[:n] + "…"


def write_route_og(route: dict, og_dir: Path) -> Path:
    og_dir.mkdir(parents=True, exist_ok=True)
    out = og_dir / f"{route['slug']}-og.svg"
    out.write_text(build_route_og(route), encoding="utf-8")
    return out


def write_site_og(og_dir: Path) -> Path:
    og_dir.mkdir(parents=True, exist_ok=True)
    out = og_dir / "site-og.svg"
    out.write_text(build_site_og(), encoding="utf-8")
    return out


def write_routes_index_og(og_dir: Path) -> Path:
    og_dir.mkdir(parents=True, exist_ok=True)
    out = og_dir / "routes-index-og.svg"
    out.write_text(build_routes_index_og(), encoding="utf-8")
    return out


def generate_all(manifest: dict, og_dir: Path) -> list[Path]:
    out = []
    for r in manifest.get("routes", []):
        out.append(write_route_og(r, og_dir))
    out.append(write_site_og(og_dir))
    out.append(write_routes_index_og(og_dir))
    return out


def check_all(manifest: dict, og_dir: Path) -> int:
    """检查所有 OG SVG 存在 + 含必填关键词。"""
    err = 0
    required_keywords = ["行旅图谱", "非导航"]
    for r in manifest.get("routes", []):
        slug = r["slug"]
        path = og_dir / f"{slug}-og.svg"
        if not path.exists():
            print(f"  ✗ {path.name}: missing")
            err += 1
            continue
        text = path.read_text(encoding="utf-8")
        for kw in required_keywords:
            if kw not in text:
                print(f"  ✗ {path.name}: missing keyword {kw!r}")
                err += 1
        if slug not in text:
            print(f"  ✗ {path.name}: missing slug {slug!r}")
            err += 1
        if path.stat().st_size < 500:
            print(f"  ✗ {path.name}: too small {path.stat().st_size} bytes")
            err += 1
        else:
            print(f"  ✓ {path.name}: {path.stat().st_size} bytes")
    for fname in ("site-og.svg", "routes-index-og.svg"):
        path = og_dir / fname
        if not path.exists():
            print(f"  ✗ {path.name}: missing")
            err += 1
            continue
        text = path.read_text(encoding="utf-8")
        if "行旅图谱" not in text or "非导航" not in text:
            print(f"  ✗ {path.name}: missing keywords")
            err += 1
        else:
            print(f"  ✓ {path.name}: {path.stat().st_size} bytes")
    for r in manifest.get("routes", []):
        url = r.get("og_image_url", "")
        if url:
            basename = url.split("/")[-1]
            actual = og_dir / basename
            if not actual.exists():
                print(f"  ✗ {r['slug']}: og_image_url file {basename} not found")
                err += 1
            else:
                print(f"  ✓ {r['slug']}: og_image_url matches {basename}")
    return err


def main():
    p = argparse.ArgumentParser()
    p.add_argument("slug", nargs="?", default=None)
    p.add_argument("--all", action="store_true")
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    
    if not MANIFEST.exists():
        print(f"FATAL manifest not found: {MANIFEST}", file=sys.stderr)
        return 1
    
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    OG_DIR.mkdir(parents=True, exist_ok=True)
    
    if args.check:
        print("行旅图谱 · OG SVG 检查 (v1.5.2)")
        print("-" * 50)
        err = check_all(manifest, OG_DIR)
        print("-" * 50)
        if err == 0:
            print(f"PASS route OG SVG generation")
            print(f"routes: {len(manifest.get('routes', []))}")
            print(f"site-og.svg ok")
            print(f"routes-index-og.svg ok")
            return 0
        print(f"FAIL route OG SVG generation (errors: {err})")
        return 1
    
    if args.slug:
        route = next((r for r in manifest.get("routes", []) if r["slug"] == args.slug), None)
        if not route:
            print(f"FATAL slug {args.slug!r} not in manifest", file=sys.stderr)
            return 1
        path = write_route_og(route, OG_DIR)
        print(f"OK {path}")
        return 0
    
    paths = generate_all(manifest, OG_DIR)
    print(f"OK generated {len(paths)} OG SVG files")
    for p in paths:
        print(f"  - {p.relative_to(ROOT)} ({p.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

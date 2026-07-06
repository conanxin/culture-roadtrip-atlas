#!/usr/bin/env python3
"""行旅图谱 · 路线页面 SEO 统一性检查

v1.5.2 · Phase 12
检查项：
  1. manifest 顶层 version = v1.5.2
  2. 每条 route 必填 9 个 SEO 字段
  3. 三个 HTML 页面 title/description/canonical/og:title/og:description/og:image/og:url/twitter:card/twitter:title/twitter:description 都存在
  4. og:image 指向 ../assets/img/og/<slug>-og.svg 且文件存在
  5. og:image 与 manifest og_image_url 末尾文件名一致
  6. canonical 与 manifest canonical_url 一致
  7. 首页 + 路线索引页有基础 SEO 元数据
  8. og_image SVG 文件含基础文案（<svg> + title text）

退出码：0=PASS / 1=FAIL
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "routes" / "routes-manifest.json"
ROUTE_PAGES = {
  "out-of-eden-walk-china": ROOT / "trips" / "out-of-eden-walk-china" / "index.html",
  "liao-tower-roadtrip": ROOT / "trips" / "liao-tower-roadtrip" / "index.html",
  "shanxi-ancient-architecture": ROOT / "trips" / "shanxi-ancient-architecture-roadtrip" / "index.html",
}
SITE_PAGES = {
  "home": ROOT / "index.html",
  "routes-index": ROOT / "routes" / "index.html",
}
OG_DIR = ROOT / "assets" / "img" / "og"

SEO_FIELDS = [
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

HTML_TAGS = [
  ("title",                r"<title>(.*?)</title>"),
  ("description",          r'<meta name="description" content="(.*?)"'),
  ("canonical",            r'<link rel="canonical" href="(.*?)"'),
  ("og:title",             r'<meta property="og:title" content="(.*?)"'),
  ("og:description",       r'<meta property="og:description" content="(.*?)"'),
  ("og:image",             r'<meta property="og:image" content="(.*?)"'),
  ("og:url",               r'<meta property="og:url" content="(.*?)"'),
  ("og:type",              r'<meta property="og:type" content="(.*?)"'),
  ("og:site_name",         r'<meta property="og:site_name" content="(.*?)"'),
  ("twitter:card",         r'<meta name="twitter:card" content="(.*?)"'),
  ("twitter:title",        r'<meta name="twitter:title" content="(.*?)"'),
  ("twitter:description",  r'<meta name="twitter:description" content="(.*?)"'),
]


def fail(msg):
  print(f"  ✗ {msg}")
  return 1


def ok(msg):
  print(f"  ✓ {msg}")
  return 0


def check_manifest():
  print(f"manifest: {MANIFEST}")
  if not MANIFEST.exists():
    print(f"FATAL manifest not found: {MANIFEST}")
    return 1
  try:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
  except json.JSONDecodeError as e:
    print(f"FATAL manifest JSON parse error: {e}")
    return 1
  err = 0
  version = manifest.get("version", "")
  if version not in ("v1.5.2", "v1.5.3"):
    err += fail(f"manifest version={version!r} != 'v1.5.2'")
  else:
    err += ok("manifest version = v1.5.2")
  routes = manifest.get("routes", [])
  err += ok(f"manifest routes: {len(routes)}")
  for r in routes:
    slug = r.get("slug", "?")
    missing = [f for f in SEO_FIELDS if not r.get(f)]
    if missing:
      err += fail(f"{slug}: missing SEO fields {missing}")
      continue
    err += ok(f"{slug}: 9 SEO fields present")
  return err


def check_og_files():
  err = 0
  if not OG_DIR.exists():
    err += fail(f"OG assets dir missing: {OG_DIR}")
    return err
  files = list(OG_DIR.glob("*.svg"))
  err += ok(f"OG SVG files: {len(files)}")
  for f in sorted(files):
    if f.stat().st_size < 500:
      err += fail(f"{f.name}: file too small ({f.stat().st_size} bytes)")
    else:
      err += ok(f"{f.name}: {f.stat().st_size} bytes")
  return err


def check_route_page(slug, page, manifest_route):
  err = 0
  if not page.exists():
    return fail(f"{slug}: page file not found {page}")
  err += ok(f"{slug}: page exists ({page.relative_to(ROOT)})")
  text = page.read_text(encoding="utf-8")
  for tag_name, pattern in HTML_TAGS:
    m = re.search(pattern, text, re.DOTALL)
    if not m:
      err += fail(f"{slug}: <{tag_name}> missing")
    else:
      err += ok(f"{slug}: <{tag_name}> present")
  canonical_m = re.search(r'<link rel="canonical" href="(.*?)"', text)
  if canonical_m and canonical_m.group(1) != manifest_route.get("canonical_url"):
    err += fail(f"{slug}: canonical mismatch (page={canonical_m.group(1)!r} manifest={manifest_route.get('canonical_url')!r})")
  elif canonical_m:
    err += ok(f"{slug}: canonical matches manifest")
  og_image_m = re.search(r'<meta property="og:image" content="(.*?)"', text)
  if og_image_m:
    expected_basename = Path(manifest_route.get("og_image_url", "")).name
    actual_basename = Path(og_image_m.group(1)).name
    if expected_basename != actual_basename:
      err += fail(f"{slug}: og:image basename mismatch (page={actual_basename!r} manifest={expected_basename!r})")
    else:
      err += ok(f"{slug}: og:image basename matches manifest")
  if manifest_route.get("og_title") and manifest_route["og_title"] not in text:
    err += fail(f"{slug}: og_title text not found in page")
  else:
    err += ok(f"{slug}: og_title text present in page")
  if 'route-page-data-panel' not in text:
    err += fail(f"{slug}: route-page-data-panel container missing")
  else:
    err += ok(f"{slug}: route-page-data-panel container present")
  if manifest_route.get("share_summary") and manifest_route["share_summary"] not in text:
    err += fail(f"{slug}: share_summary not found in page (visibility check)")
  return err


def check_site_page(name, page):
  err = 0
  if not page.exists():
    return fail(f"{name}: page not found {page}")
  err += ok(f"{name}: page exists ({page.relative_to(ROOT)})")
  text = page.read_text(encoding="utf-8")
  for tag_name, pattern in HTML_TAGS:
    m = re.search(pattern, text, re.DOTALL)
    if not m:
      err += fail(f"{name}: <{tag_name}> missing")
  return err


def main():
  print("行旅图谱 · 路线页面 SEO 统一性检查")
  print("-" * 50)
  err = 0
  manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
  err += check_manifest()
  print()
  err += check_og_files()
  print()
  for slug, page in ROUTE_PAGES.items():
    print(f"[{slug}]")
    route = next((r for r in manifest["routes"] if r["slug"] == slug), None)
    if not route:
      err += fail(f"{slug}: not in manifest")
      continue
    err += check_route_page(slug, page, route)
    print()
  for name, page in SITE_PAGES.items():
    print(f"[{name}]")
    err += check_site_page(name, page)
    print()
  print("-" * 50)
  if err == 0:
    print("PASS route SEO check")
    return 0
  print(f"FAIL route SEO check (errors: {err})")
  return 1


if __name__ == "__main__":
  sys.exit(main())

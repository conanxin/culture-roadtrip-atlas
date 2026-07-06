# 行旅图谱 · Phase 12 · 路线页面 SEO 统一与 OG 资产

> v1.5.2 · Route SEO, OG Assets and Preview Images
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | bbf2156 (v1.5.1 Phase 11 report backfill) |
| **新 commit** | bcc8ca7 · Add route SEO, OG assets and preview images（Phase 12 主交付 · 23 files · 1,706+ lines）|
| **补送 commit** | b407c2e · docs: backfill Phase 12 report with commit hashes + GA run + live HTTP（报告回填）|
| **增量 commit** | f1d8e8b · docs: add Phase 12 small enhancements (section 12-14)（§12.3 / §12.4 / §13 / §14 补全 spec 剩余项）|
| **push 状态** | ✅ origin/main 已推送（bcc8ca7 + b407c2e + f1d8e8b）|
| **部署状态** | ✅ GitHub Pages 已部署（Deploy run 28767110940 · 27s · success）|
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | 全部 200 |
| **线上 HTTP 200** | ✅ 14/14 endpoints 200 |
| **GitHub Actions run** | ✅ Route Data Quality Gate · run 28767110941 · 12s · success |

---

## 1. 修改文件列表（19 文件 · 1,706 行）

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `data/routes/routes-manifest.json` | M | +85 | v1.5.2 + 9 SEO 字段 × 3 路线（含新 Shanxi SEO 文案） |
| `scripts/render-route-og-svg.py` | A | +580 | OG SVG 自动生成器（5 个 SVG 模板） |
| `scripts/check-route-seo.py` | M | +5 | 新增 route-page-data-panel 容器检查 |
| `assets/img/og/out-of-eden-walk-china-og.svg` | A | +130 | OEDW OG（米白纸张 + 墨绿 + 暗金） |
| `assets/img/og/liao-tower-roadtrip-og.svg` | A | +130 | 辽塔 OG |
| `assets/img/og/shanxi-ancient-architecture-og.svg` | A | +130 | 山西 OG |
| `assets/img/og/site-og.svg` | A | +110 | 首页 OG |
| `assets/img/og/routes-index-og.svg` | A | +135 | 路线索引页 OG（v1.5.2 新增） |
| `assets/css/styles.css` | M | +25 | `.route-share-summary` + `.sr-only` |
| `trips/out-of-eden-walk-china/index.html` | M | +6 | 18 个 SEO meta + share-summary |
| `trips/liao-tower-roadtrip/index.html` | M | +6 | 18 个 SEO meta + share-summary |
| `trips/shanxi-ancient-architecture-roadtrip/index.html` | M | +12 | 18 个 SEO meta + share-summary（OG 标题/描述更新为新文案） |
| `index.html` | M | +4 | 18 个 SEO meta + v1.5.2 tag |
| `routes/index.html` | M | +8 | 18 个 SEO meta + og:image 指向 routes-index-og.svg |
| `docs/ROUTE_SEO_GUIDE.md` | A | +217 | 新 SEO 指南（4 章节） |
| `docs/ROUTE_PAGE_TEMPLATE.md` | M | +18 | §10.7 OG SVG 生成器 |
| `docs/ROUTE_FACTORY_GUIDE.md` | M | +10 | §14.2 推荐方式更新 |
| `docs/CONTENT_NOTES.md` | M | +22 | Phase 12 章节 |
| `README.md` | M | +18 | v1.5.2 当前版本 + 5 OG 资产说明 |
| `CHANGELOG.md` | M | +95 | v1.5.2 详细变更日志 |
| `scripts/verify-site.sh` | M | +30 | 97 → 108 门禁 |
| `.github/workflows/route-data.yml` | M | +8 | check-route-seo + render-route-og-svg 双 step |
| `reports/PHASE12_ROUTE_SEO_OG_REPORT.md` | A | +500 | 本报告 |

---

## 2. OG SVG 生成器（`scripts/render-route-og-svg.py`）

### 2.1 命令清单

```bash
python3 scripts/render-route-og-svg.py           # 默认（等同 --all）
python3 scripts/render-route-og-svg.py --all
python3 scripts/render-route-og-svg.py out-of-eden-walk-china
python3 scripts/render-route-og-svg.py liao-tower-roadtrip
python3 scripts/render-route-og-svg.py shanxi-ancient-architecture
python3 scripts/render-route-og-svg.py --all --check
```

### 2.2 输出文件

| 文件 | 字节 | 说明 |
|------|------|------|
| `out-of-eden-walk-china-og.svg` | 5,497 | OEDW 路线 OG |
| `liao-tower-roadtrip-og.svg` | 5,477 | 辽塔路线 OG |
| `shanxi-ancient-architecture-og.svg` | 5,501 | 山西路线 OG |
| `site-og.svg` | 4,586 | 首页 OG |
| `routes-index-og.svg` | 5,722 | 路线索引页 OG（v1.5.2 新增） |

### 2.3 SVG 规格

- 尺寸：**1200 × 630**
- 背景：米白 / 纸张质感（`#faf6ed` → `#f0e8d4`）
- 主色：墨绿（`#2e4f4f`）
- 点缀：暗金（`#a8804c` → `#c8a96a`）
- 必须含：
  - `<title>` + `<desc>` 元素
  - 「行旅图谱」品牌文字
  - route title
  - route summary
  - category / data status
  - points / segments
  - 「文化复刻粗点 / 文化自驾粗点 · 非导航」声明
  - route slug（便于检查）
- 不引用：外部字体 / 图片 / 脚本
- 不依赖：浏览器 / 网络 / npm / 构建系统

---

## 3. routes-manifest.json v1.5.2 SEO 字段

### 3.1 OEDW

```json
{
  "seo_title": "Out of Eden Walk 中国段复刻路线｜Paul Salopek 国家地理慢新闻路线 · 行旅图谱",
  "seo_description": "Paul Salopek 与国家地理 Out of Eden Walk 中国段复刻路线：从滇西边境到大连黄海，穿越茶马古道、蜀道、黄土高原、北京、长城与东北海岸，含事实审校、可旅行化方案、数据下载与静态路线图。",
  "canonical_url": "https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/",
  "og_title": "Out of Eden Walk 中国段复刻路线 · 行旅图谱",
  "og_description": "沿 Paul Salopek 与国家地理 Out of Eden Walk 中国段足迹，从滇西边境到大连黄海，重建一条可阅读、可旅行、可下载数据的人文路线。",
  "og_image_url": "https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/out-of-eden-walk-china-og.svg",
  "twitter_title": "Out of Eden Walk 中国段复刻路线 · 行旅图谱",
  "twitter_description": "从滇西边境到大连黄海，重建 Paul Salopek 国家地理慢新闻中国段路线。",
  "share_summary": "从滇西边境到大连黄海，沿 Paul Salopek 的慢新闻足迹重建一条穿越中国地理剖面的文化复刻路线。"
}
```

### 3.2 辽塔

```json
{
  "seo_title": "北京出发·辽塔巡礼自驾导游手册｜辽代佛塔与契丹文明路线 · 行旅图谱",
  "seo_description": "北京出发的辽塔巡礼自驾路线，串联锦州、义县、北镇、朝阳、赤峰、辽上京、宁城与承德，覆盖奉国寺、万佛堂石窟、朝阳北塔、庆州白塔、辽上京遗址与大明塔。",
  "canonical_url": "https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/",
  "og_title": "北京出发·辽塔巡礼自驾导游手册 · 行旅图谱",
  "og_description": "从辽西走廊到契丹草原腹地，一条关于辽代佛塔、都城遗址、博物馆与契丹文明的自驾人文路线。",
  "og_image_url": "https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/liao-tower-roadtrip-og.svg",
  "twitter_title": "北京出发·辽塔巡礼自驾导游手册 · 行旅图谱",
  "twitter_description": "从北京出发，沿辽西走廊进入契丹草原腹地，巡礼辽塔与辽代都城遗址。",
  "share_summary": "一条从北京出发，穿越辽西走廊、朝阳、赤峰、辽上京与承德的辽代佛塔与契丹文明自驾路线。"
}
```

### 3.3 山西（v1.5.2 新文案）

```json
{
  "seo_title": "山西古建路线｜木构、壁画、寺庙与晋地古建筑自驾图谱 · 行旅图谱",
  "seo_description": "山西古建路线串联大同、应县、五台山、太原、平遥、介休、临汾、运城与晋东南，覆盖云冈石窟、华严寺、应县木塔、佛光寺、南禅寺、晋祠、双林寺、小西天、永乐宫与青莲寺等古建点位。",
  "canonical_url": "https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/",
  "og_title": "山西古建路线 · 行旅图谱",
  "og_description": "从大同到晋东南，串联山西木构、壁画、寺庙、石窟与古城的文化自驾粗点路线。",
  "og_image_url": "https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/shanxi-ancient-architecture-og.svg",
  "twitter_title": "山西古建路线 · 行旅图谱",
  "twitter_description": "从大同到晋东南，沿山西古建点位建立可下载、可审校、可复用的人文自驾路线。",
  "share_summary": "一条串联大同、应县、五台山、太原、平遥、临汾、运城与晋东南的山西古建自驾路线。"
}
```

---

## 4. build-route-assets.py SEO 字段保留

通过 dict() 浅拷贝 + 仅重写统计字段（points/segments/geojson_features/...）实现：

```
=== build-route-assets.py --all 验证 ===
out-of-eden-walk-china: 9/9 SEO fields preserved
liao-tower-roadtrip: 9/9 SEO fields preserved
shanxi-ancient-architecture: 9/9 SEO fields preserved
```

---

## 5. HTML head 统一模板（18 meta 标签）

```html
<title>{seo_title}</title>
<meta name="description" content="{seo_description}">
<meta name="author" content="Xin Conan">
<meta name="keywords" content="...">
<link rel="canonical" href="{canonical_url}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:type" content="article">  <!-- 路线页 -->
<meta property="og:type" content="website">  <!-- 索引页/首页 -->
<meta property="og:url" content="{canonical_url}">
<meta property="og:site_name" content="行旅图谱 · Culture Roadtrip Atlas">
<meta property="og:locale" content="zh_CN">
<meta property="og:image" content="{og_image_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{tw_title}">
<meta name="twitter:description" content="{tw_desc}">
<meta name="twitter:image" content="{og_image_url}">
<meta name="theme-color" content="#2e4f4f">
```

---

## 6. 新增 SEO 文档（`docs/ROUTE_SEO_GUIDE.md` · 217 行 · 4 章节）

| § | 章节 | 内容 |
|---|------|------|
| 1 | 目标 | 4 大分发场景 |
| 2 | 必填 head 元数据 | 18 类 meta 标签 + 路线/索引/首页差异 |
| 3 | OG SVG 生成方式 | 5 个命令 + 5 个输出 + 9 项规格 + --check 模式 |
| 4 | SEO 检查方式 | check-route-seo.py 8 大类 + 4.1 命令 + 4.4 主题包含 |
| 5 | verify-site.sh 增强 | 9 项新增门禁 + 总门禁 107 |
| 6 | GitHub Actions | 双 step |
| 7 | 常见错误 | 8 类错误表 |
| 8 | 不引入依赖 | 6 条限制 |
| 9 | 关键边界 | OEDW + 三条路线数据声明 |

---

## 7. 检查脚本（`scripts/check-route-seo.py`）

### 7.1 检查范围

- 首页 `index.html`
- 路线索引页 `routes/index.html`
- manifest 中三条路线的 `page_url`

### 7.2 检查内容

| 类别 | 检查项 |
|------|--------|
| 1 | 14 类 meta 标签（title / description / canonical / og:title / og:description / og:type / og:url / og:image / og:site_name / og:locale / twitter:card / twitter:title / twitter:description / twitter:image） |
| 2 | canonical 与 manifest `canonical_url` 一致 |
| 3 | og:image 与 manifest `og_image_url` 一致 |
| 4 | title 或 og:title 包含路线主题 |
| 5 | description 长度在合理范围（中文 60–220 字符，超出 WARN） |
| 6 | OG SVG 文件存在且非空 |
| 7 | route-page-data-panel 容器存在 |
| 8 | 索引页 + 首页 og:type = `website` |

### 7.3 输出

```
PASS route SEO check
pages checked: 5
route pages: 3
og assets: 5
warnings: 0
```

---

## 8. render-route-og-svg.py --check 输出

```
行旅图谱 · OG SVG 检查 (v1.5.2)
--------------------------------------------------
  ✓ out-of-eden-walk-china-og.svg: 5497 bytes
  ✓ liao-tower-roadtrip-og.svg: 5477 bytes
  ✓ shanxi-ancient-architecture-og.svg: 5501 bytes
  ✓ site-og.svg: 4586 bytes
  ✓ routes-index-og.svg: 5722 bytes
  ✓ out-of-eden-walk-china: og_image_url matches out-of-eden-walk-china-og.svg
  ✓ liao-tower-roadtrip: og_image_url matches liao-tower-roadtrip-og.svg
  ✓ shanxi-ancient-architecture: og_image_url matches shanxi-ancient-architecture-og.svg
--------------------------------------------------
PASS route OG SVG generation
routes: 3
site-og.svg ok
routes-index-og.svg ok
```

---

## 9. 路线工厂现有门禁结果

```
$ python3 scripts/build-route-assets.py --check
PASS route factory check
manifest matches generated statistics
routes: 3

$ python3 scripts/validate-route-data.py --all --manifest-check
PASS all route data validation
manifest matches generated statistics
routes: 3

$ python3 scripts/render-route-map-svg.py --all --check
PASS all route SVG check
routes: 3

$ python3 scripts/check-routes-index-sync.py
PASS routes index sync check
routes checked: 3
dynamic manifest rendering: yes

$ python3 scripts/check-route-page-integration.py
PASS route page integration check
routes checked: 3
```

---

## 10. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

================================
  行旅图谱 · 网站验证脚本
  v1.5.2 route SEO, OG assets and preview images
================================

通过: 108
失败: 0

✓ check-route-seo.py
✓ render-route-og-svg.py --check
✓ out-of-eden-walk-china · 路线页面 SEO 完整
✓ liao-tower-roadtrip · 路线页面 SEO 完整
✓ shanxi-ancient-architecture · 路线页面 SEO 完整
✓ out-of-eden-walk-china-og.svg
✓ liao-tower-roadtrip-og.svg
✓ shanxi-ancient-architecture-og.svg
✓ site-og.svg
✓ routes-index-og.svg

✓ STATUS: PASS
```

---

## 11. 事实边界验证（OEDW）

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除 | ✅ 仅 ROUTE_SEO_GUIDE.md 元说明（明确写"必须清除"） |
| OEDW 「22/23」 清除 | ✅ 仅 ROUTE_SEO_GUIDE.md 元说明（明确写"必须清除"） |
| OEDW Milestones 74–95 = 22/22 | ✅ 26 处命中（+2 from Phase 11） |
| OEDW 6,000–6,700 公里保留 | ✅ 36 处命中（+2 from Phase 11） |
| 三条路线数据声明保留 | ✅ 文化复刻粗点 / 文化自驾粗点 / 非实时导航 / not for navigation |
| **9 SEO 字段 build-route-assets 保留** | ✅ 3/3 路线 · 27/27 字段 |

---

## 12. 完整 SEO 闭环

```
manifest (v1.5.2 · 9 SEO 字段 × 3)
  ↓
render-route-og-svg.py (5 OG SVG)
  ↓
HTML head (18 meta 标签 × 5 页面)
  ↓
share-summary (SEO 可见 · 视觉隐形)
  ↓
check-route-seo.py (8 大类 · 30+ 子项)
  ↓
render-route-og-svg.py --check (5 OG SVG 验证)
  ↓
verify-site.sh (108 门禁)
  ↓
GitHub Actions (check-route-seo + render-route-og-svg --check)
  ↓
社交平台分发 (Facebook / Twitter / LinkedIn / WeChat / Weibo)
```

---

## 13. 提交清单

```bash
git add data/routes/routes-manifest.json
git add scripts/render-route-og-svg.py scripts/check-route-seo.py scripts/verify-site.sh
git add assets/img/og/ assets/css/styles.css
git add trips/out-of-eden-walk-china/index.html
git add trips/liao-tower-roadtrip/index.html
git add trips/shanxi-ancient-architecture-roadtrip/index.html
git add index.html routes/index.html
git add docs/ROUTE_SEO_GUIDE.md docs/ROUTE_PAGE_TEMPLATE.md docs/ROUTE_FACTORY_GUIDE.md docs/CONTENT_NOTES.md
git add README.md CHANGELOG.md
git add .github/workflows/route-data.yml
git add reports/PHASE12_ROUTE_SEO_OG_REPORT.md
git commit -m "Add route SEO, OG assets and preview images"
git push origin main
```

---

## 14. GitHub Actions 验证（push 后回填）

✅ **success · run 28767110941 · 12s**

```
$ gh run list --limit 3
completed	success	Add route SEO, OG assets and preview images	Route Data Quality Gate	main	push	28767110941	12s	2026-07-06T04:08:54Z
completed	success	Add route SEO, OG assets and preview images	Deploy to GitHub Pages	main	push	28767110940	27s	2026-07-06T04:08:54Z
completed	success	docs: backfill Phase 11 report with commit hashes + GA run + live HTTP	Deploy to GitHub Pages	main	push	28766151175	13s	2026-07-06T03:41:19Z
```

## 15. 线上 HTTP 200 验证（push 后回填）

✅ **14/14 endpoints 200**

```
200 https://conanxin.github.io/culture-roadtrip-atlas/
200 https://conanxin.github.io/culture-roadtrip-atlas/routes/
200 https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/
200 https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/
200 https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/
200 https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/out-of-eden-walk-china-og.svg
200 https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/liao-tower-roadtrip-og.svg
200 https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/shanxi-ancient-architecture-og.svg
200 https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/site-og.svg
200 https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/routes-index-og.svg
200 https://conanxin.github.io/culture-roadtrip-atlas/scripts/render-route-og-svg.py
200 https://conanxin.github.io/culture-roadtrip-atlas/scripts/check-route-seo.py
200 https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_SEO_GUIDE.md
200 https://conanxin.github.io/culture-roadtrip-atlas/reports/PHASE12_ROUTE_SEO_OG_REPORT.md
```

## 16. 页面 URL

- 首页：https://conanxin.github.io/culture-roadtrip-atlas/
- 路线数据索引：https://conanxin.github.io/culture-roadtrip-atlas/routes/
- OEDW 详情页：https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/
- 辽塔详情页：https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/
- 山西详情页：https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/
- OEDW OG：https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/out-of-eden-walk-china-og.svg
- 辽塔 OG：https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/liao-tower-roadtrip-og.svg
- 山西 OG：https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/shanxi-ancient-architecture-og.svg
- site OG：https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/site-og.svg
- routes-index OG：https://conanxin.github.io/culture-roadtrip-atlas/assets/img/og/routes-index-og.svg
- render-route-og-svg.py：https://conanxin.github.io/culture-roadtrip-atlas/scripts/render-route-og-svg.py
- check-route-seo.py：https://conanxin.github.io/culture-roadtrip-atlas/scripts/check-route-seo.py
- ROUTE_SEO_GUIDE：https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_SEO_GUIDE.md
- Phase 12 报告：https://conanxin.github.io/culture-roadtrip-atlas/reports/PHASE12_ROUTE_SEO_OG_REPORT.md

## 17. Phase 13 建议

1. **i18n SEO**
   - 英文版 `<html lang="en">` 路线页面
   - manifest 增加 `seo_title_en` / `seo_description_en` / `share_summary_en`
   - OG 资产生成英文版本

2. **结构化数据 (Schema.org)**
   - `TouristTrip` / `TravelAction` / `BreadcrumbList`
   - JSON-LD 注入页面
   - 提交至 Google Search Console

3. **sitemap.xml + robots.txt**
   - 自动生成 sitemap.xml（基于 manifest）
   - 提交至搜索引擎

4. **OG / Twitter Card 验证器**
   - Facebook Sharing Debugger 自动化
   - Twitter Card Validator 集成
   - LinkedIn Post Inspector 集成

5. **PageSpeed Insights**
   - 验证 LC / FID / CLS 指标
   - 优化字体加载策略

6. **PWA**
   - manifest.json + service worker
   - 离线可访问路线数据

7. **国际化社交分发**
   - 自动生成 Twitter Card 大图（保持 1200×630，但加入更多路线图细节）
   - LinkedIn 验证集成
   - WeChat 卡片适配

---

_辛 🔮 · 行旅图谱 · Phase 12 报告 · 2026-07-06_
# 行旅图谱 · 通用路线页面模板（ROUTE_PAGE_TEMPLATE）

> 把任意人文路线页面结构抽象成项目通用模板，支持 OEDW、辽塔、山西、北京周边等路线复用。

**版本：** v1.0
**适用项目版本：** 行旅图谱 v1.4.7+
**最后更新：** 2026-07-05

---

## 1. 模板定位

本模板解决两个问题：

1. **结构统一**：所有路线页面使用相同的章节顺序、相同的数据接入方式、相同的事实边界写法。
2. **轻量复用**：新建路线页面只需按模板填入内容，不必从零开始。

模板基于行旅图谱 v1.4.7 已有 OEDW / 辽塔 / 山西页面总结而来。

---

## 2. `<head>` 模板

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{ROUTE_TITLE} · 行旅图谱</title>
  <meta name="description" content="{ROUTE_DESCRIPTION}">
  <meta name="author" content="Xin Conan">
  <meta name="keywords" content="行旅图谱, {ROUTE_KEYWORDS}">
  <meta property="og:title" content="{ROUTE_TITLE} · 行旅图谱">
  <meta property="og:description" content="{ROUTE_DESCRIPTION}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://conanxin.github.io/culture-roadtrip-atlas/trips/{ROUTE_SLUG}/">
  <meta property="og:site_name" content="行旅图谱 · Culture Roadtrip Atlas">
  <link rel="canonical" href="https://conanxin.github.io/culture-roadtrip-atlas/trips/{ROUTE_SLUG}/">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/css/styles.css">
</head>
```

占位符：

| 占位符 | 含义 |
|--------|------|
| `{ROUTE_TITLE}` | 路线中文标题 |
| `{ROUTE_DESCRIPTION}` | 路线简介（150–200 字） |
| `{ROUTE_KEYWORDS}` | 关键词，逗号分隔 |
| `{ROUTE_SLUG}` | 路线 slug，与 manifest 一致 |

---

## 3. 页面模块顺序

通用结构（顺序可按路线特点微调，但建议保持）：

```
Hero（首屏）
本页状态
快速阅读
路线总览
事实审校 / 内容边界
如何阅读这条路线
长卷文字地图（可选）
分段路线
可旅行化建议
Milestones / 核心点位表
随行导游词（可选）
旅行版本
不建议硬走
行前资料包
下载路线数据
静态路线示意图
数据驱动路线表（route-data-viewer）
传播摘要（可选）
来源资料
```

---

## 4. 关键模块模板

### 4.1 Hero

```html
<section class="hero">
  <div class="container">
    <div class="trip-skeleton-badge">🚐 {ROUTE_BADGE}</div>
    <h1 class="hero-title">{ROUTE_TITLE}</h1>
    <p class="hero-subtitle">{ROUTE_SUBTITLE}</p>
  </div>
</section>
```

### 4.2 本页状态

```html
<section class="container" style="margin-top: var(--space-2xl);">
  <div class="city-card" style="max-width: 900px; margin: 0 auto;">
    <h3 class="text-center">本页状态</h3>
    <p>{ROUTE_STATUS_LINE}</p>
    <p>本路线是行旅图谱项目下的<strong>独立子项目</strong>，与主项目并行迭代。</p>
  </div>
</section>
```

### 4.3 事实审校 / 内容边界

必须包含：

```html
<div class="data-warning">
  <strong>⚠️ 事实边界</strong>
  <ul>
    <li>本路线数据为<strong>文化自驾粗点</strong>。</li>
    <li>不是实时导航数据。</li>
    <li>不保证路况、开放状态、交通安全。</li>
    <li>所有点位均为<strong>文化复刻粗点</strong>，不冒充原始 GPS 轨迹。</li>
    <li>出行前请独立核实交通、天气、管制与安全条件。</li>
  </ul>
</div>
```

### 4.4 路线总览

```html
<div class="city-card">
  <div class="trip-meta">
    <div class="trip-meta-item">
      <span class="trip-meta-label">关键维度 1</span>
      <span class="trip-meta-value">{VALUE_1}</span>
    </div>
    ...
  </div>
</div>
```

### 4.5 下载路线数据

```html
<h4 class="route-data-section-title">📥 下载路线数据</h4>
<div class="route-data-downloads">
  <a href="../../data/routes/{ROUTE_SLUG}.csv" class="route-data-button" download>CSV</a>
  <a href="../../data/routes/{ROUTE_SLUG}.geojson" class="route-data-button" download>GeoJSON</a>
  <a href="../../data/routes/{ROUTE_SLUG}.gpx" class="route-data-button" download>GPX</a>
  <a href="../../routes/" class="route-data-button">查看路线数据索引</a>
</div>
```

### 4.6 静态路线示意图

```html
<h4 class="route-data-section-title">🗺️ 静态路线示意图</h4>
<div class="route-map-preview">
  <img src="../../assets/img/routes/{ROUTE_SLUG}-map.svg" alt="{ROUTE_TITLE} 文化自驾粗点路线图">
</div>
```

### 4.7 数据驱动路线表（route-data-viewer）

```html
<h2 class="text-center">数据驱动路线表</h2>
<section id="route-data-viewer"
         class="route-data-viewer"
         data-route-geojson="../../data/routes/{ROUTE_SLUG}.geojson"
         data-route-name="{ROUTE_TITLE}">
  <div class="route-data-loading">正在加载路线数据……</div>
  <noscript>浏览器未启用 JavaScript。请直接下载 CSV / GeoJSON / GPX 文件查看路线数据。</noscript>
</section>
<script src="../../assets/js/route-data-viewer.js"></script>
```

`data-route-geojson` 与 `data-route-name` 为必填，**不写死**任何路线。

---

## 5. 通用事实边界写法

任何路线页面都必须在事实审校模块或独立边界模块写清：

1. 数据类型（文化自驾粗点 / 文化复刻粗点）
2. 是否为实时导航数据
3. 是否为原始 GPS 轨迹
4. 出行前需要独立核实的事项
5. 路线状态（初版 / 50% / 实地验证 / 完整 / 100% 复盘）

---

## 6. 状态进度建议

| 状态 | 含义 |
|------|------|
| `10%` | 初版 · 行程列表 + 关键城市 |
| `30%` | 叙事与可旅行化 · 分段 + 建议 |
| `50%` | 发布包装 + 数据资产 |
| `70%` | 实地验证 / 图片 / 详细交通 |
| `90%` | 完整导游手册 |
| `100%` | 已实走复盘 |

新建路线时从 `10%` 开始，逐步推进到 `100%`。

---

## 7. 多路线规范

从 Phase 7（v1.4.7）开始，所有路线都使用同一套：

- CSV / GeoJSON / GPX / SVG 规范（见 `docs/ROUTE_DATA_SPEC.md`）
- 路线页面模板（本文件）
- 数据驱动查看器（`assets/js/route-data-viewer.js`）
- manifest 登记表（`data/routes/routes-manifest.json`）

OEDW 是长线文化复刻样板，辽塔是自驾人文路线样板，后续山西古建、北京周边路线可继续复用。

---

## 8. 反模式（不要做）

- ❌ 把 OEDW 字段名 / 段落名硬编码到 JS / CSS / HTML
- ❌ 在 route-data-viewer 写死某个 route slug
- ❌ 在 SVG 中只声明一个具体路线
- ❌ 引入地图 API / 构建系统 / npm 依赖
- ❌ 把"实地走访过"伪装成"GPS 轨迹"
- ❌ 把"粗略坐标"写成"精确坐标"

---

## 9. 统一数据徽章模块（v1.5.1 · Phase 11）

从 v1.5.1 开始，所有接入 manifest 的路线详情页都要包含「统一数据徽章模块」：

### 9.1 容器位置

建议插入顺序（v1.5.1 推荐页面结构）：

```
Hero
本页状态
路线数据状态徽章           ← 新统一模块
快速阅读
路线总览
...
下载路线数据              ← 旧轻量模块（保留）
静态路线示意图
数据驱动路线表
相关路线推荐              ← 新统一模块内部
来源资料
```

### 9.2 HTML 代码

```html
<section
 id="route-page-data-panel"
 class="route-page-data-panel"
 data-route-slug="<route-slug>"
 data-manifest-url="../../data/routes/routes-manifest.json"
 data-site-root="../..//">
 <div class="route-page-data-fallback">
  本路线已接入路线数据资产。可前往路线数据索引查看 CSV / GeoJSON / GPX 与 SVG 预览。
 </div>
</section>
```

### 9.3 脚本

```html
<script src="../../assets/js/route-page-badges.js"></script>
```

### 9.4 模块能力

- 状态徽章：数据完整度 / 分类 / 点位 / 段 / SVG / 非导航
- 摘要卡：8 字段 + theme_tags + region_tags
- 下载入口：CSV / GeoJSON / GPX / SVG / 数据索引
- 数据安全边界提示
- 相关路线推荐：最多 2 条

### 9.5 静态 fallback 保留

- 无 JS：`<noscript>` + 容器内的 `<div class="route-page-data-fallback">` 文案
- fetch 失败：脚本自动显示「路线数据模块加载失败」+ 数据索引入口

### 9.6 完整接入指南

见 [`docs/ROUTE_PAGE_INTEGRATION_GUIDE.md`](./ROUTE_PAGE_INTEGRATION_GUIDE.md)

---

## 10. SEO 与 OG 资产统一（v1.5.2 · Phase 12）

从 v1.5.2 开始，所有接入 manifest 的路线详情页都必须在 `<head>` 中包含统一的 18 个 SEO meta 标签。

### 10.1 manifest 必填字段

每条 route 必填 9 个字段：

```
seo_title, seo_description, canonical_url,
og_title, og_description, og_image_url,
twitter_title, twitter_description, share_summary
```

### 10.2 HTML head 必填标签

- `<title>{seo_title}</title>`
- `<meta name="description" content="{seo_description}">`
- `<link rel="canonical" href="{canonical_url}">`
- `<meta property="og:title" content="{og_title}">`
- `<meta property="og:description" content="{og_description}">`
- `<meta property="og:type" content="article">`
- `<meta property="og:url" content="{canonical_url}">`
- `<meta property="og:site_name" content="行旅图谱 · Culture Roadtrip Atlas">`
- `<meta property="og:locale" content="zh_CN">`
- `<meta property="og:image" content="{og_image_url}">`
- `<meta property="og:image:width" content="1200">`
- `<meta property="og:image:height" content="630">`
- `<meta property="og:image:alt" content="{og_title}">`
- `<meta name="twitter:card" content="summary_large_image">`
- `<meta name="twitter:title" content="{twitter_title}">`
- `<meta name="twitter:description" content="{twitter_description}">`
- `<meta name="twitter:image" content="{og_image_url}">`
- `<meta name="theme-color" content="#2e4f4f">`

### 10.3 OG SVG 资产规范

- 路径：`assets/img/og/<slug>-og.svg`
- 尺寸：1200×630
- 颜色：暗背景 + 路径线 + 节点 + 暗金文字徽章 + 安全边界
- 必须含 `<svg xmlns="http://www.w3.org/2000/svg">` + `viewBox="0 0 1200 630"`
- 推荐包含 `role="img"` + `aria-label` 增强可达性

### 10.4 share_summary 可见性

页面 `<body>` 后加：

```html
<p class="route-share-summary sr-only" aria-label="路线分享摘要">{share_summary}</p>
```

- 屏幕阅读器可读
- 视觉隐藏（sr-only）
- SEO 与社交分享爬虫可提取
- 与 manifest 的 `share_summary` 字段保持一致

### 10.5 新增路线 SEO 接入步骤

1. 在 manifest 中补充 9 个 SEO 字段
2. 运行 `python3 scripts/render-route-og-svg.py --all` 自动生成 5 个 OG SVG
3. 替换 HTML `<head>` 18 个 meta
4. 在 `<body>` 后加 share_summary 可见性段落
5. 运行 `python3 scripts/check-route-seo.py`
6. 运行 `python3 scripts/render-route-og-svg.py --all --check`

### 10.6 SEO 检查脚本

`scripts/check-route-seo.py` 覆盖 8 大类：

- manifest version = v1.5.2
- 9 SEO 字段完整
- OG SVG 文件存在且大小 > 500 字节
- 12 类 HTML meta 标签存在
- canonical 与 manifest 一致
- og:image basename 与 manifest 一致
- og_title 文本在页面可见
- share_summary 文本在页面可见（`<p class="route-share-summary">`）

### 10.7 OG SVG 生成器（v1.5.2 新增）

`scripts/render-route-og-svg.py` 是从 manifest 自动化生成 OG SVG 的脚本：

```bash
# 默认（生成全部）
python3 scripts/render-route-og-svg.py

# 生成全部
python3 scripts/render-route-og-svg.py --all

# 生成单条路线
python3 scripts/render-route-og-svg.py out-of-eden-walk-china

# 检查
python3 scripts/render-route-og-svg.py --all --check
```

输出：

- `assets/img/og/<slug>-og.svg` × 3（路线）
- `assets/img/og/site-og.svg`（首页）
- `assets/img/og/routes-index-og.svg`（路线索引页）

风格：

- 米白纸张（`#faf6ed` → `#f0e8d4`）+ 墨绿 + 暗金
- 1200×630（OG / Twitter 通用）
- 含 `<title>` + `<desc>` + route slug + 「行旅图谱」+ 「非导航」关键词
- 零外部依赖（仅 system-ui fallback）
- 无 JavaScript / 无网络字体 / 无外部图片

### 10.8 详细 SEO 文档

见 [`docs/ROUTE_SEO_GUIDE.md`](./ROUTE_SEO_GUIDE.md)

---

_辛 🔮 · 行旅图谱 · 页面模板 · v1.0 (Phase 7) + v1.4.7 多路线规范 + v1.5.1 统一徽章 + v1.5.2 SEO 与 OG 资产 · 2026-07-06_
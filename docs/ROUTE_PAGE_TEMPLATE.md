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

_辛 🔮 · 行旅图谱 · 页面模板 · 2026-07-05_
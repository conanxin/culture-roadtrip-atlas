# 行旅图谱 · 路线页面接入指南

> 把任何路线详情页接入统一的「路线数据状态徽章 + 摘要卡 + 下载入口 + 相关路线推荐」模块。
> 配套规范：[ROUTE_DATA_SPEC.md](./ROUTE_DATA_SPEC.md) · [ROUTE_PAGE_TEMPLATE.md](./ROUTE_PAGE_TEMPLATE.md) · [ROUTE_FACTORY_GUIDE.md](./ROUTE_FACTORY_GUIDE.md)

**版本：** v1.0
**适用项目版本：** 行旅图谱 v1.5.1+
**最后更新：** 2026-07-06

---

## 1. 目标

通过统一的 `route-page-badges.js` 脚本，让任意路线详情页都能自动展示：

- 路线数据状态徽章（数据完整度 / 分类 / 点位 / 段 / SVG / 非导航）
- 路线数据摘要卡（点位、段落、features、waypoints、theme_tags、region_tags）
- 数据下载入口（CSV / GeoJSON / GPX / SVG / 数据索引）
- 数据安全边界提示（统一文案）
- 相关路线推荐（最多 2 条，按 category / theme_tags / region_tags / featured / points 排序）

数据源统一来自 `data/routes/routes-manifest.json`，避免页面与 manifest 漂移。

---

## 2. 必备条件

接入前需要满足：

| 条件 | 说明 |
|------|------|
| route 已登记在 `data/routes/routes-manifest.json` | `slug` / `page_url` 必填 |
| route 有 `page_url` | 形如 `../trips/<route-slug>/` |
| 数据路线有 CSV / GeoJSON / GPX / SVG | planned-data 可只登记不显示下载 |
| `assets/js/route-page-badges.js` 已部署 | 当前已包含 |
| `docs/ROUTE_PAGE_INTEGRATION_GUIDE.md` 已部署 | 当前已包含 |

---

## 3. 页面接入代码

### 3.1 容器

在页面合适位置插入：

```html
<section
 id="route-page-data-panel"
 class="route-page-data-panel"
 data-route-slug="<route-slug>"
 data-manifest-url="../../data/routes/routes-manifest.json"
 data-site-root="../../">
 <div class="route-page-data-fallback">
  本路线已接入路线数据资产。可前往路线数据索引查看 CSV / GeoJSON / GPX 与 SVG 预览。
 </div>
</section>
```

### 3.2 必填属性

| 属性 | 必填 | 说明 |
|------|------|------|
| `id="route-page-data-panel"` | ✅ | 脚本入口选择器 |
| `data-route-slug` | ✅ | 必须与 manifest 中 `slug` 完全一致 |
| `data-manifest-url` | ⚠️ 推荐 | 默认由 `data-site-root` + `data/routes/routes-manifest.json` 推导 |
| `data-site-root` | ⚠️ 推荐 | 默认 `../../`（详情页在 `trips/<slug>/` 下） |

### 3.3 脚本引入

页面底部（`</body>` 前）加入：

```html
<script src="../../assets/js/route-page-badges.js"></script>
```

### 3.4 完整示例（OEDW 页面）

```html
<section
 id="route-page-data-panel"
 class="route-page-data-panel trip-template-section container"
 data-route-slug="out-of-eden-walk-china"
 data-manifest-url="../../data/routes/routes-manifest.json"
 data-site-root="../..//"
 style="margin-top: var(--space-2xl);">
 <div class="city-card" style="max-width: 1100px; margin: 0 auto;">
  <div class="route-page-data-fallback">
   本路线已接入路线数据资产。
  </div>
 </div>
</section>

<!-- ... -->

<script src="../../assets/js/route-page-badges.js"></script>
```

---

## 4. 推荐插入位置

按页面阅读节奏，建议插入顺序：

```
Hero
本页状态 / 路线总览
路线数据状态徽章   ← 新统一模块
下载路线数据 / 路线数据 (旧轻量模块)
静态路线示意图 / 静态 SVG
数据驱动路线表 (route-data-viewer)
...
相关路线推荐       ← 新统一模块（含在 route-page-badges.js 内）
来源资料
```

要点：

- 把新模块放在「下载路线数据」之前，作为状态摘要优先呈现
- 「相关路线推荐」会由脚本自动追加在 panel 末尾，不需要单独 section
- 旧「下载路线数据」/「路线数据」模块可保留，但建议把标题改为「路线数据下载」，避免与新模块「路线数据状态」重名

---

## 5. URL 规则（重要）

manifest 里的 URL 形如：

```
../data/routes/out-of-eden-walk-china.csv
../data/routes/out-of-eden-walk-china.geojson
../assets/img/routes/out-of-eden-walk-china-map.svg
../trips/out-of-eden-walk-china/
../routes/
```

这些都是面向 `routes/index.html` 的相对路径。在详情页中（位于 `trips/<slug>/index.html`）不能直接使用。

### 5.1 转换规则

`route-page-badges.js` 通过 `data-site-root` 做转换：

| manifest URL 形态 | siteRoot = `../../` | 结果 |
|-------------------|---------------------|------|
| `../data/routes/x.csv` | `../../` | `../../data/routes/x.csv` |
| `../trips/x/` | `../../` | `../../trips/x/` |
| `../routes/` | `../../` | `../../routes/` |
| `http(s)://...` | 任意 | 原样使用 |
| 已是当前页相对路径 | 任意 | 原样使用 |

### 5.2 siteRoot 配置

- 详情页位于 `trips/<slug>/index.html` → `data-site-root="../../"`
- 索引页位于 `routes/index.html` → `data-site-root="../"`（实际 routes/index.html 不需要此脚本）
- 嵌入子页（如 `trips/<slug>/sub/...`） → `data-site-root="../../../"`

---

## 6. 必跑检查

```
python3 scripts/check-route-page-integration.py
./scripts/verify-site.sh
```

`check-route-page-integration.py` 检查项：

1. 每条有 page_url 的 route：页面文件存在
2. 页面含 `data-route-slug="<slug>"` 且 slug 与 manifest 一致
3. 页面含 `#route-page-data-panel` 容器
4. 页面引入 `route-page-badges.js`
5. 数据完整路线（含 csv_url）页面含「路线数据」或「路线数据状态」关键词
6. 页面声明 `data-site-root`
7. `route-page-badges.js` 存在且含核心关键词
8. `ROUTE_PAGE_INTEGRATION_GUIDE.md` 存在且含核心章节

---

## 7. 常见错误

| 错误 | 后果 | 修复 |
|------|------|------|
| 忘记设置 `data-route-slug` | 脚本显示「配置错误」 | 在容器上加 `data-route-slug="<slug>"` |
| slug 与 manifest 不一致 | 脚本显示「未找到路线」 | 改 slug 与 manifest 完全一致 |
| `data-site-root` 层级错误 | 下载链接 404 | 详情页用 `../../`；子页用 `../../../` |
| 页面未引入 `route-page-badges.js` | 容器仅显示 fallback 文案 | `</body>` 前加 `<script src="../../assets/js/route-page-badges.js"></script>` |
| 推荐路线包含当前路线 | 视觉冗余 | 脚本内部已用 `slug !== current.slug` 过滤；如有异常检查 manifest slug 字段 |
| 下载链接 404 | 资源未找到 | 检查 `data-site-root` 与 manifest 中 `csv_url` / `geojson_url` 等字段 |
| 容器位置错乱 | 渲染正常但页面节奏乱 | 放在「Hero + 路线总览」之后，「旧下载模块」之前 |
| 新旧模块重名 | 视觉冲突 | 旧模块标题改为「路线数据下载」 |

---

## 8. 相关路线推荐逻辑

```javascript
function scoreRelated(route, other) {
  if (other.slug === route.slug) return -1;       // 不推荐自己
  var score = 0;
  if (other.category === route.category) score += 10;   // 同类优先
  var themeOverlap = ... ;                          // theme_tags 交集 ×3
  var regionOverlap = ... ;                         // region_tags 交集 ×2
  if (other.featured) score += 1;
  score += (other.points || 0) / 100;
  return score;
}
```

排序：`score desc → points desc`，取前 2 条。

每个推荐卡片显示：

- 标题（`title`）
- 状态徽章 + 分类徽章
- 一句话摘要（`route_summary`）
- 主题标签（`theme_tags` 前 4 个）
- 「进入路线 →」「数据索引 →」两个动作

---

## 9. 不引入依赖

- ❌ 无 npm / 第三方 JS 库
- ❌ 无后端 / 构建系统
- ❌ 无地图 API
- ✅ 纯 Vanilla JS（与 `routes-index.js` / `route-data-viewer.js` 风格一致）

---

## 10. 当前三条路线接入状态

| slug | 页面路径 | data-site-root | 状态 |
|------|----------|----------------|------|
| `out-of-eden-walk-china` | `trips/out-of-eden-walk-china/index.html` | `../../` | ✅ v1.5.1 接入 |
| `liao-tower-roadtrip` | `trips/liao-tower-roadtrip/index.html` | `../../` | ✅ v1.5.1 接入 |
| `shanxi-ancient-architecture` | `trips/shanxi-ancient-architecture-roadtrip/index.html` | `../../` | ✅ v1.5.1 接入 |

每页都已含：

- `<section id="route-page-data-panel" data-route-slug="<slug>" data-manifest-url="../../data/routes/routes-manifest.json" data-site-root="../../">`
- `<script src="../../assets/js/route-page-badges.js"></script>`

---

_辛 🔮 · 行旅图谱 · 路线页面接入指南 · v1.0 · 2026-07-06_
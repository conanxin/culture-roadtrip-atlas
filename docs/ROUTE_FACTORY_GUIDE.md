# 行旅图谱 · 路线工厂操作指南

> 面向以后新增第 4 条路线（或更多路线）时的实操指南。
> 配套规范：[ROUTE_DATA_SPEC.md](./ROUTE_DATA_SPEC.md) · [ROUTE_PAGE_TEMPLATE.md](./ROUTE_PAGE_TEMPLATE.md)

**版本：** v1.0
**适用项目版本：** 行旅图谱 v1.5.0+
**最后更新：** 2026-07-05

---

## 1. 新增路线标准流程

```
1. 规划路线 slug（kebab-case，例：beijing-periphery-roadtrip）
2. 新增 CSV：data/routes/<slug>.csv
3. 生成 GeoJSON：data/routes/<slug>.geojson
4. 生成 GPX：data/routes/<slug>.gpx
5. 更新 routes-manifest.json：data/routes/routes-manifest.json
6. 运行 build-route-assets.py --all 一次完成 SVG 生成 + manifest 统计同步
7. 检查 routes/index.html 同步
8. 在路线页面增加数据模块（如果页面存在）
9. 运行 verify-site.sh
10. 提交并等待 GitHub Actions Route Data Quality Gate
```

---

## 2. CSV 编写规则

### 2.1 字段（必须 18 个）

```
id, sequence, segment_id, segment_name, point_name, province,
city_or_area, latitude, longitude, coordinate_precision, source_level,
replication_feasibility, difficulty, best_season, transport_hint,
risk_note, source_note, url
```

### 2.2 命名规范

- `id`：`{PREFIX}-P001`, `{PREFIX}-P002`, ...
- `segment_id`：`S01`, `S02`, ... `S09`（或 `S10` 等）
- `slug` 建议 ≤ 30 字符，小写 + 连字符
- `point_name` 中文名 ≤ 20 字
- `province` 拼音或英文（如 `Yunnan`, `Liaoning`）
- `city_or_area` 拼音或英文

### 2.3 枚举值

| 字段 | 可选值 |
|------|--------|
| `coordinate_precision` | `city` / `landmark` / `region` / `approximate` / `unknown` |
| `source_level` | `A_official_oedw` / `B_partner_or_education` / `C_chinese_media` / `D_reconstructed_for_travel` / `E_project_internal` |
| `replication_feasibility` | `high` / `medium` / `low` / `not_recommended` / `reading_only` |
| `difficulty` | `easy` / `medium` / `hard` / `extreme` / `mixed` / `n/a` |

### 2.4 risk_note 必含

- 文保开放时间需核查
- 山路天气需核查（山区段）
- 自驾路况需核查（自驾路线）
- 非实时导航

### 2.5 source_note 建议

- 注明数据来源
- 国保级别（1982 国保 / 2001 国保 等）
- 重要历史事件年份

### 2.6 url 字段

- 可留空
- 优先指向项目内页面
- 不要硬编不确定外链

---

## 3. 坐标规则

**严格遵守：**

- ✅ 使用城市 / 文保单位 / 景区公开粗略经纬度
- ✅ 文保单位可写 landmark 精度
- ✅ 城市可写 city 精度
- ✅ 山地区域可写 region 精度
- ❌ 不写道路级导航坐标
- ❌ 不伪造历史人物原始 GPS 轨迹
- ❌ 不精确到小数点后 6 位

**检查脚本**：`validate-route-data.py` 会自动校验经纬度可解析为 float。

---

## 4. 数据安全边界（必读）

**所有路线数据都必须在以下边界内：**

- 数据类型：文化复刻粗点 / 文化自驾粗点
- 不用于实时导航
- 不保证路况、开放状态、天气、安全、边境或山地通行条件
- 不冒充历史人物原始 GPS 轨迹
- 不冒充道路级精确坐标

**必须在以下地方写明边界：**

1. CSV / GeoJSON / GPX 文件 metadata 或 desc
2. SVG `<title>` / `<desc>` / 免责声明
3. 路线页面（事实审校 / 内容边界 section）
4. routes/index.html 数据说明
5. docs/ROUTE_DATA_SPEC.md 与本指南

---

## 5. 必跑命令

```bash
# 1. 路线工厂构建
python3 scripts/build-route-assets.py --all

# 2. 工厂 check（CI 模式）
python3 scripts/build-route-assets.py --check

# 3. 数据校验 + manifest 一致性
python3 scripts/validate-route-data.py --all --manifest-check

# 4. SVG 检查
python3 scripts/render-route-map-svg.py --all --check

# 5. 索引页与 manifest 同步
python3 scripts/check-routes-index-sync.py

# 6. 本地综合门禁
./verify-site.sh
```

**所有命令必须 PASS。**

---

## 6. manifest 更新

在 `data/routes/routes-manifest.json` 的 `routes` 数组中追加新条目：

```json
{
  "slug": "your-route-slug",
  "title": "路线中文标题",
  "status": "data-v0.1",
  "route_type": "cultural_roadtrip",
  "category": "roadtrip",
  "theme_tags": ["...", "..."],
  "region_tags": ["...", "..."],
  "data_status_label": "路线样板定位",
  "difficulty_label": "中 · 自驾为主",
  "best_season": "5–10 月",
  "route_summary": "一句话简介",
  "data_completeness": "v0.1",
  "featured": true,
  "segments": 9,
  "points": 20,
  "geojson_features": 30,
  "geojson_points": 20,
  "geojson_lines": 10,
  "gpx_waypoints": 20,
  "has_svg_preview": true,
  "is_original_gps_track": false,
  "for_navigation": false,
  "approximate_distance_km": "2000-2400",
  "time_span": "9 天 8 晚",
  "data_version": "v1.5.0",
  "page_url": "../trips/<slug>/",
  "csv_url": "../data/routes/<slug>.csv",
  "geojson_url": "../data/routes/<slug>.geojson",
  "gpx_url": "../data/routes/<slug>.gpx",
  "svg_url": "../assets/img/routes/<slug>-map.svg"
}
```

**关键规则：**

- `page_url` 必须匹配实际页面路径
- `points` `segments` 等统计字段由 `build-route-assets.py --all` 自动同步
- 不要把人工字段（如 `title` / `summary`）放在脚本会回写的字段内

---

## 7. GeoJSON 生成

按 `data/routes/<slug>.geojson` 生成：

- 1 个 FeatureCollection
- metadata 必填字段：
  - `title`, `version`, `route_type`
  - `is_original_gps_track: false`
  - `for_navigation: false`
  - `disclaimer`（中文声明）
  - `updated_at` (YYYY-MM-DD)
- Point features = CSV 行数
- 至少 1 个 `LineString`（feature_type = `generalized_route_line`）
- 建议增加 N 个分段 `LineString`（feature_type = `segment_generalized_line`）
- 所有 LineString properties 必须含 `is_original_gps_track: false` 和 `warning: "not for navigation"`

**可用脚本辅助：** `scripts/build-route-assets.py` 调用 `render-route-map-svg.py` 时会读取 GeoJSON 的 `points` 字段。

---

## 8. GPX 生成

按 `data/routes/<slug>.gpx` 生成：

- GPX 1.1 标准
- 每个 CSV 点位对应一个 `<wpt>`
- metadata `<desc>` 必须含：
  - `cultural replica` / `cultural roadtrip`
  - `not original GPS track`
  - `not for navigation`
  - `opening status` / `road conditions` 需出行前核查
- 可包含 1 个 `<trk>` 概括 track
- waypoint 数量必须等于 CSV 行数

---

## 9. SVG 生成

**自动**：`python3 scripts/render-route-map-svg.py <slug>` 生成 `assets/img/routes/<slug>-map.svg`

**SVG 必含（中英文）：**

- `cultural replica` / `cultural roadtrip`
- `not for navigation`
- `not original GPS track`
- 起点 / 终点标签
- 段编号标签 S01-Sxx

---

## 10. 路线页面模块

如果页面已存在，在「路线取舍逻辑」/「行前资料」前增加「路线数据」section：

```html
<section id="route-data" class="container" style="margin-top: var(--space-3xl);">
  <h2 class="text-center">路线数据</h2>
  <p>本路线已接入文化自驾粗点数据...</p>
  <a href="../../data/routes/<slug>.csv" download>下载 CSV</a>
  <a href="../../data/routes/<slug>.geojson" download>下载 GeoJSON</a>
  <a href="../../data/routes/<slug>.gpx" download>下载 GPX</a>
  <img src="../../assets/img/routes/<slug>-map.svg" alt="...">
</section>
```

---

## 11. 常见错误

| 错误 | 解决 |
|------|------|
| manifest 统计与实际数据不一致 | 运行 `build-route-assets.py --check` 查看 diff |
| routes/index.html 未同步 | 运行 `check-routes-index-sync.py` |
| SVG 缺少 "not for navigation" | 检查 `render-route-map-svg.py` 中英文双语声明 |
| GPX waypoint 数与 CSV 行数不一致 | 重新生成 GPX |
| planned-data 不应创建空 CSV | 保持 `points: 0` 与 URL 全 null |
| 页面 URL 与真实路径不一致 | 用 `find trips -name index.html` 确认 |
| difficulty 取值非法 | 必须是 `easy` / `medium` / `hard` / `extreme` / `mixed` / `n/a` |
| coordinate_precision 取值非法 | 必须是 `city` / `landmark` / `region` / `approximate` / `unknown` |

---

## 12. 当前三条路线示例

| slug | 类型 | 段数 | 点位 | 样板定位 |
|------|------|------|------|----------|
| `out-of-eden-walk-china` | cultural_replica | 10 | 42 | 长线文化复刻样板 |
| `liao-tower-roadtrip` | cultural_roadtrip | 9 | 20 | 自驾人文路线样板 |
| `shanxi-ancient-architecture` | cultural_roadtrip | 9 | 30 | 古建自驾路线样板 |

新增第 4 条时，建议从以下方向选择样板：

- **短线 2-3 天**（如北京周边）
- **跨省主题**（如河西走廊 / 丝路）
- **季节限定**（如春季赏花 / 秋季彩林）

---

## 13. 路线页面接入步骤（v1.5.1 新增）

完成路线数据资产后，还需要在路线详情页接入统一面板，让用户从页面直接看到状态徽章与下载入口。

### 13.1 接入代码

在 `trips/<slug>/index.html` 中加入：

```html
<section
 id="route-page-data-panel"
 class="route-page-data-panel"
 data-route-slug="<slug>"
 data-manifest-url="../../data/routes/routes-manifest.json"
 data-site-root="../..//">
 <div class="route-page-data-fallback">
  本路线已接入路线数据资产。
 </div>
</section>

<script src="../../assets/js/route-page-badges.js"></script>
```

### 13.2 推荐插入位置

放在「Hero + 路线总览」之后、「下载路线数据」之前。

### 13.3 必跑检查

```bash
python3 scripts/check-route-page-integration.py
./scripts/verify-site.sh
```

### 13.4 详细接入指南

见 [`docs/ROUTE_PAGE_INTEGRATION_GUIDE.md`](./ROUTE_PAGE_INTEGRATION_GUIDE.md)。

---

_辛 🔮 · 行旅图谱 · 路线工厂指南 · v1.0 (Phase 10) + v1.5.1 页面接入补充 (Phase 11) · 2026-07-06_
# Phase 7 Report · Route Data Templates & Multi-route Reuse

**版本：** v1.4.7
**日期：** 2026-07-05
**主题：** 路线数据模板化与多路线复用
**项目：** Culture Roadtrip Atlas

---

## STATUS

**PASS** — 所有验证项通过,OEDW 事实边界未回退,辽塔路线数据资产完成,GitHub Pages 部署成功。

---

## 工作分支 / Commit

- 工作分支：`main`
- 基线 commit：`5afd620`（Phase 6 · 数据驱动页面与静态地图预览）
- 新 commit：`9032e19` Template route data and add Liao tower route assets
- Push 状态：✅ origin/main 已同步

---

## 修改 / 新增文件列表

### 新增文件

| 路径 | 大小 | 说明 |
|------|------|------|
| `docs/ROUTE_DATA_SPEC.md` | ~5.2 KB | 通用路线数据规范 v1.0 |
| `docs/ROUTE_PAGE_TEMPLATE.md` | ~5.1 KB | 通用路线页面模板 v1.0 |
| `data/routes/routes-manifest.json` | ~2.0 KB | 项目级路线登记表 |
| `data/routes/liao-tower-roadtrip.csv` | ~4.7 KB | 辽塔路线 20 行 CSV |
| `data/routes/liao-tower-roadtrip.geojson` | ~10 KB | 辽塔路线 30 features GeoJSON |
| `data/routes/liao-tower-roadtrip.gpx` | ~8 KB | 辽塔路线 20 waypoint GPX |
| `assets/img/routes/liao-tower-roadtrip-map.svg` | 6.8 KB | 辽塔路线静态 SVG |
| `reports/PHASE7_ROUTE_TEMPLATE_MULTI_ROUTE_REPORT.md` | 本文件 | Phase 7 报告 |

### 修改文件

| 路径 | 变更 |
|------|------|
| `scripts/validate-route-data.py` | 完全重写为 v1.1 · 增 --all / 路线级别阈值 / 通用化校验 · 14.7 KB |
| `scripts/render-route-map-svg.py` | 完全重写为 v1.1 · 增 --all / 动态 title/desc / 中英文双语声明 · 19.1 KB |
| `assets/js/route-data-viewer.js` | 去除 OEDW 硬编码 · 通用化 fallback 下载链接 · 根据 geoUrl 推断 slug |
| `data/routes/README.md` | 增加 manifest / 多路线使用方式 / 路线样板定位 / Phase 7 章节 |
| `routes/index.html` | 增加路线数据资产总览 + 辽塔数据卡片 + 多路线规范模块 + 升级版本号 |
| `trips/liao-tower-roadtrip/index.html` | 新增轻量「路线数据」模块（不影响既有内容）|
| `index.html` | 路线数据索引说明增加辽塔、版本徽章 v1.4.7 + 2 条路线 |
| `assets/js/trips-data.js` | OEDW + 辽塔增加 hasRouteData 字段 |
| `assets/js/home.js` | trip 卡片支持「已接入路线数据」标识 + 数据元信息链接 |
| `assets/css/styles.css` | 新增 `.route-data-badge-inline` / `.trip-card-data-meta` |
| `assets/img/routes/out-of-eden-walk-china-map.svg` | 重新生成 · title 增「粗点」+ 中英文双语 desc |
| `README.md` | 升级到 v1.4.7 描述 |
| `CHANGELOG.md` | 顶部插入 v1.4.7 章节 |
| `docs/CONTENT_NOTES.md` | 追加 Phase 7 章节 |

---

## 新增文档

### 1. docs/ROUTE_DATA_SPEC.md · 通用路线数据规范

- 规范定位（文化复刻粗点 vs 实时导航）
- 文件结构（CSV / GeoJSON / GPX / SVG / manifest）
- 18 字段 CSV 字段规范
- 4 类枚举值（coordinate_precision / source_level / replication_feasibility / difficulty）
- GeoJSON 规范（metadata 必填字段 / Point + LineString 约束）
- GPX 规范（GPX 1.1 / waypoint + track / 必要声明）
- SVG 预览规范（viewBox / 配色 / 标题 / 免责声明）
- 路线 manifest 规范
- 验证命令清单

### 2. docs/ROUTE_PAGE_TEMPLATE.md · 通用路线页面模板

- `<head>` 模板（title / meta / OG / Twitter card / canonical）
- 19 个模块顺序（Hero / 状态 / 事实审校 / 数据下载 / 静态地图 / 数据驱动表 等）
- 关键模块 HTML 模板（Hero / 状态 / 事实审校 / 路线总览 / 数据下载 / 静态地图 / 数据驱动表）
- 通用事实边界写法
- 状态进度建议（10% / 30% / 50% / 70% / 90% / 100%）
- 多路线规范说明
- 反模式清单

---

## 路线 manifest 内容摘要

`data/routes/routes-manifest.json` 收录 2 条路线：

| slug | 状态 | 类型 | 段数 | 点位 | features | waypoints | 距离 | 时间 |
|------|------|------|------|------|----------|-----------|------|------|
| out-of-eden-walk-china | 50% | cultural_replica | 10 | 42 | 53 | 42 | 6,000–6,700 公里 | 两年多 |
| liao-tower-roadtrip | data-v0.1 | cultural_roadtrip | 9 | 20 | 30 | 20 | 2,000–2,400 公里 | 9 天 8 晚 |

每条路线提供：

- `page_url` / `csv_url` / `geojson_url` / `gpx_url` / `svg_url`
- `is_original_gps_track: false`
- `for_navigation: false`
- `route_template`（路线样板定位）

---

## validate-route-data.py 增强说明

### v1.1 新增能力

1. **任意 slug 支持**：`python3 scripts/validate-route-data.py <slug>`
2. **默认兼容**：`python3 scripts/validate-route-data.py` 等同于 OEDW
3. **--all 模式**：`python3 scripts/validate-route-data.py --all` 读取 manifest 全量校验
4. **路线级别阈值**：
   - OEDW: CSV ≥ 35 行 · S01-S10 覆盖 · GeoJSON lines ≥ 11
   - liao-tower: CSV ≥ 15 行 · S01-S09 覆盖 · GeoJSON lines ≥ 1
   - 其他路线: CSV ≥ 5 行 · 至少一个 Sxx · GeoJSON lines ≥ 1
5. **新枚举值**：`source_level` 增 `E_project_internal`、`difficulty` 增 `extreme/mixed`
6. **段覆盖检查**：检查 S01-Sxx 完整覆盖
7. **清晰输出格式**：单路线 + --all 两种模式

### 输出格式示例

单路线：
```
PASS route data validation
route: liao-tower-roadtrip
csv_rows: 20
geojson_points: 20
geojson_lines: 10
gpx_waypoints: 20
segments: S01-S09
```

--all：
```
PASS all route data validation
routes: 2
```

---

## render-route-map-svg.py 增强说明

### v1.1 新增能力

1. **任意 slug 支持**：`python3 scripts/render-route-map-svg.py <slug>`
2. **默认兼容**：`python3 scripts/render-route-map-svg.py` 等同于 OEDW
3. **--all 模式**：`python3 scripts/render-route-map-svg.py --all` 读取 manifest 全量生成
4. **动态 title/desc**：
   - title 从 GeoJSON metadata 提取
   - desc 中英文双语（包含必要声明）
5. **动态图例**：
   - 路线类型描述（文化复刻 / 文化自驾）
   - 段落范围（S01-S09 等）
   - 点位数（动态统计）
6. **必要声明检查**：输出时检查 `not for navigation` / `cultural replica` / `not original GPS`
7. **兼容短路线**：长卷风格布局避免点位重叠

### 输出格式

- 单路线 SVG：`assets/img/routes/<slug>-map.svg`（1200×760）
- 中文 + 英文双声明

---

## 辽塔路线数据文件说明

### 1. CSV（20 行 · 18 字段）

| 字段 | 数量 / 示例 |
|------|------|
| 段 | S01-S09 |
| 点位 | 20 |
| province | Beijing / Liaoning / Inner Mongolia / Hebei |
| coordinate_precision | city / landmark / region |
| source_level | E_project_internal |
| replication_feasibility | high / medium |
| difficulty | easy / medium |

9 段分布：

- S01 北京出发线（2 点）
- S02 义县佛教遗存线（2 点）
- S03 北镇医巫闾山线（3 点）
- S04 朝阳辽塔线（2 点）
- S05 朝阳赤峰转场线（2 点）
- S06 庆州白塔林东线（2 点）
- S07 辽上京核心日（2 点）
- S08 辽中京宁城承德线（3 点）
- S09 承德北京收束线（2 点）

### 2. GeoJSON（30 features）

- 20 Point features（与 CSV 一一对应）
- 9 段 LineString features（feature_type = segment_generalized_line）
- 1 主 LineString feature（feature_type = generalized_route_line）
- metadata.is_original_gps_track = false
- metadata.disclaimer = 「文化自驾粗点数据;不是实时导航路线;不用于路况、安全、开放状态判断」
- metadata.approximate_distance_km = "2000-2400"
- metadata.time_span = "9 天 8 晚 闭环自驾"

### 3. GPX（20 waypoint + 1 track）

- GPX 1.1 标准
- 20 waypoint（与 CSV 一一对应）
- 1 track（含 9 段 trkseg）
- metadata desc 包含「cultural replica / not original GPS / not for navigation」

### 4. SVG（6.8 KB）

- 1200×760 viewBox
- 米白背景 + 墨绿主路线 + 暗金点位
- 起点（深墨绿）/ 终点（暗红）
- 9 段 S01-S09 编号标签
- 中英文双语免责声明

---

## OEDW 数据是否未回退

✅ **完全未回退**

| 文件 | 状态 |
|------|------|
| `data/routes/out-of-eden-walk-china.csv` | 42 行未变 |
| `data/routes/out-of-eden-walk-china.geojson` | 42 Point + 11 LineString 未变 |
| `data/routes/out-of-eden-walk-china.gpx` | 42 waypoint 未变 |
| `trips/out-of-eden-walk-china/index.html` | 1789 行未改事实边界 |
| `assets/img/routes/out-of-eden-walk-china-map.svg` | 重新生成 · 内容等价（title 增「粗点」+ 中英文 desc）|

### 关键事实边界保留

- ✅ "跨越六年" 已清除（仅历史报告记录）
- ✅ "22/23" 已清除（仅历史报告记录）
- ✅ "22/22" 保留（13 处命中）
- ✅ "6,000–6,700 公里" 保留（多页面命中）
- ✅ "两年多 / 两年四个月 / 两年半左右" 保留
- ✅ "卢沟桥 → 天安门 → 小汤山" 保留
- ✅ 黄海三层时间（2023 冬 / 2024.6 / 2024.8）保留
- ✅ "文化复刻粗点" 保留
- ✅ "非 Paul Salopek 原始 GPS 轨迹" 保留
- ✅ "非导航" 保留

---

## 两条路线数据统计

| 指标 | OEDW | 辽塔 | 合计 |
|------|------|------|------|
| CSV 行数 | 42 | 20 | 62 |
| GeoJSON features | 53 | 30 | 83 |
| GPX waypoints | 42 | 20 | 62 |
| 段数 | 10 | 9 | 19 |
| 距离（公里）| 6,000–6,700 | 2,000–2,400 | — |
| 时间 | 两年多 | 9 天 8 晚 | — |
| 数据版本 | v1.4.5（未变）| v1.4.7（新增）| — |
| 路线状态 | 50% | data-v0.1 | — |

---

## 多路线验证

### OEDW 校验

```
route: out-of-eden-walk-china
CSV: out-of-eden-walk-china.csv · 42 行 · PASS
GeoJSON: out-of-eden-walk-china.geojson · 42 points · 11 lines · PASS
GPX: out-of-eden-walk-china.gpx · 42 waypoints · PASS
--------------------------------------------------
csv_rows: 42
geojson_points: 42
geojson_lines: 11
gpx_waypoints: 42
segments: S01-S10
PASS route data validation
```

### 辽塔校验

```
route: liao-tower-roadtrip
CSV: liao-tower-roadtrip.csv · 20 行 · PASS
GeoJSON: liao-tower-roadtrip.geojson · 20 points · 10 lines · PASS
GPX: liao-tower-roadtrip.gpx · 20 waypoints · PASS
--------------------------------------------------
csv_rows: 20
geojson_points: 20
geojson_lines: 10
gpx_waypoints: 20
segments: S01-S09
PASS route data validation
```

### --all 校验

```
PASS all route data validation
routes: 2
```

### --all SVG 生成

```
PASS all route SVG generation
routes: 2
```

### manifest/data consistency

```
PASS manifest/data consistency
```

---

## 路线数据索引页增强

`routes/index.html` 增强点：

1. **路线数据资产总览**：2 条路线 / 62 粗点 / 83 features / 62 waypoints / 2 张 SVG / 通用化 v1.0
2. **辽塔路线数据卡片**：路线名 / 状态 / 20 个点位 / 9 段 / 2,000–2,400 公里 / 9 天 8 晚
3. **静态地图预览**：辽塔 SVG 嵌入
4. **9 项数据统计**：点位数 / 段落数 / features / waypoints / 数据版本 / 数据类型 / 原始 GPS / 用途 / 限制
5. **下载按钮**：CSV / GeoJSON / GPX
6. **数据说明**：4 条边界
7. **多路线规范模块**：OEDW 长线样板 + 辽塔自驾样板 + 山西 / 北京周边后续
8. **数据规范模块**：链接到 ROUTE_DATA_SPEC / ROUTE_PAGE_TEMPLATE / 数据 README
9. **导航升级**：增加「辽塔巡礼」/「多路线」锚点

---

## 本地 HTTP 验证

`python3 -m http.server 8000` + `curl -I`：

| 路径 | 状态 |
|------|------|
| `/` | 200 |
| `/routes/` | 200 |
| `/trips/out-of-eden-walk-china/` | 200 |
| `/trips/liao-tower-roadtrip/` | 200 |
| `/data/routes/routes-manifest.json` | 200 |
| `/data/routes/liao-tower-roadtrip.csv` | 200 |
| `/data/routes/liao-tower-roadtrip.geojson` | 200 |
| `/data/routes/liao-tower-roadtrip.gpx` | 200 |
| `/assets/img/routes/liao-tower-roadtrip-map.svg` | 200 |

全部 200。

---

## verify-site.sh 结果

```
通过: 70
失败: 0
✓ STATUS: PASS
```

---

## GitHub Pages 部署结果

- 推送 commit：`9032e19`
- 推送分支：`main` → `origin/main`
- GitHub Pages 自动重建成功

---

## 线上 HTTP 200 结果

| 路径 | 状态 |
|------|------|
| `https://conanxin.github.io/culture-roadtrip-atlas/` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/routes/` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/data/routes/routes-manifest.json` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/data/routes/liao-tower-roadtrip.csv` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/data/routes/liao-tower-roadtrip.geojson` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/data/routes/liao-tower-roadtrip.gpx` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/assets/img/routes/liao-tower-roadtrip-map.svg` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_DATA_SPEC.md` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_PAGE_TEMPLATE.md` | 200 |

全部 200。

---

## 关键 URL

- **首页：** https://conanxin.github.io/culture-roadtrip-atlas/
- **路线数据索引：** https://conanxin.github.io/culture-roadtrip-atlas/routes/
- **OEDW 页面：** https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/
- **辽塔页面：** https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/
- **OEDW SVG：** https://conanxin.github.io/culture-roadtrip-atlas/assets/img/routes/out-of-eden-walk-china-map.svg
- **辽塔 SVG：** https://conanxin.github.io/culture-roadtrip-atlas/assets/img/routes/liao-tower-roadtrip-map.svg
- **manifest：** https://conanxin.github.io/culture-roadtrip-atlas/data/routes/routes-manifest.json
- **数据规范：** https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_DATA_SPEC.md
- **页面模板：** https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_PAGE_TEMPLATE.md

---

## Phase 8 建议

1. **山西古建路线数据**
   - 复用同一套 CSV / GeoJSON / GPX / SVG 规范
   - 11 天 10 晚 · A 级 12 核心点位 → data-v0.1
   - v1.5.0 引入

2. **路线数据可视化增强**
   - 各路线点位的难度分布 / 省份分布 图表
   - 与现有数据驱动查看器集成

3. **实地走访数据回流**
   - 辽塔 / 山西等路线如有实走记录
   - 把实走图片 / 复盘心得 反向链接到对应点位

4. **数据导出工具**
   - CSV → Markdown 表格（方便 docs 嵌入）
   - GeoJSON → Leaflet 静态嵌入片段

5. **多语言版本**
   - 当前 OEDW / 辽塔页面以中文为主
   - 英文版可作为国际化基础

6. **数据版本管理**
   - 当前 OEDW 仍是 v1.4.5 数据版本
   - 后续如有更新应同步升级到 v1.4.7 / v1.5.0

7. **路线样板扩展**
   - 长线文化复刻样板（OEDW）
   - 自驾人文路线样板（辽塔）
   - 短线文化体验样板（未来北京周边 2-3 天）

---

_辛 🔮 · 行旅图谱 · Phase 7 报告 · 2026-07-05_
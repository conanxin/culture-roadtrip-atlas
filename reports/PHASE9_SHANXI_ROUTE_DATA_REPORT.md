# Phase 9 Report · Shanxi Ancient Architecture Route Data Production

**版本：** v1.4.9
**日期：** 2026-07-05
**主题：** 山西古建路线数据生产
**项目：** Culture Roadtrip Atlas

---

## STATUS

**PASS** — 山西古建路线从 planned-data 升级为 data-v0.1 · 30 个粗点 · 9 段路线 · 11 天 10 晚 · 全部门禁通过。

---

## 工作分支 / Commit

- 工作分支：`main`
- 基线 commit：`b57e92c`（Phase 8 · 路线工厂自动化与质量门禁）
- 新 commit：`026510a` Produce Shanxi ancient architecture route data
- Push 状态：✅ origin/main 已同步
- GitHub Actions：✅ Route Data Quality Gate 成功（commit 026510a3 · 2026-07-05T01:14:10Z）

---

## Canonical 山西页面路径

**最终 canonical path：** `trips/shanxi-ancient-architecture-roadtrip/index.html`

决策依据：
- `find trips -maxdepth 2 -name index.html` 显示 `trips/shanxi-ancient-architecture-roadtrip/index.html` 已存在
- manifest 原本指向 `../trips/shanxi-ancient-architecture/` 是错误的
- 按 spec §2 规则 3：「如果已有页面实际路径是 trips/shanxi/ 或其他路径，不要盲目新增重复页面；优先保留现有真实页面，并同步修正 manifest page_url」
- 因此保留现有真实页面，并修正 manifest page_url 为 `../trips/shanxi-ancient-architecture-roadtrip/`

---

## 修改 / 新增文件列表

### 新增文件

| 路径 | 大小 | 说明 |
|------|------|------|
| `data/routes/shanxi-ancient-architecture.csv` | ~7 KB | 山西路线 30 行 CSV |
| `data/routes/shanxi-ancient-architecture.geojson` | ~14 KB | 山西路线 40 features GeoJSON |
| `data/routes/shanxi-ancient-architecture.gpx` | ~12 KB | 山西路线 30 waypoint GPX |
| `assets/img/routes/shanxi-ancient-architecture-map.svg` | 7.6 KB | 山西路线静态 SVG |
| `reports/PHASE9_SHANXI_ROUTE_DATA_REPORT.md` | 本文件 | Phase 9 报告 |

### 修改文件

| 路径 | 变更 |
|------|------|
| `data/routes/routes-manifest.json` | shanxi-ancient-architecture 从 planned-data 升级为 data-v0.1 · 修正 page_url |
| `routes/index.html` | 山西路线数据卡片（v1.4.9 新增）+ 总览统计 3 条 + 路线样板 |
| `trips/shanxi-ancient-architecture-roadtrip/index.html` | 新增「路线数据」轻量模块（不动既有内容）|
| `data/routes/README.md` | 山西数据资产入表 + Phase 9 章节 |
| `index.html` | meta + hero 升级到 3 条路线 + 路线数据索引说明 |
| `assets/js/trips-data.js` | 山西 trip 卡片增加 hasRouteData 字段 |
| `scripts/build-route-assets.py` | 修 bug · 失败时不再用空 stats 覆盖 manifest |
| `README.md` | v1.4.9 描述 + 山西古建路线数据章节 |
| `CHANGELOG.md` | 顶部插入 v1.4.9 章节 |
| `docs/CONTENT_NOTES.md` | 追加 Phase 9 章节 |
| `docs/ROUTE_DATA_SPEC.md` | §12 当前已接入路线（OEDW + 辽塔 + 山西）|

---

## 新增山西数据资产

| 资产 | 路径 | 大小 | 统计 |
|------|------|------|------|
| CSV | `data/routes/shanxi-ancient-architecture.csv` | ~7 KB | 30 行 · 18 字段 |
| GeoJSON | `data/routes/shanxi-ancient-architecture.geojson` | ~14 KB | 30 Point + 10 LineString = 40 features |
| GPX | `data/routes/shanxi-ancient-architecture.gpx` | ~12 KB | 30 waypoint + 1 track |
| SVG | `assets/img/routes/shanxi-ancient-architecture-map.svg` | 7.6 KB | 1200×760 |

### 点位数

**30** 个粗点（推荐 32-36 · 实做 30）

### 段落数

**9** 段（S01-S09）

### GeoJSON Features

**40**（30 Point + 10 LineString：1 主线 + 9 分段线）

### GPX Waypoints

**30**

### 9 段分布

| 段 | 名称 | 点位数 | 主要点位 |
|----|------|--------|----------|
| S01 | 大同古都与云冈线 | 4 | 大同 / 云冈石窟 / 华严寺 / 善化寺 |
| S02 | 浑源恒山应县木构线 | 4 | 浑源 / 悬空寺 / 恒山 / 应县木塔 |
| S03 | 五台山早期木构线 | 3 | 五台山 / 佛光寺 / 南禅寺 |
| S04 | 太原晋祠府城线 | 3 | 太原 / 晋祠 / 山西博物院 |
| S05 | 平遥双林镇国线 | 3 | 平遥古城 / 双林寺 / 镇国寺 |
| S06 | 介休灵石霍州线 | 3 | 后土庙 / 张壁古堡 / 霍州署 |
| S07 | 临汾洪洞隰县线 | 3 | 广胜寺飞虹塔 / 小西天 |
| S08 | 运城永乐解州线 | 3 | 运城 / 永乐宫 / 解州关帝庙 |
| S09 | 晋东南长治晋城线 | 4 | 长治 / 法兴寺 / 青莲寺 / 玉皇庙 |

---

## Manifest 更新

- **路线总数：** 3
- **data-v0.1 路线：** 2（辽塔 + 山西）
- **planned-data 路线：** 0
- **山西 status：** `data-v0.1`
- **山西 stats：** `points: 30` · `segments: 9` · `geojson_features: 40` · `geojson_points: 30` · `geojson_lines: 10` · `gpx_waypoints: 30` · `has_svg_preview: true`
- **山西 page_url：** 修正为 `../trips/shanxi-ancient-architecture-roadtrip/`

---

## 路线工厂验证

- `build-route-assets.py --all`：✅ PASS route factory build（routes: 3）
- `build-route-assets.py --check`：✅ PASS route factory check
- `validate-route-data.py shanxi-ancient-architecture`：✅ PASS route data validation
- `validate-route-data.py --all`：✅ PASS all route data validation
- `validate-route-data.py --all --manifest-check`：✅ PASS + manifest matches
- `render-route-map-svg.py --all --check`：✅ PASS all route SVG check
- `check-routes-index-sync.py`：✅ PASS routes index sync check（routes checked: 3）
- `verify-site.sh`：✅ STATUS: PASS（通过 79 / 失败 0）
- GitHub Actions Route Data Quality Gate：✅ completed/success（commit 026510a3）

---

## 山西页面数据模块说明

在 `trips/shanxi-ancient-architecture-roadtrip/index.html` 现有「路线取舍逻辑」section 之前，新增轻量「路线数据」section：

- 静态 SVG 嵌入（1200×760）
- CSV / GeoJSON / GPX 下载按钮
- 数据说明（4 条边界）
- 不影响既有「路线取舍逻辑」/「观察清单」/「现场怎么看」等核心模块

---

## 事实边界验证

- OEDW「跨越六年」是否清除：✅ 实际内容 0 命中（仅历史报告记录）
- OEDW「22/23」是否清除：✅ 实际内容 0 命中（仅历史报告记录）
- OEDW Milestones 74–95 是否仍为 22/22：✅ 16 处命中保留
- OEDW 6,000–6,700 公里是否保留：✅ 25 处命中保留
- OEDW 是否未回退：✅ CSV / GeoJSON / GPX 完整保留
- 辽塔是否未回退：✅ 20 点 / 30 features / 20 waypoints 完整保留
- 山西数据是否标注文化自驾粗点 / 非导航 / 不保证开放状态：✅ GPX / GeoJSON / SVG / 页面均含声明

---

## 验证结果

- **本地 HTTP**：✅ 8 个路径全部 200
- **GitHub Pages**：✅ 已部署（commit 026510a）
- **线上 HTTP 200**：✅ 8 个路径全部 200（含山西数据文件与 SVG）
- **GitHub Actions**：✅ 3 次连续 success（80ff7a3 / b57e92c / 026510a）

---

## 关键 URL

- **首页：** https://conanxin.github.io/culture-roadtrip-atlas/
- **路线数据索引：** https://conanxin.github.io/culture-roadtrip-atlas/routes/
- **山西路线页面：** https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/
- **山西 CSV：** https://conanxin.github.io/culture-roadtrip-atlas/data/routes/shanxi-ancient-architecture.csv
- **山西 GeoJSON：** https://conanxin.github.io/culture-roadtrip-atlas/data/routes/shanxi-ancient-architecture.geojson
- **山西 GPX：** https://conanxin.github.io/culture-roadtrip-atlas/data/routes/shanxi-ancient-architecture.gpx
- **山西 SVG：** https://conanxin.github.io/culture-roadtrip-atlas/assets/img/routes/shanxi-ancient-architecture-map.svg
- **manifest：** https://conanxin.github.io/culture-roadtrip-atlas/data/routes/routes-manifest.json

---

## Phase 10 建议

1. **山西路线数据 v0.2**
   - 实地走访照片 / 复盘心得
   - 天气 / 季节性细节
   - 与 11 个 A 级 / 5 个 B 级文保单位的对应关系图

2. **山西路线页面增强**
   - 「路线数据」模块已经有基础 · 可加 route-data-viewer 容器
   - 添加「数据驱动路线表」（4 筛选器 + 表格）
   - 9 段分章添加 18 字段元数据

3. **北京周边路线**
   - v1.5.0 候选
   - 2-3 天短途 · 燕赵古道 / 长城 / 皇家园林
   - 复用 Phase 8 路线工厂

4. **数据驱动页面扩展**
   - 三路线并排对比卡
   - 难度分布 / 省份分布可视化
   - 实时难度+季节性叠加

5. **路线质量提升**
   - 把 v1.4.8 路线工厂流程写入 CI
   - 每次 PR 自动运行 build + validate + svg + sync + verify
   - 失败时 PR 不可合并

6. **公开数据下载**
   - 当前 3 条路线 × 4 格式 = 12 文件 · 总计 ~80 KB
   - 未来可加 ZIP 打包

7. **数据快照与历史**
   - 每次 build-route-assets.py 写一个 history snapshot
   - 跟踪 manifest 演化

8. **第三方数据源接入**
   - 接入 1-2 个公开 CSV 来源（国保单位清单 / 文旅部开放名单）
   - 自动校验 source_level

---

_辛 🔮 · 行旅图谱 · Phase 9 报告 · 2026-07-05_
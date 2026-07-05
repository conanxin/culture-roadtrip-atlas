# Phase 8 Report · Route Factory Automation & Quality Gates

**版本：** v1.4.8
**日期：** 2026-07-05
**主题：** 路线工厂自动化与质量门禁
**项目：** Culture Roadtrip Atlas

---

## STATUS

**PASS** — 所有本地 + CI 门禁通过,OEDW / 辽塔数据未回退,山西 planned-data 骨架就位,GitHub Actions workflow 成功运行。

---

## 工作分支 / Commit

- 工作分支：`main`
- 基线 commit：`59b85cc`（Phase 7 · 路线模板化与多路线复用）
- 新 commit：
  - `4f05db4` Add route factory automation and quality gates（verify-site.sh）
  - `80ff7a3` Add route factory, validators, and CI workflow（其余 11 文件）
- Push 状态：✅ origin/main 已同步
- GitHub Actions：✅ Route Data Quality Gate 成功（commit 80ff7a3 · 28724758328 · 15s）

---

## 修改 / 新增文件列表

### 新增文件

| 路径 | 大小 | 说明 |
|------|------|------|
| `scripts/build-route-assets.py` | 12.5 KB | 路线工厂入口 · 校验 + SVG + manifest 同步 |
| `scripts/check-routes-index-sync.py` | 3.5 KB | manifest 与 routes/index.html 漂移检查 |
| `.github/workflows/route-data.yml` | 1.3 KB | GitHub Actions Route Data Quality Gate |
| `reports/PHASE8_ROUTE_FACTORY_QUALITY_GATES_REPORT.md` | 本文件 | Phase 8 报告 |

### 修改文件

| 路径 | 变更 |
|------|------|
| `scripts/validate-route-data.py` | 增强为 v1.2 · `--json` 输出 + `--manifest-check` 模式 + 跳过 planned-data |
| `scripts/render-route-map-svg.py` | 增强为 v1.2 · `--check` 模式 + 跳过 planned-data |
| `scripts/verify-site.sh` | 增加 §8 Route data gates（70 → 79 项） |
| `data/routes/routes-manifest.json` | 增加 `geojson_points` / `geojson_lines` 字段 + 山西 planned-data 条目 |
| `routes/index.html` | 资产总览显示 3 条 · 新增质量门禁模块 · 新增路线工厂流程模块 · 山西 planned-data 卡片 |
| `docs/ROUTE_DATA_SPEC.md` | 追加 §11 路线工厂脚本说明 |
| `README.md` | v1.4.8 描述 + 路线工厂与质量门禁命令段 |
| `CHANGELOG.md` | 顶部插入 v1.4.8 章节 |
| `docs/CONTENT_NOTES.md` | 追加 Phase 8 章节 |

---

## 新增自动化

### 1. build-route-assets.py · 路线工厂入口

**功能**：

- 读取 manifest · 遍历每条路线
- 调用 `validate-route-data.py` 校验数据
- 调用 `render-route-map-svg.py` 生成 SVG
- 统计每条路线的 CSV / GeoJSON / GPX / SVG
- 回写 manifest 统计字段
- planned-data 路线自动跳过
- `--check` 模式：只校验不回写

**输出示例 (build)**：

```
PASS route factory build
routes: 3
- out-of-eden-walk-china: 42 points, 53 features, 42 waypoints, 10 segments, svg ok
- liao-tower-roadtrip: 20 points, 30 features, 20 waypoints, 9 segments, svg ok
manifest updated: data/routes/routes-manifest.json
```

**输出示例 (--check)**：

```
PASS route factory check
manifest matches generated statistics
routes: 3
```

### 2. check-routes-index-sync.py · 漂移检查

**功能**：

- 读取 manifest + routes/index.html
- 检查每条 route 的 slug / title / URL 文件名是否在 index 页面出现
- planned-data 路线只检查 slug

**输出**：

```
PASS routes index sync check
routes checked: 3
```

### 3. validate-route-data.py 增强说明（v1.2）

| 增强 | 说明 |
|------|------|
| `--json` | 输出 JSON 格式结果，方便 CI 解析 |
| `--manifest-check` | 校验 manifest 统计字段与实际数据一致 |
| planned-data 支持 | 自动跳过 url=null 的 planned-data 路线 |

**JSON 输出示例**：

```json
{
  "status": "PASS",
  "routes": [
    {
      "slug": "out-of-eden-walk-china",
      "passed": true,
      "csv_rows": 42,
      "geojson_points": 42,
      "geojson_lines": 11,
      "gpx_waypoints": 42,
      "segments": ["S01", "S02", ..., "S10"]
    }
  ]
}
```

### 4. render-route-map-svg.py 增强说明（v1.2）

| 增强 | 说明 |
|------|------|
| `--check` | 只校验 SVG 是否存在 + 包含必要声明，不重新生成 |
| planned-data 跳过 | `--all` / `--all --check` 都跳过 |

### 5. verify-site.sh 门禁增强

新增 §8 Route data gates（70 → 79 项）：

| 检查 | 说明 |
|------|------|
| 5 个关键文件 | routes-manifest / OEDW CSV / 辽塔 CSV / OEDW SVG / 辽塔 SVG |
| `validate-route-data.py --all --manifest-check` | |
| `render-route-map-svg.py --all --check` | |
| `build-route-assets.py --check` | |
| `check-routes-index-sync.py` | |

最终结果：**79 / 0** PASS / FAIL。

### 6. .github/workflows/route-data.yml

- **name**: Route Data Quality Gate
- **触发**：push / pull_request 修改 `data/routes/**`, `assets/img/routes/**`, `scripts/**`, `routes/**`, `trips/**`, `docs/ROUTE_DATA_SPEC.md`, `.github/workflows/route-data.yml`
- **Job**：
  - ubuntu-latest
  - checkout
  - setup-python 3.x
  - `validate-route-data.py --all --manifest-check`
  - `render-route-map-svg.py --all --check`
  - `build-route-assets.py --check`
  - `check-routes-index-sync.py`
  - `verify-site.sh`
- **不使用**：外部服务 / artifact 上传 / 安全扫描

---

## Manifest 更新摘要

| slug | status | 段数 | 点位 | features | waypoints | svg | route_type |
|------|--------|------|------|----------|-----------|-----|------------|
| out-of-eden-walk-china | 50% | 10 | 42 | 53 (42P+11L) | 42 | ✅ | cultural_replica |
| liao-tower-roadtrip | data-v0.1 | 9 | 20 | 30 (20P+10L) | 20 | ✅ | cultural_roadtrip |
| shanxi-ancient-architecture | planned-data | 0 | 0 | 0 | 0 | ❌ | cultural_roadtrip |

新增加字段：

- `geojson_points`：Point feature 数
- `geojson_lines`：LineString feature 数

新增加路线：

- `shanxi-ancient-architecture` · planned-data · 4 个 URL 全 null · 不创建空数据

---

## 山西 planned-data 条目说明

```json
{
  "slug": "shanxi-ancient-architecture",
  "title": "山西古建路线",
  "status": "planned-data",
  "route_type": "cultural_roadtrip",
  "segments": 0,
  "points": 0,
  "geojson_features": 0,
  "geojson_points": 0,
  "geojson_lines": 0,
  "gpx_waypoints": 0,
  "has_svg_preview": false,
  "is_original_gps_track": false,
  "for_navigation": false,
  "approximate_distance_km": null,
  "time_span": "11 天 10 晚 / 8 天压缩 / 14 天慢行",
  "data_version": null,
  "page_url": "../trips/shanxi-ancient-architecture/",
  "csv_url": null,
  "geojson_url": null,
  "gpx_url": null,
  "svg_url": null,
  "route_template": "Long-distance cultural roadtrip (Tang/Song/Liao/Jin wood structures)"
}
```

校验脚本与工厂脚本自动跳过此条目。索引页显示为 planned-data 卡片，不提供下载按钮。

---

## OEDW 数据是否未回退

✅ **完全未回退**

| 文件 | 状态 |
|------|------|
| `data/routes/out-of-eden-walk-china.csv` | 42 行未变 |
| `data/routes/out-of-eden-walk-china.geojson` | 42 Point + 11 LineString 未变 |
| `data/routes/out-of-eden-walk-china.gpx` | 42 waypoint 未变 |
| `assets/img/routes/out-of-eden-walk-china-map.svg` | 重新生成 · 内容等价 |
| `trips/out-of-eden-walk-china/index.html` | 未改事实边界 |

### 关键事实边界保留

- ✅ "跨越六年" 仅历史报告记录（实际内容 0 命中）
- ✅ "22/23" 仅历史报告记录（实际内容 0 命中）
- ✅ "22/22" 保留（15 处命中）
- ✅ "6,000–6,700 公里" 保留（25 处命中）
- ✅ "两年多 / 两年四个月 / 两年半左右" 保留
- ✅ "卢沟桥 → 天安门 → 小汤山" 保留
- ✅ 黄海三层时间（2023 冬 / 2024.6 / 2024.8）保留
- ✅ "文化复刻粗点" 保留
- ✅ "非 Paul Salopek 原始 GPS 轨迹" 保留
- ✅ "非导航" 保留

---

## 辽塔数据是否未回退

✅ **完全未回退**

| 文件 | 状态 |
|------|------|
| `data/routes/liao-tower-roadtrip.csv` | 20 行未变 |
| `data/routes/liao-tower-roadtrip.geojson` | 20 Point + 10 LineString 未变 |
| `data/routes/liao-tower-roadtrip.gpx` | 20 waypoint 未变 |
| `assets/img/routes/liao-tower-roadtrip-map.svg` | 重新生成 · 内容等价 |
| `trips/liao-tower-roadtrip/index.html` | 保留 Phase 7 路线数据模块 |

---

## 本地命令验证结果

```text
===build--all===
PASS route factory build
routes: 3
- out-of-eden-walk-china: 42 points, 53 features, 42 waypoints, 10 segments, svg ok
- liao-tower-roadtrip: 20 points, 30 features, 20 waypoints, 9 segments, svg ok
manifest updated: data/routes/routes-manifest.json

===build--check===
PASS route factory check
manifest matches generated statistics
routes: 3

===validate--all===
PASS all route data validation
routes: 2

===validate--all --manifest-check===
PASS all route data validation
manifest matches generated statistics
routes: 2

===validate--all --json===
status: PASS, routes: 2

===render--all===
PASS all route SVG generation
routes: 3

===render--all --check===
PASS all route SVG check
routes: 2

===check-routes-index-sync===
PASS routes index sync check
routes checked: 3
```

---

## verify-site.sh 结果

```
通过: 79
失败: 0
✓ STATUS: PASS
```

- 原 70 项检查 + 9 项 Route data gates = 79 项
- Route data gates：
  - 5 个关键文件存在
  - validate-route-data.py --all --manifest-check PASS
  - render-route-map-svg.py --all --check PASS
  - build-route-assets.py --check PASS
  - check-routes-index-sync.py PASS

---

## GitHub Actions 运行结果

```
Route Data Quality Gate: completed/success | 80ff7a3f | 2026-07-05T00:45:45Z
```

- 触发 commit：`80ff7a3`
- 状态：success
- 耗时：15s

---

## GitHub Pages 部署结果

- 推送 commit：`80ff7a3`（含 `4f05db4` 之上）
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
| `https://conanxin.github.io/culture-roadtrip-atlas/assets/img/routes/out-of-eden-walk-china-map.svg` | 200 |
| `https://conanxin.github.io/culture-roadtrip-atlas/assets/img/routes/liao-tower-roadtrip-map.svg` | 200 |

全部 200。

---

## Phase 9 建议

1. **山西古建路线数据化（v1.5.0 候选）**
   - 11 天 10 晚 · 11 个 A 级核心点位 → data-v0.1
   - 复用 build-route-assets.py 一次完成校验 + SVG + manifest 同步
   - 复用 ROUTE_DATA_SPEC 18 字段

2. **build-route-assets.py 增强**
   - 支持 `--slug <slug> --check` 模式（按 Phase 8 spec 实际未单测）
   - 增加 `--dry-run` 模式（不回写 manifest，只输出计划）
   - 增加统计字段回写前的 diff 输出

3. **验证脚本进一步拆分**
   - `validate-route-data.py` 拆分为 base + 各路线 threshold 配置文件
   - `check-routes-index-sync.py` 增加更多字段（segments / has_svg_preview 等）

4. **GitHub Actions 矩阵**
   - 当前只在 ubuntu-latest 运行
   - 可考虑增加 Python 3.10 / 3.11 / 3.12 矩阵

5. **数据下载 / 浏览增强**
   - route-data-viewer.js 支持 planned-data 路线占位卡
   - 移动端体验优化

6. **数据驱动页面扩展**
   - OEDW / 辽塔 / 山西 三路线并排对比
   - manifest 统计可视化（用纯 CSS/SVG 简单图表）

7. **路线 manifest 元数据扩展**
   - 增加 `route_difficulty_distribution`（自动统计）
   - 增加 `province_coverage`（自动统计）
   - 增加 `last_updated` 单路线级别

8. **自动数据快照**
   - 每次 build-route-assets.py 写一个 history JSON
   - 跟踪 manifest 演化

---

_辛 🔮 · 行旅图谱 · Phase 8 报告 · 2026-07-05_
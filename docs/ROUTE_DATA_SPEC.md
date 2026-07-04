# 行旅图谱 · 通用路线数据规范（ROUTE_DATA_SPEC）

> 把任意人文路线沉淀为可下载、可审校、可复用的 CSV / GeoJSON / GPX 数据资产。

**版本：** v1.0
**适用项目版本：** 行旅图谱 v1.4.7+
**最后更新：** 2026-07-05

---

## 1. 规范定位

行旅图谱的路线数据是**文化复刻粗点**（cultural replica waypoints）数据，用于：

- ✅ 研究 / 写作 / 旅行规划参考
- ✅ 静态地图制作（QGIS / geojson.io / Leaflet / Mapbox）
- ✅ 表格分析与可视化（Pandas / Excel / Numbers）
- ✅ 与行旅图谱路线页面双向联动

它**不是**：

- ❌ 实时导航数据
- ❌ 路况 / 开放状态 / 安全判断依据
- ❌ 历史人物或作者（如 Paul Salopek）的原始 GPS 轨迹
- ❌ 户外穿越或紧急救援参考

---

## 2. 文件结构

每条路线在仓库中产生四个核心文件：

```
data/routes/
├── routes-manifest.json       # 项目级路线登记表（所有路线共享）
├── <route-slug>.csv           # 点位表格
├── <route-slug>.geojson       # 几何 + 元数据
├── <route-slug>.gpx           # 路线 waypoint / track
└── README.md                  # 数据目录说明
assets/img/routes/
└── <route-slug>-map.svg       # 静态 SVG 路线示意图（基于 GeoJSON 生成）
```

`<route-slug>` 命名规范：小写字母 + 连字符，例如 `out-of-eden-walk-china`、`liao-tower-roadtrip`。

---

## 3. CSV 字段规范

CSV 文件使用 UTF-8 编码、首行为表头。**18 个必需字段**（顺序固定）：

| # | 字段 | 类型 | 说明 |
|---|------|------|------|
| 1 | `id` | string | 点位唯一编号（`<route-prefix>-Pxxx`） |
| 2 | `sequence` | int | 全线序号（1, 2, 3, …） |
| 3 | `segment_id` | string | 段编号（`S01`–`S10` 等） |
| 4 | `segment_name` | string | 段中文名 |
| 5 | `point_name` | string | 点位中文名 |
| 6 | `province` | string | 省份（拼音或英文） |
| 7 | `city_or_area` | string | 城市或区域 |
| 8 | `latitude` | float | WGS84 纬度 |
| 9 | `longitude` | float | WGS84 经度 |
| 10 | `coordinate_precision` | enum | 坐标精度（见 §4.1） |
| 11 | `source_level` | enum | 来源等级（见 §4.2） |
| 12 | `replication_feasibility` | enum | 复刻可行性（见 §4.3） |
| 13 | `difficulty` | enum | 旅行难度（见 §4.4） |
| 14 | `best_season` | string | 最佳季节（中文短语） |
| 15 | `transport_hint` | string | 交通提示 |
| 16 | `risk_note` | string | 风险提示 |
| 17 | `source_note` | string | 来源说明 |
| 18 | `url` | string | 官方来源 URL（可空） |

---

## 4. 字段取值规范

### 4.1 coordinate_precision

| 取值 | 含义 |
|------|------|
| `city` | 城市级精度 |
| `landmark` | 景区 / 古迹 / 地标级精度 |
| `region` | 区域级精度（覆盖一个县/区） |
| `approximate` | 近似坐标（不可精确导航） |
| `unknown` | 不确定位置 |

### 4.2 source_level

| 取值 | 含义 |
|------|------|
| `A_official_oedw` | A 级 · Out of Eden Walk 官方 milestone / dispatch（仅 OEDW 路线使用） |
| `B_partner_or_education` | B 级 · 合作地图、NatGeo Education、官方合作伙伴 |
| `C_chinese_media` | C 级 · 中文媒体、纪录片、展览材料 |
| `D_reconstructed_for_travel` | D 级 · 基于公开材料重建的旅行节点 |
| `E_project_internal` | E 级 · 行旅图谱项目内整理（路线页面、笔记、行程表） |

### 4.3 replication_feasibility

| 取值 | 含义 |
|------|------|
| `high` | 高 · 普通旅行者可直接复刻 |
| `medium` | 中 · 需要准备或请向导 |
| `low` | 低 · 不建议普通复刻 |
| `not_recommended` | 不推荐 |
| `reading_only` | 仅作阅读背景 |

### 4.4 difficulty

| 取值 | 含义 |
|------|------|
| `easy` | 容易 |
| `medium` | 中等 |
| `hard` | 困难 |
| `extreme` | 极限 |
| `mixed` | 混合（多段难度不同） |

---

## 5. GeoJSON 规范

### 5.1 顶层结构

```json
{
  "type": "FeatureCollection",
  "name": "<route-slug>-<route-type>",
  "metadata": { ... },
  "features": [ ... ]
}
```

### 5.2 metadata 必填字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 路线标题（中文） |
| `version` | string | 数据版本（如 `v1.4.7`） |
| `route_type` | string | `cultural_replica` 或 `cultural_roadtrip` |
| `is_original_gps_track` | bool | 必须为 `false` |
| `disclaimer` | string | 非原始轨迹 / 非导航声明 |
| `updated_at` | string | YYYY-MM-DD |

### 5.3 features

- **Point feature** 与 CSV 一一对应（顺序、ID、字段均匹配）。
- 至少 1 个 `LineString`（generalized_route_line），由所有 Point 顺序连接。
- 鼓励为每个 segment 增加 1 个分段 `LineString`（feature_type = `segment_generalized_line`）。
- 所有 LineString 的 `properties` 必须包含 `is_original_gps_track: false` 与 `disclaimer: "not for navigation"`。

---

## 6. GPX 规范

- 符合 GPX 1.1。
- 每个 CSV 点位对应一个 `<wpt>` waypoint（含 lat/lon/name/desc）。
- 可有 1 个 `<trk>` 概括 track（段顺序连接）。
- `<metadata><desc>` 必须包含 `cultural replica` / `not original GPS` / `not for navigation`。
- waypoint 数量必须等于 CSV 行数。

---

## 7. SVG 预览规范

由 GeoJSON 自动生成（`scripts/render-route-map-svg.py`），无外部底图：

- 1200 × 760 viewBox
- 米白背景 + 墨绿主路线 + 暗金点位
- 起点（深墨绿）+ 终点（暗红）特别标注
- 段落编号标签（S01–Sxx）
- 顶部标题 + 底部图例 + 红色免责声明
- `<title>` 与 `<desc>` 中必须声明 `cultural replica` / `not for navigation` / `not original GPS track`

---

## 8. 路线 manifest（routes-manifest.json）

项目级登记表，所有路线共享：

```json
{
  "version": "v1.4.7",
  "updated_at": "YYYY-MM-DD",
  "description": "...",
  "routes": [
    {
      "slug": "out-of-eden-walk-china",
      "title": "...",
      "status": "50%",
      "route_type": "cultural_replica",
      "segments": 10,
      "points": 42,
      ...
    }
  ]
}
```

每次新增或修改路线数据后必须同步更新 manifest，确保 `validate-route-data.py --all` 与 `render-route-map-svg.py --all` 能正确遍历。

---

## 9. 验证命令

```bash
# 单路线校验
python3 scripts/validate-route-data.py <route-slug>

# 默认校验 OEDW
python3 scripts/validate-route-data.py

# 校验所有路线（读取 manifest）
python3 scripts/validate-route-data.py --all

# 单路线生成 SVG
python3 scripts/render-route-map-svg.py <route-slug>

# 默认生成 OEDW SVG
python3 scripts/render-route-map-svg.py

# 生成所有路线 SVG（读取 manifest）
python3 scripts/render-route-map-svg.py --all
```

校验失败时必须修正 CSV / GeoJSON / GPX 一致性与字段完整性后再提交。

---

## 10. 扩展规则

新增路线时：

1. 先复制本规范并按路线特点调整 `segments` / `points` 期望值。
2. 用同样的 18 个 CSV 字段。
3. 用同样的 GeoJSON / GPX / SVG 元数据声明。
4. 在 `routes-manifest.json` 增加条目。
5. 用 `validate-route-data.py --all` 和 `render-route-map-svg.py --all` 全量验证。

---

_辛 🔮 · 行旅图谱 · 数据规范 · 2026-07-05_
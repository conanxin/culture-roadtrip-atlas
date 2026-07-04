# 路线数据 · 行旅图谱

> 把行旅图谱中的人文路线沉淀为可下载、可审校、可复用的数据资产。

**最后更新：** 2026-07-04
**项目版本：** v1.4.5
**数据精度：** 文化复刻粗点（approximate）

---

## 一、数据目录说明

本目录收录行旅图谱中各条人文路线的可下载数据资产。所有数据均为**文化复刻粗点**（cultural replica waypoints），不是 Paul Salopek 原始 GPS 轨迹，也不应用于导航或安全穿越指引。

**数据使用范围：**
- ✅ 研究 / 写作 / 旅行规划参考
- ✅ 静态地图制作（QGIS / geojson.io / Leaflet 等）
- ✅ 表格分析与可视化
- ❌ 不用于实时导航
- ❌ 不用于安全穿越或紧急救援
- ❌ 不代表路况、开放状态、交通管制的当前实际情况

---

## 二、当前数据文件

| 文件 | 格式 | 用途 | 大小 |
|------|------|------|------|
| `out-of-eden-walk-china.csv` | CSV | 表格分析、Excel / Pandas | ~7 KB |
| `out-of-eden-walk-china.geojson` | GeoJSON | QGIS / geojson.io / Leaflet 静态地图 | ~14 KB |
| `out-of-eden-walk-china.gpx` | GPX 1.1 | 粗略 waypoint 查看（不可导航）| ~12 KB |

未来规划：
- `liao-tower-roadtrip.csv/geojson/gpx` （规划中）
- `shanxi-ancient-architecture-roadtrip.csv/geojson/gpx` （规划中）

---

## 三、字段说明

### CSV 字段（18 个）

| 字段 | 说明 | 示例 |
|------|------|------|
| `id` | 点位唯一编号 | `OEDW-P001` |
| `sequence` | 全线序号（1–42）| 1 |
| `segment_id` | 段编号（S01–S10）| S01 |
| `segment_name` | 段中文名 | 滇西重启线 |
| `point_name` | 点位中文名 | 腾冲 |
| `province` | 省份（拼音或英文）| Yunnan |
| `city_or_area` | 城市或区域 | Tengchong |
| `latitude` / `longitude` | WGS84 经纬度 | 25.0204 |
| `coordinate_precision` | 坐标精度（见下）| city |
| `source_level` | 来源等级（见下）| A_official_oedw |
| `replication_feasibility` | 复刻可行性（见下）| high |
| `difficulty` | 旅行难度 | easy / medium / hard |
| `best_season` | 最佳季节 | Oct-Apr |
| `transport_hint` | 交通提示 | 腾冲驼峰机场 / 高铁保山 |
| `risk_note` | 风险提示 | 边境管控禁止普通徒步 |
| `source_note` | 来源说明 | Milestone 74 (2021-10) |
| `url` | 官方来源 URL | （空表示无官方 URL）|

### coordinate_precision 取值

| 值 | 含义 |
|---|------|
| `city` | 城市级精度 |
| `landmark` | 景区 / 古迹 / 地标级精度 |
| `region` | 区域级精度（覆盖一个县/区）|
| `approximate` | 近似坐标（不可精确导航）|
| `unknown` | 不确定位置 |

### source_level 取值

| 值 | 含义 |
|---|------|
| `A_official_oedw` | A 级 · Out of Eden Walk 官方 milestone/dispatch |
| `B_partner_or_education` | B 级 · 合作地图、NatGeo Education、官方合作伙伴 |
| `C_chinese_media` | C 级 · 中文媒体、纪录片、展览材料 |
| `D_reconstructed_for_travel` | D 级 · 基于公开材料重建的旅行节点 |

### replication_feasibility 取值

| 值 | 含义 |
|---|------|
| `high` | 高 · 普通旅行者可直接复刻 |
| `medium` | 中 · 需要准备或请向导 |
| `low` | 低 · 不建议普通复刻 |
| `not_recommended` | 不推荐 |
| `reading_only` | 仅作阅读背景 |

---

## 四、数据限制

### 4.1 不是原始 GPS 轨迹

本目录所有数据基于以下公开材料整理：
- Out of Eden Walk 官方 milestone / dispatch（74–95 全部 22 条）
- NatGeo Education 与合作伙伴地图
- 中文媒体（解放日报、上观新闻、纪录片《永远的行走：与中国相遇》）
- 上海纽约大学 ICA 展览材料

**Paul Salopek 原始 GPS 轨迹由 National Geographic 持有，本项目未访问、未伪造、未重建。**

### 4.2 文化复刻粗点定义

- 允许使用城市、景区、古道节点、港口等公开可识别地点的粗略经纬度
- 不伪造精确步行轨迹
- 不把不确定村镇写成精确坐标
- 不确定点位使用附近城市、景区或区域中心点

### 4.3 时间口径

| 时间点 | 含义 |
|-------|------|
| 2021 秋 | 云南西部重启（Milestone 74）|
| 2023 冬 | 主体步行抵达黄海附近 |
| 2024.6 | 补齐大连港缺口 |
| 2024.8 | 发布《Goodbye to China》总结 |

### 4.4 路线归属

- Milestone 74–95 = 22 条 = 中国陆上行走段
- Milestone 96+ = 黄海渡船段，不计入中国陆上复刻
- Milestone 93、94 官方页面写辽宁，部分后续制图说明曾误写吉林，以 milestone 独立页面为准

### 4.5 里程口径

中国段官方《Goodbye to China》表述为 "more than 6,000 kilometers"，《New Map: Ancient Roads of China》表述为 "6,700 kilometers"，本数据采用区间口径 **约 6,000–6,700 公里**。

---

## 五、如何使用

### 5.1 CSV（表格分析）

```bash
# 用 Excel / Numbers 直接打开
open data/routes/out-of-eden-walk-china.csv

# 用 Pandas
python3 -c "
import pandas as pd
df = pd.read_csv('data/routes/out-of-eden-walk-china.csv')
print(df.groupby('segment_id').size())
"
```

### 5.2 GeoJSON（静态地图）

```bash
# geojson.io 在线查看
open https://geojson.io  # 然后拖入文件

# QGIS 桌面
file → open → 选择 out-of-eden-walk-china.geojson

# Leaflet / Mapbox 静态嵌入
# 示例：https://leafletjs.com/examples/geojson/
```

### 5.3 GPX（粗略 waypoint 查看）

```bash
# 仅作粗略 waypoint 查看，**不要用于导航**
# 可用工具：Google Earth、GPX Viewer、QGIS
open data/routes/out-of-eden-walk-china.gpx
```

⚠️ **GPX 文件仅作为 waypoint 数据保存格式，不应用于任何导航设备或户外活动。**

---

## 六、安全说明

- 边境、深山、高海拔路段（高黎贡山、木里、横断山）必须请当地向导
- 不要单独徒步穿越无人区
- 不要在车流密集的 G108 / G316 / G1 / 京哈高速 / 包茂高速 沿公路步行
- 北京 113 公里 / 70 英里三日城市步行线，必须分段走，不要连续硬走
- 实地走访前请以最新官方材料为准
- 数据中标注的 risk_note 与 difficulty 仅供参考，实际出行前需独立评估

---

## 七、未来 Phase 6 可扩展方向

1. **多路线数据化**
   - 辽塔巡礼路线数据（v1.5.0）
   - 山西古建路线数据（v1.5.0）
   - 其他规划中路线

2. **数据增强**
   - 实地走访照片链接
   - 维度更高的语义标注（POI 类型、文化主题）
   - 多语言版本（中英文）

3. **可视化增强**
   - SVG 路线示意图（基于本数据生成）
   - 与 leaflet 静态嵌入结合的离线浏览页

4. **数据校验工具**
   - 自动检查坐标范围（中国境内）
   - 自动检查字段完整性
   - 与路线页内容的一致性检查

---

_辛 🔮 · 行旅图谱 · 数据资产 · 2026-07-04_
---

## Phase 6 · 数据处理流程（v1.4.6 新增）

### 处理流程

```
CSV / GeoJSON / GPX
  ↓ validate-route-data.py 校验
PASS / FAIL
  ↓ render-route-map-svg.py 渲染
assets/img/routes/<slug>-map.svg
  ↓ route-data-viewer.js (前端 fetch)
#route-data-viewer 容器 → 摘要 + 筛选器 + 表格
```

### 脚本使用方式

#### 1. 校验数据

```bash
python3 scripts/validate-route-data.py
```

输出示例：
```
行旅图谱 · 路线数据校验
route: out-of-eden-walk-china
--------------------------------------------------
CSV: out-of-eden-walk-china.csv · 42 行 · PASS
GeoJSON: out-of-eden-walk-china.geojson · 42 points · 11 lines · PASS
GPX: out-of-eden-walk-china.gpx · 42 waypoints · PASS
--------------------------------------------------
PASS route data validation
```

退出码：
- 0 = PASS
- 1 = FAIL

#### 2. 生成 SVG 静态地图

```bash
python3 scripts/render-route-map-svg.py
```

输出：
- `assets/img/routes/out-of-eden-walk-china-map.svg`（~9 KB）
- SVG 必含 `not Paul Salopek original GPS track` / `not for navigation` / `cultural replica`

#### 3. 自定义 slug

两个脚本都支持传入其他 route slug：

```bash
python3 scripts/validate-route-data.py liao-tower-roadtrip
python3 scripts/render-route-map-svg.py liao-tower-roadtrip
```

### SVG 预览说明

- 宽高 1200 × 760
- 米白背景 + 墨绿路线 + 暗金点位
- 起点（深墨绿）+ 终点（暗红）特别标注
- 10 段 S01–S10 编号标签
- 顶部标题 + 底部图例 + 红色免责声明
- 移动端可缩放（viewBox 缩放）

### 数据驱动页面说明

`assets/js/route-data-viewer.js` 用 fetch() 加载 GeoJSON，渲染到 `<section id="route-data-viewer">` 容器中：

```html
<section id="route-data-viewer"
         class="route-data-viewer"
         data-route-geojson="../../data/routes/out-of-eden-walk-china.geojson"
         data-route-name="Out of Eden Walk 中国段">
  <div class="route-data-loading">正在加载路线数据……</div>
  <noscript>浏览器未启用 JavaScript。请直接下载 CSV / GeoJSON / GPX 文件查看路线数据。</noscript>
</section>
```

页面底部引入：
```html
<script src="../../assets/js/route-data-viewer.js"></script>
```

特性：
- 4 个筛选器（段落 / 省份 / 难度 / 可复刻性）
- 表格字段：序号 / 段落 / 点位 / 省份 / 地区 / 精度 / 难度 / 可复刻性 / 风险提示
- 失败 fallback 显示下载链接
- 无依赖、纯 Vanilla JS


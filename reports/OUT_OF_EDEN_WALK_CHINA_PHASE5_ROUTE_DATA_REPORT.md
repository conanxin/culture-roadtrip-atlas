# Out of Eden Walk China · Phase 5 Route Data · 报告

**版本：** v1.4.5
**日期：** 2026-07-04
**任务定位：** Out of Eden Walk 中国段 · 地图数据与路线索引
**工作分支：** main
**基线 commit：** 7d025f1 (Phase 4)
**新 commit：** 见推送后 `git log --oneline -1`

---

## 一、STATUS

**PASS**

---

## 二、Git 信息

- **工作分支：** main
- **基线 commit：** 7d025f1 (Phase 4 发布包装)
- **新 commit：** 见 `git log --oneline -1` 推送后
- **push 目标：** origin/main

---

## 三、修改文件清单

| 文件 | 操作 | 说明 |
|-----|------|------|
| `data/routes/out-of-eden-walk-china.csv` | 新增 | 42 行 · 18 字段 · 10 段覆盖 |
| `data/routes/out-of-eden-walk-china.geojson` | 新增 | 53 Feature · 42 Point + 11 LineString |
| `data/routes/out-of-eden-walk-china.gpx` | 新增 | GPX 1.1 · 42 waypoints + 1 track |
| `data/routes/README.md` | 新增 | 数据说明、字段定义、使用方法、Phase 6 方向 |
| `routes/index.html` | 新增 | 路线数据索引页 · Hero + 说明 + 卡片 + 未来路线 |
| `trips/out-of-eden-walk-china/index.html` | 修改 | 1690 → 1755 行 · 新增"下载路线数据"模块 + 版本升级到 v1.4.5 |
| `assets/css/styles.css` | 追加 | 6765 → 7113 行 · 新增 v1.4.5 样式约 250 行 |
| `index.html` | 修改 | 导航增加"路线数据"链接 + 底部新增 CTA 卡片 |
| `README.md` | 修改 | 版本表新增 v1.4.5 · OEDW 状态更新 · 新增 routes URL |
| `CHANGELOG.md` | 修改 | 顶部新增 v1.4.5 章节 |
| `docs/CONTENT_NOTES.md` | 修改 | 追加 Phase 5 章节 |
| `reports/OUT_OF_EDEN_WALK_CHINA_PHASE5_ROUTE_DATA_REPORT.md` | 新增 | 本报告 |

---

## 四、数据文件清单

| 文件 | 大小 | 格式 | 用途 |
|-----|------|------|------|
| `data/routes/out-of-eden-walk-china.csv` | ~7 KB | CSV UTF-8 | 表格分析、Excel、Pandas |
| `data/routes/out-of-eden-walk-china.geojson` | ~14 KB | GeoJSON FeatureCollection | QGIS、geojson.io、Leaflet 静态地图 |
| `data/routes/out-of-eden-walk-china.gpx` | ~12 KB | GPX 1.1 | 粗略 waypoint 查看（不可导航）|
| `data/routes/README.md` | ~4 KB | Markdown | 数据说明、字段、使用方法 |
| `routes/index.html` | ~10 KB | HTML | 路线数据索引页 |

---

## 五、数据规模

### CSV
- **行数：** 42
- **字段数：** 18（id / sequence / segment_id / segment_name / point_name / province / city_or_area / latitude / longitude / coordinate_precision / source_level / replication_feasibility / difficulty / best_season / transport_hint / risk_note / source_note / url）

### GeoJSON
- **总 Feature 数：** 53
  - Point：42（与 CSV 一一对应）
  - LineString：11（1 主路线 + 10 段路线）
- **元数据：** title / version / route_type / is_original_gps_track / disclaimer / source_scope / updated_at / coordinate_systems / approximate_distance_km / time_span / segments_count / points_count

### GPX
- **waypoint 数：** 42
- **track 数：** 1（42 个 track point，连接所有 waypoint）
- **metadata：** name / desc（含 "Cultural replica waypoints and generalized route only; not Paul Salopek's original GPS track; not for navigation."）/ author / copyright / link / time / keywords / bounds

---

## 六、10 段路线覆盖情况

| 段 | 段名 | 点位数 | 关键点位 |
|---|------|------|---------|
| S01 | 滇西重启线 | 5 | 边境 / 腾冲 / 和顺 / 高黎贡山 / 大理 |
| S02 | 大理丽江雪山线 | 4 | 喜洲 / 洱源 / 丽江 / 玉龙雪山 |
| S03 | 茶马古道木里线 | 3 | 泸沽湖 / 木里 / 康定 |
| S04 | 川西南雅安线 | 5 | 天全 / 雅安 / 平乐 / 三星堆 / 绵竹 |
| S05 | 剑门蜀道汉中线 | 4 | 剑门关 / 广元 / 汉中 / 秦岭 |
| S06 | 关中陕北线 | 4 | 西安 / 宜君 / 延安 / 壶口 |
| S07 | 晋西雁门关线 | 4 | 吕梁 / 忻州 / 雁门关 / 周口店 |
| S08 | 北京城市步行线 | 4 | 卢沟桥 / 天安门 / 胡同 / 小汤山 |
| S09 | 京北长城承德线 | 3 | 司马台 / 古北口 / 承德 |
| S10 | 辽宁大连黄海线 | 6 | 锦州 / 沈阳 / 辽阳 / 乡村 / 大连港 / 黄海 |
| **合计** | **10 段** | **42 点** | |

---

## 七、数据字段说明

### coordinate_precision（5 级）

| 值 | 含义 |
|---|------|
| `city` | 城市级精度 |
| `landmark` | 景区 / 古迹 / 地标级 |
| `region` | 区域级（覆盖一个县/区）|
| `approximate` | 近似坐标（不可精确导航）|
| `unknown` | 不确定位置 |

### source_level（4 级）

| 值 | 含义 |
|---|------|
| `A_official_oedw` | A 级 · Out of Eden Walk 官方 milestone/dispatch |
| `B_partner_or_education` | B 级 · 合作地图、NatGeo Education |
| `C_chinese_media` | C 级 · 中文媒体、纪录片、展览 |
| `D_reconstructed_for_travel` | D 级 · 基于公开材料重建 |

### replication_feasibility（5 级）

| 值 | 含义 |
|---|------|
| `high` | 高 · 普通旅行者可直接复刻 |
| `medium` | 中 · 需要准备或请向导 |
| `low` | 低 · 不建议普通复刻 |
| `not_recommended` | 不推荐 |
| `reading_only` | 仅作阅读背景 |

---

## 八、"文化复刻粗点 / 非原始 GPS / 非导航"声明覆盖

| 位置 | 是否覆盖 |
|------|---------|
| CSV（间接通过 README 说明） | ✓ |
| GeoJSON metadata.disclaimer | ✓ "本数据不是 Paul Salopek 原始 GPS 轨迹，仅为文化复刻路线粗点。" |
| GeoJSON LineString properties.warning | ✓ "Generalized cultural replica line only. Not for navigation. Not Paul Salopek's original GPS track." |
| GeoJSON LineString properties.is_original_gps_track | ✓ false |
| GPX metadata.desc | ✓ "Cultural replica waypoints and generalized route only; not Paul Salopek's original GPS track; not for navigation." |
| GPX trk.desc | ✓ "Generalized cultural replica track connecting 10 segments and 42 waypoints. Not Paul Salopek's original GPS track. Not for navigation." |
| `data/routes/README.md` 全文 | ✓ 多处说明 |
| `routes/index.html` 数据说明卡 | ✓ 多处说明 |
| `trips/out-of-eden-walk-china/index.html` 下载模块 | ✓ 多处说明 |

---

## 九、URL 列表

| 类型 | URL |
|------|-----|
| 路线数据索引页 | https://conanxin.github.io/culture-roadtrip-atlas/routes/ |
| CSV | https://conanxin.github.io/culture-roadtrip-atlas/data/routes/out-of-eden-walk-china.csv |
| GeoJSON | https://conanxin.github.io/culture-roadtrip-atlas/data/routes/out-of-eden-walk-china.geojson |
| GPX | https://conanxin.github.io/culture-roadtrip-atlas/data/routes/out-of-eden-walk-china.gpx |
| OEDW 页面 | https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/ |

---

## 十、验证结果

### 10.1 本地数据验证（用户指定脚本）

```
PASS data validation: 42 CSV rows, 42 GeoJSON points, 11 line(s)
```

### 10.2 本地 HTTP（用户指定）

| URL | HTTP |
|-----|------|
| `/` | 200 |
| `/routes/` | 200 |
| `/trips/out-of-eden-walk-china/` | 200 |
| `/data/routes/out-of-eden-walk-china.csv` | 200 |
| `/data/routes/out-of-eden-walk-china.geojson` | 200 |
| `/data/routes/out-of-eden-walk-china.gpx` | 200 |

### 10.3 verify-site.sh

```
STATUS: PASS（70 通过 / 0 失败）
```

### 10.4 关键事实边界验证

| 事实点 | 状态 | 结果 |
|-------|------|------|
| "跨越六年" | ✅ 清除 | grep 无 result |
| "22/23" | ✅ 清除 | grep 无 result |
| Milestones 74–95 = 22/22 | ✅ 保留 | HTML 2 处命中 |
| 6,000–6,700 公里 | ✅ 保留 | HTML 10 处命中 |
| 北京段 卢沟桥→天安门→小汤山 | ✅ 保留 | 卢沟桥 11、小汤山 11 |
| 黄海三层时间 | ✅ 保留 | HTML 12 处命中 |

### 10.5 关键词验收

| 关键词 | 结果 |
|-------|------|
| 下载路线数据 | OEDW 2 处 |
| 路线数据索引 | 13 处 |
| 文化复刻粗点 | 11 处 |
| 不是 Paul 原始 GPS / not paul salopek | 5 处 |
| out-of-eden-walk-china.geojson | 5 处 |
| out-of-eden-walk-china.csv | 7 处 |
| out-of-eden-walk-china.gpx | 5 处 |

### 10.6 GitHub Pages

- 推送后等待 30-60s
- HTTP/2 200（待推送后验证）

### 10.7 线上 HTTP 200

- 见 10.6（推送后验证）

---

## 十一、Phase 6 建议（不在本轮范围）

1. **多路线数据化**
   - 辽塔巡礼路线数据（v1.5.0）
   - 山西古建路线数据（v1.5.0）
   - 其他 5 条规划中路线

2. **数据可视化**
   - 基于 GeoJSON 的 SVG 路线示意图
   - 与 Leaflet 静态嵌入结合的离线浏览页
   - 与 D3 的拓扑图（段→点位层级）

3. **数据校验工具**
   - 自动检查坐标范围（中国境内）
   - 自动检查字段完整性
   - 与路线页内容的一致性检查（点位同步）

4. **多语言版本**
   - 中英文双语 GeoJSON 属性
   - 英文版路线数据索引页

5. **POI 语义标注**
   - POI 类型（古城 / 山地 / 海港 / 关隘）
   - 文化主题（茶马古道 / 蜀道 / 长城 / 黄土）
   - 朝代 / 历史时期

6. **路线数据 API**
   - 不引入后端，但可生成静态 JSON-LD
   - 便于 SEO 和结构化数据

---

_辛 🔮 · 2026-07-04 · Out of Eden Walk China Phase 5 Route Data_
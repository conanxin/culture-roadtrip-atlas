# Out of Eden Walk China · Phase 6 Data-driven Map Preview · 报告

**版本：** v1.4.6
**日期：** 2026-07-04
**任务定位：** Out of Eden Walk 中国段 · 数据驱动页面与静态地图预览
**工作分支：** main
**基线 commit：** 781740a (Phase 5)
**新 commit：** 见推送后 `git log --oneline -1`

---

## 一、STATUS

**PASS**

---

## 二、修改文件清单

| 文件 | 操作 | 说明 |
|-----|------|------|
| `scripts/validate-route-data.py` | 新增 | 永久数据校验脚本（固化 Phase 5 临时校验逻辑）|
| `scripts/render-route-map-svg.py` | 新增 | GeoJSON → SVG 静态地图生成脚本 |
| `assets/img/routes/out-of-eden-walk-china-map.svg` | 新增 | 静态 SVG 路线示意图（9232 字节，1200×760）|
| `assets/js/route-data-viewer.js` | 新增 | 前端数据查看器（Vanilla JS · 无依赖）|
| `assets/css/styles.css` | 追加 | 7429 行 · 新增 v1.4.6 样式约 200 行 |
| `trips/out-of-eden-walk-china/index.html` | 修改 | 1755 → 1792 行 · 新增静态地图 + 数据驱动表模块 |
| `routes/index.html` | 修改 | 新增 SVG 预览 + 数据统计 + 数据规范 + 处理流程 |
| `index.html` | 修改 | CTA 文案更新 · trips-data.js 状态更新 |
| `assets/js/trips-data.js` | 修改 | OEDW 状态字段更新 |
| `README.md` | 修改 | 版本表新增 v1.4.6 · OEDW 状态更新 |
| `CHANGELOG.md` | 修改 | 顶部新增 v1.4.6 章节 |
| `docs/CONTENT_NOTES.md` | 修改 | 追加 Phase 6 章节 |
| `data/routes/README.md` | 修改 | 追加 Phase 6 数据处理流程 |
| `reports/OUT_OF_EDEN_WALK_CHINA_PHASE6_DATA_DRIVEN_REPORT.md` | 新增 | 本报告 |

---

## 三、新增脚本

### `scripts/validate-route-data.py`

固化 Phase 5 临时数据校验逻辑为永久脚本：

- 只用 Python 标准库
- 默认校验 OEDW，可通过参数传入其他 route slug
- 输出 PASS / FAIL 状态码
- 退出码：0 PASS / 1 FAIL
- 校验 CSV / GeoJSON / GPX 三种格式

### `scripts/render-route-map-svg.py`

GeoJSON → SVG 静态地图生成：

- 只用 Python 标准库
- 使用 bounding-box equirectangular projection
- 不使用外部底图、不调用地图 API
- SVG 必须包含 "not Paul Salopek original GPS track" / "not for navigation" / "cultural replica"

---

## 四、SVG 生成结果

```
行旅图谱 · 路线 SVG 生成
input:  data/routes/out-of-eden-walk-china.geojson
output: assets/img/routes/out-of-eden-walk-china-map.svg
  ✓ contains: 'not Paul Salopek'
  ✓ contains: 'not for navigation'
  ✓ contains: 'cultural replica'
OK: SVG generated · 9232 bytes
```

### SVG 内容

| 元素 | 描述 |
|------|------|
| viewBox | 1200 × 760 |
| 背景 | 米白 #fbf7ec |
| 主路线 | 墨绿 #6b8e23（实线 2.5px · opacity 0.85）|
| 段路线 | 浅墨绿 #9caf6f（虚线 1.4px）|
| 点位 | 暗金 #b8860b（42 个圆点）|
| 起点 | 深墨绿 #5d8a3a |
| 终点 | 暗红 #a8423a |
| 段落标签 | S01–S10（11px sans-serif）|
| 图例 | 起点/终点/粗点/主路线/分路线 + 红色免责声明 |
| 标题 | 中文标题 + 副标题（v1.4.6 · 42 点 · 10 段 · 6,000-6,700 km）|

### 必含关键词

- ✓ "not Paul Salopek original GPS track"
- ✓ "not for navigation"
- ✓ "cultural replica"

---

## 五、数据驱动页面模块

### OEDW 页面

新增两个 section：

1. **静态路线示意图**（`#static-map`）
   - 嵌入 `<img src="../../assets/img/routes/out-of-eden-walk-china-map.svg">`
   - 图注明确"非 Paul Salopek 原始 GPS 轨迹 · 非导航"

2. **数据驱动路线表**（`#route-table`）
   - 容器 `<section id="route-data-viewer" data-route-geojson="..." data-route-name="...">`
   - 引用 `<script src="../../assets/js/route-data-viewer.js"></script>`

### route-data-viewer.js 功能

| 功能 | 实现 |
|------|------|
| fetch GeoJSON | `fetch(geoUrl)` |
| 自动摘要 | 6 项（点位 / 段 / 省份 / 高复刻 / 中复刻 / 低复刻）+ 10 段分布 |
| 4 筛选器 | 段落 / 省份 / 难度 / 可复刻性 |
| 表格字段 | 序号 / 段落 / 点位 / 省份 / 地区 / 精度 / 难度 / 可复刻性 / 风险提示 |
| 徽章样式 | 高（绿）/ 中（金）/ 低（浅金）/ 注意（红）|
| 失败 fallback | 显示下载链接 + 错误信息 |
| noscript fallback | 直接显示下载链接 |
| 依赖 | 无 |

---

## 六、路线数据索引页增强

新增/增强模块：

1. **静态地图预览**（在 OEDW 卡片内）
2. **数据统计**（9 项：点位数 / 段落数 / GeoJSON features / GPX waypoints / 数据版本 / 数据类型 / 原始 GPS / 用途 / 限制）
3. **数据规范 section**（字段定义、来源等级、精度等级、复刻可行性等级）
4. **数据处理流程 section**（4 步：数据源 → 校验 → 渲染 → 展示）

---

## 七、验证结果

### 7.1 数据验证脚本（用户指定）

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

### 7.2 SVG 文件检查（用户指定）

```
✓ 文件存在且非空
✓ 'not Paul Salopek original GPS track': 1
✓ 'not for navigation': 1
✓ 'cultural replica': 1
```

### 7.3 本地 HTTP（用户指定）

| URL | HTTP |
|-----|------|
| `/` | 200 |
| `/routes/` | 200 |
| `/trips/out-of-eden-walk-china/` | 200 |
| `/assets/img/routes/out-of-eden-walk-china-map.svg` | 200 |
| `/assets/js/route-data-viewer.js` | 200 |
| `/data/routes/out-of-eden-walk-china.geojson` | 200 |

### 7.4 verify-site.sh

```
STATUS: PASS（70 通过 / 0 失败）
```

### 7.5 关键词验收（用户指定）

| 关键词 | 结果 |
|-------|------|
| 静态路线示意图 | OEDW 2 处 |
| 数据驱动路线表 | OEDW 2 处 |
| route-data-viewer | HTML+JS+CSS 共 19 处 |
| out-of-eden-walk-china-map.svg | 6 处 |
| validate-route-data.py | 14 处 |
| render-route-map-svg.py | 13 处 |
| CSV/GeoJSON/GPX → validate | 1 处 |
| 跨越六年 | 0（清除）|
| 22/23 | 0（清除）|
| 22/22 | 11 处 |
| 文化复刻粗点 | 25 处 |
| 不是 Paul 原始 GPS | 6 处 |
| not for navigation | 28 处 |

### 7.6 事实边界验证

| 事实点 | 状态 | 结果 |
|-------|------|------|
| "跨越六年" | ✅ 清除 | grep 无 result |
| "22/23" | ✅ 清除 | grep 无 result |
| Milestones 74–95 = 22/22 | ✅ 保留 | 11 处命中 |
| 文化复刻粗点 | ✅ 保留 | 25 处 |
| 不是 Paul 原始 GPS | ✅ 保留 | 6 处 |

### 7.7 GitHub Pages

- 推送后等待 30-60s
- HTTP/2 200（待推送后验证）

---

## 八、可选浏览器 smoke

环境无浏览器（Playwright / Chromium 未安装）。**未执行浏览器 smoke，不阻塞发布。**

---

## 九、Phase 7 建议

1. **多路线数据驱动**
   - 辽塔巡礼路线数据 + 数据驱动展示
   - 山西古建路线数据 + 数据驱动展示
   - 其他规划中路线

2. **SVG 样式变体**
   - 多主题（深色 / 浅色 / 国画风）
   - 多投影（mercator / azimuthal）

3. **前端可视化增强**
   - 段落分布柱状图
   - 复刻性饼图
   - 难度统计

4. **数据导出**
   - PDF 表格
   - Markdown 表格
   - HTML 片段

5. **POI 语义标注升级**
   - POI 类型（古城 / 山地 / 海港 / 关隘）
   - 文化主题（茶马古道 / 蜀道 / 长城 / 黄土）
   - 朝代 / 历史时期

6. **数据 API 化**
   - 生成静态 JSON-LD
   - 便于 SEO 与结构化数据

7. **离线浏览**
   - 全部数据打包 ZIP
   - 包含 SVG / CSV / GeoJSON / GPX

---

_辛 🔮 · 2026-07-04 · Out of Eden Walk China Phase 6 Data-driven Map Preview_
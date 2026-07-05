# 行旅图谱 · 更新日志

本项目使用语义化版本号（Semantic Versioning）。所有重要变更都会记录在此。

---

## v1.4.9 · Shanxi Ancient Architecture Route Data Production (2026-07-05)

### 主要变更
- **新增数据资产**：`data/routes/shanxi-ancient-architecture.csv`（30 行 · 18 字段 · 9 段）
- **新增数据资产**：`data/routes/shanxi-ancient-architecture.geojson`（30 Point + 10 LineString = 40 features）
- **新增数据资产**：`data/routes/shanxi-ancient-architecture.gpx`（30 waypoint + 1 track）
- **新增静态地图**：`assets/img/routes/shanxi-ancient-architecture-map.svg`（7.6 KB · 1200×760）
- **manifest 升级**：`shanxi-ancient-architecture` 从 planned-data 升级为 data-v0.1
  - `points: 30` · `segments: 9` · `geojson_features: 40` · `geojson_points: 30` · `geojson_lines: 10` · `gpx_waypoints: 30` · `has_svg_preview: true`
- **manifest page_url 修正**：`../trips/shanxi-ancient-architecture-roadtrip/`（匹配实际页面路径）
- **山西页面新增模块**：「路线数据」轻量模块（CSV / GeoJSON / GPX 下载 + SVG 预览）
- **routes/index.html 增强**：
  - 山西路线数据卡片（v1.4.9 新增 · 30 个点位 · 9 段 · 2,400–2,800 公里）
  - 总览统计更新：3 条 / 0 规划中 / 92 CSV / 123 features / 92 waypoints / 3 张 SVG
  - 山西路线样板定位为「长线木构遗产样板」
- **assets/js/trips-data.js**：山西 trip 卡片增加 hasRouteData 字段
- **data/routes/README.md**：山西数据资产入表 + Phase 9 章节
- **docs/ROUTE_DATA_SPEC.md**：增加「当前已接入路线」章节（OEDW + 辽塔 + 山西）
- **验证**：路线工厂门禁 + verify-site.sh + GitHub Actions 全部 PASS（3 条路线）

### 重要边界
- 所有路线数据仍为**文化复刻 / 文化自驾粗点**
- OEDW 事实边界完整保留
- 辽塔数据未回退
- 山西数据声明：文化自驾粗点 / 非实时导航 / 不保证开放状态、门票、预约、维修闭馆
- 不引入地图 API / 后端 / 数据库 / 构建系统 / npm 依赖
- 不破坏 OEDW / 辽塔 / 山西等页面
- 不改动 Phase 2–8 事实边界

### 山西 9 段分布
- S01 大同古都与云冈线（4 点 · 大同 / 云冈石窟 / 华严寺 / 善化寺）
- S02 浑源恒山应县木构线（4 点 · 浑源 / 悬空寺 / 恒山 / 应县木塔）
- S03 五台山早期木构线（3 点 · 五台山 / 佛光寺 / 南禅寺）
- S04 太原晋祠府城线（3 点 · 太原 / 晋祠 / 山西博物院）
- S05 平遥双林镇国线（3 点 · 平遥古城 / 双林寺 / 镇国寺）
- S06 介休灵石霍州线（3 点 · 后土庙 / 张壁古堡 / 霍州署）
- S07 临汾洪洞隰县线（3 点 · 广胜寺飞虹塔 / 小西天）
- S08 运城永乐解州线（3 点 · 运城 / 永乐宫 / 解州关帝庙）
- S09 晋东南长治晋城线（4 点 · 长治 / 法兴寺 / 青莲寺 / 玉皇庙）

### 文档链接
- [docs/ROUTE_DATA_SPEC.md](./docs/ROUTE_DATA_SPEC.md)
- [data/routes/routes-manifest.json](./data/routes/routes-manifest.json)
- [reports/PHASE9_SHANXI_ROUTE_DATA_REPORT.md](./reports/PHASE9_SHANXI_ROUTE_DATA_REPORT.md)

## v1.4.8 · Route Factory Automation and Quality Gates (2026-07-05)

### 主要变更
- **新增脚本**：`scripts/build-route-assets.py`（路线工厂入口 · 校验 + SVG + manifest 同步）
- **新增脚本**：`scripts/check-routes-index-sync.py`（manifest / index.html 漂移检查）
- **新增 workflow**：`.github/workflows/route-data.yml`（Route Data Quality Gate · CI 自动验证）
- **增强 `validate-route-data.py`**：v1.2 · 支持 `--json` 输出 + `--manifest-check` 模式
- **增强 `render-route-map-svg.py`**：v1.2 · 支持 `--check` 模式（只校验不生成）
- **增强 `verify-site.sh`**：增加 9 项 Route data gates（70 → 79 项）
- **manifest 增强**：
  - 增加 `geojson_points` / `geojson_lines` 统计字段
  - 增加山西古建路线 `planned-data` 条目
- **routes/index.html 增强**：
  - 资产总览显示 3 条路线（2 已有 + 1 规划中）
  - 新增「质量门禁」模块
  - 新增「路线工厂流程」模块
  - 山西古建显示为 planned-data 卡片
- **docs/ROUTE_DATA_SPEC.md 增强**：新增 §11 路线工厂脚本说明
- **新增命令**：
  - `python3 scripts/build-route-assets.py --all`
  - `python3 scripts/build-route-assets.py --check`
  - `python3 scripts/validate-route-data.py --all --json`
  - `python3 scripts/validate-route-data.py --all --manifest-check`
  - `python3 scripts/render-route-map-svg.py --all --check`
  - `python3 scripts/check-routes-index-sync.py`

### 重要边界
- 所有路线数据仍为**文化复刻 / 文化自驾粗点**
- OEDW 事实边界完整保留（22/22 / 6,000–6,700 / 两年多 / 黄海三层 / 文化复刻粗点）
- 辽塔数据未回退
- planned-data 路线不创建空数据文件
- 不引入地图 API / 后端 / 数据库 / 构建系统 / npm 依赖
- 不破坏 OEDW / 辽塔 / 山西等页面
- 不改动 Phase 2–7 事实边界

### 文档链接
- [docs/ROUTE_DATA_SPEC.md](./docs/ROUTE_DATA_SPEC.md)
- [docs/ROUTE_PAGE_TEMPLATE.md](./docs/ROUTE_PAGE_TEMPLATE.md)
- [data/routes/routes-manifest.json](./data/routes/routes-manifest.json)
- [reports/PHASE8_ROUTE_FACTORY_QUALITY_GATES_REPORT.md](./reports/PHASE8_ROUTE_FACTORY_QUALITY_GATES_REPORT.md)

## v1.4.7 · Route data templates and multi-route reuse (2026-07-05)

### 主要变更
- **新增规范文档**：`docs/ROUTE_DATA_SPEC.md`（通用路线数据规范 v1.0）
- **新增页面模板**：`docs/ROUTE_PAGE_TEMPLATE.md`（通用路线页面模板 v1.0）
- **新增 manifest**：`data/routes/routes-manifest.json`（项目级路线登记表）
- **增强 `validate-route-data.py`**：支持任意 slug + `--all` 模式 + 路线级别阈值（OEDW / liao / 默认）
- **增强 `render-route-map-svg.py`**：支持任意 slug + `--all` 模式 + 动态 title/desc + 中英文双语声明
- **新增辽塔巡礼路线数据**：
  - `data/routes/liao-tower-roadtrip.csv`（20 行 · 18 字段 · 9 段）
  - `data/routes/liao-tower-roadtrip.geojson`（20 Point + 10 LineString）
  - `data/routes/liao-tower-roadtrip.gpx`（20 waypoint + 1 track）
  - `assets/img/routes/liao-tower-roadtrip-map.svg`（6.8 KB · 1200×760）
- **优化 `route-data-viewer.js`**：去除 OEDW 硬编码、通用化 fallback 下载链接、根据 geoUrl 推断 slug
- **增强 `routes/index.html`**：路线数据资产总览 + 辽塔巡礼数据卡片 + 多路线规范模块 + 总览统计
- **优化 `trips-data.js` / `home.js`**：trip 卡片支持 "已接入路线数据" 标识 + 数据元信息链接
- **CSS 新增**：`.route-data-badge-inline`、`.trip-card-data-meta`
- **辽塔页面新增**：「路线数据」轻量模块（不动既有内容）
- **首页更新**：路线数据索引说明增加辽塔、版本徽章 v1.4.7 + 2 条路线
- **新增命令**：
  - `python3 scripts/validate-route-data.py --all`
  - `python3 scripts/render-route-map-svg.py --all`

### 重要边界
- 所有路线数据仍为**文化复刻 / 文化自驾粗点**
- OEDW 事实边界完整保留（22/22 milestones、6,000–6,700 公里、两年多、黄海三层时间、文化复刻粗点）
- SVG 必须包含 "not for navigation" / "cultural replica" / "not original GPS"（中英文）
- 不引入地图 API / 后端 / 数据库 / 构建系统 / npm 依赖
- 不破坏 OEDW / 辽塔 / 山西等页面
- 不改动 Phase 2–6 事实边界

### 文档链接
- [docs/ROUTE_DATA_SPEC.md](./docs/ROUTE_DATA_SPEC.md)
- [docs/ROUTE_PAGE_TEMPLATE.md](./docs/ROUTE_PAGE_TEMPLATE.md)
- [data/routes/routes-manifest.json](./data/routes/routes-manifest.json)

## v1.4.6 · Out of Eden Walk China Phase 6 · Data-driven Map Preview (2026-07-04)

### 主要变更
- **新增脚本**：`scripts/validate-route-data.py`（固化 Phase 5 临时校验）+ `scripts/render-route-map-svg.py`（GeoJSON → 纯静态 SVG）
- **静态 SVG 地图**：`assets/img/routes/out-of-eden-walk-china-map.svg`（9.2 KB · 1200×760 · 墨绿/米白/暗金风格）
- **前端数据查看器**：`assets/js/route-data-viewer.js`（Vanilla JS · 无依赖 · fetch GeoJSON · 4 筛选器 · 表格渲染 · fallback）
- **OEDW 页面新增模块**：「静态路线示意图」+「数据驱动路线表」（含筛选器）
- **routes/index.html 增强**：SVG 预览 + 9 项数据统计 + 数据规范 + 数据处理流程
- **首页 CTA 更新**：明确"不依赖地图 API"
- **CSS 新增**约 200 行：static-route-map / route-data-viewer / route-data-summary-grid / route-data-filters / route-data-table-wrap / route-data-viewer-table / route-data-badge 系列 / data-process-flow / route-map-preview

### 重要边界
- 所有路线数据仍为**文化复刻粗点**
- SVG 必须包含 "not Paul Salopek original GPS track" / "not for navigation" / "cultural replica"
- 不引入地图 API / 后端 / 数据库 / 构建系统 / npm 依赖
- 不破坏辽塔 / 山西等其他页面
- 不改动 Phase 2–5 事实边界

### SVG 内容

- **背景**：米白 #fbf7ec
- **路线**：墨绿主路线（实线 2.5px）+ 10 段分路线（虚线 1.4px）
- **点位**：暗金 42 个圆点 · 起点深墨绿 / 终点暗红
- **段落标签**：S01–S10 居中标注于段落中心
- **图例**：起点 / 终点 / 粗点 / 主路线 / 分路线 + 红色免责声明
- **标题**：中文标题 + 副标题（版本 / 点位数 / 段数 / 里程）
- **footer**：脚本生成标识

### Phase 6 核心脚本

```bash
# 校验数据
python3 scripts/validate-route-data.py

# 生成 SVG
python3 scripts/render-route-map-svg.py

# 输出
#  → data/routes/out-of-eden-walk-china.{csv,geojson,gpx}
#  → assets/img/routes/out-of-eden-walk-china-map.svg
```

---

## v1.4.5 · Out of Eden Walk China Phase 5 · Route Data (2026-07-04)

### 主要变更
- **3 种路线数据文件**：CSV (42 行 / 18 字段) / GeoJSON (42 Point + 1 主 LineString + 10 段 LineString) / GPX 1.1 (42 waypoints + 1 track)
- **数据目录**：`data/routes/` 新增 `out-of-eden-walk-china.csv` / `.geojson` / `.gpx` + `README.md`
- **路线数据索引页**：`routes/index.html` 全新页面，含 Hero / 三种格式说明 / 路线数据卡片 / 下载按钮 / 未来路线 / 关于
- **首页入口**：导航增加"路线数据"链接，新增 CTA 卡片"路线数据索引"
- **OEDW 页面新增"下载路线数据"模块**：3 种格式下载按钮 + 数据摘要表 + 6 个字段（版本 / 类型 / 段点 / 精度 / 用途 / 限制）
- **CSS 新增**：route-data-card / route-data-grid / route-data-downloads / route-data-button / data-format-badge / data-warning / data-index-grid / data-index-card / data-meta-list / data-file-list / data-status-badge / route-data-inline 约 250 行
- **首页 + OEDW 版本号**：v1.4.4 → v1.4.5

### 重要边界
- 所有数据均为**文化复刻粗点**（cultural replica waypoints）
- **不是 Paul Salopek 原始 GPS 轨迹**（明确标注在 CSV / GeoJSON / GPX 元数据中）
- **不用于导航**（明确标注）
- 不引入地图 API / 后端 / 构建系统
- 不破坏辽塔 / 山西等其他页面

### 数据精度分级
- `city` - 城市级
- `landmark` - 景区 / 地标级
- `region` - 区域级
- `approximate` - 近似坐标（不可精确导航）
- `unknown` - 不确定位置

### 来源等级
- `A_official_oedw` - 官方 Out of Eden Walk milestone/dispatch
- `B_partner_or_education` - 合作地图、NatGeo Education
- `C_chinese_media` - 中文媒体、纪录片、展览
- `D_reconstructed_for_travel` - 基于公开材料重建

### 复刻可行性
- `high` / `medium` / `low` / `not_recommended` / `reading_only`

---

## v1.4.4 · Out of Eden Walk China Phase 4 · Launch Package (2026-07-04)

### 主要变更
- **页面体验增强**：新增快速阅读目录（10 个锚点）、阅读进度条（顶部细线）、返回顶部按钮（滚动 600px 后出现）
- **移动端长表格**：Milestones 表格 + 21–28 天精华版表格外层包裹 `.mobile-scroll-table`，加 `← 左右滑动 →` 提示
- **本页状态卡片**：v1.4.4 · 50% · 已交付：事实审校/可旅行化/叙事导览/发布包装
- **适合谁使用**：4 类适合人群 + 4 类不适合人群（卡片式布局）
- **首页推荐位**：OEDW 卡片新增 `代表长线 · 已完成 Phase 4` 渐变徽章 + 边框高亮 + 进度 30% → 50%
- **SEO polish**：title 加副标题、canonical 链接、og:site_name / og:locale、Twitter Card（summary 类型）
- **发布文案模块**：朋友圈版（100–180 字）/ 小红书版（标题+正文）/ 公众号导语版（400–600 字）/ README 简介版（120–200 字），共 4 个可复制文本块
- **JS 新增**：内联 26 行 Vanilla JS · 阅读进度 + 返回顶部 · requestAnimationFrame 节流 · 无依赖 · JS 禁用时不影响阅读
- **CSS 新增**：reading-progress / quick-read-nav / page-status-card / audience-grid / mobile-scroll-table / scroll-hint / back-to-top / launch-copy-grid / featured-route-badge 等约 230 行

### 重要边界
- 不修改 v1.0 / v1.4 / v1.4.1 / v1.4.2 / v1.4.3 架构
- 不回退 Phase 2 / Phase 3 事实边界
- 不引入后端 / 数据库 / 地图 API / 构建系统
- 不引入任何 JS 库（内联 Vanilla JS）
- 不破坏辽塔 / 山西等其他页面

---

## v1.4.3 · Out of Eden Walk China Phase 3 · Narrative Guide (2026-07-04)

### 主要变更
- 新增「如何阅读这条路线」模块：4 张卡片交代复刻路线的正确打开方式（不是挑战路线 / 中国地理剖面线 / 慢新闻路线 / 可分年完成的长线）
- 新增「中国段长卷地图」模块：12 个现场节点的长卷式文字地图（滇西边境 → 黄海港口），不使用外部地图 API
- 新增「10 段随行导游词」模块：每段 300–500 字沉静式人文导览 + 现场观察提示
- 21–28 天精华版表格新增「每日主题」列：D1–D28 共 9 个区段的每日主题标题（如 D1 从边境沉默进入滇西、D11 剑门关：蜀道难现场）
- 6 段短线版本新增字段：适合人群 / 最适合季节 / 推荐旅行方式 / 一句话主题 / 不适合人群
- 新增「行前资料包」模块：5 类资料（A 必读官方材料 / B 中国段主题阅读方向 / C 观看材料 / D 出发前准备 checklist / E 旅行记录模板）
- 新增「传播摘要」模块：30 秒 / 3 分钟 / 讲解员三个可复制版本（原创中文，不使用营销词）
- 新增 CSS 样式：reading-guide-grid / scroll-map / narrative-guide-grid / prep-pack-grid / share-summary-grid / daily-theme 等
- 顶部导航精简：移除低频入口，新增 阅读 / 长卷 / 导游词 / 资料包 / 传播 5 个模块入口
- 移动端响应式：长卷地图节点、每日主题表格、卡片网格自适应

### 重要边界
- 不修改 v1.0 / v1.4 / v1.4.1 / v1.4.2 架构
- 不回退 Phase 2 事实边界（"约 6,000–6,700 公里"、"两年多"、"22/22"、"卢沟桥→天安门→小汤山"、黄海三层时间）
- 不引入后端、不引入数据库、不调用地图 API、不引入构建系统
- 不重新做架构、不破坏已有路线（辽塔 / 山西古建）
- 不添加未经核验的事实（所有导游词基于 Phase 2 已审校的 milestone / dispatch）

---

## v1.4.2 · Out of Eden Walk China Phase 2 (2026-07-04)

### 主要变更
- 事实审校：修正“跨越六年”为“历时两年多”、中段时间口径校准（2021 秋 / 2023 冬 / 2024.6 / 2024.8 四个时间点）、里程采用区间口径 6,000–6,700 km
- Milestones 覆盖修正为 22/22，Milestone 91 URL 本次验证返回 200 已收录
- 新增事实审校模块（来源等级 A/B/C、页面原则、已知不确定点）
- Milestones 表格升级为事实审校表：新增“来源状态”“旅行复刻建议”两列
- 10 段路线可旅行化增强：入口/出口城市、交通、徒步/自驾/公交、难度、最佳季节、关键风险、不建议复刻方式、替代走法
- 新增 21–28 天精华版逐日框架（9 段 D 编号）
- 新增 6 段短线版本（云南线 / 川西线 / 蜀道秦岭线 / 陕北山西线 / 北京长城线 / 东北收束线）
- 新增“不建议硬走”清单（6 类边界）
- 资料清单补充 B 级：ArcGIS / Esri / Harvard CGA / NatGeo Education（部分 URL 为“待补”状态）
- 来源核验日期：2026-07-04

### 重要边界
- 不修改 v1.0 / v1.4 / v1.4.1 架构
- 不提供 Paul 原始 GPS 逐点复刻
- 逆推 / 双口径里程 / 部分村镇译名转写都已在页面中明示

---

## v1.4.1 · Out of Eden Walk China (2026-07-04)

### 主要变更
- 新增第三条路线：Out of Eden Walk 中国段复刻路线
- 路线定位：基于 Paul Salopek / National Geographic Out of Eden Walk 中国段公开材料整理的"文化复刻路线"
- 中国段主线：云南 → 四川 → 陕西 → 山西 → 河北/北京 → 辽宁 → 大连黄海
- 10 段路线设计（溜西重启 / 大理丽江 / 茶马古道与木里 / 川西南雅安 / 剑门蜀道汉中 / 关中陕北 / 晋西雁门关 / 北京城市步行 / 京北长城承德 / 辽宁大连黄海）
- Milestones 表格：官方 74-95 全部覆盖（Milestone 91 待官方 URL，96+ 为黄海渡船段不计）
- 10 个关键故事卡片（边境中断 / 高黎贡山绿色方舟 / 茶马古道挑夫 / 木里旧王国 / 剑门关 / 汉中封控 / 黄土高原 / 周口店 / 北京迷宫 / 大连黄海）
- 3 种复刻版本：45-60 天研究型 / 21-28 天精华压缩 / 分省分段
- 资料来源：官方 Out of Eden Walk / National Geographic 全部 milestone 与 dispatch 链接、中文纪录片《永远的行走：与中国相遇》、上海纽约大学 ICA 展览、解放日报/澎湃新闻报道
- 首页：路线总数 6 → 7，规划中 5 → 6；新增路线卡片
- verify-site.sh 不变（本轮主要是内容型新增，不新增验证项）
- README / CONTENT_NOTES / CHANGELOG 同步更新

### 重要边界
- 本路线 **非官方授权路线**，不提供原始 GPS 轨迹
- 是 "文化复刻路线"，不是 Paul 原始足迹的逐点复刻
- 路线地点存在模糊与口径差异，已在页面中标注

---

## v1.4 · Shanxi Cultural Guide Lite (2026-07-04)

### 主要变更
- 山西古建自驾线从「实用信息核验」升级为「文化导览草稿」
- 12 个 A 级核心点位完整导览草稿（每个含：30 秒导入 / 现场怎么看 / 3-5 个观察点 / 300-600 字导游式讲解草稿 / 离开前回望 / 2-3 个自我提问 / 与整条路线的关系 / 草稿状态标签）
- 5 个 B 级强烈推荐点位简短导览（一句话价值 / 现场重点 / 观察问题 / 是否适合纳入主线）
- 山西古建现场怎么看总导览模块（6 个观察顺序 + 彩塑壁画特殊提醒）
- 古建观察清单（10 项可勾选，localStorage 保存）
- 山西古建关键词进阶（新增 8 个词条：殿堂 / 悬山歇山庑殿 / 减柱造 / 叉手与托脚 / 悬塑 / 水陆画 / 明清修缮 / 国保单位）
- 导览草稿状态说明
- 首页状态：实用信息核验中 → 文化导览草稿中（进度 60% → 70%）
- verify-site.sh 增加 11 项 v1.4 关键词检查（73 → 84 项），全部 PASS
- README / CONTENT_NOTES / CHANGELOG 同步更新

---

## v1.0 · Stable Release (2026-07-04)

### 🎉 首个稳定发布版

将「行旅图谱」整理为第一个稳定发布版。统一项目说明、首页展示、路线状态、SEO 基础信息、版本记录、文档结构。

### 主要变更
- 首页统一首屏：明确项目定位为个人人文旅行路线库
- 路线状态总览：1 条完整路线 + 1 条规划中骨架页 + 4 条卡片
- 首页 + 两个路线页补充基础 meta 标签（title / description / og:*）
- 站内导航一致性：所有页面均可返回首页
- README 完整结构：项目定位 / 当前路线列表 / 如何添加新路线 / 当前版本
- CHANGELOG.md 完整记录
- scripts/verify-site.sh 验证脚本
- Git tag v1.0.0

### 累计成果
- 路线：1 条完整（辽塔巡礼）+ 1 条规划中骨架页（山西古建）
- 数据：sourceIndex(29) / preDepartureChecklist(10) / 14 景点 sources
- 景点：14 个重点景点 + 17 个候选点位
- 模块：路线总览 / 路线示意图 / Day 高亮 / 主题路径 / 景点关系网络 / 今日模式 / 复盘预习 / 行前 7 天学习计划 / 阅读路线 / 时间轴 / 五京体系 / 形制比较 / 概念图谱 / 资料来源索引 / 核对清单 / 文物图录档案 / 线描示意 / 城市章节 / 摘句 / 故事线

### Git Tag
- v1.0.0






## v1.3 · Shanxi Practical Fact Audit (2026-07-04)

### 主要变更
- 山西古建自驾线从「路线校准」升级为「实用信息核验」
- 17 个 A/B 级点位实用信息卡（开放时间 / 闭馆日 / 门票 / 预约 / 停车 / 拍照限制 / 建议停留时间 / 地图搜索词 / 高德 + 百度地图搜索链接）
- 7 个高风险点位提示
- 出发前必须核验面板（10 项可勾选，localStorage）
- 11 天主路线每日核对事项
- 资料来源 v1.3 增强说明
- 首页状态：路线校准中 → 实用信息核验中（进度 45% → 60%）
- verify-site.sh 增加 11 项检查（62 → 73 项），全部 PASS
- README / CONTENT_NOTES / CHANGELOG 同步更新

---

## v1.2 · Shanxi Route Calibration (2026-07-04)

### 主要变更
- 山西古建自驾线从「研究建档」升级为「路线校准」
- 3 种行程版本：11 天 10 晚深度版（推荐）/ 8 天压缩版 / 14 天慢行版
- 11 天主路线每日含：住宿城市 + 核心景点 + 备选 + 取舍提醒 + Plan B
- 每日分时草案（上午 / 中午 / 下午 / 晚上表格）
- 候选点位状态分级：主线必入 / 主线强烈推荐 / 主线备选 / 压缩版可舍弃 / 后续专题路线
- 路线取舍逻辑（6 条）
- 山西古建路线图示意（纯 SVG，标记晋北 / 晋中 / 晋南 / 晋东南）
- 下一步待核验清单（10 项）
- 首页状态：研究建档中 → 路线校准中（进度 30% → 45%）
- verify-site.sh 增加 v1.2 关键词检查（10 项），总检查 52 → 62 项
- README / CONTENT_NOTES / CHANGELOG 同步更新

---

## v1.1 · Shanxi Route Research (2026-07-04)

### 主要变更
- 山西古建自驾线升级为「研究建档版」
- 候选点位分级（A 核心必看 12 个 / B 强烈推荐 5 个 / C 可选补充 2 个）
- 5 段路线研究框架（每段主题 + A/B 级核心点位）
- 6 类资料来源索引
- 10 个山西古建关键词词条
- 2 个初步行程方案（8 天压缩版 / 11-12 天深度版）
- 首页状态从「规划中」更新为「研究建档中」
- verify-site.sh 增加山西页关键词检查（17 项）
- README / CONTENT_NOTES / CHANGELOG 同步更新

### 山西路线状态升级
- v0.9：规划中骨架页（路线方向 + 17 个候选点位）
- v1.1：研究建档（点位分级 + 研究框架 + 资料来源 + 关键词 + 初步行程）
- 下一步：等待实地走访 + 完整路线校准


---

## v0.9 · Trip Template & Second Route Skeleton (2026-07-04)

### 主要变更
- docs/TRIP_TEMPLATE.md：标准路线页面模板（13 章节 + 字段规范 + 状态说明 + 视觉规范 + 新增路线最小步骤）
- trips/shanxi-ancient-architecture-roadtrip/index.html：第二条路线规划中骨架页（6 段路线 / 17 个候选点位 / 全部标注待核对）
- 首页山西古建卡片按钮从 disabled 改为「查看规划」并可点击进入骨架页
- 状态视觉区分：status-live / status-planning / status-draft / status-reviewed
- 可复用样式类：trip-skeleton / planning-note / trip-template-section / candidate-spot
- README 增加「如何添加新路线」最小步骤

---

## v0.8 · Multi Trip Framework (2026-07-04)

### 主要变更
- 首页升级为路线库首页（不再是单条行程入口）
- Featured Trip 区块：辽塔巡礼作为当前主推路线
- 路线库：6 条路线卡片（1 已上线 / 5 规划中）
- 8 个分类筛选按钮（全部/古建/石窟/博物馆/自驾/徒步/边疆史/城市史）
- 路线状态说明（已上线/规划中/待实地复盘/已实地复盘）
- "一条路线如何被整理" 8 步方法论模块
- 新增 assets/js/trips-data.js（路线库数据）
- 新增 assets/js/home.js（首页渲染/筛选逻辑）

---

## v0.7 · Heritage Visual Polish (2026-07-04)

### 主要变更
- 重点景点档案卡：7 个核心景点的文物图录式档案
- 辽塔线描示意：纯 SVG 4 类塔形（密檐/白塔/双塔/花塔）
- 城市章节封面：6 个城市章节（壹-陆）
- 导游词摘句：7 个重点景点高亮引言
- 路线故事线：5 幕叙事卡片
- 阅读层级：section-hint 标签（先看这个 / 现场重点 / 如果时间有限）
- 页面版本更新到 v0.7

---

## v0.6 · Source and Fact Audit (2026-07-04)

### 主要变更
- 资料来源索引：6 类资料分组（官方/博物馆/纪录片/书籍/研究/旅行整理）
- 14 个重点景点增加 sources 字段（每景点 3-4 条资料）
- 出发前实时核对清单：10 项 localStorage 可勾选
- 事实核对标签：出发前需核对 / 旅行整理 / 资料整理
- 内容风险说明
- 页面版本信息
- Workflow 升级：actions/setup-node@v4 with node-version: '24'

---

## v0.5 · Route Map Visualization (2026-07-04)

### 主要变更
- 路线示意图：纯 SVG 路线图，9 个城市节点
- Day 高亮：Day 1-9 按钮
- 主题路径：5 个主题切换（辽塔线/石窟线/都城线/博物馆线/返程线）
- 景点关系网络：5 组关系项
- 路线阶段卡片：5 段
- 路线总览 Meta

---

## v0.4 · Knowledge Deepening (2026-07-04)

### 主要变更
- 辽代时间轴：9 个关键节点
- 辽五京体系：5 座都城卡片
- 辽塔形制比较：6 种塔形制
- 核心概念图谱：11 个词条
- 出发前阅读路线：3 种预习方案
- 资料来源与事实核对
- 景点之间的关系：14 个重点景点

---

## v0.3 · Site Companion Mode (2026-07-04)

### 主要变更
- 今日模式：9 天切换
- 到达前导入：17 个重点景点 + 按钮
- 现场怎么看步骤化导览
- 离开前回望
- 今晚复盘 / 明日预习
- 行前 7 天学习计划：localStorage 打卡
- 现场模式底部导航
- 进度面板
- 语音不支持提示

---

## v0.2 · Content Route Calibration (2026-07-04)

### 主要变更
- 分时日程（上午/中午/下午/晚上）
- 替代方案（时间不够/闭馆/雨天）
- 景点实用信息（开放时间/闭馆日/门票/停车）
- 语音朗读状态检测 + 停止按钮
- 手机端体验优化
- 地图链接（高德/百度）

---

## v0.1 · Initial Release (2026-07-04)

### 主要变更
- 项目初始框架
- 行程页：9 天 8 晚自驾行程
- 景点卡片：13 个景点
- 随行导游词：7 篇 800 字讲解
- 城市介绍：7 个
- 主题词典：6 个词条
- 美食模块
- 行前书影音资料包
- 打卡进度（localStorage）
- 语音朗读（speechSynthesis）
- GitHub Pages 自动部署

---

*Built with static HTML + CSS + Vanilla JavaScript. No frameworks. No backend. No database. Just a human traveler's notebook.*
# 行旅图谱 · 更新日志

本项目使用语义化版本号（Semantic Versioning）。所有重要变更都会记录在此。

---

## v1.5.7 · OEDW Dispatch Deep Review and Source Concordance (2026-07-06)

### 主要变更

- **OEDW 页面从 Milestones 中文故事索引版升级为官方 Dispatch 对照解读版**
- **页面顶部状态**：完成度 88% → 90% · Dispatch 基础复核版
- **22 条 milestone 官方 URL 全部 200**（v1.5.7 验证，2026-07-06）
- **官方 Dispatch 资料对照表**（22 行 × 9 字段）：
  - Milestone / 官方标题 / 官方资料状态 / 核心主题+关键词 / 人物场景地貌 / 复刻段落 / 28天执行卡 / 复刻提醒 / 官方链接
  - 22/22 全部已建立对照
- **22 条 milestone 核心主题 + 关键词覆盖**：
  - 22 条每条 3-6 个关键词标签
  - 总计关键词 100+ 个（边境/雨季/绿色方舟/村落/茶马古道/木里旧王国/长征/蜀道/空城/秦岭/黄土/窑洞/民间艺术/山西古城/城乡过渡/早期现代人/长城/玉米/乌鸦/工业迁移/黄海等）
- **22 条 milestone 人物/场景/地貌字段**：
  - 22 条每条 1-2 句中文概括
  - 覆盖：人物（Paul/当地人/手工艺人/边境检查员/外卖骑手）+ 场景（空城/等待/告别）+ 地貌（雨林/雪山/草原/黄土塬/沿海工业）
- **复刻段落映射**（22/22 完成）：
  - 第 1 段: 74, 75
  - 第 2 段: 76
  - 第 3 段: 77, 78
  - 第 4 段: 79, 80
  - 第 5 段: 81, 82, 83
  - 第 6 段: 84, 85
  - 第 7 段: 86, 87, 88, 89
  - 第 9 段: 90
  - 第 10 段: 91, 92, 93, 94, 95
- **28 天执行卡映射**（22/22 完成）：
  - D1-D2 / D3 / D4-D6 / D7 / D8 / D9 / D9-D10 / D12 / D13 / D13 / D15-D16 / D16 / D18-D19 / D19 / D19 / D20 / D24 / D26 / D26 / D26 / D26-D27 / D27-D28
- **官方资料状态统计**：
  - 21 条「官方页面已复核」(reviewed)
  - 1 条「官方页面可访问」(readable) - M91
  - 0 条「官方链接待复核」/「访问受限」
- **新增「如何阅读 Out of Eden Walk 的 Dispatch」**（5 张卡片）：
  1. 它不是景点说明
  2. 它不是 GPS 路书
  3. 它把大历史放进小场景
  4. 它适合慢读
  5. 中文复刻要保留不确定性
- **新增「从官方故事到复刻路线」**（4 步流程）：
  1. 官方 Milestone（叙事节点和故事入口）
  2. Dispatch 主题（人物、场景、地貌和历史线索）
  3. 中文路线解读（地理、文化和旅行主题）
  4. 文化复刻行程（城市、县域、公共景区、博物馆和安全观察点）
- **更新「仍需实地验证 · 细节资料」**：
  - ✅ Milestones 74–95 共 22 条基础中文摘要已完成
  - ✅ 官方 dispatch 基础复核已完成（v1.5.7 · 22/22 URL 200）
  - 对 22 条 dispatch 进行二次深读（待逐条展开）
  - 每条 milestone 的代表图片（待补充）
  - 现场实拍图（待贡献）
  - 点位开放状态 + 实地可达性
  - 中文参考书目与延伸阅读
- **页面顶部导航更新**：新增「Dispatch」锚点
- **页面版本号全量更新**：v1.5.6 → v1.5.7（hero badge / page-meta × 2 / footer / 状态卡 / 描述 / 风险说明）
- **manifest v1.5.7**：
  - 顶层 `version` = `v1.5.7`
  - OEDW data_status_label：**长线文化复刻样板 · Dispatch 基础复核版**
  - OEDW route_summary 补齐官方 Dispatch 资料对照表
  - 9/9 SEO 字段保留
- **check-route-seo.py**：`manifest version` 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5 / v1.5.6 / v1.5.7
- **CSS 增强**：`assets/css/styles.css` + 130 行（.oedw-dispatch-review / .oedw-dispatch-table-wrap / .oedw-dispatch-table / .oedw-dispatch-status-reviewed / .oedw-dispatch-status-readable / .oedw-dispatch-status-pending / .oedw-dispatch-status-limited / .oedw-dispatch-keywords / .oedw-dispatch-keyword / .oedw-dispatch-method-grid / .oedw-dispatch-method-card / .oedw-source-concordance / .oedw-source-flow / .oedw-source-flow-step / .oedw-excerpt-note 等 15 个新类）

### 版权与引用边界

- ✅ 允许：中文摘要 / 中文转述 / 主题提炼 / 关键词整理 / 官方链接
- ❌ 不整段搬运官方正文
- ❌ 不做全文翻译
- ❌ 不复制官方 dispatch 全文作为景区攻略

### 不修改

- ❌ 辽塔页面（v1.5.4 状态保留）
- ❌ 山西页面（v1.5.4 状态保留）
- ❌ CSV / GeoJSON / GPX 坐标数据
- ❌ SVG 路线示意图
- ❌ OG SVG（SEO 检查不要求）
- ❌ 路线工厂门禁脚本
- ❌ 地图 API / 后端 / 数据库 / npm 依赖

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅（再次确认 22 条全部完成）
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：v1.5.4 状态保留

### 验证

- 路线工厂门禁：全部 PASS
- SEO / OG 门禁：全部 PASS
- verify-site.sh：全部 PASS
- GitHub Actions：Route Data Quality Gate success
- 数量校验：22/22 Milestone 编号（74-95）全部出现
- 官方 URL 校验：22/22 全部 200

### 报告

- `reports/OEDW_DISPATCH_DEEP_REVIEW_REPORT.md`

---

## v1.5.6 · OEDW Milestones Chinese Story Index (2026-07-06)

### 主要变更

- **OEDW Milestones 74–95 全部完成 22/22 中文摘要**
- **页面顶部状态**：完成度 85% → 88% 可用草案 v0.9（中文摘要已完成，剩余 12% 是视觉资料 + 实地核验）
- **Milestones 74–95 中文故事索引（22 张卡片）**：
  - 每条 6 字段：中文摘要 / 路线意义 / 复刻建议 / 不确定点 / 可复刻程度 / 官方链接
  - 22 条 milestone 编号：74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95
  - 每条 80-160 字中文摘要
- **可复刻程度分级**（5 个 badge）：
  - **易复刻** (5 条)：74, 80, 81, 85, 86, 89, 95
  - **可分段** (4 条)：76, 82, 84, 90
  - **主题** (5 条)：79, 83, 87, 88, 91
  - **避免** (7 条)：75, 77, 78, 92, 93, 94
  - **待核验** (1 条)：无（91 已用 "仅作阅读背景" 归入主题类）
- **新增「如何从官方 Milestone 读到旅行路线」**（4 张说明卡）：
  1. 官方 Milestone 是叙事节点
  2. Dispatch 是故事，不是攻略
  3. 文化复刻要看主题
  4. 普通旅行者要降维
- **更新「仍需实地验证」中"细节资料"清单**：
  - ✅ Milestones 74–95 共 22 条基础中文摘要已完成
  - 官方 dispatch 深度复核（待逐条展开）
  - 每条 milestone 的代表图片（待补充）
  - 现场实拍图（待贡献）
  - 点位开放状态 + 实地可达性
  - 中文参考书目与延伸阅读
- **页面顶部导航更新**：新增「故事索引」锚点
- **页面版本号全量更新**：v1.5.5 → v1.5.6（hero badge / page-meta / footer / 状态卡）
- **manifest v1.5.6**：
  - 顶层 `version` = `v1.5.6`
  - OEDW data_status_label：**长线文化复刻样板 · Milestones 中文索引版**
  - OEDW route_summary 补齐 22 条中文摘要
  - 9/9 SEO 字段保留
- **check-route-seo.py**：`manifest version` 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5 / v1.5.6
- **CSS 增强**：`assets/css/styles.css` + 120 行（.oedw-milestone-index / .oedw-milestone-grid / .oedw-milestone-card / .oedw-milestone-number / .oedw-milestone-title / .oedw-milestone-meta / .oedw-milestone-block / .oedw-replication-badge / .oedw-replication-easy / .oedw-replication-segment / .oedw-replication-theme / .oedw-replication-avoid / .oedw-replication-pending / .oedw-milestone-link / .oedw-official-reading-grid / .oedw-official-reading-card 等 16 个新类）

### 不复制官方长文

- ❌ 不复制 National Geographic / Out of Eden Walk 原文
- ❌ 不做全文翻译
- ❌ 不伪造 Paul Salopek 原始 GPS
- ❌ 不写成官方旅行路线
- ✅ 仅做中文摘要、转述、引用短标题、引用官方 URL

### 不修改

- ❌ 辽塔页面（v1.5.4 状态保留）
- ❌ 山西页面（v1.5.4 状态保留）
- ❌ CSV / GeoJSON / GPX 坐标数据
- ❌ SVG 路线示意图
- ❌ OG SVG（SEO 检查不要求）
- ❌ 路线工厂门禁脚本
- ❌ 地图 API / 后端 / 数据库 / npm 依赖

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅（再次确认 22 条全部有中文摘要）
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：v1.5.4 状态保留

### 验证

- 路线工厂门禁：全部 PASS
- SEO / OG 门禁：全部 PASS
- verify-site.sh：全部 PASS
- GitHub Actions：Route Data Quality Gate success
- 数量校验：22/22 Milestone 编号（74-95）全部出现

### 报告

- `reports/OEDW_MILESTONES_CHINESE_STORY_INDEX_REPORT.md`

---

## v1.5.5 · OEDW China Route Deep Optimization (2026-07-06)

### 主要变更

- **OEDW 中国段从可执行行程升级为深度执行版**
- **页面顶部状态修正**：进度 10% 规划中 → 完成度 85% 可用草案 v0.9（仍未做实地验证）
- **6 个新模块**：
  1. **如何使用这条路线**（4 张卡片 · 7 天 / 14 天 / 28 天 / 阅读版）
  2. **按时间选择你的 OEDW 中国段**（7 / 14 / 28 天三列选择器）
  3. **不同人群怎么走**（5 卡片 · 第一次走 / 摄影者 / 写作者 / 亲子家庭 / 高强度旅行者）
  4. **28 天每日执行卡**（28 张 · 7 字段：Day / 过夜建议 / 上午 / 下午 / 傍晚 / 最小完成版 / 可选加点 / 撤退策略 / 今日不要硬加点）
  5. **住宿区域与交通方式总表**（14 区域 · 6 字段：区域 / 过夜地 / 进入方式 / 离开方式 / 适合停留 / 风险提醒）
  6. **仍需实地验证的部分**（5 类：实地可达性 / 住宿交通 / 开放状态 / 细节资料 / 用户反馈）
- **页面顶部导航更新**：使用 / 导游词 / 执行卡 / 7/14/28 / 住宿交通 / 人群 / 待验证 / 数据
- **页面版本号全量更新**：v1.4.6 → v1.5.5（hero badge / page-meta / footer）
- **manifest v1.5.5**：
  - 顶层 `version` = `v1.5.5`
  - OEDW data_status_label：**长线文化复刻样板 · OEDW 深度执行版**
  - OEDW route_summary 补齐 7/14/28 天选择器 + 28 天每日执行卡 + 住宿交通总表
  - 9/9 SEO 字段保留
- **check-route-seo.py**：`manifest version` 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5
- **CSS 增强**：`assets/css/styles.css` + 200+ 行（14 个新类：.oedw-status-updated / .oedw-use-guide / .oedw-use-card / .oedw-execution-section / .oedw-execution-grid / .oedw-execution-card / .oedw-execution-meta / .oedw-minimum-box / .oedw-addon-box / .oedw-fallback-box / .oedw-do-not-box / .oedw-audience-grid / .oedw-audience-card / .oedw-transport-table / .oedw-pending-verification / .oedw-pending-card）
- **OEDW 路线导航 + 状态文案同步更新**：
  - 旧文案「本条路线尚在规划中。如需查看已上线的完整路线，请参考辽塔巡礼路线」已被替换
  - 旧文案「本页为规划中路线...不作为正式出行方案」已更新为「可用草案 v0.9 · 85% ...出发前请以最新官方材料与实地核实为准」

### 不修改

- ❌ 辽塔页面（v1.5.4 状态保留）
- ❌ 山西页面（v1.5.4 状态保留）
- ❌ CSV / GeoJSON / GPX 坐标数据
- ❌ SVG 路线示意图
- ❌ OG SVG（SEO 检查不要求）
- ❌ 路线工厂门禁脚本
- ❌ 地图 API / 后端 / 数据库 / npm 依赖

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：v1.5.4 状态保留

### 验证

- 路线工厂门禁：全部 PASS
- SEO / OG 门禁：全部 PASS
- verify-site.sh：全部 PASS
- GitHub Actions：Route Data Quality Gate success

### 报告

- `reports/OEDW_CHINA_ROUTE_DEEP_OPTIMIZATION_REPORT.md`

---

## v1.5.4 · Route Itinerary Field Guide Sprint 2 (2026-07-06)

### 主要变更

- **从可执行行程升级为随身导游手册**
- **OEDW 增强**：
  - 新增 28 天每日导游词表（28 段 · 含今日导游词 / 建议停留 / 现场观察 / 拍摄点 / 今日不要硬做）
  - 新增 OEDW 现场记录模板（8 个问题 · 路/人/声/动/旧/失/得/主角）
  - 新增 OEDW 拍摄 / 记录建议（5 类 · 道路 / 人 / 地貌 / 边界 / 日常）
- **辽塔增强**：
  - 新增 9 天每日导游词表（9 段）
  - 新增 核心点建议停留时长表（10 点 · 含奉国寺 / 万佛堂 / 朝阳北塔 / 庆州白塔 / 辽上京 / 大明塔 / 北镇庙 / 牛河梁 / 赤峰辽文化 / 承德避暑山庄）
  - 新增 如何读一座辽塔（6 步读图顺序 · 位置→轮廓→基座→塔身→檐部→环境）
  - 新增 辽塔拍摄与观察建议（6 类 · 全景/中景/近景/逆光/侧光/黄昏）
- **山西增强**：
  - 新增 12 天每日导游词表（12 段）
  - 新增 核心古建建议停留时长表（16 点 · 云冈 / 华严 / 善化 / 应县木塔 / 佛光 / 南禅 / 晋祠 / 双林 / 镇国 / 广胜 / 小西天 / 永乐宫 / 法兴 / 崇庆 / 青莲 / 府城玉皇庙）
  - 新增 如何读一座山西古建（7 步读图顺序 · 山门轴线→台基屋顶→梁架→塑像→壁画→修缮→环境）
  - 新增 古建拍摄与观察建议（6 类 · 结构/空间/细部/壁画/环境/修缮）
- **三条路线统一「今日不要硬加点」字段**：跨城日 + 高原 / 边境 / 古建 / 博物馆阅读疲劳明确提示
- **cleanup**：
  - 修正上轮 Phase 13 误写（CONTENT_NOTES.md / ROUTE_ITINERARY_OPTIMIZATION_SPRINT1_REPORT.md）
  - 修正辽塔「辆牲」错字为「牺牲」（trips/liao-tower-roadtrip/index.html + CHANGELOG.md）
- **manifest v1.5.4**：
  - 顶层 `version` = `v1.5.4`
  - OEDW data_status_label：长线文化复刻样板 · 已完成每日导游词
  - 辽塔 data_status_label：自驾人文路线样板 · 已完成读塔顺序
  - 山西 data_status_label：古建自驾路线样板 · 已完成古建读图顺序
  - 3 路线 route_summary 补齐「每日导游词 / 停留时长 / 拍摄点 / 读图顺序」
  - 9 SEO 字段保留
- **CSS 增强**：`assets/css/styles.css` + 213 行（.field-guide-section / .field-guide-grid / .field-guide-card / .field-guide-table / .duration-badge / .observation-list / .photo-tip-grid / .photo-tip-card / .reading-sequence / .do-not-add-note 等 14 个新类）
- **check-route-seo.py**：`manifest version` 接受 v1.5.2 / v1.5.3 / v1.5.4
- **首页 + 路线索引页轻量更新**：
  - index.html 增加「每日导游词 / 停留时长 / 拍摄点 / 读图顺序」说明
  - routes/index.html 增加「现场导览信息 / 每日导游词 / 停留时长」说明

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：**文化自驾粗点** / **非实时导航** / **不保证开放状态、门票、预约、维修闭馆**

### 不引入

- ❌ 地图 API
- ❌ 后端 / 数据库
- ❌ 构建系统 / npm 依赖
- ❌ 浏览器截图
- ❌ 实时交通 / 实时路况 / 实时门票价格
- ❌ IntersectionObserver / 复杂性能优化

### 验证

- 路线工厂门禁：全部 PASS（build-route-assets / validate-route-data / render-route-map-svg）
- SEO / OG 门禁：全部 PASS（check-routes-index-sync / check-route-page-integration / render-route-og-svg / check-route-seo）
- verify-site.sh：全部 PASS
- GitHub Actions：Route Data Quality Gate success

### 报告

- `reports/ROUTE_ITINERARY_FIELD_GUIDE_SPRINT2_REPORT.md`

---

## v1.5.3 · Route Itinerary Optimization Sprint 1 (2026-07-06)

### 主要变更

- **从系统建设回到具体路线**：补充不同时间预算下的行程版本与取舍原则
- **OEDW 增强**：
  - 新增 28 天推荐节奏表（13 段 · 含驾驶强度 / 可压缩性 / 取舍建议）
  - 6 条短线升级为「年度分段完成版本」· 补齐入口城市 / 出口城市 / 交通 / 适合人群 / 核心看点 / 最佳季节 / 难度 / 不可错过 / 可以删减 / 不建议做法
  - 新增「如何取舍这条长线」原则：6 门判断（只走 7 天 / 走 14 天 / 写作/摄影项目 / 核心提示）
- **辽塔增强**：
  - 新增 9 天优化版自驾节奏表（9 段 · 含驾驶强度 / 参观强度 / 当日重点 / 备选删减）
  - 新增 5 天压缩版（D1–D5 佛塔主轴）· 牺牲北镇 / 牛河梁 / 部分博物馆
  - 新增 12 天深度版（12 段 · 增加医巫闾山 / 牛河梁 / 博物馆多点）
  - 新增「辽塔路线取舍原则」：4 门判断（时间不足 / 博物馆型 / 自然地理型 / 亲子轻松型）
- **山西增强**：
  - 路线总览补充 4 主题拆分（北部石窟与辽金木构 / 中部晋祠与平遥体系 / 南部壁画与道教建筑 / 晋东南早期木构）
  - 新增 10–12 天标准版（12 段）· 可压缩性标注
  - 新增 7 天压缩版（7 段 · 首次去山西优先北部 + 中部）
  - 新增 15 天深度版（9 段 · 拍摄 / 写作 / 古建学习 · 每 3–4 天安排一个低强度日）
  - 新增「山西古建取舍原则」：4 门判断（初次 / 壁画爱好者 / 木构爱好者 / 注意事项）
- **manifest v1.5.3**：
  - 顶层 `version` = `v1.5.3`
  - 三条路线的 `data_status_label` 改为「已完成线路优化」
  - `route_summary` 补齐「已补充压缩版/标准版/深度版」描述
  - 9 SEO 字段保留不变
- **CSS 增强**：`assets/css/styles.css` + 195 行（.itinerary-optimization-section / .itinerary-version-card / .itinerary-table / .route-choice-principles / .route-cut-list / .route-intensity-badge 等 14 个新类）
- **首页 + 路线索引页轻量更新**：
  - index.html 增加「三条路线已补充压缩版 / 标准版 / 深度版」说明
  - routes/index.html 增加「路线详情页已开始补充不同时间预算下的线路版本」说明

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：**文化自驾粗点** / **非实时导航** / **不保证开放状态、门票、预约、维修闭馆**

### 不引入

- ❌ 地图 API
- ❌ 后端 / 数据库
- ❌ 构建系统 / npm 依赖
- ❌ 浏览器截图
- ❌ 实时交通 / 实时路况 / 实时门票价格

### 验证

- 路线工厂门禁：全部 PASS（build-route-assets / validate-route-data / render-route-map-svg）
- SEO / OG 门禁：全部 PASS（check-routes-index-sync / check-route-page-integration / render-route-og-svg / check-route-seo）
- verify-site.sh：全部 PASS
- GitHub Actions：Route Data Quality Gate success

### 报告

- `reports/ROUTE_ITINERARY_OPTIMIZATION_SPRINT1_REPORT.md`

---

## v1.5.2 · Route SEO, OG Assets and Preview Images (2026-07-06)

### 主要变更

- **OG SVG 生成器** `scripts/render-route-og-svg.py`（约 600 行）
  - 从 routes-manifest.json 自动生成社交分享 SVG
  - 风格：米白纸张 + 墨绿 + 暗金
  - 尺寸：1200×630（OG / Twitter 通用）
  - 支持命令：`render-route-og-svg.py` / `--all` / `<slug>` / `--all --check`
  - 零依赖、无浏览器、不需网络字体（仅使用 system-ui fallback）
- **5 个 OG SVG 资产**：
  - `out-of-eden-walk-china-og.svg` (5,497 字节)
  - `liao-tower-roadtrip-og.svg` (5,477 字节)
  - `shanxi-ancient-architecture-og.svg` (5,501 字节)
  - `site-og.svg` (4,586 字节 · 首页)
  - `routes-index-og.svg` (5,722 字节 · 路线索引页)
  - 每个 SVG 含 `<title>` + `<desc>` + route slug + 「行旅图谱」+ 「非导航」关键词
- **routes-manifest.json v1.5.2 SEO 字段**
  - 顶层 `version` 升级为 `v1.5.2`
  - 每条路线增加 9 个 SEO 字段：seo_title / seo_description / canonical_url / og_title / og_description / og_image_url / twitter_title / twitter_description / share_summary
  - **build-route-assets.py --all 不丢字段**：验证 9 个 SEO 字段被保留（dict() 浅拷贝 + 仅重写统计字段）
- **统一三条路线详情页 + 首页 + 路线索引页 `<head>` 模板**
  - 18 个标准 meta 标签：title / description / canonical / og:title / og:description / og:type / og:url / og:site_name / og:locale / og:image / og:image:width / og:image:height / og:image:alt / twitter:card（`summary_large_image`）/ twitter:title / twitter:description / twitter:image / theme-color
  - 路线索引页 og:image 指向 `routes-index-og.svg`（新）
  - 首页 og:image 指向 `site-og.svg`
  - 三条详情页 og:image 指向各自路线 og
- **share_summary 可见性**
  - 每条路线页 `<body>` 后加 `<p class="route-share-summary sr-only">{share_summary}</p>`
  - 屏幕阅读器可读、视觉隐藏
  - SEO 与社交分享爬虫可提取
- **新增 SEO 检查脚本** `scripts/check-route-seo.py`（约 220 行）
  - 检查范围：首页 + 路线索引页 + manifest 中三条路线的 page_url
  - 检查内容：14 类 meta 标签存在 · canonical 一致 · og:image basename 一致 · 主题包含 · OG SVG 文件存在 · panel 容器存在
  - 输出：`PASS route SEO check / pages checked: 5 / route pages: 3 / og assets: 5`
- **CSS 增强** `assets/css/styles.css`（+ 25 行）
  - `.route-share-summary` + `.sr-only` 两个类
- **`scripts/verify-site.sh` v1.5.2 增强**
  - 增加 5 个 OG SVG 文件存在性检查
  - 增加 `check-route-seo.py` 调用
  - 增加 `render-route-og-svg.py --all --check` 调用
  - 增加三条详情页 SEO 完整检查
  - 总门禁 97 → 107
- **`.github/workflows/route-data.yml` 同步**
  - 加入 `python3 scripts/check-route-seo.py` step
  - 加入 `python3 scripts/render-route-og-svg.py --all --check` step
- **新增文档** `docs/ROUTE_SEO_GUIDE.md`
  - 4 章节：目标 · 必填 head 元数据 · OG SVG 生成 · SEO 检查
  - 含命令清单、字段表、常见错误

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：**文化自驾粗点** / **非实时导航** / **不保证开放状态、门票、预约、维修闭馆**

### 不引入

- ❌ 地图 API
- ❌ 后端 / 数据库
- ❌ 构建系统 / npm 依赖
- ❌ 浏览器截图（已声明不依赖）

### 验证

- `python3 scripts/build-route-assets.py --all` 保留 9 个 SEO 字段 ✅
- `python3 scripts/build-route-assets.py --check` PASS
- `python3 scripts/validate-route-data.py --all --manifest-check` PASS
- `python3 scripts/render-route-map-svg.py --all --check` PASS
- `python3 scripts/check-routes-index-sync.py` PASS
- `python3 scripts/check-route-page-integration.py` PASS
- `python3 scripts/check-route-seo.py` PASS · 5 pages · 3 route pages · 5 og assets
- `python3 scripts/render-route-og-svg.py --all --check` PASS · 5 files
- `bash scripts/verify-site.sh` PASS · **107 项门禁全 PASS**（v1.5.1 97 项 + v1.5.2 新增 10 项）
- `.github/workflows/route-data.yml` 同步 · 加入 SEO + OG SVG 双 step

### 报告

- `reports/PHASE12_ROUTE_SEO_OG_REPORT.md`

---

## v1.5.1 · Route Page Unified Data Badges and Related Routes (2026-07-06)

### 主要变更

- **统一三条路线详情页的 `<head>` 模板**
  - OEDW / 辽塔 / 山西：18 个标准 meta 标签全量补齐
  - title / description / canonical / og:title / og:description / og:type / og:url / og:site_name / og:locale / og:image / og:image:width / og:image:height / og:image:alt / twitter:card（`summary_large_image`）/ twitter:title / twitter:description / twitter:image / theme-color
  - keyword 文案按 share_summary 首句抽取，避免随机拼接
- **首页 + 路线索引页 SEO 补齐**
  - 18 个标准 meta 标签全量补齐
  - title / canonical / og:image 指向 `site-og.svg`
  - 主题色统一为 `#2e4f4f`
- **OG SVG 资产（4 张 1200×630）**
  - `assets/img/og/out-of-eden-walk-china-og.svg` (3,867 字节 · 墨绿 + 暗金 · 复刻文化)
  - `assets/img/og/liao-tower-roadtrip-og.svg` (4,001 字节 · 暖棕 + 暗金 · 辽代自驾)
  - `assets/img/og/shanxi-ancient-architecture-og.svg` (3,877 字节 · 茶色 + 暗金 · 古建自驾)
  - `assets/img/og/site-og.svg` (3,593 字节 · 墨绿 + 暗金 · 行旅图谱总图)
  - 风格一致：沿用「暗背景 + 路径线 + 节点 + 文字徽章 + 安全边界」结构
- **routes-manifest.json v1.5.2**
  - 顶层 `version` 升级为 `v1.5.2`
  - 每条路线增加 9 个 SEO 字段
- **share_summary 页面可见性**
  - 每条路线页 `<body>` 后加 `<p class="route-share-summary sr-only">{share_summary}</p>`
  - 屏幕阅读器可读、视觉上隐形；SEO 与社交分享爬虫可提取
- **新增 `scripts/check-route-seo.py`**
  - 8 大类检查：manifest version / 9 SEO 字段 / OG SVG 文件大小 / 12 类 HTML meta / canonical 一致 / og:image basename 一致 / og_title 与 share_summary 可见性
- **CSS 增强**：`assets/css/styles.css` 增加 `.route-share-summary` 与 `.sr-only` 两个类
- **`scripts/verify-site.sh` v1.5.2 增强**
  - 增加 4 个 OG SVG 文件存在性检查
  - 增加 `check-route-seo.py` 调用
  - 增加三条详情页 SEO 完整检查（og:image + twitter:card + canonical）
  - 总门禁 97 → 105
- **`.github/workflows/route-data.yml` 同步**
  - 加入 `python3 scripts/check-route-seo.py` step

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：**文化自驾粗点** / **非实时导航** / **不保证开放状态、门票、预约、维修闭馆**

### 不引入

- ❌ 地图 API
- ❌ 后端 / 数据库
- ❌ 构建系统 / npm 依赖
- ❌ 浏览器截图（已声明不依赖）

### 验证

- `python3 scripts/build-route-assets.py --check` PASS
- `python3 scripts/validate-route-data.py --all --manifest-check` PASS
- `python3 scripts/render-route-map-svg.py --all --check` PASS
- `python3 scripts/check-routes-index-sync.py` PASS
- `python3 scripts/check-route-page-integration.py` PASS
- `python3 scripts/check-route-seo.py` PASS · 8 类检查全 PASS
- `bash scripts/verify-site.sh` PASS · **105 项门禁全 PASS**（v1.5.1 97 项 + v1.5.2 新增 8 项）

### 报告

- `reports/PHASE12_ROUTE_SEO_OG_REPORT.md`

---

## v1.5.1 · Route Page Unified Data Badges and Related Routes (2026-07-06)

### 主要变更

- **新增 `assets/js/route-page-badges.js`（375 行）**
  - 读取 routes-manifest.json · 按 `data-route-slug` 渲染统一模块
  - 状态徽章：数据完整度 / 分类 / 点位 / 段 / SVG / 非导航
  - 摘要卡：8 字段（路线名 / 数据状态 / 最佳季节 / 难度 / 点位 / 段落 / GeoJSON / GPX）+ theme_tags / region_tags
  - 下载入口：CSV / GeoJSON / GPX / SVG / 数据索引
  - 数据安全边界提示
  - 相关路线推荐：最多 2 条 · 按 category（+10）/ theme_tags 交集（×3）/ region_tags 交集（×2）/ featured（+1）/ points 排序
  - URL 转换：manifest 的 `../data/...` `../trips/...` 路径按 `data-site-root` 重写
  - fetch 失败 fallback / 无 JS fallback / 不推荐自己
  - 无依赖、纯 Vanilla JS
- **三条路线详情页接入统一模块**
  - OEDW：`trips/out-of-eden-walk-china/index.html` · `data-route-slug="out-of-eden-walk-china"`
  - 辽塔：`trips/liao-tower-roadtrip/index.html` · `data-route-slug="liao-tower-roadtrip"`
  - 山西：`trips/shanxi-ancient-architecture-roadtrip/index.html` · `data-route-slug="shanxi-ancient-architecture"`
  - 三页均插入 `route-page-data-panel` 容器 + 引入 `route-page-badges.js`
- **CSS 增强 `assets/css/styles.css`（+304 行）**
  - `.route-page-data-panel` / `.route-page-data-header` / `.route-page-data-title` / `.route-page-data-badges` / `.route-page-data-badge-*`（full / v01 / planned / svg / points / segments / not-nav / category-long_walk / category-roadtrip / category-architecture）
  - `.route-page-data-summary-grid` / `.route-page-data-summary-item` / `.route-page-data-summary-text` / `.route-page-data-tags`
  - `.route-page-data-actions` / `.route-page-data-action`
  - `.route-page-data-warning`
  - `.route-related-section` / `.route-related-grid` / `.route-related-card` / `.route-related-tags` / `.route-related-tag`
  - `.route-page-data-fallback`
  - 移动端单列 / 按钮可堆叠 / 标签自动换行
- **新增 `docs/ROUTE_PAGE_INTEGRATION_GUIDE.md`（287 行）**
  - 10 章节：目标 / 必备条件 / 接入代码 / 推荐插入位置 / URL 规则 / 必跑检查 / 常见错误 / 推荐逻辑 / 不引入依赖 / 当前状态
  - 包含 OEDW / 辽塔 / 山西 三条路线接入示例
- **新增 `scripts/check-route-page-integration.py`**
  - 检查 8 项：manifest 路由 / 页面文件 / data-route-slug 一致 / 容器存在 / 脚本引入 / data-site-root 声明 / 数据完整路线含「路线数据」关键词 / badges JS + guide 文件存在
- **`scripts/verify-site.sh` v1.5.1 增强**
  - 增加 `route-page-badges.js` / `ROUTE_PAGE_INTEGRATION_GUIDE.md` 文件存在性检查
  - 增加 `check-route-page-integration.py` 调用
  - 增加三条详情页接入检查（data-route-slug + route-page-badges.js + route-page-data-panel）
  - 总门禁 91 → 97
- **`.github/workflows/route-data.yml` 同步**
  - 加入 `python3 scripts/check-route-page-integration.py` step
- **`docs/ROUTE_PAGE_TEMPLATE.md` 同步**
  - 加入统一数据徽章模块章节
  - 更新推荐页面结构：Hero → 本页状态 → 路线数据状态徽章 → 快速阅读 → 路线总览 → ... → 下载路线数据 → 静态路线示意图 → 数据驱动路线表 → 相关路线推荐 → 来源资料
- **`docs/ROUTE_FACTORY_GUIDE.md` 同步**
  - §8 新增：路线页面接入步骤（新增路线完成后，运行 check-route-page-integration.py）

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：**文化自驾粗点** / **非实时导航** / **不保证开放状态、门票、预约、维修闭馆**

### 不引入

- ❌ 地图 API
- ❌ 后端 / 数据库
- ❌ 构建系统 / npm 依赖
- ❌ 第三方 JS 库

### 验证

- `python3 scripts/build-route-assets.py --check` PASS
- `python3 scripts/validate-route-data.py --all --manifest-check` PASS
- `python3 scripts/render-route-map-svg.py --all --check` PASS
- `python3 scripts/check-routes-index-sync.py` PASS · routes checked: 3 · dynamic manifest rendering: yes
- `python3 scripts/check-route-page-integration.py` PASS · routes checked: 3
- `bash scripts/verify-site.sh` PASS · **97 项门禁全 PASS**（v1.5.0 91 项 + v1.5.1 新增 6 项）
- `.github/workflows/route-data.yml` 同步

### 报告

- `reports/PHASE11_ROUTE_PAGE_INTEGRATION_REPORT.md`

---

## v1.5.0 · Route Index Experience and Multi-Route Search (2026-07-06)

### 主要变更

- **routes/index.html 升级为路线资产管理页**
  - 新增「路线仪表盘」section（`#dashboard`），由 `assets/js/routes-index.js` 从 `routes-manifest.json` 动态渲染
  - 仪表盘包含：统计区（路线总数 / 已有数据路线 / CSV 点位总数 / 段落总数 / GeoJSON Feature / SVG 预览）+ 搜索 + 分类筛选 + 完整度筛选 + 地区筛选 + 排序 + 路线卡片列表 + 路线对比表
  - 保留无 JS fallback（noscript 提示 + 下方三条路线硬编码卡片）
  - fetch 失败 fallback：提示 manifest 加载失败，引导使用静态索引
  - 版本号徽章：v1.4.9 → v1.5.0
- **新增前端脚本 `assets/js/routes-index.js`（381 行）**
  - 纯 Vanilla JS · 无依赖
  - 使用 `data-route-slug` / `data-route-geojson` / `data-route-name` 模式，与 `route-data-viewer.js` 保持一致
  - 工具函数 `$` / `escapeHtml` / `basename` 复用
  - 渲染统计 / 渲染卡片 / 过滤 + 排序 / 渲染对比表 / 渲染筛选控件
  - 失败 / 空结果状态处理
- **manifest 检索字段增强**
  - `version`: v1.5.0
  - 每条 route 增加：`category` / `theme_tags` / `region_tags` / `data_status_label` / `difficulty_label` / `best_season` / `route_summary` / `data_completeness` / `featured`
  - OEDW: long_walk / 5 theme tags / 6 region tags / 长线文化复刻样板 / 高·分段复刻 / 分段选择·山地避开恶劣天气 / full / featured
  - 辽塔: roadtrip / 5 theme tags / 4 region tags / 自驾人文路线样板 / 中·自驾为主 / 5–10 月 / v0.1 / featured
  - 山西: architecture / 5 theme tags / 6 region tags / 古建自驾路线样板 / 中高·点位分散 / 4–10 月 / v0.1 / featured
- **首页（index.html）路线数据资产统计**
  - Hero subtitle 更新：3 条路线 / 92 个文化复刻粗点 / 3 张 SVG 路线图
  - meta description：v1.5.0 接入 3 条路线数据资产、92 个文化复刻粗点、3 张静态 SVG 路线图
  - 路线数据索引 section：从「两条路线」更新为「三条路线」，版本标签 v1.4.9 → v1.5.0
- **新增文档 `docs/ROUTE_FACTORY_GUIDE.md`（285 行）**
  - 面向以后新增第 4 条路线（或更多路线）时的实操指南
  - 1. 新增路线标准流程（10 步）
  - 2. CSV 编写规则（18 字段、枚举、命名规范）
  - 3. 坐标规则（粗点不伪造、不导航、不写道路级导航坐标）
  - 4. 数据安全边界（文化复刻粗点 / 文化自驾粗点声明）
  - 5. 必跑命令（5 条核心 + verify-site.sh）
  - 6. 常见错误（manifest 统计漂移 / HTML 未同步 / SVG 缺 not for navigation / GPX waypoint 不一致 / planned-data 不应创建空 CSV / URL 与真实路径不一致）
  - 7. 当前三条路线示例（OEDW / 辽塔 / 山西）
- **CSS 增强 `assets/css/styles.css`（+ 334 行）**
  - 新增 `.routes-manifest-dashboard` / `.route-index-toolbar` / `.route-index-search` / `.route-index-cards` / `.route-index-card` / `.route-index-card-featured` / `.route-index-tags` / `.route-index-tag` / `.route-data-stat-grid` / `.route-data-stat-card` / `.route-data-stat-num` / `.route-data-stat-label` / `.route-compare-table` / `.route-status-badge` / `.route-status-full` / `.route-status-v01` / `.route-status-planned` / `.route-category-badge` / `.route-category-long-walk` / `.route-category-roadtrip` / `.route-category-architecture` / `.route-index-empty` / `.route-index-loading` / `.route-index-section-title`
  - 墨绿 / 米白 / 暗金风格延续
  - 移动端卡片单列 / 表格可横向滚动 / 筛选器自动换行
- **`scripts/check-routes-index-sync.py` v1.1**
  - 增加检查 routes-index.js 必填字段（slug / title / category / theme_tags / region_tags / points / segments / has_svg_preview）
  - 增加检查 #routes-manifest-dashboard 容器
  - 增加检查 routes/index.html 引入 routes-index.js
  - 增加检查 routes-manifest.json 引用
  - PASS 输出：`dynamic manifest rendering: yes`
- **`scripts/verify-site.sh` v1.5.0 增强**
  - 增加 routes-index.js / ROUTE_FACTORY_GUIDE.md / routes-manifest.json grep 检查
  - 保留 Phase 8 / Phase 9 79 项门禁
- **`.github/workflows/route-data.yml` 同步**
  - 加入 `python3 scripts/check-routes-index-sync.py` step
  - 加入 `bash scripts/verify-site.sh` step
- **`assets/js/route-data-viewer.js`**：保持完全通用化（已 Phase 7 完成），本次仅注释更新

### 重要边界（OEDW）

- 不出现「跨越六年」❌
- 不出现「22/23」❌
- Milestones 74–95 = **22/22** ✅
- 里程口径：**约 6,000–6,700 公里** ✅
- 北京段：**卢沟桥 → 天安门 → 小汤山** ✅
- 黄海终点：**2023 冬 / 2024.6 / 2024.8** ✅
- 时间跨度 manifest 字段：「2021 秋 → 2023 冬 → 2024.6 → 2024.8」 ✅

### 路线数据声明

- OEDW：**文化复刻粗点** / **非原始 GPS** / **非导航**
- 辽塔 / 山西：**文化自驾粗点** / **非实时导航** / **不保证开放状态、门票、预约、维修闭馆**

### 路线统计

- 路线总数：**3**
- 已有数据路线：**3**（OEDW / 辽塔 / 山西）
- planned-data：0
- CSV 点位总数：**92**（OEDW 42 + 辽塔 20 + 山西 30）
- 总段落数：**28**（OEDW 10 + 辽塔 9 + 山西 9）
- GeoJSON Feature：123
- SVG 预览：**3**
- categories：long_walk / roadtrip / architecture

### 不引入

- ❌ 地图 API
- ❌ 后端 / 数据库
- ❌ 构建系统 / npm 依赖
- ❌ 第三方 JS 库

### 验证

- `python3 scripts/build-route-assets.py --all` PASS
- `python3 scripts/build-route-assets.py --check` PASS
- `python3 scripts/validate-route-data.py --all --manifest-check` PASS
- `python3 scripts/render-route-map-svg.py --all --check` PASS
- `python3 scripts/check-routes-index-sync.py` PASS · routes checked: 3 · dynamic manifest rendering: yes
- `bash scripts/verify-site.sh` PASS（79+ 项门禁）
- `.github/workflows/route-data.yml` 同步

### 报告

- `reports/PHASE10_ROUTE_INDEX_SEARCH_REPORT.md`

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
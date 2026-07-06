# 行旅图谱 · 内容说明

## 项目定位

「行旅图谱」是一个个人人文旅行项目库，坚持以下原则：

1. **内容深度优先**：每条路线追求"随行导游"式的讲解，而非旅游攻略的清单
2. **纯静态架构**：不使用后端、数据库、地图 API，确保长期可维护
3. **无商业目的**：个人项目，不接广告、不做推广

## 第一个行程：北京出发·辽塔巡礼自驾导游手册

### 内容来源与可靠性

所有景点信息基于以下来源整理：

**官方/学术资料**:
- 各博物馆官方介绍
- 全国重点文物保护单位记录
- 相关考古报告与学术论文

**已阅读并参考**:
- 《辽史》脱脱等 中华书局点校本
- 《契丹国志》叶隆礼 贾敬颜校注
- 《辽金元史十五讲》张国维
- 《中国古代建筑史》第三卷（宋辽金西夏建筑）

**实地考察备注**:
- 部分细节（如开放时间、门票价格）可能随季节变化，建议出行前以官方公告为准
- 本手册内容为个人学习与旅行记录，不作为商业向导

### 景点讲解撰写原则

**重点景点（7个）**:
每个重点景点包含完整的随行导游词，约800字，结构如下：
- 30秒导入：建立场景感
- 现场怎么看：观察要点
- 3-5个观察点：具体细节
- 800字随行讲解：历史与现场融合
- 离开前回望：总结升华
- 2-3个自我提问：引导深度思考

**其他景点**:
简短的背景介绍与参观要点，不做展开式讲解。

### 数据结构

景点卡片字段：
- 名称、城市、类型、推荐等级
- 建议停留时间
- 一句话价值
- 为什么去
- 现场怎么看
- 重点细节
- 随行导游词
- 离开前回望
- 自我提问
- 美食搭配
- 地图搜索词
- 资料推荐

### 交互功能说明

所有交互功能均使用浏览器原生 API：

**localStorage 存储**:
- `visited_spots`: 已去景点列表
- `wanted_spots`: 想去景点列表
- `listened_spots`: 已听讲解列表
- `read_materials`: 已读书影音列表

**speechSynthesis 朗读**:
- 使用 `window.speechSynthesis` API
- 语言设置为中文
- 语速、语调使用默认值

**地图跳转**:
- 高德地图：`https://restapi.amap.com/v3/place/text?keywords={景点名}`
- 百度地图：`https://map.baidu.com/search/{景点名}/`

### 更新记录

**2026-07-04**: 初始版本发布
- 完成首页与辽塔巡礼行程页
- 包含9天8晚完整行程规划
- 7个重点景点完整导游词
- 6个城市介绍
- 美食模块
- 行前书影音资料包

## 未来路线储备

待添加路线：
- [ ] 山西古建巡礼（唐辽宋金元木构为主线）
- [ ] 丝绸之路河西段（石窟与丝路遗存）
- [ ] 江南古镇水乡（园林与士大夫文化）
- [ ] 西藏寺庙与朝圣路线

## 贡献与反馈

本项目为个人学习项目，内容如有疏漏欢迎指正。但不做商业合作邀请。


## v0.3 现场使用版 (2026-07-04)

### 新增功能
- 今日模式：9天行程切换，每日主题/路线/车程/住宿/必看/美食/提醒
- 到达前导入：17个重点景点 arrivalIntro + 按钮
- 现场怎么看：stepGuide 3-6步骤化导览
- 离开前回望：beforeLeave 字段
- 今晚复盘/明日预习：eveningReview 字段
- 行前7天学习计划：localStorage 打卡
- 现场模式底部导航：移动端 今日/路线/景点/朗读/打卡
- 进度面板：打卡/已听/已读/行前学习
- 语音不支持提示

### 数据更新
- 9天行程：+ eveningReview (今晚复盘/明日预习/今晚建议)
- 17个重点景点：+ arrivalIntro / stepGuide / beforeLeave
- 全局：+ prepPlan (行前7天学习计划)


## v0.4 知识深化版 (2026-07-04)

### 新增功能
- 辽代时间轴：9个关键节点（916-1125）可展开
- 辽五京体系：5座都城卡片（标记本行程涉及）
- 辽塔形制比较：6种塔形制对应本路线景点
- 核心概念图谱：11个词条可展开（契丹/辽/捺钵/五京/二元制度等）
- 出发前阅读路线：3种预习方案（30分钟/2小时/7天）
- 资料来源与事实核对：5类资料 + 出发前必读提醒
- 景点之间的关系：14个重点景点 relationship 字段

### 数据更新
- 全局：+ timeline(9), fiveCapitals(5), pagodaTypes(6), concepts(11), readingRoutes(3), sources(5)
- 14个重点景点：+ relationship 字段

### Workflow 改进
- 增加 NODE_VERSION 环境变量
- 移除 environment 引用避免保护规则


## v0.5 路线可视化版 (2026-07-04)

### 新增功能
- 路线示意图：纯 SVG 路线图，9 个城市节点（北京、锦州、义县、北镇、朝阳、赤峰、巴林左旗、宁城、承德）
- Day 高亮交互：Day 1-9 按钮，点击高亮当天城市节点和路线段
- 主题路径切换：5 个主题（辽塔线、石窟线、都城线、博物馆线、返程线）
- 景点关系网络：5 组关系项，点击跳转到对应景点卡片
- 路线阶段卡片：5 个阶段说明
- 路线总览 Meta：推荐天数/路线类型/核心主题/路线阶段

### JS 新增函数
- initRouteMap, highlightRouteDay, highlightThemeRoute
- initRelationNetwork, initV5


## v0.6 资料来源与事实核对版 (2026-07-04)

### 新增功能
- 资料来源索引：6 类资料分组（官方资料/博物馆/纪录片/书籍/研究/旅行整理），含可信度标签
- 14 个重点景点增加 sources 字段（每景点 3-4 条资料）
- 出发前实时核对清单：10 项 localStorage 可勾选
- 内容风险说明：出发前需二次核对提示
- 页面版本信息：v0.6 / 2026-07-04 / 规划资料

### 数据更新
- 全局：+ sourceIndex(29), preDepartureChecklist(10)
- 14 个重点景点：+ sources 字段

### Workflow 改进
- 升级 actions/setup-node@v4 with node-version: '24'
- 解决 Node.js 20 deprecated 警告
- 部署首次直接成功，无需重试


## v0.7 Heritage Visual Polish (2026-07-04)

### 新增功能
- 重点景点档案卡：7 个核心景点的文物图录式档案（编号/标签/字段）
- 辽塔线描示意：纯 SVG 4 类塔形（密檐/白塔/双塔/花塔）
- 城市章节封面：6 个城市章节（锦州/义县北镇/朝阳/赤峰/巴林左旗/宁城承德）
- 导游词摘句：7 个重点景点高亮引言
- 路线故事线：5 幕叙事卡片
- 阅读层级：section-hint 标签（先看这个 / 现场重点 / 如果时间有限）
- 页面版本更新到 v0.7


## v0.8 Multi Trip Framework (2026-07-04)

### 新增功能
- 首页升级为路线库首页
- Featured Trip 区块（辽塔巡礼作为主推）
- 6 条路线卡片：1 条已上线 / 5 条规划中
- 8 个分类筛选按钮（古建/石窟/博物馆/自驾/徒步/边疆史/城市史）
- 路线状态说明（已上线/规划中/待实地复盘/已实地复盘）
- "一条路线如何被整理" 8 步方法论

### 新增文件
- assets/js/trips-data.js：路线库数据
- assets/js/home.js：首页渲染/筛选逻辑

### 现有数据
- 6 条路线：
  - 北京出发·辽塔巡礼自驾导游手册（已上线 100%）
  - 山西古建自驾线（规划中 20%）
  - 北京周边辽金古建线（规划中 30%）
  - 河西走廊文化线（规划中 10%）
  - 滇越铁路文化线（规划中 5%）
  - Via Francigena 徒步线（规划中 0%）

### 现有行程页
- trips/liao-tower-roadtrip/index.html：保持 v0.7 全部功能不变


## v0.9 Trip Template & Second Route Skeleton (2026-07-04)

### 新增功能
- docs/TRIP_TEMPLATE.md：标准路线页面模板
- trips/shanxi-ancient-architecture-roadtrip/index.html：第二条路线规划中骨架页
- 首页山西古建卡片按钮从 disabled 改为「查看规划」
- 状态样式区分：status-live / status-planning / status-draft / status-reviewed
- 可复用样式类：trip-skeleton / planning-note / trip-template-section / candidate-spot

### 第二条路线
- 名称：山西古建自驾线
- 状态：规划中 · 20%
- 路线：北京 → 大同 → 应县 → 五台山周边 → 太原 → 平遥 / 介休 → 长治 / 晋城 → 北京
- 17 个候选点位：云冈石窟、华严寺、善化寺、应县木塔、佛光寺、南禅寺、晋祠、双塔寺、镇国寺、双林寺、介休后土庙、长治观音堂、崇庆寺、法兴寺、小西天、玉皇庙、青莲寺
- 全部点位标注「待核对」

### 完整路线 vs 规划中路线
- 辽塔巡礼：v0.7 完整路线（已上线 100%）
- 山西古建：v0.9 规划中骨架页（20%）


## v1.0 Stable Release (2026-07-04)

### 主要变更
- 统一项目版本为 v1.0.0 stable release
- 首页 Hero 副标题明确：1 条完整路线 + 1 条规划中
- 三页 SEO 基础 meta：title / description / og:title / og:description / og:type / og:url / keywords
- README 重写：项目定位 / 当前路线列表 / 如何添加新路线 / 当前版本 / 页面链接
- CHANGELOG.md 完整版本历史（v0.1 - v1.0）
- scripts/verify-site.sh：41 项验证检查
- Git tag v1.0.0

### 当前页面状态
- index.html：路线库首页
- trips/liao-tower-roadtrip/index.html：辽塔巡礼（v0.7 完整路线）
- trips/shanxi-ancient-architecture-roadtrip/index.html：山西古建（v0.9 规划中骨架页）

### 路线角色
- **辽塔页**：完整路线样板（v0.1 - v0.7），可作为正式出行方案
- **山西页**：规划中骨架页（v0.9），仅列出候选点位，**不作为正式出行方案**
- 其他 4 条规划中路线（河西走廊 / 滇越铁路 / Via Francigena / 北京周边辽金）：仅首页卡片


## v1.1 Shanxi Route Research (2026-07-04)

### 主要变更
- 山西古建自驾线从 v0.9 骨架页升级为 v1.1 研究建档版
- 候选点位分级：A 核心必看（12 个）/ B 强烈推荐（5 个）/ C 可选补充（2 个）
- 5 段路线研究框架（每段主题明确，含 A/B 级核心点位）
- 6 类资料来源索引（官方文旅/文物博物馆/建筑史/纪录片/书籍论文/旅行整理）
- 10 个山西古建关键词词条（木构/斗栱/梁架/彩塑/壁画/密檐塔/辽金寺院/晋东南古建/地方信仰/佛教空间）
- 2 个初步行程方案：8 天压缩版 / 11-12 天深度版
- 首页状态从「规划中」更新为「研究建档中」

### 山西页当前状态
- 状态：研究建档中 · 30%
- 已完成：候选点位分级、5 段路线研究框架、资料来源索引、关键词、初步行程方案
- 待完成：每日行程、景点详情、开放时间、门票、停车、来源深度核对、随行导游词、实地复盘

### 当前页面状态
- 辽塔页：完整路线样板（v0.1-v0.7），可作为正式出行方案
- 山西页：研究建档中（v1.1），**不作为正式出行方案**


## v1.2 Shanxi Route Calibration (2026-07-04)

### 主要变更
- 山西古建自驾线从「研究建档」升级为「路线校准」
- 推荐主路线：11 天 10 晚深度版（每日含住宿 + 核心景点 + 备选 + 取舍提醒 + Plan B）
- 8 天压缩版（明确舍弃哪些点）
- 新增 14 天慢行版
- 候选点位状态分级：主线必入 12 / 主线强烈推荐 5 / 主线备选 / 压缩版可舍弃 / 后续专题路线
- 路线取舍逻辑（6 条说明为什么不能把山西古建塞进短线）
- 11 天主路线每日分时草案（上午/中午/下午/晚上）
- 山西古建路线图示意（纯 SVG，标记晋北/晋中/晋南/晋东南）
- 下一步待核验清单（10 项）
- 首页状态：研究建档中 → 路线校准中（进度 30% → 45%）

### 山西页当前状态
- 状态：路线校准中 · 45%
- 已完成：候选点位分级 + 5 段路线研究框架 + 资料来源索引 + 关键词 + 3 种行程版本 + 每日分时草案 + 路线图示意 + 待核验清单
- 待完成：实地走访 + 每日行程精调 + 完整来源核对 + 随行导游词


## v1.4 Shanxi Cultural Guide Lite (2026-07-04)

### 主要变更
- 山西古建自驾线从「实用信息核验」升级为「文化导览草稿」
- 12 个 A 级核心点位完整导览草稿（A 级点位：云冈石窟 / 华严寺 / 善化寺 / 应县木塔 / 佛光寺 / 南禅寺 / 晋祠 / 镇国寺 / 双林寺 / 小西天 / 玉皇庙 / 青莲寺）
- 5 个 B 级强烈推荐点位简短导览（B 级点位：双塔寺 / 介休后土庙 / 长治观音堂 / 崇庆寺 / 法兴寺）
- 山西古建现场怎么看总导览模块（插入在路线总览之后、路线研究框架之前）
- 古建观察清单（10 项可勾选，localStorage 保存）
- 山西古建关键词进阶（新增 8 个词条）
- 导览草稿状态说明（插入在导览模块开头）
- 首页状态更新（进度 60% → 70%，状态改为"文化导览草稿中"）
- verify-site.sh 增加 11 项 v1.4 关键词检查

### 山西页当前状态
- 状态：规划中 · 文化导览草稿中 · 70%
- 已完成：候选点位分级 + 5 段路线研究框架 + 资料来源索引 + 关键词 + 3 种行程版本 + 每日分时草案 + 路线图示意 + 待核验清单 + 17 个点位实用信息 + 7 个高风险提示 + 出发前核验面板 + 每日核对事项 + **12 个 A 级导览草稿** + **5 个 B 级简短导览** + **山西古建现场怎么看** + **古建观察清单** + **关键词进阶**
- 待完成：实地走访 + 完整信息二次核对

---

## v1.3 Shanxi Practical Fact Audit (2026-07-04)

### 主要变更
- 山西古建自驾线从「路线校准」升级为「实用信息核验」
- 17 个 A/B 级点位实用信息卡（每个含：开放时间、闭馆日、门票/预约、停车、拍照/参观限制、建议停留时间、特别提示、高德地图、百度地图）
- 7 个高风险点位提示（佛光寺、南禅寺、小西天、玉皇庙、青莲寺、崇庆寺、法兴寺）
- 出发前必须核验面板（10 项可勾选，localStorage 保存）
- 11 天主路线每日核对事项
- 资料来源 v1.3 增强：官方信息来源 / 地图信息说明 / 核验日期说明 / 旅行整理说明
- 首页状态：路线校准中 → 实用信息核验中（进度 45% → 60%）

### 山西页当前状态
- 状态：实用信息核验中 · 60%
- 已完成：候选点位分级 + 5 段路线研究框架 + 资料来源索引 + 关键词 + 3 种行程版本 + 每日分时草案 + 路线图示意 + 待核验清单 + **17 个点位实用信息** + **7 个高风险提示** + **出发前核验面板** + **每日核对事项**
- 待完成：实地走访 + 完整信息二次核对


## Out of Eden Walk 中国段复刻路线 (2026-07-04)

### 路线定位

本路线基于 **Paul Salopek / National Geographic Out of Eden Walk** 中国段公开材料（Milestones 74–95、Dispatches）整理，是一条 **文化复刻路线**，而非 Paul 原始 GPS 轨迹的逐点复刻。

**重要边界**：
- 本路线 **非官方授权路线**，未获得 Paul Salopek 或 National Geographic 的授权或背书
- 不提供原始 GPS 轨迹、不保证逐段地理位置完全一致
- 路线地点存在部分模糊与口径差异（不同报道间命名、距离不同），已在页面中用注释说明
- 实地走访前请以最新官方材料为准

### 已完成模块

- 路线总览（2021 秋重启至 2024 夏抵达大连黄海）
- 10 段路线设计（滇西重启 / 大理丽江 / 茶马古道与木里 / 川西南雅安 / 剑门蜀道汉中 / 关中陕北 / 晋西雁门关 / 北京城市步行 / 京北长城承德 / 辽宁大连黄海）
- 时间线（按官方 Milestones 发布顺序排列，2021-10 至 2024-08）
- Milestones 表格（74–95，含大致地点、发布年份、路线段、主题、官方链接）
- 10 个关键故事卡片（每段对应一个）
- 3 种现实复刻版本（45-60 天研究型 / 21-28 天精华版 / 分省分段）
- 资料来源清单（官方 Out of Eden Walk / National Geographic 链接 + 中文报道 / 纪录片 / 展览）

### 待完成模块

- Milestone 91（"I'm a satisfied man"）官方页面 URL 尚未确认
- 实地走访验证（路线地点、点位实用信息）
- 详细分时日程、住宿与交通建议
- 每个 milestone 的中文摘要（目前仅有标题）
- 视觉资料（现场照片、路线地图）

### 当前状态

- 状态：规划中 · 文化复刻路线 · 10%
- 已完成：路线总览、10 段路线、时间线、Milestones 表格、10 个故事、3 种复刻版本、官方资料清单
- 待完成：实地走访、点位实用信息、详细分时日程、视觉资料

### 与已上线路线的关系

- **辽塔巡礼**：已上线完整路线，自驾主题；本路线是"文化复刻 + 慢新闻"主题，徒步/公路混合
- **山西古建自驾线**：规划中路线，自驾 + 古建主题；与本路线的"晋西雁门关 / 周口店 / 北京段"在地理上有重叠（雁门关、周口店），但叙事视角完全不同


## Out of Eden Walk 中国段复刻路线 · Phase 2 事实审校与可旅行化 (2026-07-04)

### 校准内容

- **时间口径**：中国段 = 2021 年秋重启 → 2023 年冬抵近黄海 → 2024 年 6 月补齐大连港 → 2024 年 8 月发布《Goodbye to China》
- **里程口径**：官方双口径 《Goodbye to China》"more than 6,000 kilometers" + 《New Map: Ancient Roads of China》"6,700 kilometers" → 页面采用区间口径 约 6,000–6,700 公里
- **Milestones 覆盖**：22/22（Milestone 91 URL 通过相邻 Milestone 92 页 Previous 链接追到 `milestone-91-im-satisfied-man`，验证返回 200，已作为官方页面收录）
- **Milestone 96+**：黄海渡船段 / 离开中国后，不计入中国陆上复刻路线

### 新增模块

- 事实审校模块（来源等级 A/B/C / 页面原则 / 已知不确定点）
- Milestones 表格升级为事实审校表（新增来源状态、旅行复刻建议两列）
- 10 段路线可旅行化字段（入口 / 出口 / 交通 / 徒步 / 自驾 / 公交 / 难度 / 季节 / 风险 / 不建议 / 替代）
- 21–28 天精华版逐日框架（D1–D28）
- 6 段短线版本（云南线 / 川西线 / 蜀道秦岭线 / 陕北山西线 / 北京长城线 / 东北收束线）
- 不建议硬走清单（6 类边界）
- 资料清单新增 B 级来源组

### 待办

- Milestone 91 官方正文详细提取（本次仅确认 URL 可达，未提取正文细节）
- B 级补充来源的稳定 URL：Esri / ArcGIS storytelling map · 上海纽约大学 ICA 展期详情
- 中文村镇译名实地核对（Shouguozhangzhi / Xiaoguan / Ciyotouzhen / Li Jia Tun）

---

## Out of Eden Walk 中国段 · Phase 3 叙事导览版（v1.4.3）

### 范围
本轮在 Phase 2 事实审校与可旅行化基础上，升级为「随行导游式长卷页面」。

### 新增模块
1. **如何阅读这条路线**（4 张卡片）
   - 不是挑战路线 / 中国地理剖面线 / 慢新闻路线 / 可分年完成的长线

2. **中国段长卷地图**（12 个节点）
   - 从滇西边境到大连黄海的长卷式文字地图
   - 不使用外部地图 API
   - 每个节点含：标题 / 描述 / 对应 milestone

3. **10 段随行导游词**
   - 每段 300–500 字沉静式人文导览
   - 每段结尾给「现场观察」提示
   - 写作原则：不写营销、不写百科、解释"为什么这一段重要"

4. **21–28 天每日主题**（表格新增列）
   - 覆盖 D1–D28 共 9 个区段
   - 每天 10–20 字主题（如"D1 从边境沉默进入滇西"）
   - 不只写地点，写主题

5. **6 段短线适合人群**（每条新增 5 个字段）
   - 适合人群 / 最适合季节 / 推荐旅行方式 / 一句话主题 / 不适合人群

6. **行前资料包**（5 类）
   - A 必读官方材料 / B 中国段主题阅读方向 / C 观看材料 / D 出发前准备 checklist / E 旅行记录模板

7. **传播摘要**（3 个版本）
   - 30 秒版（朋友圈 / 小红书）
   - 3 分钟版（公众号）
   - 讲解员版（展览 / 视频旁白）
   - 全部原创中文，核心信息一致

### 严格保留
- Phase 2 事实边界（"约 6,000–6,700 公里"、"两年多"、"22/22"、"卢沟桥→天安门→小汤山"、黄海三层时间）
- 不修改 v1.0 / v1.4 / v1.4.1 / v1.4.2 架构
- 不引入后端、不引入数据库、不调用地图 API、不引入构建系统

### 写作原则
- 沉静 > 营销
- 现场感 > 形容词堆砌
- "为什么重要" > "是什么"
- 每段导游词不新增未经核验的事实

---


---

## Out of Eden Walk 中国段 · Phase 4 页面体验与发布包装（v1.4.4）

### 范围
本轮在 Phase 3 叙事导览版基础上，把页面升级为"可以公开展示、移动端友好、可分享、可验收的代表性作品页"。

### 页面体验增强清单
1. **快速阅读目录**（10 个锚点按钮）
   - 桌面端横向按钮，移动端可横向滚动
   - 锚点跳转到现有模块（不重复内容）

2. **阅读进度条**（顶部细线）
   - 3px 高度 · 渐变色（暗金 → 墨绿）
   - 跟随滚动百分比更新宽度
   - z-index 9999，固定在顶部

3. **返回顶部按钮**
   - 滚动 600px 后淡入显示
   - 平滑滚动到顶部
   - 桌面端右下角，移动端缩小 + 调整位置

4. **移动端长表格滚动**
   - Milestones 表格（22 行）+ 21–28 天精华版表格（9 行）外层包裹
   - 移动端显示"← 左右滑动查看完整表格 →"提示

### SEO / Open Graph / Canonical Polish
- title 增加副标题（"Paul Salopek 国家地理慢新闻路线 · 行旅图谱"）
- description 精炼到 120–160 中文字符
- canonical 链接完整 URL
- og:site_name / og:locale 补充
- Twitter Card（summary 类型，无图片）

### 本页状态 + 适合谁使用
- 版本 / 完成度 / 已交付 / 仍待完善 4 项
- 适合人群 4 类（深度旅行者 / 慢新闻写作 / 年度旅行 / 古道长城）
- 不适合人群 4 类（GPS 硬走 / 无准备山地 / 打卡党 / 精确复刻派）

### 首页推荐位强化
- OEDW 卡片新增 `代表长线 · 已完成 Phase 4` 渐变徽章
- 卡片左边框高亮（暗金 3px）
- 进度 30% → 50%
- 状态字段更新为 "50% · 事实审校 + 可旅行化 + 叙事导览 + 发布包装"

### 发布文案模块
4 个可复制文本块：
1. 朋友圈版（100–180 字）
2. 小红书版（标题 + 正文 + 标签）
3. 公众号导语版（400–600 字）
4. README 简介版（120–200 字）

### 链接抽检（spot check）
8 个关键外链 HTTP 200 抽检：
- Out of Eden Walk 官方首页
- Goodbye to China
- New Map: Ancient Roads of China
- Walking Map: Mazes of Beijing
- Rediscovering China's Capital on Foot
- Meeting a Dawn Human
- Qing Roads
- Milestone 91

### 严格保留
- Phase 2 / Phase 3 事实边界（"约 6,000–6,700 公里"、"两年多"、"22/22"、"卢沟桥→天安门→小汤山"、黄海三层时间）

### 技术决策
- **JS 内联无依赖**：阅读进度 + 返回顶部只用 26 行 Vanilla JS，无 jQuery / 无 npm
- **JS 禁用友好**：进度条宽度初始 0，按钮隐藏，用户禁用 JS 时不影响页面阅读
- **requestAnimationFrame 节流**：避免高频 scroll 事件性能问题
- **CSS only 进度条动画**：无 JS 也可静态显示 0%（不破坏布局）

---


---

## Out of Eden Walk 中国段 · Phase 5 路线数据资产（v1.4.5）

### 范围
本轮把 Out of Eden Walk 中国段页面从"公开代表页"升级为项目内可复用的路线数据资产。

### 数据文件清单

| 文件 | 格式 | 大小 | 用途 |
|------|------|------|------|
| `data/routes/out-of-eden-walk-china.csv` | CSV | ~7 KB | 表格分析、Excel、Pandas |
| `data/routes/out-of-eden-walk-china.geojson` | GeoJSON | ~14 KB | QGIS、geojson.io、Leaflet 静态地图 |
| `data/routes/out-of-eden-walk-china.gpx` | GPX 1.1 | ~12 KB | 粗略 waypoint 查看（不可导航）|
| `data/routes/README.md` | Markdown | ~4 KB | 数据说明、字段定义、使用方法 |
| `routes/index.html` | HTML | ~10 KB | 路线数据索引页 |

### 数据规模

- **42 个点位**（覆盖 10 个段落）
- **18 个字段**（id / sequence / segment_id / segment_name / point_name / province / city_or_area / latitude / longitude / coordinate_precision / source_level / replication_feasibility / difficulty / best_season / transport_hint / risk_note / source_note / url）
- **GeoJSON 53 个 Feature**：42 Point + 1 主 LineString + 10 段 LineString
- **GPX 42 个 waypoints + 1 个 track**

### 段覆盖

| 段 | 点位数 | 代表点 |
|---|------|------|
| S01 滇西重启线 | 5 | 边境 / 腾冲 / 和顺 / 高黎贡山 / 大理 |
| S02 大理丽江雪山线 | 4 | 喜洲 / 洱源 / 丽江 / 玉龙雪山 |
| S03 茶马古道木里线 | 3 | 泸沽湖 / 木里 / 康定 |
| S04 川西南雅安线 | 5 | 天全 / 雅安 / 平乐 / 三星堆 / 绵竹 |
| S05 剑门蜀道汉中线 | 4 | 剑门关 / 广元 / 汉中 / 秦岭 |
| S06 关中陕北线 | 4 | 西安 / 宜君 / 延安 / 壶口 |
| S07 晋西雁门关线 | 4 | 吕梁 / 忻州 / 雁门关 / 周口店 |
| S08 北京城市步行线 | 4 | 卢沟桥 / 天安门 / 胡同 / 小汤山 |
| S09 京北长城承德线 | 3 | 司马台 / 古北口 / 承德 |
| S10 辽宁大连黄海线 | 6 | 锦州 / 沈阳 / 辽阳 / 乡村粗点 / 大连港 / 黄海 |

### 严格保留

- 所有数据均标注 **"不是 Paul Salopek 原始 GPS 轨迹"**
- 所有数据均标注 **"不用于导航"**
- 顶部 metadata 包含 disclaimer / source_scope / updated_at / coordinate_systems / approximate_distance_km

### Phase 6 可扩展

1. 多路线数据化（辽塔、山西、其他 5 条规划中路线）
2. 数据可视化（基于 GeoJSON 的 SVG 路线示意图）
3. 数据校验工具（坐标范围、字段完整性、内容一致性）
4. 多语言版本（中英对照）

---


---

## Out of Eden Walk 中国段 · Phase 6 数据驱动展示与静态地图预览（v1.4.6）

### 范围
本轮把 OEDW 页面从"静态下载"升级为"数据驱动 + 可视化"。

### 新增脚本

#### `scripts/validate-route-data.py`
- 固化 Phase 5 临时校验逻辑
- 校验 CSV / GeoJSON / GPX 三种格式
- 输出 PASS / FAIL 状态码
- 默认校验 OEDW，可通过参数传入其他 slug
- 用法：`python3 scripts/validate-route-data.py`

#### `scripts/render-route-map-svg.py`
- 基于 GeoJSON 生成纯静态 SVG 路线示意图
- 使用 bounding-box equirectangular projection
- 不使用外部底图、不调用地图 API
- 输出：`assets/img/routes/<slug>-map.svg`
- 用法：`python3 scripts/render-route-map-svg.py`

### 新增文件

| 文件 | 大小 | 用途 |
|------|------|------|
| `scripts/validate-route-data.py` | ~10 KB | 永久校验脚本 |
| `scripts/render-route-map-svg.py` | ~14 KB | SVG 生成脚本 |
| `assets/img/routes/out-of-eden-walk-china-map.svg` | ~9 KB | 静态 SVG 路线图 |
| `assets/js/route-data-viewer.js` | ~12 KB | 前端数据查看器 |

### 前端数据查看器功能

- `fetch()` GeoJSON
- 自动生成摘要（6 项：点位 / 段 / 省份 / 高复刻 / 中复刻 / 低复刻）
- 自动生成段落分布（10 个段卡片）
- 4 个筛选器：段落 / 省份 / 难度 / 可复刻性
- 表格字段：序号 / 段落 / 点位 / 省份 / 地区 / 精度 / 难度 / 可复刻性 / 风险提示
- 徽章样式：高（绿）/ 中（金）/ 低（浅金）/ 注意（红）
- 失败 fallback：直接显示下载链接 + 错误信息
- noscript fallback：直接显示下载链接

### OEDW 页面新增模块

1. **静态路线示意图**（`#static-map`）
   - 嵌入 SVG 图片
   - 图注明确"非 Paul Salopek 原始 GPS 轨迹 · 非导航"

2. **数据驱动路线表**（`#route-table`）
   - 容器 `<section id="route-data-viewer" data-route-geojson="..." data-route-name="...">`
   - 引用 `assets/js/route-data-viewer.js`

### routes/index.html 增强

- 新增"数据规范"section
- 新增"数据处理流程"section（4 步：数据源 → 校验 → 渲染 → 展示）
- OEDW 卡片内新增 SVG 预览 + 9 项数据统计

### 数据处理流程（标准化）

```
CSV / GeoJSON / GPX
  ↓ validate-route-data.py
PASS / FAIL
  ↓ render-route-map-svg.py
assets/img/routes/<slug>-map.svg
  ↓ route-data-viewer.js (前端 fetch)
#route-data-viewer 容器 → 摘要 + 筛选器 + 表格
```

### 严格保留

- Phase 2-5 事实边界
- "文化复刻粗点" 标注
- "非 Paul Salopek 原始 GPS" 标注
- "非导航" 标注

### Phase 7 可扩展

1. 多路线数据驱动（辽塔、山西、其他规划中路线）
2. SVG 样式变体（多主题 / 多投影）
3. 前端数据可视化（柱状图 / 饼图）
4. 数据导出（PDF / Markdown 表格）
5. POI 语义标注升级

---


## Phase 7 · 路线数据模板化与多路线复用（v1.4.7 · 2026-07-05）

Phase 7 完成路线数据模板化与多路线复用：

- **新增 ROUTE_DATA_SPEC**（docs/ROUTE_DATA_SPEC.md）· 通用路线数据规范 v1.0
  - 定位 / 文件结构 / CSV 18 字段 / 4 类枚举 / GeoJSON / GPX / SVG 规范
- **新增 ROUTE_PAGE_TEMPLATE**（docs/ROUTE_PAGE_TEMPLATE.md）· 通用路线页面模板 v1.0
  - head 模板 / 19 个模块顺序 / 关键模块示例 / 状态进度建议
- **新增 routes-manifest**（data/routes/routes-manifest.json）
  - 项目级路线登记表 · v1.4.7 · 2 条路线
- **校验脚本支持任意路线**：`scripts/validate-route-data.py`
  - 任意 slug / `--all` / 路线级别阈值 / 通用化校验
- **SVG 生成脚本支持任意路线**：`scripts/render-route-map-svg.py`
  - 任意 slug / `--all` / 动态 title/desc / 中英文双语声明
- **辽塔巡礼成为第二条路线数据资产**：
  - CSV 20 行 · GeoJSON 30 features · GPX 20 waypoints · SVG 6.8 KB
  - 文化自驾粗点 · 9 段路线 · 9 天 8 晚闭环
- **路线数据查看器通用化**：`assets/js/route-data-viewer.js`
  - 去除 OEDW 硬编码 · fallback 下载链接根据 geoUrl 推断 slug
- **路线数据索引页增强**：`routes/index.html`
  - 路线数据资产总览 + 辽塔巡礼数据卡片 + 多路线规范模块
- **首页 trip 卡片增强**：
  - "已接入路线数据" 标识 + 数据元信息链接
- **事实边界严格保留**：
  - OEDW 22/22 / 6,000–6,700 公里 / 两年多 / 黄海三层时间 / 文化复刻粗点
- **反模式坚持**：
  - 不引入地图 API / 不引入构建系统 / 不引入 npm 依赖

后续山西古建、北京周边等路线可继续复用同一套规范与脚本。

## Phase 8 · 路线工厂自动化与质量门禁（v1.4.8 · 2026-07-05）

Phase 8 完成路线工厂自动化与质量门禁：

- **新增 build-route-assets.py**：路线工厂入口，一条命令完成「校验 + SVG 生成 + manifest 统计同步」
- **增强 validate-route-data.py**：新增 `--json` 输出 + `--manifest-check` 模式
- **增强 render-route-map-svg.py**：新增 `--check` 模式（只校验不生成）+ 自动跳过 planned-data 路线
- **新增 check-routes-index-sync.py**：manifest 与 routes/index.html 漂移检查
- **verify-site.sh 接入路线数据门禁**：70 → 79 项检查
- **新增 GitHub Actions route-data workflow**：Route Data Quality Gate
- **manifest 增强**：增加 `geojson_points` / `geojson_lines` 字段
- **新增山西古建 planned-data 条目**：status=planned-data · URL 全 null · 不创建空数据
- **routes/index.html 增强**：质量门禁模块 + 路线工厂流程模块

OEDW 事实边界完整保留。辽塔数据未回退。所有 planned-data 路线不会误生成空文件。

---


## Phase 9 · 山西古建路线数据生产（v1.4.9 · 2026-07-05）

Phase 9 完成山西古建路线数据生产：

- `shanxi-ancient-architecture` 从 planned-data 升级为 data-v0.1
- 新增山西古建路线 CSV / GeoJSON / GPX / SVG（30 个粗点、9 段路线、11 天 10 晚）
- 9 段分布：S01 大同云冈 / S02 浑源恒山应县 / S03 五台山早期木构 / S04 太原晋祠 / S05 平遥双林镇国 / S06 介休灵石霍州 / S07 临汾洪洞隰县 / S08 运城永乐解州 / S09 晋东南长治晋城
- 山西页面增加「路线数据」轻量模块
- 路线工厂门禁验证三路线通过
- OEDW / 辽塔数据未回退
- 实际页面路径 `trips/shanxi-ancient-architecture-roadtrip/` 已同步到 manifest

---

## Phase 10 · 路线索引体验与多路线检索（v1.5.0 · 2026-07-06）

Phase 10 完成路线索引体验与多路线检索：

- `routes/index.html` 升级为「路线资产管理页」，从「下载索引页」升级为带搜索 / 筛选 / 排序 / 对比 / 统计的仪表盘
- 新增 `assets/js/routes-index.js`（381 行），纯 Vanilla JS · 无依赖 · 从 `routes-manifest.json` 动态渲染路线卡片、对比表与统计区
- manifest 检索字段增强：每条 route 增加 `category` / `theme_tags` / `region_tags` / `data_status_label` / `difficulty_label` / `best_season` / `route_summary` / `data_completeness` / `featured`
- 首页（`index.html`）Hero subtitle + meta description 同步更新到 v1.5.0 / 3 条路线 / 92 个文化复刻粗点 / 3 张 SVG
- 新增 `docs/ROUTE_FACTORY_GUIDE.md`（285 行），写清楚以后新增第 4 条路线的实操步骤、CSV 规则、坐标规则、数据安全边界、必跑命令、常见错误
- CSS 增强 `assets/css/styles.css`（+ 334 行），统一墨绿 / 米白 / 暗金风格，新增 dashboard / toolbar / cards / compare / status badge / category badge 等样式
- `scripts/check-routes-index-sync.py` v1.1 增强：检查 routes-index.js 必填字段 + dashboard 容器 + manifest 引用 + JS 动态渲染支持
- `scripts/verify-site.sh` v1.5.0 增强：增加 routes-index.js / ROUTE_FACTORY_GUIDE / routes-manifest.json grep 检查
- `.github/workflows/route-data.yml` 同步加入 `check-routes-index-sync.py` 与 `verify-site.sh` step
- `assets/js/route-data-viewer.js` 保持完全通用化（Phase 7 已完成，本次仅注释更新）
- 路线数据声明：3 条路线统一标注 **文化复刻粗点 / 文化自驾粗点 / 非实时导航 / 不保证开放状态**
- 不引入地图 API / npm 依赖 / 构建系统 / 后端
- OEDW 事实边界完整保留：6,000–6,700 公里 / 22/22 milestones / 卢沟桥→天安门→小汤山 / 黄海三层时间
- 路线统计：3 路线 / 92 点位 / 28 段落 / 3 SVG / 0 planned-data
- categories：long_walk / roadtrip / architecture

---

## Phase 11 · 路线页面统一数据徽章与跨页面推荐（v1.5.1 · 2026-07-06）

Phase 11 完成路线页面统一数据徽章与跨页面推荐：

- 新增 `assets/js/route-page-badges.js`（375 行），从 `routes-manifest.json` 读取并渲染统一模块：
  - 状态徽章（数据完整度 / 分类 / 点位 / 段 / SVG / 非导航）
  - 路线数据摘要卡（8 字段）+ theme_tags / region_tags
  - 数据下载入口（CSV / GeoJSON / GPX / SVG / 数据索引）
  - 数据安全边界提示
  - 相关路线推荐（最多 2 条，按 category / theme_tags / region_tags / featured / points 排序）
  - URL 转换（manifest 的 `../data/...` / `../trips/...` 按 `data-site-root` 重写）
- 三条路线详情页接入统一面板：
  - OEDW：`trips/out-of-eden-walk-china/index.html`
  - 辽塔：`trips/liao-tower-roadtrip/index.html`
  - 山西：`trips/shanxi-ancient-architecture-roadtrip/index.html`
- CSS 增强 `assets/css/styles.css`（+304 行），统一墨绿 / 米白 / 暗金风格，新增 route-page-data-panel / summary / actions / warning / related 样式
- 新增 `docs/ROUTE_PAGE_INTEGRATION_GUIDE.md`（287 行，10 章节）
- 新增 `scripts/check-route-page-integration.py`：检查 8 项（manifest 路由 / 页面文件 / data-route-slug 一致 / 容器存在 / 脚本引入 / data-site-root / 数据路线关键词 / 文件存在性）
- `scripts/verify-site.sh` v1.5.1 增强：增加 6 项 v1.5.1 检查（1 项 integration check + 3 项详情页接入 + 2 项文件存在性），总门禁 91 → 97
- `.github/workflows/route-data.yml` 加入 `check-route-page-integration.py` step
- `docs/ROUTE_PAGE_TEMPLATE.md` 加入统一数据徽章模块章节
- `docs/ROUTE_FACTORY_GUIDE.md` 加入 §8 路线页面接入步骤
- 不引入地图 API / npm 依赖 / 构建系统 / 后端
- OEDW 事实边界完整保留
- 形成 首页 → 路线索引 → 路线详情页 → 相关路线 → 数据下载 闭环

---

## Phase 12 · 路线页面 SEO 统一与 OG 资产 (v1.5.2 · 2026-07-06)

Phase 12 完成路线页面 SEO 统一与 OG 资产：

- 统一三条路线详情页的 `<head>` 模板：18 个标准 meta 标签（title / description / canonical / og:* / twitter:card `summary_large_image` / twitter:* / theme-color）
- 首页 + 路线索引页 SEO 补齐：18 个标准 meta 标签
- OG SVG 资产 × 4（1200×630）：
  - `assets/img/og/out-of-eden-walk-china-og.svg` (3,867 字节)
  - `assets/img/og/liao-tower-roadtrip-og.svg` (4,001 字节)
  - `assets/img/og/shanxi-ancient-architecture-og.svg` (3,877 字节)
  - `assets/img/og/site-og.svg` (3,593 字节)
- routes-manifest.json v1.5.2：每条路线增加 9 个 SEO 字段（seo_title / seo_description / canonical_url / og_title / og_description / og_image_url / twitter_title / twitter_description / share_summary）
- share_summary 可读性：每条路线页 `<body>` 后加 `<p class="route-share-summary sr-only">{share_summary}</p>`，屏幕阅读器可读、视觉隐形
- CSS 增强：`.route-share-summary` + `.sr-only` 两个类
- 新增 `scripts/check-route-seo.py`：8 大类检查（manifest version / 9 SEO 字段 / OG 文件大小 / 12 类 HTML meta / canonical 一致 / og:image basename 一致 / og_title 可见 / share_summary 可见）
- `scripts/verify-site.sh` v1.5.2 增强：增加 8 项 v1.5.2 检查，总门禁 97 → 105
- `.github/workflows/route-data.yml` 加入 `check-route-seo.py` step
- 不引入地图 API / npm 依赖 / 构建系统 / 浏览器截图
- OEDW 事实边界完整保留
- 形成完整 SEO 闭环：manifest → 页面 head → OG 资产 → 社交分享

---

## Phase 12 · 路线页面 SEO 统一与 OG 资产 (v1.5.2 · 2026-07-06)

Phase 12 完成路线页面 SEO 统一与 OG 资产：

- 新增 OG SVG 生成器 `scripts/render-route-og-svg.py`：从 routes-manifest.json 自动生成 · 风格米白纸张 + 墨绿 + 暗金 · 1200×630 · 零依赖
- 5 个 OG SVG 资产：
  - `assets/img/og/out-of-eden-walk-china-og.svg` (5,497 字节)
  - `assets/img/og/liao-tower-roadtrip-og.svg` (5,477 字节)
  - `assets/img/og/shanxi-ancient-architecture-og.svg` (5,501 字节)
  - `assets/img/og/site-og.svg` (4,586 字节 · 首页)
  - `assets/img/og/routes-index-og.svg` (5,722 字节 · 路线索引页)
- 每个 SVG 含 `<title>` + `<desc>` + route slug + 「行旅图谱」+ 「非导航」关键词
- 统一三条路线详情页 + 首页 + 路线索引页 `<head>` 模板：18 个标准 meta 标签
- 路线索引页 og:image 指向 `routes-index-og.svg`（v1.5.2 新增）
- 首页 og:image 指向 `site-og.svg`
- routes-manifest.json v1.5.2：每条路线增加 9 个 SEO 字段
- **build-route-assets.py --all 不丢字段**：9 个 SEO 字段被 dict() 浅拷贝保留
- share_summary 可见性：每条路线页 `<body>` 后加 `<p class="route-share-summary sr-only">{share_summary}</p>`
- CSS 增强：`.route-share-summary` + `.sr-only` 两个类
- 新增 `scripts/check-route-seo.py`：14 类 meta 标签 + canonical/og:image 一致性 + panel 容器检查
- 新增 `scripts/render-route-og-svg.py --all --check`：OG SVG 文件存在 + 关键词检查
- `scripts/verify-site.sh` v1.5.2 增强：增加 10 项 v1.5.2 检查（5 OG 文件 + 1 SEO check + 1 OG SVG check + 3 详情页 SEO），总门禁 97 → 107
- `.github/workflows/route-data.yml` 加入 `check-route-seo.py` 与 `render-route-og-svg.py --check` 双 step
- 新增 `docs/ROUTE_SEO_GUIDE.md`：4 章节 SEO 文档
- 不引入地图 API / npm 依赖 / 构建系统 / 浏览器截图
- OEDW 事实边界完整保留
- 形成完整 SEO 闭环：manifest → 页面 head → OG 资产 → 社交分享


## 线路优化专项 v1.5.3 (Route Itinerary Optimization Sprint 1) (2026-07-06)

从系统建设回到具体路线。补充不同时间预算下的行程版本与取舍原则：

- OEDW 新增 28 天推荐节奏表 · 6 条年度短线升级 · 「如何取舍这条长线」原则
- 辽塔新增 9 天优化版 · 5 天压缩版 · 12 天深度版 · 「辽塔路线取舍原则」
- 山西新增 10–12 天标准版 · 7 天压缩版 · 15 天深度版 · 「山西古建取舍原则」
- manifest v1.5.3：data_status_label + route_summary 轻微更新
- CSS 增强 195 行（.itinerary-optimization-section / .itinerary-table / .route-choice-principles / .route-intensity-badge 等 14 个新类）
- 首页 + 路线索引页轻量更新
- 不引入地图 API / npm / 构建系统 / 浏览器截图 / 实时交通
- OEDW 事实边界完整保留

## 线路优化专项 v1.5.4 (Route Itinerary Field Guide Sprint 2) (2026-07-06)

从可执行行程升级为随身导游手册。三条路线补充每日导游词、核心点停留时长、拍摄观察建议和读图顺序：

- OEDW 新增 28 天每日导游词 · 现场记录模板 · 拍摄记录建议 · 今日不要硬加点
- 辽塔新增 9 天每日导游词 · 核心点停留时长 · 如何读一座辽塔 · 拍摄建议 · 今日不要硬加点
- 山西新增 12 天每日导游词 · 核心古建停留时长 · 如何读一座山西古建 · 拍摄观察建议 · 今日不要硬加点
- cleanup: 修正上轮 Phase 13 误写 + 辽塔「辆牲」错字为「牺牲」
- manifest v1.5.4：data_status_label / route_summary 轻微更新
- CSS 增强 213 行（.field-guide-section / .field-guide-table / .duration-badge / .reading-sequence / .do-not-add-note 等 14 个新类）
- check-route-seo.py 接受 v1.5.2 / v1.5.3 / v1.5.4
- 首页 + 路线索引页轻量更新
- 不引入地图 API / npm / 构建系统 / 浏览器截图 / 实时交通
- OEDW 事实边界完整保留

## OEDW 深度优化 v1.5.5 (OEDW China Route Deep Optimization) (2026-07-06)

修正 Out of Eden Walk 中国段页面顶部状态显示（10% 规划中 → 85% 可用草案 v0.9），并将 OEDW 中国段从「可执行行程」升级为「深度执行版」。

- 页面状态：完成度 85% · 可用草案 v0.9 · 仍需实地验证（不写 100%）
- 新增 6 个模块：
  - 如何使用这条路线（7/14/28/阅读 4 张卡片）
  - 按时间选择你的 OEDW 中国段（7/14/28 三列）
  - 不同人群怎么走（5 卡片）
  - 28 天每日执行卡（28 张 · Day/过夜/上午/下午/傍晚/最小完成版/可选加点/撤退策略/今日不要硬加点）
  - 住宿区域与交通方式总表（14 区域）
  - 仍需实地验证的部分（5 类）
- OEDW 页面顶部导航锚点更新
- 页面版本号全量更新：v1.4.6 → v1.5.5
- manifest v1.5.5：OEDW data_status_label = 长线文化复刻样板 · OEDW 深度执行版
- check-route-seo.py 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5
- CSS 增强 200+ 行
- 旧文案「本条路线尚在规划中」「本页为规划中路线」已替换
- 不改辽塔页面 / 不改山西页面 / 不改 CSV/GeoJSON/GPX/SVG 坐标
- 不新增地图 API / npm / 构建系统
- OEDW 事实边界完整保留

## OEDW Milestones 中文故事索引 v1.5.6 (OEDW Milestones Chinese Story Index) (2026-07-06)

Out of Eden Walk 中国段 Milestones 74–95 共 22 条已补充中文摘要、路线意义、复刻建议和待验证点；页面从执行版进一步升级为官方叙事节点的中文阅读索引。

- 页面状态：完成度 88% · 可用草案 v0.9 · 中文摘要已完成；剩余 12% 是视觉资料 + 实地核验
- 22 条 milestone 全部补充中文摘要：
  - 编号：74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95
  - 字段：中文摘要 / 路线意义 / 复刻建议 / 不确定点 / 可复刻程度 / 官方链接
  - 5 个可复刻程度分级：易复刻 / 可分段 / 主题 / 避免 / 待核验
- 新增「如何从官方 Milestone 读到旅行路线」4 张说明卡
- 22 条 milestone 编号全部出现在页面（已通过数量校验）
- 不复制官方长文 / 不做全文翻译 / 不伪造 Paul Salopek 原始 GPS
- 顶部「仍需实地验证 · 细节资料」更新：中文摘要已完成，待视觉资料
- OEDW 页面顶部导航锚点新增「故事索引」
- manifest v1.5.6：OEDW data_status_label = 长线文化复刻样板 · Milestones 中文索引版
- check-route-seo.py 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5 / v1.5.6
- CSS 增强 120 行
- 不改辽塔页面 / 不改山西页面 / 不改 CSV/GeoJSON/GPX/SVG 坐标
- 不新增地图 API / npm / 构建系统
- OEDW 事实边界完整保留

## OEDW Dispatch 深度复核与资料对照 v1.5.7 (OEDW Dispatch Deep Review and Source Concordance) (2026-07-06)

Out of Eden Walk 中国段 Milestones 74–95 共 22 条补充官方资料状态、核心主题、关键词、人物/场景/地貌、复刻段落映射和 28 天执行卡映射；页面从 Milestones 中文故事索引版升级为官方 Dispatch 对照解读版。

- 页面状态：完成度 90% · Dispatch 基础复核版
- 22 条 milestone 官方 URL 全部 200（v1.5.7 验证 2026-07-06）
- 22/22 全部建立对照
- 22 条核心主题 + 关键词覆盖（100+ 关键词）
- 22 条人物/场景/地貌字段覆盖
- 22 条复刻段落映射（10 段）
- 22 条 28 天执行卡映射
- 21 条「官方页面已复核」+ 1 条「官方页面可访问」(M91)
- 新增「官方 Dispatch 资料对照表」22 行 × 9 字段
- 新增「如何阅读 Out of Eden Walk 的 Dispatch」5 张卡片
- 新增「从官方故事到复刻路线」4 步流程
- OEDW 页面顶部导航新增「Dispatch」锚点
- 页面版本号全量更新：v1.5.6 → v1.5.7
- manifest v1.5.7：OEDW data_status_label = 长线文化复刻样板 · Dispatch 基础复核版
- check-route-seo.py 接受 v1.5.2/3/4/5/6/7
- CSS 增强 130 行
- 不整段搬运官方正文 / 不做全文翻译 / 不伪造 Paul Salopek 原始 GPS
- 不改辽塔页面 / 不改山西页面 / 不改 CSV/GeoJSON/GPX/SVG 坐标
- 不新增地图 API / npm / 构建系统
- OEDW 事实边界完整保留

# 行旅图谱 · Culture Roadtrip Atlas

> 为自驾、徒步、古建、博物馆与历史地理旅行准备的个人导游手册库

**GitHub Pages**: https://conanxin.github.io/culture-roadtrip-atlas/

---

## 项目定位

「行旅图谱」是一个**个人人文旅行路线库**。

每条路线都按统一框架整理：路线骨架、景点档案、随行导游词、城市与美食、行前书影音、资料来源核对、现场模式、实地复盘。

与旅游攻略不同，行旅图谱追求的不是"打卡清单"，而是**"随行导游"式的沉浸体验**——每到一个地方，你会知道为什么这个地方值得来，它在中国（乃至世界）历史和文化的坐标中处于什么位置，应该怎么看、怎么感受、怎么思考。

技术层面，这是一个**纯静态网站**：HTML + CSS + Vanilla JavaScript，部署于 GitHub Pages。在浏览器原生能力的范围内（localStorage、speechSynthesis）实现尽可能丰富的交互。

---

## 当前版本

**v1.5.8 · OEDW Visual Materials and Bibliography Pack**（2026-07-06）

三条路线详情页已接入统一数据状态徽章、数据摘要、下载入口和相关路线推荐。

路线数据索引现支持多路线搜索、筛选、排序、对比，并通过 `routes-manifest.json` 驱动展示。

路线数据索引现已包含 3 条真实数据路线：Out of Eden Walk 中国段、辽塔巡礼、山西古建。已接入 3 条路线数据资产，包含 **92 个文化复刻粗点、28 个路线段、3 张静态 SVG 路线图**，支持 CSV / GeoJSON / GPX 下载。

v1.5.0（路线索引体验与多路线检索）+ v1.4.9（山西古建路线数据生产）+ v1.4.8（路线工厂自动化与质量门禁）+ v1.4.7（路线模板化与多路线复用）+ v1.4.6（数据驱动页面与静态地图预览）+ v1.4.5（路线数据资产）+ v1.4.3-1.4.4（叙事/发布包装）保留。

v1.5.8 在 v1.5.7 基础上：

- **v1.5.8 · OEDW 视觉资料与参考书目补全**：页面新增视觉资料占位表、参考书目 5 类、出发前核查清单 5 类
- OEDW 页面状态 90% → 92% · 视觉资料与书目准备版
- 新增「视觉资料占位与来源管理」表格（22 行 · Milestone/视觉状态/需要补拍/官方链接）
- 新增「参考书目与延伸阅读」5 类（官方/英文/中文/学术/衍生）
- 新增「出发前核查清单」5 类（证件与手续/健康与安全/交通与时段/开放状态/资料与装备）
- 视觉资料状态：22 条全部「官方图片链接 · 待实拍」（不下载官方图片到仓库）
- OEDW 页面顶部导航新增「视觉/书目/出发前」3 个锚点
- 页面版本号全量更新：v1.5.7 → v1.5.8（hero badge / page-meta × 2 / footer / 状态卡 / 描述 / 风险说明）
- manifest v1.5.8：OEDW data_status_label = 长线文化复刻样板 · 视觉资料与书目准备版
- check-route-seo.py：接受 v1.5.2/3/4/5/6/7/8
- CSS 增强（.oedw-visual-pack / .oedw-visual-table / .oedw-visual-status-* / .oedw-bibliography / .oedw-bibliography-section-* / .oedw-checklist-grid / .oedw-checklist-card / .oedw-source-note 等 16 个新类）
- 不下载 / 不复制 / 不搬运官方图片到仓库
- 不把视觉占位写成已经实拍完成
- 不改辽塔页面 / 不改山西页面 / 不改 CSV/GeoJSON/GPX/SVG 坐标

v1.5.7 在 v1.5.6 基础上：

- **v1.5.7 · OEDW Dispatch 深度复核与资料对照**：Milestones 74–95 共 22 条补充官方资料状态、核心主题、关键词、人物/场景/地貌、复刻段落映射和 28 天执行卡映射
- 22 条 milestone 官方 URL 全部 200（v1.5.7 验证）
- 新增「官方 Dispatch 资料对照表」22 行（9 字段：Milestone/官方标题/官方资料状态/核心主题/人物场景地貌/复刻段落/28天执行卡/复刻提醒/官方链接）
- 新增「如何阅读 Out of Eden Walk 的 Dispatch」5 张卡片
- 新增「从官方故事到复刻路线」4 步流程
- 官方资料状态：21 条「官方页面已复核」+ 1 条「官方页面可访问」(M91)
- OEDW 页面状态 88% → 90% · Dispatch 基础复核版
- OEDW 页面顶部导航新增「Dispatch」锚点
- manifest v1.5.7：OEDW data_status_label = 长线文化复刻样板 · Dispatch 基础复核版
- check-route-seo.py：接受 v1.5.2/3/4/5/6/7
- CSS 增强（.oedw-dispatch-review / .oedw-dispatch-table / .oedw-dispatch-status / .oedw-dispatch-keywords / .oedw-dispatch-method-grid / .oedw-source-concordance / .oedw-source-flow / .oedw-excerpt-note 等 14 个新类）
- 不复制官方长文 / 不做全文翻译 / 不伪造 Paul Salopek 原始 GPS
- 不改辽塔页面 / 不改山西页面 / 不改 CSV/GeoJSON/GPX/SVG 坐标

v1.5.6 在 v1.5.5 基础上：

- **v1.5.6 · Out of Eden Walk 中国段 Milestones 中文故事索引**：Milestones 74–95 共 22 条已补充中文摘要、路线意义、复刻建议和待验证点；新增「如何从官方 Milestone 读到旅行路线」4 张说明卡
- OEDW 页面顶部状态：85% → 88% 可用草案 v0.9
- 新增 Milestones 74–95 中文故事索引（22 张卡片 · 6 字段 · 中文摘要/路线意义/复刻建议/不确定点/可复刻程度/官方链接）
- 新增「如何从官方 Milestone 读到旅行路线」4 张卡片
- 可复刻程度分级：易复刻 / 可分段 / 主题 / 避免 / 待核验
- 更新「仍需实地验证」中"细节资料"清单：中文摘要已完成，待视觉资料
- OEDW 页面顶部导航锚点新增「故事索引」
- manifest v1.5.6：OEDW data_status_label = 长线文化复刻样板 · Milestones 中文索引版
- check-route-seo.py：接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5 / v1.5.6
- CSS 增强（.oedw-milestone-index / .oedw-milestone-grid / .oedw-milestone-card / .oedw-milestone-meta / .oedw-replication-badge / .oedw-official-reading-grid / .oedw-official-reading-card 等 14 个新类）
- 不改辽塔页面 / 不改山西页面 / 不改 CSV/GeoJSON/GPX/SVG 坐标 / 不复制官方长文 / 不引入地图 API
- 所有 22 条 milestone 仅做中文摘要、转述和路线解读，不做全文翻译

v1.5.5 在 v1.5.4 基础上：

- **v1.5.5 · Out of Eden Walk 中国段深度执行版**：OEDW 中国段页面更新为可用草案 v0.9 (85%)，补充 7/14/28 天选择器、28 天每日执行卡、住宿区域与交通方式总表、不同人群版本和仍需实地验证清单
- OEDW 页面顶部状态：10% 规划中 → 85% 可用草案 v0.9
- 新增「如何使用这条路线」4 张卡片（7/14/28/阅读）
- 新增「按时间选择你的 OEDW 中国段」三列选择器
- 新增 28 天每日执行卡（28 张 · 7 字段 · Day/过夜/上午/下午/傍晚/最小完成版/可选加点/撤退策略/今日不要硬加点）
- 新增 住宿区域与交通方式总表（14 区域 · 6 字段）
- 新增 不同人群怎么走（5 卡片：第一次走/摄影者/写作者/亲子家庭/高强度旅行者）
- 新增 仍需实地验证的部分（5 类：实地可达性/住宿交通/开放状态/细节资料/用户反馈）
- OEDW 页面顶部导航锚点更新为：使用/导游词/执行卡/7/14/28/住宿交通/人群/待验证/数据
- manifest v1.5.5：OEDW data_status_label = 长线文化复刻样板 · OEDW 深度执行版
- check-route-seo.py：接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5
- CSS 增强 200+ 行（.oedw-status-updated / .oedw-use-guide / .oedw-use-card / .oedw-execution-section / .oedw-execution-card / .oedw-minimum-box / .oedw-addon-box / .oedw-fallback-box / .oedw-do-not-box / .oedw-audience-grid / .oedw-audience-card / .oedw-transport-table / .oedw-pending-verification / .oedw-pending-card 等 14 个新类）
- 不改辽塔页面 / 不改山西页面 / 不改 CSV/GeoJSON/GPX/SVG 坐标 / 不新增地图 API / 不引入 npm

v1.5.4 在 v1.5.3 基础上：

- **v1.5.4 · 每日导游词、停留时长与读图顺序**：三条路线补充每日导游词、核心点停留时长、拍摄观察建议和古建 / 辽塔读图顺序
- OEDW 新增 28 天每日导游词 + 现场记录模板 + 拍摄记录建议 + 今日不要硬加点
- 辽塔新增 9 天每日导游词 + 核心点停留时长 + 如何读一座辽塔 + 拍摄建议 + 今日不要硬加点
- 山西新增 12 天每日导游词 + 核心古建停留时长 + 如何读一座山西古建 + 拍摄观察建议 + 今日不要硬加点
- manifest v1.5.4：data_status_label / route_summary 轻微更新
- cleanup: 修正上轮 Phase 13 阶段标注误写 + 辽塔「辆牲」错字 → 「牺牲」
- CSS 增强 213 行（.field-guide-section / .field-guide-grid / .field-guide-card / .field-guide-table / .duration-badge / .observation-list / .photo-tip-grid / .photo-tip-card / .reading-sequence / .do-not-add-note 等 14 个新类）

v1.5.3 在 v1.5.2 基础上：

- **v1.5.3 · 三条路线线路优化专项**：OEDW / 辽塔 / 山西古建三条路线补充压缩版 / 标准版 / 深度版与取舍原则，提升现实旅行可执行性
- OEDW 补充 28 天推荐节奏 + 6 条年度短线 + 取舍原则
- 辽塔新增 5 天压缩版 + 9 天优化版 + 12 天深度版 + 取舍原则
- 山西新增 7 天压缩版 + 10–12 天标准版 + 15 天深度版 + 取舍原则
- manifest v1.5.3：data_status_label / route_summary 轻微更新

v1.5.2 在 v1.5.1 基础上：

- **统一三条路线详情页的 `<head>` 模板**：title / description / canonical / og:title / og:description / og:image / og:url / og:type / og:site_name / og:locale / og:image:width / og:image:height / og:image:alt / twitter:card（升级为 `summary_large_image`）/ twitter:title / twitter:description / twitter:image / theme-color
- **新增 OG SVG 生成器** `scripts/render-route-og-svg.py`：从 routes-manifest.json 自动生成 · 支持 `python3 scripts/render-route-og-svg.py` / `--all` / `<slug>` / `--all --check`
- **5 个 OG SVG 资产**（1200×630 · 米白纸张风格 · 含 `<title>` 与 `<desc>`）：
  - `assets/img/og/out-of-eden-walk-china-og.svg` (5,497 字节)
  - `assets/img/og/liao-tower-roadtrip-og.svg` (5,477 字节)
  - `assets/img/og/shanxi-ancient-architecture-og.svg` (5,501 字节)
  - `assets/img/og/site-og.svg` (4,586 字节 · 首页)
  - `assets/img/og/routes-index-og.svg` (5,722 字节 · 路线索引页)
- **首页 + 路线索引页 SEO 补齐**：title / description / canonical / og:* / twitter:* 全套元数据 + 主题色
- **routes-manifest.json v1.5.2**：每条路线增加 9 个 SEO 字段（seo_title / seo_description / canonical_url / og_title / og_description / og_image_url / twitter_title / twitter_description / share_summary）
- **新增 路线页面 SEO 检查脚本** `scripts/check-route-seo.py`：8 大类检查（manifest version · 9 SEO 字段 · og 文件大小 · title/description/canonical/og/twitter 12 类 meta · canonical 一致 · og:image basename 一致 · og_title / share_summary 可读）
- **verify-site.sh 增强**：增加 v1.5.2 检查（1 项 SEO check + 1 项 OG SVG check + 3 项详情页 SEO 完整 + 1 项 routes-index-og 存在性），总门禁 97 → 107
- **GitHub Actions 同步**：`.github/workflows/route-data.yml` 加入 `check-route-seo.py` 与 `render-route-og-svg.py --check` 两个 step
- **路线详情页 share-summary**：每页加 `<p class="route-share-summary sr-only">{share_summary}</p>`，供 SEO 与社交分享使用
- **`build-route-assets.py --all` 不丢字段**：验证 9 个 SEO 字段被保留
- **零依赖**：不引入构建系统 / npm / 外部图像 API / 浏览器截图
- **保留 OEDW 事实边界**：6,000–6,700 公里 / 22/22 milestones / 卢沟桥→天安门→小汤山 / 黄海三层时间 / 文化复刻粗点

v1.5.1 在 v1.5.0 基础上：

- **三条路线详情页统一数据状态徽章**：`assets/js/route-page-badges.js` 从 routes-manifest.json 动态渲染徽章 / 摘要 / 下载 / 数据安全边界 / 相关路线推荐
- **三个面板插入位置**：OEDW / 辽塔 / 山西 详情页在「Hero + 路线总览」之后、「下载路线数据」之前插入 `route-page-data-panel`
- **相关路线推荐**：每页最多推荐 2 条，按 category（+10）/ theme_tags 交集（×3）/ region_tags 交集（×2）/ featured（+1）/ points（÷100）排序
- **新增文档**：[`docs/ROUTE_PAGE_INTEGRATION_GUIDE.md`](./docs/ROUTE_PAGE_INTEGRATION_GUIDE.md) — 面向以后接入第 4 条路线详情页的实操指南
- **新增检查脚本**：`scripts/check-route-page-integration.py` 检查每条有 page_url 的 route：页面存在 / `data-route-slug` 一致 / 容器存在 / 脚本引入 / `data-site-root` 声明 / 数据路线含「路线数据」关键词
- **verify-site.sh 增强**：增加 6 项 v1.5.1 检查（1 项 integration check + 3 项详情页接入 + 2 项文件存在性），总门禁 91 → 97
- **GitHub Actions 同步**：`.github/workflows/route-data.yml` 加入 `check-route-page-integration.py`
- **零依赖**：不引入地图 API / npm 依赖 / 构建系统 / 后端
- **保留 OEDW 事实边界**：6,000–6,700 公里 / 22/22 milestones / 卢沟桥→天安门→小汤山 / 黄海三层时间

v1.5.0 在 v1.4.9 基础上：

- **路线数据索引升级为资产管理页**：`routes/index.html` 引入 manifest 驱动的「路线仪表盘」，支持搜索 / 筛选 / 排序 / 对比 / 统计
- **新增前端脚本** `assets/js/routes-index.js`：纯 Vanilla JS · 无依赖 · 从 `routes-manifest.json` 渲染多路线卡片、对比表、统计区
- **manifest 检索字段增强**：每条路线增加 `category` / `theme_tags` / `region_tags` / `data_status_label` / `difficulty_label` / `best_season` / `route_summary` / `data_completeness` / `featured` 字段
- **首页路线数据资产统计**：新增三张小统计卡（路线 / 点位 / SVG）
- **新增文档**：[`docs/ROUTE_FACTORY_GUIDE.md`](./docs/ROUTE_FACTORY_GUIDE.md) — 面向以后新增第 4 条路线的实操指南
- **路线工厂门禁增强**：`scripts/check-routes-index-sync.py` v1.1 检查 routes-index.js 必填字段 + dashboard 容器 + manifest 引用
- **GitHub Actions 同步**：`.github/workflows/route-data.yml` 加入 `check-routes-index-sync.py` 与 `verify-site.sh`
- **路线数据声明**：3 条路线统一标注 **文化复刻粗点 / 文化自驾粗点 / 非实时导航 / 不保证开放状态**
- **零依赖**：不引入地图 API、不引入 npm、不引入构建系统
- **保留 OEDW 事实边界**：6,000–6,700 公里 / 22/22 milestones / 卢沟桥→天安门→小汤山 / 黄海三层时间



## 路线索引体验（v1.5.0）

行旅图谱路线数据索引升级为「路线资产管理页」：

- **路线仪表盘**（`routes/index.html#dashboard`）：从 `routes-manifest.json` 动态加载 · 路线总数 / 已有数据路线 / 总点位数 / 总段落数 / GeoJSON Feature / SVG 预览实时统计
- **搜索**：搜索 `title` / `route_summary` / `theme_tags` / `region_tags` / `data_status_label`
- **筛选**：分类（长线徒步 / 自驾 / 古建）/ 完整度（full / v0.1 / planned）/ 地区（从 region_tags 自动生成）
- **排序**：推荐 / 点位数从高到低 / 名称
- **路线对比表**：路线 · 分类 · 状态 · 点位 · 段落 · SVG · 最佳季节 · 难度 · 主题
- **无 JS fallback**：保留三条路线硬编码卡片（OEDW / 辽塔 / 山西）+ 路线工厂流程 + 质量门禁
- **fetch 失败 fallback**：提示「路线 manifest 加载失败」，引导使用静态索引

### 路线工厂文档

新增 [`docs/ROUTE_FACTORY_GUIDE.md`](./docs/ROUTE_FACTORY_GUIDE.md)，包括：

1. 新增路线标准流程（10 步）
2. CSV 编写规则（18 字段、枚举、命名规范）
3. 坐标规则（粗点不伪造、不导航）
4. 数据安全边界（文化复刻 / 文化自驾粗点声明）
5. 必跑命令（5 条核心 + verify-site.sh）
6. 常见错误（6 类）
7. 当前三条路线示例（OEDW / 辽塔 / 山西）

## 山西古建路线数据（v1.4.9）

```bash
# 三条路线统一路线工厂命令
python3 scripts/build-route-assets.py --all

# 校验
python3 scripts/validate-route-data.py shanxi-ancient-architecture
python3 scripts/validate-route-data.py --all --manifest-check
python3 scripts/render-route-map-svg.py --all --check
python3 scripts/check-routes-index-sync.py
./verify-site.sh
```

山西古建路线是 v1.4.9 投入的第三条真实数据路线：
- CSV 30 行 / 18 字段 / 9 段 S01-S09
- GeoJSON 30 Point + 10 LineString = 40 features
- GPX 30 waypoint + 1 track
- SVG 7.6 KB / 1200×760
- 类型：cultural_roadtrip / D_reconstructed_for_travel
- 9 段分布：S01 大同云冈 / S02 浑源恒山应县 / S03 五台山早期木构 / S04 太原晋祠 / S05 平遥双林镇国 / S06 介休灵石霍州 / S07 临汾洪洞隰县 / S08 运城永乐解州 / S09 晋东南长治晋城

---

---

## 路线工厂与质量门禁（v1.4.8）

```bash
# 路线工厂 · 构建所有 manifest 路线
python3 scripts/build-route-assets.py --all

# 路线工厂 · CI 校验（不回写）
python3 scripts/build-route-assets.py --check

# 数据校验 + manifest 统计一致
python3 scripts/validate-route-data.py --all --manifest-check

# SVG 检查
python3 scripts/render-route-map-svg.py --all --check

# 索引页同步检查
python3 scripts/check-routes-index-sync.py

# 本地综合门禁
./verify-site.sh
```

GitHub Actions `Route Data Quality Gate` 在 push / PR 时自动运行上述 5 项 + `verify-site.sh`。

---

v1.4.7 在 v1.4.6 基础上：

- 新增通用路线数据规范 `docs/ROUTE_DATA_SPEC.md`
- 新增通用路线页面模板 `docs/ROUTE_PAGE_TEMPLATE.md`
- 新增路线 manifest `data/routes/routes-manifest.json`
- 增强 `validate-route-data.py`：支持任意 slug + `--all` + 路线级别阈值
- 增强 `render-route-map-svg.py`：支持任意 slug + `--all` + 动态 title/desc
- 新增辽塔巡礼路线 CSV / GeoJSON / GPX / SVG（20 粗点、9 段、9 天 8 晚闭环）
- 优化 `route-data-viewer.js`：去除 OEDW 硬编码、通用化 fallback 下载链接
- 增强路线数据索引页：多路线卡片 + 总览统计 + 多路线规范模块
- 优化 `trips-data.js` / `home.js`：trip 卡片支持"已接入路线数据" 标识

v1.4 在 v1.3 基础上：
- 12 个 A 级核心点位导览草稿（云冈石窟 / 华严寺 / 善化寺 / 应县木塔 / 佛光寺 / 南禅寺 / 晋祠 / 镇国寺 / 双林寺 / 小西天 / 玉皇庙 / 青莲寺）
- 5 个 B 级强烈推荐点位简短导览（双塔寺 / 介休后土庙 / 长治观音堂 / 崇庆寺 / 法兴寺）
- 山西古建现场怎么看总导览（6 个观察顺序 + 彩塑壁画特殊提醒）
- 古建观察清单（10 项可勾选，localStorage 保存）
- 山西古建关键词进阶（新增殿堂 / 悬山歇山庑殿 / 减柱造 / 叉手与托脚 / 悬塑 / 水陆画 / 明清修缮 / 国保单位）
- 导览草稿状态说明
- 首页状态：实用信息核验中 → 文化导览草稿中（进度 60% → 70%）
- verify-site.sh 增加 11 项 v1.4 关键词检查（73 → 84 项），全部 PASS
- README / CONTENT_NOTES / CHANGELOG 同步更新

v1.3.0 · Shanxi Practical Fact Audit（2026-07-04）

山西古建自驾线进入"路线校准"阶段：3 种行程版本（11 天主路线 / 8 天压缩版 / 14 天慢行版）、11 天主路线每日分时草案、路线取舍逻辑、点位状态分级、下一步待核验清单。

v1.1.0（研究建档）+ v1.0.0（稳定发布）保留。

v1.1.0 · Shanxi Route Research（2026-07-04）

山西古建自驾线进入"研究建档"阶段：点位分级（A/B/C）、5 段路线研究框架、资料来源索引、10 个核心关键词、2 个初步行程方案。

v1.0.0 · Stable Release（2026-07-04）

### 累计成果（v0.1 → v1.0）

| 版本 | 主题 | 关键模块 |
|------|------|---------|
| v0.1 | 基础框架 | 行程页、景点卡片、导游词、语音朗读、打卡 |
| v0.2 | 内容校准 | 分时日程、替代方案、实用信息、地图链接 |
| v0.3 | 现场使用 | 今日模式、到达前导入、复盘预习、行前学习计划 |
| v0.4 | 知识深化 | 时间轴、五京体系、形制比较、概念图谱、阅读路线 |
| v0.5 | 路线可视化 | 路线示意图、Day 高亮、主题路径、关系网络 |
| v0.6 | 资料与事实核对 | 资料来源索引、核对清单、来源标签、Workflow 升级 |
| v0.7 | 文物图录视觉 | 档案卡、线描示意、城市章节、摘句、故事线 |
| v0.8 | 多路线框架 | 路线库首页、Featured Trip、筛选、方法论、6 条路线 |
| v0.9 | 路线模板与第二路线 | TRIP_TEMPLATE.md、山西古建骨架页 |
| v1.0 | 稳定发布 | 统一版本、SEO、CHANGELOG、verify-site.sh、tag v1.0.0 |
| v1.1 | 山西路线研究建档 | 点位分级 A/B/C、5 段研究框架、资料来源、关键词、初步行程方案 |
| v1.2 | 山西路线校准 | 11天主路线/8天压缩/14天慢行三版本、每日分时草案、路线取舍逻辑、待核验清单 |
| v1.3 | 山西实用信息核验 | 17个点位实用信息卡（开放时间/门票/停车/拍照）、高风险提示、出发前核验面板 |
| v1.4 | 山西文化导览草稿 | 12 A级 + 5 B级点位导览、山西古建现场怎么看、古建观察清单、关键词进阶 |
| v1.4.1 | Out of Eden Walk 中国段 | Paul Salopek 中国段复刻路线，10 分段、Milestone 74-95、3 种复刻版本 |
| v1.4.2 | Phase 2 事实审校与可旅行化 | 事实审校模块、Milestones 表格升级、10 段可旅行化字段、21-28 天精华版日程、6 段短线版、不建议硬走清单 |
| v1.4.3 | Phase 3 叙事导览版 | 如何阅读路线、长卷文字地图、10 段随行导游词、每日主题、6 段短线适合人群、行前资料包、传播摘要 |
| v1.4.4 | Phase 4 发布包装 | 快速阅读目录、阅读进度、返回顶部、移动端表格、SEO/OG/canonical、Twitter Card、本页状态、适合谁使用、代表长线徽章、发布文案 4 版 |
| v1.4.5 | Phase 5 路线数据资产 | CSV 42 点 + GeoJSON + GPX + data/README + 路线数据索引页 routes/、OEDW 下载模块、首页入口 |
| v1.4.6 | Phase 6 数据驱动展示 | validate-route-data.py + render-route-map-svg.py + 静态 SVG 地图 + route-data-viewer.js 数据驱动表 + 4 筛选器 |

---

## 当前路线列表

### ✅ 已上线完整路线（1 条）

| 路线 | 状态 | 进度 | 链接 |
|------|------|------|------|
| 北京出发·辽塔巡礼自驾导游手册 | 已上线 | 100% | [查看](https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/) |

**辽塔巡礼**：9 天 8 晚 · 北京闭环自驾 · 核心主题：辽塔 / 契丹 / 捺钵 / 五京制度

### 🚧 规划中路线（6 条）

| 路线 | 状态 | 进度 | 链接 |
|------|------|------|------|
| 山西古建自驾线 | 规划中 · 文化导览草稿中（v1.4） | 70% | [查看规划](https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/) |
| Out of Eden Walk 中国段复刻路线 | 规划中（v1.4.6 · 页面发布包装完成 + 路线数据资产完成 + 数据驱动展示 + 静态 SVG 地图预览） | 50% | [查看规划](https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/) |
| 北京周边辽金古建线 | 规划中 | 30% | 首页卡片 |
| 河西走廊文化线 | 规划中 | 10% | 首页卡片 |
| 滇越铁路文化线 | 规划中 | 5% | 首页卡片 |
| Via Francigena 徒步线 | 规划中 | 0% | 首页卡片 |

---

## 页面链接

| 页面 | URL |
|------|-----|
| 首页（路线库） | https://conanxin.github.io/culture-roadtrip-atlas/ |
| 路线数据索引 | https://conanxin.github.io/culture-roadtrip-atlas/routes/ |
| 辽塔巡礼（已上线完整路线） | https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/ |
| 山西古建（规划中骨架页） | https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/ |
| Out of Eden Walk 中国段（规划中文化复刻） | https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/ |

---

## 技术栈

- HTML5 + CSS3 + Vanilla JavaScript
- 纯静态网站，无后端、无数据库、无 API Key 依赖
- GitHub Pages 托管（自动部署）
- 浏览器原生功能：localStorage（进度）、speechSynthesis（语音朗读）
- 浏览器原生 SVG（路线示意图、塔形线描）
- 浏览器原生 CSS Grid / Flexbox（响应式布局）

---

## 目录结构

```
culture-roadtrip-atlas/
├── index.html                          # 路线库首页
├── README.md
├── CHANGELOG.md                        # 版本更新日志
├── .github/workflows/pages.yml          # GitHub Pages CI（Node.js 24）
├── trips/
│   ├── liao-tower-roadtrip/             # 已上线完整路线（v0.7）
│   │   ├── index.html
│   │   └── ...
│   └── shanxi-ancient-architecture-roadtrip/  # 规划中骨架页（v0.9-v1.4）
│       └── index.html
│   └── out-of-eden-walk-china/          # 规划中文化复刻路线（v1.4.1-v1.4.2）
│       └── index.html
├── assets/
│   ├── css/styles.css                   # 统一样式（v0.1-v1.0 累计 ~4200 行）
│   └── js/
│       ├── trips-data.js                # 路线库数据（v0.8，含 7 条路线）
│       ├── home.js                      # 首页渲染/筛选（v0.8）
│       ├── liao-tower-data.js           # 辽塔行程数据（v0.1-v0.6）
│       └── app.js                       # 辽塔行程交互（v0.1-v0.7）
├── docs/
│   ├── TRIP_TEMPLATE.md                 # 路线页面模板（v0.9）
│   └── CONTENT_NOTES.md                 # 内容说明
├── reports/                             # 每个版本的报告
│   ├── BUILD_AND_DEPLOY_REPORT.md
│   ├── v0_2_content_route_calibration_report.md
│   ├── ...
│   └── v1_4_shanxi_cultural_guide_lite_report.md
│   └── OUT_OF_EDEN_WALK_CHINA_ROUTE_REPORT.md
└── scripts/
    └── verify-site.sh                   # 网站验证脚本（v1.0）
```

---

## 如何添加新路线

**最小步骤（参考 docs/TRIP_TEMPLATE.md）：**

1. **创建目录和文件**
   - `trips/<route-id>/index.html`

2. **更新首页数据**
   - 编辑 `assets/js/trips-data.js`
   - 添加路线条目，设置 `status: "规划中"`，`progress: <small>`

3. **更新文档**
   - `README.md`：在版本历史增加新条目
   - `docs/CONTENT_NOTES.md`：增加开发进度说明
   - `CHANGELOG.md`：记录版本变更

4. **部署验证**
   - commit + push to main
   - 等待 GitHub Pages 部署
   - 验证 HTTP 200
   - 运行 `./scripts/verify-site.sh`

**参考骨架：** `trips/shanxi-ancient-architecture-roadtrip/index.html`（v0.9 规划中路线）

**参考完整路线：** `trips/liao-tower-roadtrip/index.html`（v1.0 已上线完整路线）

---

## 本地开发

```bash
# 克隆项目
git clone https://github.com/conanxin/culture-roadtrip-atlas.git
cd culture-roadtrip-atlas

# 本地预览（任意静态服务器）
python3 -m http.server 8000
# 访问 http://localhost:8000

# 运行验证脚本
./scripts/verify-site.sh
```

---

## 设计哲学

视觉风格参考文物图录与古代长卷：墨绿 / 米白 / 灰绿 / 暗金的色调，长卷式的排版布局，克制的装饰语言，古朴而不喧嚣的整体气质。每一次阅读，都像是展开一卷泛黄的史料。

---

## Git

- **Repository**: https://github.com/conanxin/culture-roadtrip-atlas
- **Tag**: v1.0.0

---

*行旅图谱 · 让每一次出发都有迹可循*

*Built with static HTML · 2026*
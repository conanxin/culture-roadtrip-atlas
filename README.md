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

**v1.4.8 · Route factory automation and quality gates**（2026-07-05）

行旅图谱现在具备路线内容页面、路线数据资产、静态 SVG 预览、路线 manifest、自动校验脚本、路线工厂构建脚本和 GitHub Actions 质量门禁。

v1.4.7（路线模板化与多路线复用）+ v1.4.6（数据驱动页面与静态地图预览）+ v1.4.5（路线数据资产）+ v1.4.3-1.4.4（叙事/发布包装）保留。

v1.4.8 在 v1.4.7 基础上：

- 新增 `scripts/build-route-assets.py` 路线工厂入口
- 增强 `validate-route-data.py` · `--json` · `--manifest-check`
- 增强 `render-route-map-svg.py` · `--check` 模式
- 新增 `scripts/check-routes-index-sync.py` 减少 manifest/index 漂移
- 增强 `verify-site.sh` 接入路线数据门禁
- 新增 `.github/workflows/route-data.yml` Route Data Quality Gate
- 山西古建路线 manifest 增加 `planned-data` 条目


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
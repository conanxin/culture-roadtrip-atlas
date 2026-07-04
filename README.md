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

**v1.0.0 · Stable Release**（2026-07-04）

首个稳定发布版。统一项目说明、首页展示、路线状态、SEO 基础信息、版本记录、文档结构。

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

---

## 当前路线列表

### ✅ 已上线完整路线（1 条）

| 路线 | 状态 | 进度 | 链接 |
|------|------|------|------|
| 北京出发·辽塔巡礼自驾导游手册 | 已上线 | 100% | [查看](https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/) |

**辽塔巡礼**：9 天 8 晚 · 北京闭环自驾 · 核心主题：辽塔 / 契丹 / 捺钵 / 五京制度

### 🚧 规划中路线（5 条）

| 路线 | 状态 | 进度 | 链接 |
|------|------|------|------|
| 山西古建自驾线 | 规划中（已建骨架页） | 20% | [查看规划](https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/) |
| 北京周边辽金古建线 | 规划中 | 30% | 首页卡片 |
| 河西走廊文化线 | 规划中 | 10% | 首页卡片 |
| 滇越铁路文化线 | 规划中 | 5% | 首页卡片 |
| Via Francigena 徒步线 | 规划中 | 0% | 首页卡片 |

---

## 页面链接

| 页面 | URL |
|------|-----|
| 首页（路线库） | https://conanxin.github.io/culture-roadtrip-atlas/ |
| 辽塔巡礼（已上线完整路线） | https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/ |
| 山西古建（规划中骨架页） | https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/ |

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
│   └── shanxi-ancient-architecture-roadtrip/  # 规划中骨架页（v0.9）
│       └── index.html
├── assets/
│   ├── css/styles.css                   # 统一样式（v0.1-v1.0 累计 ~4200 行）
│   └── js/
│       ├── trips-data.js                # 路线库数据（v0.8）
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
│   └── v1_0_stable_release_report.md
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
# 行旅图谱 · Culture Roadtrip Atlas

> 为自驾、徒步与人文旅行准备的个人导游手册

**GitHub Pages**: https://conanxin.github.io/culture-roadtrip-atlas/


## 版本信息

**当前版本**: v0.5.0 (路线可视化版)

### 版本历史
- **v0.1.0**: 基础框架上线，行程页、景点卡片、导游词、语音朗读、打卡进度
- **v0.2.0**: 内容路线校准，分时日程、替代方案、实用信息（开放时间/停车/地图链接）
- **v0.3.0**: 现场使用版，今日模式、到达前导入、现场怎么看步骤导览、离开前回望、复盘预习、行前学习计划、底部快捷导航
- **v0.4.0**: 知识深化版，辽代时间轴、五京体系、形制比较、核心概念图谱、阅读路线、资料来源、景点之间的关系
- **v0.5.0**: 路线可视化版，路线示意图、Day 高亮、主题路径、景点关系网络、路线阶段、路线总览 Meta

## 项目概述

「行旅图谱」是一个个人人文旅行项目库，收录自驾、徒步、古建、博物馆、历史地理主题路线。每条路线均包含：

- 行程规划与每日时间线
- 景点深度讲解与导游词
- 城市历史与文化背景
- 当地美食推荐
- 行前书影音资料包

## 第一个行程

### 北京出发·辽塔巡礼自驾导游手册

**路线**: 北京 → 锦州 → 义县 → 北镇 → 朝阳 → 赤峰 → 巴林左旗 → 宁城/承德 → 北京

**天数**: 9天8晚

**主题**: 从辽西走廊到契丹草原腹地，一条关于佛塔、捺钵与辽代都城的自驾路线

**核心景点**:
- 奉国寺（辽代木构与佛教造像）
- 万佛堂石窟（东北地区早期石窟）
- 朝阳北塔（五世同堂辽塔）
- 庆州白塔（辽代佛塔艺术巅峰）
- 辽上京遗址（契丹龙兴之地）
- 赤峰辽文化博物馆
- 大明塔（辽中京标志）

**Live Demo**: https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/

## 技术栈

- HTML5 + CSS3 + Vanilla JavaScript
- 纯静态网站，无后端、无数据库、无 API Key 依赖
- GitHub Pages 托管
- 浏览器原生功能：localStorage、speechSynthesis

## 目录结构

```
culture-roadtrip-atlas/
├── index.html                          # 首页
├── README.md
├── .github/workflows/pages.yml          # GitHub Pages CI
├── trips/
│   └── liao-tower-roadtrip/
│       └── index.html                  # 辽塔巡礼行程页
├── assets/
│   ├── css/styles.css                 # 统一样式
│   └── js/
│       ├── app.js                      # 交互逻辑
│       └── liao-tower-data.js          # 行程数据
├── docs/CONTENT_NOTES.md               # 内容说明
└── reports/BUILD_AND_DEPLOY_REPORT.md  # 部署报告
```

## 本地开发

```bash
# 克隆项目
git clone https://github.com/conanxin/culture-roadtrip-atlas.git
cd culture-roadtrip-atlas

# 本地预览（任意静态服务器）
python3 -m http.server 8000
# 访问 http://localhost:8000
```

## 设计哲学

视觉风格参考文物图录与古代长卷，色调以墨绿、米白、灰绿、暗金为主，克制、古朴、不喧嚣。每条路线的讲解追求"随行导游"式的沉浸感，而非旅游攻略式的清单。

---

*行旅图谱 · 让每一次出发都有迹可循*

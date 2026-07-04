# Out of Eden Walk China · Phase 4 Launch Package · 报告

**版本：** v1.4.4
**日期：** 2026-07-04
**任务定位：** Out of Eden Walk 中国段 · 页面体验与发布包装
**工作分支：** main
**基线 commit：** 291b541 (Phase 3 叙事导览版)
**新 commit：** 见下方"git commit hash"

---

## 一、STATUS

**PASS**

---

## 二、Git 信息

- **工作分支：** main
- **基线 commit：** 291b541
- **新 commit：** 见 `git log --oneline -1` 推送后
- **push 目标：** origin/main

---

## 三、修改文件清单

| 文件 | 操作 | 说明 |
|-----|------|------|
| `trips/out-of-eden-walk-china/index.html` | 修改 | 1490 → 1690 行 · 新增 6 大块（head SEO polish / 快速阅读 + 进度条 / 本页状态 + 适合谁 / 发布文案 4 版 / 表格 mobile-scroll 包裹 / back-to-top + JS）|
| `assets/css/styles.css` | 追加 | 6434 → 6765 行 · 新增 v1.4.4 样式约 230 行（reading-progress / quick-read-nav / page-status-card / audience-grid / mobile-scroll-table / scroll-hint / back-to-top / launch-copy-grid / featured-route-badge + 移动端响应式）|
| `assets/js/trips-data.js` | 修改 | OEDW entry 更新：progress 10 → 50，状态字段更新文案，新增 isLongRoute + longRouteBadge 字段 |
| `assets/js/home.js` | 修改 | 卡片渲染新增 `trip-card-long` 类与 `featured-route-badge` 徽章 |
| `README.md` | 修改 | 版本表新增 v1.4.4 行 · OEDW 进度 30% → 50% · 描述加发布包装 |
| `CHANGELOG.md` | 修改 | 顶部新增 v1.4.4 章节 |
| `docs/CONTENT_NOTES.md` | 修改 | 追加 Phase 4 章节 |
| `reports/OUT_OF_EDEN_WALK_CHINA_PHASE4_LAUNCH_REPORT.md` | 新增 | 本报告 |

---

## 四、页面体验增强清单

| 模块 | 说明 | 实现方式 |
|------|------|---------|
| 快速阅读目录 | 10 个锚点按钮（事实审校 / 长卷地图 / 分段路线 / Milestones / 随行导游词 / 21-28 天精华版 / 六段短线 / 行前资料包 / 传播摘要 / 来源资料）| 纯 HTML 锚点 + CSS grid |
| 阅读进度条 | 顶部 3px 渐变细线，滚动百分比更新宽度 | Vanilla JS + requestAnimationFrame 节流 |
| 返回顶部按钮 | 滚动 600px 后淡入显示，点击平滑滚动顶部 | Vanilla JS + CSS opacity/visibility transition |
| 移动端长表格 | Milestones 表格 + 21-28 天精华版表格外层包裹 `.mobile-scroll-table` | CSS overflow-x: auto + scroll-hint |
| 本页状态卡片 | v1.4.4 / 50% / 已交付 / 仍待完善 4 项 | CSS grid 2 列布局 |
| 适合谁使用 | 4 类适合 + 4 类不适合（卡片式布局）| CSS grid 2 列布局 + 颜色区分 |

---

## 五、移动端优化清单

| 项目 | 优化前 | 优化后 |
|------|-------|-------|
| 快速阅读目录 | 无 | 移动端横向滚动 |
| 进度条 | 无 | 3px 顶部细线 |
| 返回顶部按钮 | 无 | 缩小到 40×40，right/bottom 16px |
| Milestones 表格 | 表格溢出 | mobile-scroll-table + 左右滑动提示 |
| 21-28 天精华版 | 表格溢出 | mobile-scroll-table + 左右滑动提示 |
| 本页状态卡 | 2 列 | 移动端单列 |
| 适合谁使用 | 2 列 | 移动端单列 |

---

## 六、首页推荐位修改说明

### 数据文件 (assets/js/trips-data.js)
```js
{
    id: 'out-of-eden-walk-china',
    oneLine: '从滇西边境到大连黄海，沿 Paul Salopek 的慢新闻足迹，穿越茶马古道、蜀道、黄土高原、北京城市空间、长城与东北海岸。',
    status: '50% · 事实审校 + 可旅行化 + 叙事导览 + 发布包装',
    tags: [..., '代表长线'],
    progress: 50,        // 从 10 改为 50
    isLongRoute: true,
    longRouteBadge: '代表长线 · 已完成 Phase 4'
}
```

### 渲染逻辑 (assets/js/home.js)
```js
// 卡片类：trip-card + trip-card-featured (if isFeatured) + trip-card-long (if isLongRoute)
// 徽章：isFeatured 显示 "⭐ Featured Trip"，isLongRoute 显示 "代表长线 · 已完成 Phase 4"
```

### 视觉效果
- 卡片左边框 3px 暗金色（trip-card-long 类）
- 顶部渐变徽章（featured-route-badge 类）
- 进度条宽度 50%

---

## 七、SEO / OG / Canonical 修改说明

### title
- 优化前：`Out of Eden Walk 中国段复刻路线 · 行旅图谱`
- 优化后：`Out of Eden Walk 中国段复刻路线｜Paul Salopek 国家地理慢新闻路线 · 行旅图谱`

### meta description
- 优化前：原始 description 较长（>200 字符）
- 优化后：精炼到 120–160 中文字符范围：`Paul Salopek 与国家地理 Out of Eden Walk 中国段复刻路线：从滇西边境到大连黄海，穿越茶马古道、蜀道、黄土高原、北京、长城与东北海岸，含事实审校、可旅行化方案与随行导游词。`

### canonical
```html
<link rel="canonical" href="https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/">
```

### Open Graph 增强
- og:title 已存在（保留）
- og:description 优化
- og:url 已存在（保留）
- og:type = article（保留）
- og:site_name = 行旅图谱 · Culture Roadtrip Atlas（新增）
- og:locale = zh_CN（新增）

### Twitter Card
```html
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Out of Eden Walk 中国段复刻路线 · 行旅图谱">
<meta name="twitter:description" content="从滇西边境到大连黄海，重建 Paul Salopek 国家地理慢新闻中国段路线。">
```

无图片，不硬编 og:image。

---

## 八、发布文案模块说明

新增模块位置：`#launch-copy`（在 `#share-summary` 之后、`#sources` 之前）

| 块 | 字数 | 用途 |
|---|------|------|
| 朋友圈版 | 100–180 字 | 朋友圈 / 微博 / 状态 |
| 小红书版 | 标题（5 字）+ 正文 200–300 字 + 9 个标签 | 小红书 / Instagram |
| 公众号导语版 | 400–600 字 | 公众号 / 长微博 / 视频简介 |
| README 简介版 | 120–200 字 | GitHub README / 项目介绍 |

均不使用营销词（无"震撼""封神""史诗"），核心信息一致：约 6,000–6,700 公里、两年多、22 个 milestone、从滇西到黄海、慢新闻、文化复刻。

---

## 九、链接抽检结果

### 内链（HTTP 200）
| URL | 状态 |
|-----|------|
| http://127.0.0.1:8000/ | 200 |
| http://127.0.0.1:8000/trips/out-of-eden-walk-china/ | 200 |
| http://127.0.0.1:8000/trips/liao-tower-roadtrip/ | 200 |
| http://127.0.0.1:8000/trips/shanxi-ancient-architecture-roadtrip/ | 200 |
| http://127.0.0.1:8000/assets/css/styles.css | 200 |

### 外链（8 个关键链接抽检）
| URL | HTTP | 备注 |
|-----|------|------|
| https://outofedenwalk.nationalgeographic.org/ | 200 | 官方首页 |
| https://outofedenwalk.nationalgeographic.org/2024-08-goodbye-china/ | 200 | 中国段总结 |
| https://outofedenwalk.nationalgeographic.org/2024-07-new-map-ancient-roads-china/ | 200 | 古道地图 |
| https://outofedenwalk.nationalgeographic.org/2024-04-walking-map-mazes-beijing/ | 200 | 北京迷宫步行地图 |
| https://outofedenwalk.nationalgeographic.org/2024-04-rediscovering-chinas-capital-foot/ | 200 | 重新发现北京 |
| https://outofedenwalk.nationalgeographic.org/2024-02-meeting-dawn-human/ | 200 | 田园洞 |
| https://outofedenwalk.nationalgeographic.org/2024-06-qing-roads/ | 200 | 清代道路 |
| https://outofedenwalk.nationalgeographic.org/2024-07-milestone-91-im-satisfied-man/ | 200 | Milestone 91 |

**全部 8 个外链 HTTP 200 通过。**

---

## 十、事实边界验证结果

| 事实点 | 状态 | 结果 |
|-------|------|------|
| "跨越六年" | ✅ 清除 | grep 无 result（reports 仅作验证标记）|
| "22/23" | ✅ 清除 | grep 无 result |
| Milestones 74–95 = 22/22 | ✅ 保留 | HTML + CONTENT_NOTES 共 2 处命中 |
| 6,000–6,700 公里 | ✅ 保留 | HTML 10 处命中 |
| 卢沟桥 → 天安门 → 小汤山 | ✅ 保留 | 卢沟桥 11 处、小汤山 11 处 |
| 黄海三层时间（2023 冬 / 2024.6 / 2024.8）| ✅ 保留 | HTML 12 处命中 |

---

## 十一、验证结果汇总

### 本地 HTTP
- `/` → 200
- `/trips/out-of-eden-walk-china/` → 200
- `/trips/liao-tower-roadtrip/` → 200
- `/trips/shanxi-ancient-architecture-roadtrip/` → 200
- `/assets/css/styles.css` → 200

### verify-site.sh
- **STATUS: PASS** (70 通过 / 0 失败)

### GitHub Pages
- 推送后等待 30s，HTTP/2 200

### 线上 HTTP 200
- `https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/` → 200

### 外链抽检
- 8 个关键链接全部 200

---

## 十二、Phase 5 建议（不在本轮范围）

1. **视觉资料补充**
   - 实地走访照片（每段 2-3 张）
   - 路线线描图（手绘风）
   - SVG 海报版（朋友圈传播用）

2. **交互增强**
   - 复制按钮（一键复制发布文案）
   - 分享按钮（Web Share API）
   - 收藏到本地（localStorage）

3. **内容深化**
   - 英文版（与 Paul 报道双向引用）
   - 6 段短线的更详细分时日程
   - 与纪录片《永远的行走：与中国相遇》具体集数对应

4. **架构升级**
   - 路线库整体优化（其他 6 条路线也补足阅读体验）
   - 首页新增"完成度"过滤维度
   - 加入 PWA 基础（manifest.json）

5. **可访问性**
   - 键盘导航完整支持
   - 屏幕阅读器友好
   - 高对比度模式

---

_辛 🔮 · 2026-07-04 · Out of Eden Walk China Phase 4 Launch Package_
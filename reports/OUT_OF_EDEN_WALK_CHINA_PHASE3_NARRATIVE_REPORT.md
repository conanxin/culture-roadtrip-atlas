# Out of Eden Walk China · Phase 3 Narrative Guide · 报告

**版本：** v1.4.3
**日期：** 2026-07-04
**任务定位：** Out of Eden Walk 中国段 · 叙事化导览增强
**工作分支：** main
**主提交：** 见下方"git commit hash"

---

## 一、目标与边界

### 目标
将现有 Phase 2 "事实审校 + 可旅行化"页面升级为"随行导游式长卷页面"。

### 重要边界（严格执行）
- ✅ 不重新做架构
- ✅ 不引入后端 / 数据库 / 地图 API / 构建系统
- ✅ 不破坏已有路线（辽塔巡礼、山西古建）
- ✅ 不回退 Phase 2 事实边界

---

## 二、新增模块清单（7 个）

| 编号 | 模块 | 内容要点 | 风格 |
|-----|------|---------|------|
| 1 | 如何阅读这条路线 | 4 张卡片：不是挑战 / 地理剖面 / 慢新闻 / 分年完成 | 卡片式 |
| 2 | 中国段长卷地图 | 12 个节点：滇西边境 → 黄海港口 | 长卷式 + CSS 竖线 |
| 3 | 10 段随行导游词 | 每段 300–500 字 + 现场观察 | 沉静式 |
| 4 | 21–28 天每日主题 | 9 个区段每日主题（D1–D28） | 表格新增列 |
| 5 | 6 段短线适合人群 | 适合人群 / 季节 / 方式 / 主题 / 不适合 | 字段增强 |
| 6 | 行前资料包 | 5 类资料（A 必读 / B 主题 / C 观看 / D 准备 / E 记录模板） | 卡片式 |
| 7 | 传播摘要 | 30 秒 / 3 分钟 / 讲解员三版 | 卡片式 |

---

## 三、关键事实边界验证

| 事实点 | 状态 | 验证命令 |
|-------|------|---------|
| "跨越六年" 是否清除 | ✅ 清除 | `grep -R "跨越六年"` 无结果 |
| "22/23" 是否清除 | ✅ 清除 | `grep -R "22/23"` 无结果 |
| "22/22" 是否保留 | ✅ 保留 | `grep -R "22/22"` 命中 |
| "6,000–6,700" 是否保留 | ✅ 保留 | `grep -R "6,000–6,700"` 命中 |
| 北京段三节点（卢沟桥→天安门→小汤山） | ✅ 保留 | `grep -R "卢沟桥\|小汤山"` 命中 |
| 黄海终点三层时间（2023 冬 / 2024.6 / 2024.8） | ✅ 保留 | 多处可见 |
| Milestone 91 URL 200 | ✅ 保留 | 表格中标注 |

---

## 四、新增关键词检查

| 关键词 | 状态 |
|-------|------|
| 如何阅读这条路线 | ✅ |
| 中国段长卷地图 | ✅ |
| 随行导游词 | ✅ |
| 现场观察 | ✅ |
| 行前资料包 | ✅ |
| 传播摘要 | ✅ |
| 每日主题 | ✅ |
| 适合人群 | ✅ |

---

## 五、修改文件清单

| 文件 | 操作 | 说明 |
|-----|------|------|
| `trips/out-of-eden-walk-china/index.html` | 修改 | 1099 → 1490 行 · 新增 7 个模块 · 表格列增强 · 6 段短线字段增强 · 顶部导航精简 · 版本号 v1.4.2 → v1.4.3 |
| `assets/css/styles.css` | 追加 | 6064 → 6434 行 · 新增 v1.4.3 样式（reading-guide / scroll-map / narrative-guide / prep-pack / share-summary / daily-theme + 移动端响应式）|
| `README.md` | 修改 | 版本表新增 v1.4.3 行 · OEDW 进度 10% → 30% |
| `CHANGELOG.md` | 修改 | 顶部新增 v1.4.3 章节 |
| `docs/CONTENT_NOTES.md` | 修改 | 追加 Phase 3 章节 |
| `reports/OUT_OF_EDEN_WALK_CHINA_PHASE3_NARRATIVE_REPORT.md` | 新增 | 本报告 |

---

## 六、技术决策

### 6.1 不调用地图 API
中国段长卷地图使用纯 CSS 竖线 + 节点卡片实现，**不依赖任何外部地图服务**。
- 优势：纯静态、零依赖、长期可维护、GitHub Pages 友好
- 实现：`.scroll-map::before` 绝对定位竖线，`.scroll-map-marker` 圆形节点

### 6.2 不引入构建系统
所有内容直接写入 HTML，无 Webpack / Vite / Rollup 依赖。

### 6.3 表格移动端处理
`@media (max-width: 768px)` 中将 `.travel-version-table` 转为 `overflow-x: auto`，实现横向滚动。每日主题列在窄屏保持可读。

### 6.4 顶部导航精简
Phase 2 导航 8 项 → Phase 3 导航 9 项（增加 阅读 / 长卷 / 导游词 / 资料包 / 传播，移除 时间线 / 里程碑 / 故事 / 资料）。原 8 项模块仍存在，导航仅展示高频入口。

---

## 七、验证步骤

### 7.1 本地 HTTP
```bash
python3 -m http.server 8000 &
sleep 2
curl -I http://127.0.0.1:8000/                          # /
curl -I http://127.0.0.1:8000/trips/out-of-eden-walk-china/  # 新页面
curl -I http://127.0.0.1:8000/trips/liao-tower-roadtrip/    # 不破坏
```

### 7.2 关键词验证
```bash
grep -R "如何阅读这条路线" -n trips/out-of-eden-walk-china
grep -R "中国段长卷地图" -n trips/out-of-eden-walk-china
grep -R "随行导游词" -n trips/out-of-eden-walk-china
grep -R "现场观察" -n trips/out-of-eden-walk-china
grep -R "行前资料包" -n trips/out-of-eden-walk-china
grep -R "传播摘要" -n trips/out-of-eden-walk-china
grep -R "跨越六年" -n trips/out-of-eden-walk-china README.md docs reports   # 应为空
grep -R "22/23" -n trips/out-of-eden-walk-china README.md docs reports       # 应为空
grep -R "22/22" -n trips/out-of-eden-walk-china README.md docs reports       # 应命中
grep -R "6,000–6,700" -n trips/out-of-eden-walk-china                        # 应命中
grep -R "卢沟桥" -n trips/out-of-eden-walk-china                             # 应命中
grep -R "小汤山" -n trips/out-of-eden-walk-china                             # 应命中
```

### 7.3 部署后验证
```bash
curl -I https://conanxin.github.io/culture-roadtrip-atlas/
curl -I https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/
curl -I https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/
```

---

## 八、commit 信息

```
Enhance Out of Eden Walk China narrative guide (v1.4.3)
```

---

## 九、下一步（不在本轮范围）

- 实地走访验证（任何一段）
- 视觉资料（点位照片 / 线描图）
- 多语言版本（英文导游词）
- 与纪录片《永远的行走：与中国相遇》具体集数对应
- 6 段短线的更详细分时日程

---

_辛 🔮 · 2026-07-04 · Out of Eden Walk China Phase 3 Narrative Guide_
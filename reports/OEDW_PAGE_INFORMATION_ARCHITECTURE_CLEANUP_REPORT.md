# OEDW 页面信息架构整理 v1.5.11 · 报告

- **STATUS**: COMPLETE
- **工作分支**: `main`
- **基线 commit**: `e6bf867` (OEDW Trust Risk Reader Entry Audit 主交付) · `f8454c9` (报告回填)
- **新 commit**: 见 git log（主交付 + 报告回填）
- **push 是否成功**: ✅ origin/main 已推送
- **部署状态**: GitHub Pages Deploy（见 gh run list）

## 1. 本轮目标

v1.5.11 把 OEDW 页面从「可信度与风险审计版」升级为「结构化阅读版」：

1. 新增「页面阅读地图」5 大区。
2. 新增「三条核心阅读路径」（10 / 30 / 90 分钟）。
3. 新增「页面太长怎么办」4 类读者建议。
4. 核心 / 行程 / 资料 / 风险 / 数据 / 附录 6 类模块标识。
5. 9 个长资料模块改为原生 `<details>` 折叠。
6. 精简顶部快速导航为 10 个 pill。
7. 保持 93% 完成度（不强行升到 95% 或 100%）。

## 2. 修改文件列表

- `trips/out-of-eden-walk-china/index.html`（M · +800 行）
- `assets/css/styles.css`（M · +130 行）
- `data/routes/routes-manifest.json`（M）
- `README.md`（M）
- `CHANGELOG.md`（M）
- `docs/CONTENT_NOTES.md`（M）
- `scripts/check-route-seo.py`（M）
- `reports/OEDW_PAGE_INFORMATION_ARCHITECTURE_CLEANUP_REPORT.md`（A）

## 3. 页面阅读地图（5 大区）

| # | 大区 | 适合 |
|---|------|------|
| 1 | 核心 · 先理解这条路线 | 第一次打开页面 |
| 2 | 行程 · 想实际走一段 | 准备旅行 / 行程规划 |
| 3 | 资料 · 想读官方故事 | 研究 OEDW 官方叙事 |
| 4 | 资料 · 想拍摄 / 写作 | 摄影 / 写作 / 实地观察 |
| 5 | 数据 · 想下载和复用 | 数据复用 / 地图制作 |

## 4. 三条核心阅读路径

| 路径 | 时长 | 读者 |
|------|------|------|
| 10 分钟快速了解 | 10 min | 第一次打开 |
| 30 分钟做旅行判断 | 30 min | 准备实际出发 |
| 90 分钟做研究阅读 | 90 min | 把页面当资料库 |

## 5. quick nav 精简

从 13 个入口 → 10 个 pill：

- 状态 · 阅读地图 · 官方故事 · 28 天执行卡 · 参考书目 · 视觉资料 · 出发前核查 · 风险 · 下载数据 · FAQ

## 6. 折叠模块清单

| 模块 | 状态 | id |
|------|------|-----|
| 你应该从哪里开始 | 默认展开 | oedw-reader-entry |
| 本路线多维完成状态 | 默认展开 | oedw-status-matrix |
| 不建议普通旅行者逐点复刻的场景 | 默认展开 | oedw-risk-audit |
| 常见问题 FAQ | 默认展开 | oedw-faq |
| Milestones 74–95 中文故事索引 | 默认折叠 | oedw-milestone-index |
| 官方 Dispatch 资料对照表 | 默认折叠 | oedw-dispatch-concordance |
| Milestone 视觉资料矩阵 | 默认折叠 | oedw-visual-materials |
| 22 条 Milestone 补图清单 | 默认折叠 | oedw-shot-list |
| 参考书目与资料入口 | 默认折叠 | oedw-bibliography |
| 出发前核查清单 | 默认折叠 | oedw-pre-departure |
| 28 天每日导游词 | 默认折叠 | oedw-28day-narration |
| 28 天每日执行卡 | 默认折叠 | oedw-execution-cards |
| 住宿区域与交通方式总表 | 默认折叠 | oedw-transport |

总计 13 个折叠模块（4 默认展开 + 9 默认折叠）。

## 7. 默认展开 / 默认折叠策略

**默认展开（核心入口）：**
- 让读者第一次打开页面就能看到关键判断（读者入口 / 多维状态 / 不建议复刻场景 / FAQ）。

**默认折叠（长资料）：**
- 把 22 条长表格（Milestones / Dispatch / 视觉资料矩阵 / 补图清单 / 28 天执行卡 / 28 天导游词 / 住宿交通总表 / 参考书目 / 出发前核查清单）放入折叠，避免一次性滚动太长。

## 8. 模块类型标识

6 类 badge：

- `core`（核心）· `itinerary`（行程）· `source`（资料）· `risk`（风险）· `data`（数据）· `appendix`（附录）

应用到 ~25 个主要模块的标题前缀。

## 9. 页面太长怎么办

4 类读者建议：

1. 10 分钟快速了解（先读阅读地图 / 状态 / 审校 / 7-14-28 / FAQ）
2. 30 分钟做旅行判断（行程 + 风险 + 交通）
3. 90 分钟做研究阅读（Milestones + Dispatch + 参考书目）
4. 实地拍摄（导游词 + 视觉资料 + 补图清单）

## 10. 状态更新

- **原状态**: 93% · 可信度与风险审计版
- **新状态**: 93% · 结构化阅读版
- **完成度**: 93%（保持，不强行升到 95% 或 100%）
- **仍需验证**: 13 项（实地走访 / 视觉授权 / 开放状态 / 交通现实 / 中文参考书目原著 / 等）

## 11. 是否修改数据文件

❌ 未修改 CSV / GeoJSON / GPX / SVG 坐标。

## 12. manifest 更新

- `version`: v1.5.10 → **v1.5.11**
- `updated_at`: 2026-07-06 → **2026-07-07**
- OEDW `data_status_label`: 长线文化复刻样板 · 可信度与风险审计版 → **长线文化复刻样板 · 结构化阅读版**
- OEDW `route_summary`: 增加「页面阅读地图 / 三条核心阅读路径 / 折叠式资料模块 / 模块类型标识 / 精简导航」
- 其他路线（辽塔 / 山西）人工字段未改动
- 9/9 SEO 字段保留

## 13. 事实边界验证

| 检查项 | 状态 |
|--------|------|
| 跨越六年 | ✅ clean |
| 22/23 | ✅ clean |
| 22/22 | ✅ 10+ 处保留 |
| 6,000–6,700 | ✅ 11 处保留 |
| 10% | ✅ 完全清除（FAQ 之外） |
| 100% | ✅ 仅 FAQ 第 9 条作解释 |
| 90% | ✅ 完全清除 |
| 92% | ✅ 完全清除 |
| 93% | ✅ 保持 |
| 规划中 | ✅ 仅 HTML 注释 |

## 14. 质量门禁验证

| 检查 | 结果 |
|------|------|
| build-route-assets --all | ✅ PASS |
| build-route-assets --check | ✅ PASS |
| validate-route-data --all --manifest-check | ✅ PASS |
| render-route-map-svg --all --check | ✅ PASS |
| check-routes-index-sync | ✅ PASS |
| check-route-page-integration | ✅ PASS |
| render-route-og-svg --all --check | ✅ PASS |
| check-route-seo | ✅ PASS（v1.5.11 accepted） |
| verify-site.sh | ✅ PASS（108/108） |

## 15. 线上 HTTP 200

| 路径 | 状态 |
|------|------|
| `/` | ✅ 200 |
| `/routes/` | ✅ 200 |
| `/trips/out-of-eden-walk-china/` | ✅ 200 |
| `/reports/OEDW_PAGE_INFORMATION_ARCHITECTURE_CLEANUP_REPORT.md` | ✅ 200 |

## 16. 下一步 OEDW 优化建议

1. 落实 7/14/28 天选择器与折叠模块的视觉一致性
2. 继续补全中文参考书目原著获取
3. 真实图片实拍 / 授权补图（不下载官方图片）
4. 后续 v1.5.12 视真实使用反馈再决定（不预先承诺）

---

_报告路径：reports/OEDW_PAGE_INFORMATION_ARCHITECTURE_CLEANUP_REPORT.md_
_生成时间：2026-07-07_
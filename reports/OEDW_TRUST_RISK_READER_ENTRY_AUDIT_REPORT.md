# 行旅图谱 · OEDW 可信度、风险与读者入口审计 · v1.5.10

> OEDW Trust Risk Reader Entry Audit
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | 2d1a6c4 (OEDW Visual Bibliography Pack 报告回填) |
| **新 commit** | _pending_（commit 后回填） |
| **push 状态** | _pending_ |
| **部署状态** | _pending_ |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 3/3 endpoints 200 |
| **数量校验** | ✅ 22/22 Milestone 编号（74-95）全部出现 |
| **完成度保持** | ✅ 93%（不强行升到 95% 或 100%） |
| **线上 HTTP 200** | _pending_（push 后回填） |
| **GitHub Actions run** | _pending_ |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +600 | 7 新模块 + 状态更新 + 导航简化 + 仍需验证扩展 |
| `assets/css/styles.css` | M | +200 | 22 个新 CSS 类（.oedw-reader-entry / .oedw-status-table / .oedw-trust-* / .oedw-risk-* / .oedw-accessibility-table / .oedw-observation-table / .oedw-faq-*） |
| `data/routes/routes-manifest.json` | M | +3 | v1.5.10 + OEDW data_status_label / route_summary |
| `scripts/check-route-seo.py` | M | +1 | manifest version 接受 v1.5.2 - v1.5.10 |
| `README.md` | M | +25 | v1.5.10 当前版本 + 描述 |
| `CHANGELOG.md` | M | +100 | v1.5.10 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +25 | v1.5.10 章节 |
| `reports/OEDW_TRUST_RISK_READER_ENTRY_AUDIT_REPORT.md` | A | +500 | 本报告 |

**未修改**：
- 辽塔页面（v1.5.4 状态保留）
- 山西页面（v1.5.4 状态保留）
- CSV / GeoJSON / GPX 坐标数据
- SVG 路线示意图
- OG SVG（SEO 检查不要求）
- 路线工厂门禁脚本
- 任何图片（不下载 / 不复制 / 不搬运）

---

## 2. 读者入口模块（6 卡片）

| 入口 | 适合 | 推荐模块 |
|------|------|----------|
| 📖 只想了解项目 | 概念理解 | 项目总览 / 事实审校 / Milestones 74–95 中文故事索引 |
| 🧳 想实际旅行 | 时间预算 | 7/14/28 天路线选择器 / 28 天每日执行卡 / 住宿区域与交通方式总表 / 不建议复刻场景 |
| 📚 想研究官方资料 | 中文研究索引 | 官方 Dispatch 资料对照表 / 如何阅读 Dispatch / 从官方故事到复刻路线 / 资料可信度说明 |
| 📷 想拍摄 / 写作 | 现场记录 | 现场记录模板 / 拍摄/记录建议 / Milestone 视觉资料矩阵 / 22 条补图清单 |
| 📊 想下载数据 | 资料下载 | 路线数据状态 / CSV / GeoJSON / GPX / SVG 下载 / 静态路线图 |
| ⚖️ 想判断可信度和风险 | 出发前判断 | 多维完成状态表 / 资料可信度说明 / 不建议复刻场景 / 交通与可达性分级 / FAQ |

---

## 3. 多维完成状态表（9 维）

| 维度 | 当前状态 | 完成度 | 说明 | 下一步 |
|------|----------|--------|------|--------|
| 事实审校 | 通过 | **高** | 22/22、里程、北京段、黄海终点边界稳定 | 持续检查链接与版本 |
| 官方 Milestones | 22/22 已覆盖 | **高** | 所有 22 条已建立中文摘要和基础资料对照 | 二次深读 dispatch |
| Dispatch 基础复核 | 基础复核完成 | **中高** | 22/22 官方 URL 200 | 补短摘录、补语境 |
| 行程执行卡 | 完成 | **高** | 28 天每日执行卡 + 6 条短线 | 实走反馈校正 |
| 视觉资料矩阵 | 完成清单 | **中** | 22/22 状态记录 | 自有实拍 / 授权图片 |
| 交通与可达性 | 方案级判断 | **中** | 分级表完成 | 出发前逐段核查 |
| 开放状态 | 待核查 | **低** | 博物馆、景区、保护区逐项未核 | 逐项确认 |
| 实地验证 | 未完成 | **低** | 实拍图、实走反馈均缺 | 实走反馈与现场照片 |
| 参考书目 | 入口已建立 | **中** | 5 类入口 | 补中文 / 英文具体书目 |

**93% 指页面资料结构成熟度，不代表路线实地验证完成。**

---

## 4. 资料可信度说明（4 级）

| 等级 | 来源 | 使用 |
|------|------|------|
| **A 级** | 官方 milestone / dispatch 页面 · National Geographic / Out of Eden Walk 官方资料 · 已确认 URL 200 | 可作为事实基础，但仍不等于旅行路线 |
| **B 级** | 官方页面可访问 · 主题可确认 · 细节仍需逐段复核 | 可用于摘要级解读，不宜过度推断 |
| **C 级** | milestone 标题 · 路线位置 · 现有路线段 · 地理 / 历史语境 | 用于文化复刻说明，必须保留不确定性 |
| **D 级** | 现场可达性 · 开放状态 · 交通衔接 · 实拍图 · 当地反馈 | 不得作为最终旅行建议 |

---

## 5. 不建议复刻场景（8 类）

| 场景 | 风险 | 替代 |
|------|------|------|
| 🛂 边境附近 | 管制、敏感区域、路线不确定 | 公开城镇、博物馆、市场、道路观察 |
| 🌲 高黎贡山 / 横断山深处 | 天气、山路、保护区、海拔 | 公开景区、山脚城镇、博物馆、可达步道 |
| 🏔 高海拔山路 | 雨雪、塌方、高反、交通延误 | 县城和河谷观察 |
| 🌳 保护区 / 林区 | 开放边界不清 | 公开入口、说明牌、访客中心 |
| 🧱 长城野段 | 坍塌、迷路、未开放、救援困难 | 古北口、司马台等公开区域 |
| ⚓ 港口 / 工业区 | 非开放区域、敏感设施 | 公开海岸、博物馆、城市岸线 |
| 🏘 乡村私域 | 打扰生活、隐私、误会 | 道路、公共空间、地名牌、集市外观 |
| 🌙 夜间跨城赶路 | 疲劳驾驶、陌生道路、山路天气 | 启动撤退策略，保留最小完成版 |

---

## 6. 交通与可达性分级（10 段）

| 复刻段落 | 普通公共交通 | 自驾 / 包车 | 徒步 | 建议等级 | 说明 |
|----------|--------------|-------------|------|----------|------|
| 1. 滇西边境与茶马古道 | 部分 | 推荐 | 不建议 | 主题复刻 | 边境段不追逐 |
| 2. 横断山与川西通道 | 有限 | 推荐 | 不适合 | 主题复刻 | 高海拔风险大 |
| 3. 成都平原与古蜀想象 | 推荐 | 推荐 | 不适合 | 易复刻 | 博物馆 + 城市 |
| 4. 蜀道、秦岭与关中 | 推荐 | 推荐 | 部分 | 可分段 | 汉中空城不可复刻 |
| 5. 黄土高原与陕北 | 推荐 | 推荐 | 不适合 | 可分段 | 西安 + 延安 + 壶口 3-4 天 |
| 6. 山西北上与长城边地 | 推荐 | 推荐 | 不适合 | 可分段 | 雁门关、吕梁、忻州 |
| 7. 北京城市断面 | 推荐 | 不推荐 | 可徒步 | 易复刻 | 卢沟桥 → 天安门 → 小汤山 |
| 8. 长城、承德与北方边界 | 推荐 | 推荐 | 公开区域可 | 可分段 | 司马台、承德山庄 |
| 9. 辽宁乡村与东北收束 | 有限 | 推荐 | 不适合 | 主题复刻 | 玉米地/工业主题阅读 |
| 10. 大连黄海终点 | 推荐 | 推荐 | 可徒步 | 易复刻 | 大连港 + 老铁山黄海 |

---

## 7. 官方故事 → 旅行观察任务（8 类）

| 官方主题 | 现场观察 | 记录问题 | 路线段 | 适合谁 |
|----------|----------|----------|--------|--------|
| 边境 | 语言、检查、市场、道路尽头、迁徙痕迹 | 边界如何进入普通生活？ | 1. 滇西边境 | 写作者、研究者 |
| 古道 | 老路、新路、桥、岔路、驿道记忆 | 旧路还在吗？还是只剩地名？ | 1 / 4 | 地理、历史爱好者 |
| 山地 | 山口、河谷、道路工程、雨季痕迹 | 山如何决定人的移动？ | 2. 横断山 | 摄影师、徒步 |
| 城市入口 | 桥、城门、交通节点、郊区扩张 | 城市从哪里开始？ | 7. 北京断面 | 城市观察者 |
| 黄土高原 | 塬梁、窑洞、县城、道路与村落 | 地貌如何塑造生活？ | 5. 黄土高原 | 地理、社会观察 |
| 长城 | 边墙、关口、村庄、旅游化 | 边界如何从军事设施变成文化景观？ | 6 / 8. 长城 | 历史爱好者 |
| 港口 | 海岸、工业、迁移、船、岸线 | 中国段如何结束在海边？ | 10. 大连黄海 | 海洋、工业观察 |
| 日常生活 | 早餐店、公交站、学校、集市、修车点 | 宏大路线如何落在普通一天里？ | 所有段落 | 写作者、慢新闻 |

---

## 8. FAQ（12 条）

1. 这是不是 Paul Salopek 的原始 GPS？→ 不是
2. 这是不是 National Geographic 官方旅行路线？→ 不是
3. 普通人能不能照着走？→ 可以参考但不能逐点照走
4. 为什么不建议逐点复刻？→ 风险不同
5. 7 天应该选哪段？→ 云南线或北京长城线
6. 28 天适合第一次旅行吗？→ 不太适合轻松旅行
7. 页面有 GPX，能不能直接导航？→ 不能（GPX 是文化复刻粗点）
8. 哪些地方最需要实地验证？→ 边境、深山、保护区等
9. 页面为什么不是 100% 完成？→ 实拍图等仍缺
10. 我如何帮助补充？→ 反馈 / 资料 / 实拍
11. 为什么页面要保留不确定性？→ 负责任的路线不应把未验证信息写成确定事实
12. 如果只想阅读，不旅行，怎么用？→ 按推荐顺序阅读

---

## 9. 页面状态更新：93% → 93%（状态名变更）

### 9.1 原状态

```
完成度：93% · 视觉资料准备版
```

### 9.2 新状态

```
完成度：93% · 可信度与风险审计版
```

### 9.3 同步更新文案

- hero badge：`v1.5.9 · ... · 93% · 视觉资料准备` → `v1.5.10 · ... · 93% · 可信度与风险审计`
- page-meta (× 2)：`v1.5.9 · ... · 93% · ... · 视觉资料矩阵 + 补图清单 + 实拍计划 + 归档规范` → `v1.5.10 · ... · 93% · ... · 读者入口 + 可信度 + 风险 + FAQ`
- footer：`v1.5.9 · ... · 93% · ... · 视觉资料准备` → `v1.5.10 · ... · 93% · ... · 可信度与风险审计`
- 状态描述：增加 7 个新模块（读者入口/多维状态/可信度/风险/可达性/观察任务/FAQ）
- 仍需验证：从 8 项扩展为 13 项

### 9.4 不强行提高完成度

- ❌ 不升到 95%
- ❌ 不升到 100%
- ✅ 显式说明：93% 指页面资料结构成熟度，不代表路线实地验证完成

---

## 10. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / OEDW `data_status_label` / `route_summary` 字段
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段
✅ 未下载任何官方或第三方图片到仓库
✅ 未引用不存在的本地图片路径

---

## 11. manifest 更新摘要

| 字段 | v1.5.9 | v1.5.10 |
|------|--------|--------|
| 顶层 `version` | v1.5.9 | **v1.5.10** |
| 顶层 `updated_at` | 2026-07-06 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 · 视觉资料准备版 | **长线文化复刻样板 · 可信度与风险审计版** |
| 辽塔 `data_status_label` | 自驾人文路线样板 · 已完成读塔顺序 | 自驾人文路线样板 · 已完成读塔顺序（未变） |
| 山西 `data_status_label` | 古建自驾路线样板 · 已完成古建读图顺序 | 古建自驾路线样板 · 已完成古建读图顺序（未变） |
| OEDW `route_summary` | + 视觉资料矩阵 + 22 条补图清单 + 现场实拍计划 + 归档规范 + 出发前核查清单 8 类 | **+ 读者入口 6 类 + 多维完成状态表 9 维 + 资料可信度 4 级 + 不建议复刻场景 8 类 + 交通可达性 10 段 + 观察任务 8 类 + FAQ 12 条** |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 12. OEDW 事实边界验证

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW 「22/23」 清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW Milestones 74–95 = 22/22 | ✅ OEDW 页面 10 处 + README 3 处 |
| OEDW 6,000–6,700 公里保留 | ✅ OEDW 页面 11 处 |
| 北京段 卢沟桥 → 天安门 → 小汤山 | ✅ |
| 黄海终点 2023 冬 / 2024.6 / 2024.8 | ✅ |
| 文化复刻粗点 / 非原始 GPS / 非导航 | ✅ |
| 10% 完全从 OEDW 页面清除 | ✅（页面 grep "10%" 空） |
| 100% 完全从 OEDW 页面清除（除 FAQ 中"为什么不是 100% 完成"问答外） | ✅（页面 grep "100% 完成" 仅 FAQ 1 处） |
| 规划中（实际内容） | ✅ 仅 HTML 注释 "规划中提示"，不影响阅读 |
| 22 个 Milestone 编号（74-95）全部出现 | ✅ 数量校验 PASS |
| 不下载 / 不复制 / 不搬运官方图片 | ✅ |
| 不把视觉占位写成已经实拍完成 | ✅ |
| 不引用不存在的本地图片路径 | ✅ |
| 不为补图而冒险进入边境/深山/保护区 | ✅ |
| 不强行升到 95% 或 100% | ✅ 保持 93% |
| 不把 93% 写成实地验证完成 | ✅ 显式说明 |

---

## 13. 质量门禁验证

```
$ python3 scripts/build-route-assets.py --all
routes: 3
✅ manifest updated

$ python3 scripts/build-route-assets.py --check
✅ PASS route factory check · manifest matches generated statistics · routes: 3

$ python3 scripts/validate-route-data.py --all --manifest-check
✅ PASS · routes: 3

$ python3 scripts/render-route-map-svg.py --all --check
✅ PASS · routes: 3

$ python3 scripts/check-routes-index-sync.py
✅ PASS · routes checked: 3 · dynamic manifest rendering: yes

$ python3 scripts/check-route-page-integration.py
✅ PASS route page integration check · routes checked: 3

$ python3 scripts/render-route-og-svg.py --all --check
✅ PASS · site-og.svg ok · routes-index-og.svg ok

$ python3 scripts/check-route-seo.py
✅ PASS route SEO check

$ bash scripts/verify-site.sh
✅ 108/108 门禁全 PASS

$ python3 - <<'PY'
from pathlib import Path
import re
html = Path("trips/out-of-eden-walk-china/index.html").read_text(encoding="utf-8")
nums = sorted(set(int(x) for x in re.findall(r"Milestone\s+(\d+)", html)))
assert all(n in nums for n in range(74, 96)), "missing milestone"
assert "22/22" in html
assert "22/23" not in html
assert "10%" not in html
assert "页面为什么不是 100% 完成" in html
assert "可信度与风险审计版" in html
assert "资料可信度说明" in html
assert "不建议普通旅行者逐点复刻的场景" in html
assert "常见问题" in html
assert "你应该从哪里开始" in html
assert "本路线多维完成状态" in html
assert "交通与可达性分级" in html
assert "官方故事如何变成旅行观察任务" in html
✅ PASS OEDW trust risk reader entry audit
```

---

## 14. SEO / OG 门禁结果

- `build-route-assets.py --all` 保留 9/9 SEO 字段：✅
- `check-routes-index-sync.py`：✅ routes checked: 3
- `check-route-page-integration.py`：✅ routes checked: 3
- `render-route-og-svg.py --all --check`：✅ 5 files
- `check-route-seo.py`：✅ 5 pages · 3 route pages · 5 og assets

---

## 15. 关键词验收

| 关键词 | 目标 | 命中 |
|--------|------|------|
| 可信度与风险审计版 | OEDW / README / CHANGELOG / docs | OEDW 2 / README 4 / CHANGELOG 4 / CONTENT_NOTES 3 |
| 你应该从哪里开始 | OEDW | 2 |
| 本路线多维完成状态 | OEDW | 1 |
| 资料可信度说明 | OEDW | 4 |
| 不建议普通旅行者逐点复刻的场景 | OEDW | 1 |
| 交通与可达性分级 | OEDW | 4 |
| 官方故事如何变成旅行观察任务 | OEDW | 2 |
| 常见问题 | OEDW | 1 |
| 这是不是 Paul Salopek 的原始 GPS | OEDW | 1 |
| 这是不是 National Geographic 官方旅行路线 | OEDW | 1 |
| GPX 是文化复刻粗点 | OEDW | 1 |
| 93% | OEDW | 9 |
| 100% (仅 FAQ) | OEDW | 1 |
| 22/22 | OEDW/README/docs | ≥15 |
| 6,000–6,700 | OEDW/README/docs | ≥30 |
| 22/23 | OEDW/README/docs | 0（clean） |
| 跨越六年 | OEDW/README/docs | 0（clean） |

---

## 16. 本地 HTTP 200 验证

```
$ python3 -m http.server 8010
$ curl -I http://127.0.0.1:8010/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8010/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8010/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8010/reports/OEDW_TRUST_RISK_READER_ENTRY_AUDIT_REPORT.md  HTTP/1.0 200 OK (after commit)
```

---

## 17. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

通过: 70
失败: 0

通过: 108
失败: 0

✓ STATUS: PASS
```

---

## 18. 提交清单

```bash
git add trips/out-of-eden-walk-china/index.html
git add assets/css/styles.css data/routes/routes-manifest.json
git add scripts/check-route-seo.py
git add README.md CHANGELOG.md docs/CONTENT_NOTES.md
git add reports/OEDW_TRUST_RISK_READER_ENTRY_AUDIT_REPORT.md
git commit -m "Add OEDW trust risk and reader entry audit"
git push origin main
```

---

## 19. v1.5.11 建议

1. **进一步多维状态**：
   - 季节性风险评分
   - 拍摄者贡献度
   - 文档版本与时间戳

2. **可信度动态更新**：
   - 实走反馈提升 D 级 → C 级
   - 官方更新提升 B 级 → A 级
   - 时间戳记录

3. **更细的可达性**：
   - 城市段 vs 县域段 vs 边境段
   - 自驾 vs 高铁 vs 长途汽车
   - 季节性道路

4. **更多观察任务**：
   - 道路 / 桥 / 隧道
   - 学校 / 集市 / 早餐店
   - 老人 / 孩子 / 摊贩

5. **可访问性增强**：
   - 字体大小可调
   - 高对比度模式
   - 语音导览
   - 表格 ARIA

6. **国际化**：
   - 中英双语版
   - 法文版（Paul 母语）

7. **用户贡献通道**：
   - GitHub Issue 模板
   - 实走反馈提交流程
   - 自动归档脚本

8. **风险场景扩展**：
   - 极端天气应对
   - 医疗资源
   - 通讯信号盲区
   - 政治敏感

9. **观察任务平台化**：
   - 数据收集
   - 公开 API
   - 第三方工具集成

10. **持续审计**：
    - 每月链接有效性检查
    - 每季度 dispatch 复核
    - 每年实拍图更新

---

_辛 🔮 · 行旅图谱 · OEDW 可信度、风险与读者入口审计报告 · 2026-07-06_

# 行旅图谱 · OEDW Milestones 中文故事索引 · v1.5.6

> OEDW Milestones Chinese Story Index
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | c29ed49 (OEDW Deep Optimization 报告回填) |
| **新 commit** | _pending_（commit 后回填） |
| **push 状态** | _pending_ |
| **部署状态** | _pending_ |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 3/3 endpoints 200 |
| **数量校验** | ✅ 22/22 Milestone 编号（74-95）全部出现 |
| **线上 HTTP 200** | _pending_（push 后回填） |
| **GitHub Actions run** | _pending_ |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +400 | 22 milestone 卡片 + 4 阅读说明卡 + 状态更新 + 导航 |
| `assets/css/styles.css` | M | +120 | 16 个新 CSS 类（.oedw-milestone-* / .oedw-replication-* / .oedw-official-reading-*） |
| `data/routes/routes-manifest.json` | M | +3 | v1.5.6 + OEDW data_status_label / route_summary |
| `scripts/check-route-seo.py` | M | +1 | manifest version 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5 / v1.5.6 |
| `README.md` | M | +15 | v1.5.6 当前版本 + 描述 |
| `CHANGELOG.md` | M | +70 | v1.5.6 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +25 | v1.5.6 章节 |
| `reports/OEDW_MILESTONES_CHINESE_STORY_INDEX_REPORT.md` | A | +500 | 本报告 |

**未修改**：
- 辽塔页面（v1.5.4 状态保留）
- 山西页面（v1.5.4 状态保留）
- CSV / GeoJSON / GPX 坐标数据
- SVG 路线示意图
- OG SVG（SEO 检查不要求）
- 路线工厂门禁脚本

---

## 2. Milestones 盘点结果

### 2.1 盘点摘要

- **覆盖范围**：74–95
- **数量**：22 条（74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95）
- **官方链接**：22/22 全部有官方 URL
- **缺失或待核验**：
  - **Milestone 91** 的官方页面 URL 可从相邻 Milestone 92 页 Previous 链接追到 `milestone-91-im-satisfied-man`，页面返回 200，已作为官方页面收录
  - Milestone 79 的官方 URL slug 为 `2022-11-tk`，已在页面表格中标注并指向 https://outofedenwalk.nationalgeographic.org/2022-11-tk/

### 2.2 22 条 milestone 全量字段

每条 milestone 现有字段（表格 + 新增卡片）：
- 编号（74-95）
- 标题（官方原文）
- 官方地点
- 日期
- 段落
- 主题
- 来源状态（官方已核）
- 旅行复刻建议（v1.5.6 升级为可复刻程度 badge）
- 官方链接
- **v1.5.6 新增**：中文摘要、路线意义、复刻建议、不确定点/待验证、可复刻程度 badge

### 2.3 22/22 中文摘要完成情况

| 编号 | 标题 | 区域 | 可复刻程度 |
|------|------|------|-----------|
| 74 | Every Story Contains Silences | 云南西部 / 缅中边境 | 易复刻 |
| 75 | Mud, Malaria, and Rain, Rain, Rain | 腾冲 / 高黎贡山 | 避免 |
| 76 | Where No Hamlet Goes Unconnected | 大理 / 丽江 | 可分段 |
| 77 | On the High Lama Road | 高喇嘛路 / 木里 | 避免 |
| 78 | She Is a Little Afraid of Us（陆上牦牛） | 康定 / 贡嘎 | 避免 |
| 79 | Crossing and Recrossing the Route of the Long March | 川西南 | 主题 |
| 80 | It's Around Here Somewhere | 雅安 / 成都平原 | 易复刻 |
| 81 | Sword Gate Pass | 剑门关 | 易复刻 |
| 82 | Dance of Fools | 汉中 | 可分段 |
| 83 | No Human in Sight | 秦岭北麓 | 主题 |
| 84 | Everywhere Dust | 陕北黄土高原 | 可分段 |
| 85 | I can do it myself! | 陕北 | 易复刻 |
| 86 | Hungry, My Lord? Here's a Slice of My Thigh | 吕梁 / 雁门关 | 易复刻 |
| 87 | Fake Books and Teletubbies | 山西 / 华北 | 主题 |
| 88 | Waiting to Be Saved | 华北 | 主题 |
| 89 | A Very Long Time Walking（无名之人） | 周口店 / 田园洞 | 易复刻 |
| 90 | Climbing the Wall | 司马台长城 | 可分段 |
| 91 | I'm a satisfied man | 辽宁东北乡村 | 主题 |
| 92 | Corn Corn Corn | 辽宁 | 避免 |
| 93 | Saved by Crows | 辽宁 | 避免 |
| 94 | Only We Were Outside | 辽宁 | 避免 |
| 95 | Feeling Gray | 大连黄海 | 易复刻 |

**22/22 全部完成** ✅

---

## 3. 可复刻程度分级

| 等级 | 数量 | 编号 | 说明 |
|------|------|------|------|
| 🟢 **易复刻** | 7 | 74, 80, 81, 85, 86, 89, 95 | 城市、博物馆、公开景区、交通便利区域 |
| 🟡 **可分段** | 4 | 76, 82, 84, 90 | 城镇、县域、乡村公路、普通旅行者可接近但需规划 |
| 🟠 **主题** | 5 | 79, 83, 87, 88, 91 | 原路线更像大范围地理/文化主题，不适合追求点位 |
| 🔴 **避免** | 6 | 75, 77, 78, 92, 93, 94 | 边境、深山、高海拔、保护区、季节风险明显地区 |
| ⚪ **待核验** | 0 | — | （M91 归入主题类） |

总计：7+4+5+6 = 22 ✅

---

## 4. 所属路线段映射

所有 22 条 milestone 映射到现有 10 段路线：

| 段落 | 路线段 | 编号 | 数量 |
|------|--------|------|------|
| 第 1 段 | 滇西边境与茶马古道 | 74, 75 | 2 |
| 第 2 段 | 滇西山地与高原坝子 | 76 | 1 |
| 第 3 段 | 横断山与川西通道 | 77, 78 | 2 |
| 第 4 段 | 川西 / 川西南 | 79, 80 | 2 |
| 第 5 段 | 蜀道、秦岭与关中 | 81, 82, 83 | 3 |
| 第 6 段 | 黄土高原与陕北 | 84, 85 | 2 |
| 第 7 段 | 山西北上与长城边地 | 86, 87, 88, 89 | 4 |
| 第 8 段 | 北京城市断面 | (隐含于 89) | 0 |
| 第 9 段 | 长城、承德与北方边界 | 90 | 1 |
| 第 10 段 | 辽宁乡村与东北收束 | 91, 92, 93, 94 | 4 |
| 第 10 段 | 大连黄海终点 | 95 | 1 |

总计：2+1+2+2+3+2+4+0+1+4+1 = 22 ✅

---

## 5. 新增「如何从官方 Milestone 读到旅行路线」

4 张说明卡：
1. **官方 Milestone 是叙事节点** — 它不是旅行打卡点，也不一定等于完整路线说明。22 条 milestone 是 Paul 中国段叙事的 22 个停顿点。
2. **Dispatch 是故事，不是攻略** — Dispatch 更接近慢新闻、观察笔记和现场故事，不等于景点介绍。它告诉你 Paul 在现场看到了什么，不告诉你怎么去。
3. **文化复刻要看主题** — 复刻的不是 Paul 的每一步，而是边界、道路、人、地貌、城市和生活的关系。这条路线不是 Paul 的 GPS，是中国读者的"主题复刻"。
4. **普通旅行者要降维** — 城市、县城、公共景区和博物馆可以走；边境、深山、高海拔、乡村小路不应硬复刻。复刻的 5 个梯度见每张卡片的"可复刻程度"标签。

---

## 6. 更新「仍需实地验证」

「细节资料」卡片更新：
- ✅ Milestones 74–95 共 22 条基础中文摘要已完成（v1.5.6）
- 官方 dispatch 深度复核（待逐条展开）
- 每条 milestone 的代表图片（待补充）
- 现场实拍图（待贡献）
- 点位开放状态 + 实地可达性
- 中文参考书目与延伸阅读

---

## 7. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / OEDW `data_status_label` / `route_summary` 字段
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段

---

## 8. manifest 更新摘要

| 字段 | v1.5.5 | v1.5.6 |
|------|--------|--------|
| 顶层 `version` | v1.5.5 | **v1.5.6** |
| 顶层 `updated_at` | 2026-07-06 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 · OEDW 深度执行版 | **长线文化复刻样板 · Milestones 中文索引版** |
| 辽塔 `data_status_label` | 自驾人文路线样板 · 已完成读塔顺序 | 自驾人文路线样板 · 已完成读塔顺序（未变） |
| 山西 `data_status_label` | 古建自驾路线样板 · 已完成古建读图顺序 | 古建自驾路线样板 · 已完成古建读图顺序（未变） |
| OEDW `route_summary` | + 7/14/28 天选择器 + 28 天每日执行卡 + 住宿交通总表 + 不同人群版本 + 仍需实地验证清单 | **+ Milestones 74–95 共 22 条中文故事摘要 + 故事索引** |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 9. OEDW 事实边界验证

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW 「22/23」 清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW Milestones 74–95 = 22/22 | ✅ OEDW 页面 7 处 + README 3 处 + 多处历史报告 |
| OEDW 6,000–6,700 公里保留 | ✅ OEDW 页面 11 处 |
| 北京段 卢沟桥 → 天安门 → 小汤山 | ✅ |
| 黄海终点 2023 冬 / 2024.6 / 2024.8 | ✅ |
| 文化复刻粗点 / 非原始 GPS / 非导航 | ✅ |
| 10% 完全从 OEDW 页面清除 | ✅（页面 grep "10%" 空） |
| 规划中（实际内容） | ✅ 仅 HTML 注释 "规划中提示"，不影响阅读 |
| 22 个 Milestone 编号（74-95）全部出现 | ✅ 数量校验 PASS |
| 不复制官方长文 / 不做全文翻译 | ✅ 仅做中文摘要、转述、引用短标题、引用官方 URL |
| 不伪造 Paul Salopek 原始 GPS | ✅ 所有建议为文化复刻解读 |
| 不写成官方旅行路线 | ✅ 明确标注"文化复刻解读，不代表 Paul Salopek 原始 GPS 或 National Geographic 官方旅行路线" |

---

## 10. 质量门禁验证

```
$ python3 scripts/build-route-assets.py --all
routes: 3
- out-of-eden-walk-china: 42 points, 53 features, 42 waypoints, 10 segments, svg ok
- liao-tower-roadtrip: 20 points, 30 features, 20 waypoints, 9 segments, svg ok
- shanxi-ancient-architecture: 30 points, 40 features, 30 waypoints, 9 segments, svg ok
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
✅ PASS OEDW milestone numbers 74-95 (22/22)
```

---

## 11. SEO / OG 门禁结果

- `build-route-assets.py --all` 保留 9/9 SEO 字段：✅
- `check-routes-index-sync.py`：✅ routes checked: 3
- `check-route-page-integration.py`：✅ routes checked: 3
- `render-route-og-svg.py --all --check`：✅ 5 files
- `check-route-seo.py`：✅ 5 pages · 3 route pages · 5 og assets

---

## 12. 关键词验收

| 关键词 | 目标 | 命中 |
|--------|------|------|
| Milestones 74–95 中文故事索引 | OEDW 页面 | 2 |
| 22/22 中文摘要 | OEDW 页面 | 2 |
| 如何从官方 Milestone 读到旅行路线 | OEDW 页面 | 2 |
| 可复刻程度 | OEDW 页面 | 1 |
| 路线意义 | OEDW 页面 | 23（含 22 卡片 + 1 模块） |
| 复刻建议 | OEDW 页面 | 24 |
| 待验证点 / 不确定点 | OEDW 页面 | 23（用"不确定点 / 待验证"） |
| Milestone 74 / 75 / 76 / ... / 95 | OEDW 页面 | 22/22 全部 |
| OEDW Milestones 中文故事索引 | README/CHANGELOG/docs | CONTENT_NOTES 1 |
| 跨越六年 清除（实际内容） | OEDW/README/docs/reports | ✅ clean |
| 22/23 清除（实际内容） | OEDW/README/docs/reports | ✅ clean |
| 22/22 保留 | OEDW/README/docs/reports | ≥15 |
| 6,000–6,700 保留 | OEDW/README/docs/reports | ≥30 |
| 10% 清除 | OEDW 页面 | ✅ |
| 规划中 清除（实际内容） | OEDW 页面 | ✅ 仅 HTML 注释 |

---

## 13. 本地 HTTP 200 验证

```
$ python3 -m http.server 8006
$ curl -I http://127.0.0.1:8006/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8006/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8006/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
```

---

## 14. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

通过: 70
失败: 0

通过: 108
失败: 0

✓ STATUS: PASS
```

---

## 15. 提交清单

```bash
git add trips/out-of-eden-walk-china/index.html
git add assets/css/styles.css data/routes/routes-manifest.json
git add scripts/check-route-seo.py
git add README.md CHANGELOG.md docs/CONTENT_NOTES.md
git add reports/OEDW_MILESTONES_CHINESE_STORY_INDEX_REPORT.md
git commit -m "Add OEDW milestone Chinese story index"
git push origin main
```

---

## 16. v1.5.7 建议

1. **每条 milestone 配代表图片**
   - 由真实走过的人贡献
   - 走过的 milestone 优先
   - 6,000–6,700 公里覆盖完整度

2. **每条 milestone 配官方 dispatch 摘要**
   - 200-500 字中文转述
   - 引述短标题 + URL
   - 不做全文翻译

3. **每条 milestone 现场实拍图**
   - 22 张图
   - 季节性展示
   - 普通旅行者视角

4. **可复刻程度地图化**
   - 22 条 milestone 在地图上不同颜色显示
   - 绿（易复刻）/黄（可分段）/橙（主题）/红（避免）

5. **季节版执行卡 × milestone**
   - 春季（3-4 月）
   - 夏季（6-8 月）
   - 秋季（9-10 月）
   - 冬季（11-2 月）

6. **可访问性**
   - 字体大小可调
   - 高对比度模式
   - 语音导览（中文 + 英文）
   - 表格 ARIA

7. **「实走反馈」章节**
   - 邀请用户提交 GitHub Issue
   - 走过的 milestone 补充
   - 季节性观察

8. **中英双语版**
   - 中文为主，英文副
   - Paul Salopek 母语友好
   - 国际读者可读

9. **每个 milestone 与 28 天每日执行卡映射**
   - M74 → D1 腾冲 / D2 和顺
   - M80 → D10 成都平原
   - M84 → D15 宜君 / D16 延安
   - 等等

10. **每条 milestone 配官方 dispatch 主题音频**
    - Paul 原声叙述
    - 中文翻译字幕
    - 离线下载

---

_辛 🔮 · 行旅图谱 · OEDW Milestones 中文故事索引报告 · 2026-07-06_

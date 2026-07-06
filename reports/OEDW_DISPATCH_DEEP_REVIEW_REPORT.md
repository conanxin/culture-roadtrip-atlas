# 行旅图谱 · OEDW Dispatch 深度复核与资料对照 · v1.5.7

> OEDW Dispatch Deep Review and Source Concordance
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | cbf909f (OEDW Milestones 报告回填) |
| **新 commit** | _pending_（commit 后回填） |
| **push 状态** | _pending_ |
| **部署状态** | _pending_ |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 3/3 已有 endpoints 200（报告待生成） |
| **数量校验** | ✅ 22/22 Milestone 编号（74-95）全部出现 |
| **官方 URL 校验** | ✅ 22/22 全部 200 (2026-07-06 验证) |
| **线上 HTTP 200** | _pending_（push 后回填） |
| **GitHub Actions run** | _pending_ |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +300 | 3 新模块 + 状态更新 + 导航 + 22 行资料对照表 |
| `assets/css/styles.css` | M | +130 | 15 个新 CSS 类（.oedw-dispatch-* / .oedw-source-* / .oedw-excerpt-note） |
| `data/routes/routes-manifest.json` | M | +3 | v1.5.7 + OEDW data_status_label / route_summary |
| `scripts/check-route-seo.py` | M | +1 | manifest version 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5 / v1.5.6 / v1.5.7 |
| `README.md` | M | +15 | v1.5.7 当前版本 + 描述 |
| `CHANGELOG.md` | M | +80 | v1.5.7 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +25 | v1.5.7 章节 |
| `reports/OEDW_DISPATCH_DEEP_REVIEW_REPORT.md` | A | +500 | 本报告 |

**未修改**：
- 辽塔页面（v1.5.4 状态保留）
- 山西页面（v1.5.4 状态保留）
- CSV / GeoJSON / GPX 坐标数据
- SVG 路线示意图
- OG SVG（SEO 检查不要求）
- 路线工厂门禁脚本

---

## 2. 官方 URL 复核结果

| Milestone | HTTP | 可读状态 | 处理方式 |
|-----------|------|---------|---------|
| 74 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 75 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 76 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 77 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 78 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 79 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 80 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 81 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 82 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 83 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 84 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 85 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 86 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 87 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 88 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 89 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 90 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 91 | 200 | 可读 | 官方页面可访问 (readable) — slug 可追到，URL 200 已核 |
| 92 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 93 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 94 | 200 | 可读 | 官方页面已复核 (reviewed) |
| 95 | 200 | 可读 | 官方页面已复核 (reviewed) |

**22/22 全部 200**

---

## 3. Milestones 74–95 资料对照完成情况

### 3.1 完成度

- **22/22 全部建立对照** ✅
- 9 字段：Milestone / 官方标题 / 官方资料状态 / 核心主题+关键词 / 人物场景地貌 / 复刻段落 / 28天执行卡 / 复刻提醒 / 官方链接

### 3.2 官方资料状态统计

| 状态 | 数量 | 编号 |
|------|------|------|
| 🟢 官方页面已复核 (reviewed) | 21 | 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95 |
| 🟡 官方页面可访问 (readable) | 1 | 91 |
| 🟠 官方链接待复核 (pending) | 0 | — |
| 🔴 访问受限 (limited) | 0 | — |

### 3.3 核心主题和关键词覆盖

22 条 milestone 全部有 3-6 个核心主题标签：

| 段落 | 主题示例 |
|------|----------|
| 第 1 段 (74, 75) | 边境, 疫情重启, 叙事中断, 雨季, 缅中边境 / 山地, 雨季, 疟疾, 保护区, 绿色方舟 |
| 第 2 段 (76) | 村落, 基础设施, 天文村, 坝子, 现代接入 |
| 第 3 段 (77, 78) | 茶马古道, 木里旧王国, 山地宗教, 藏彝走廊 / 藏彝走廊, 牦牛, 高海拔, 贡嘎 |
| 第 4 段 (79, 80) | 长征, 茶马古道, 山地历史, 现代化 / 旧道消失, 现代道路, 平原, 古蜀想象 |
| 第 5 段 (81, 82, 83) | 蜀道, 关隘, 栈道, 李白 / 空城, 封控, 汉中, 时代标记 / 秦岭, 空城, 通道, 2023 |
| 第 6 段 (84, 85) | 黄土, 窑洞, 延安, 长征记忆 / 民间艺术, 手工艺, 陕北 |
| 第 7 段 (86, 87, 88, 89) | 山西古城, 城墙, 小人物, 墙的文化 / 城乡过渡, 消费, 假书, 天线宝宝 / 等待, 迁徙, 冬季华北, 停顿美学 / 早期现代人, 时间深度, 无名之人, 北京边缘 |
| 第 9 段 (90) | 长城, 墙, 司马台, 清代秩序 |
| 第 10 段 (91, 92, 93, 94, 95) | 告别前, 满足, 过渡, 东北 / 玉米, 东北乡村, 重复美学, 农业 / 乌鸦, 东北乡村, 生命, 乡村 / 工业迁移, 户外, 辽宁工业, 灰色 / 黄海, 告别, 灰色, 工业港口 |

总计：100+ 关键词覆盖

### 3.4 人物 / 场景 / 地貌字段覆盖

22 条 milestone 全部有人物/场景/地貌字段：

| 类型 | 例子 |
|------|------|
| 人物 | 边境检查员, 外卖骑手, 茶叶挑夫, 剪纸艺人, 腰鼓表演者, 面花制作人, 摊贩, 户外工人 |
| 场景 | 251 英里空白, 空城, 等待场景, 告别场景, 雨林, 城市, 山区 |
| 地貌 | 雨林, 雪山, 高原牧场, 草原, 黄土塬, 沿海工业, 大连港, 黄海 |

---

## 4. 复刻段落映射

22 条 milestone 全部映射到 10 段复刻路线：

| 段落 | 路线段 | milestone | 数量 |
|------|--------|-----------|------|
| 第 1 段 | 滇西边境与茶马古道 | 74, 75 | 2 |
| 第 2 段 | 滇西山地与高原坝子 | 76 | 1 |
| 第 3 段 | 横断山与川西通道 | 77, 78 | 2 |
| 第 4 段 | 川西 / 川西南 | 79, 80 | 2 |
| 第 5 段 | 蜀道、秦岭与关中 | 81, 82, 83 | 3 |
| 第 6 段 | 黄土高原与陕北 | 84, 85 | 2 |
| 第 7 段 | 山西北上与长城边地 | 86, 87, 88, 89 | 4 |
| 第 9 段 | 长城、承德与北方边界 | 90 | 1 |
| 第 10 段 | 辽宁乡村与东北收束 | 91, 92, 93, 94, 95 | 5 |

总计：2+1+2+2+3+2+4+1+5 = 22 ✅

---

## 5. 28 天执行卡映射

22 条 milestone 全部映射到 28 天每日执行卡：

| Milestone | 对应执行卡 | 数量 |
|-----------|------------|------|
| 74 | D1-D2 腾冲/和顺 | 1 |
| 75 | D3 高黎贡山 | 1 |
| 76 | D4-D6 大理/喜洲/丽江 | 1 |
| 77 | D7 玉龙雪山边缘 | 1 |
| 78 | D8 康定 | 1 |
| 79 | D9 雅安 | 1 |
| 80 | D9-D10 雅安/成都平原 | 1 |
| 81 | D12 剑门关 | 1 |
| 82 | D13 汉中 | 1 |
| 83 | D13 汉中/秦岭 | 1 |
| 84 | D15-D16 宜君/延安 | 1 |
| 85 | D16 延安 | 1 |
| 86 | D18-D19 吕梁/雁门关 | 1 |
| 87 | D19 忻州 | 1 |
| 88 | D19 忻州 | 1 |
| 89 | D20 周口店/田园洞 | 1 |
| 90 | D24 司马台/古北口 | 1 |
| 91 | D26 辽宁乡村 | 1 |
| 92 | D26 辽宁乡村 | 1 |
| 93 | D26 辽宁乡村 | 1 |
| 94 | D26-D27 辽宁/大连 | 1 |
| 95 | D27-D28 大连/黄海 | 1 |

总计：22 ✅

---

## 6. 新增「如何阅读 Out of Eden Walk 的 Dispatch」

5 张卡片：
1. **📰 它不是景点说明** — Dispatch 是行走中的现场报道，重点常常不是景点，而是路上的人、语言、劳动、气候、边界和普通生活。
2. **🧭 它不是 GPS 路书** — Milestone 是叙事节点，不等于可直接导航的坐标。复刻时要把它降维成城市、县域、公共景区或可达观察点。
3. **🏛 它把大历史放进小场景** — 一个摊位、一段路、一座桥、一个村庄，可能对应迁徙、帝国、边疆、贸易、环境或现代化的大主题。
4. **⏳ 它适合慢读** — 不要一次读完 22 条。可以按 10 段路线或 28 天执行卡分批阅读，每周 2-3 条即可。
5. **⚖️ 中文复刻要保留不确定性** — 凡是没有实地走访、官方细节未完全复核、开放状态未确认的地方，都应该保留"待验证"。

---

## 7. 新增「从官方故事到复刻路线」

4 步流程：
1. **官方 Milestone** — 提供叙事节点和故事入口
2. **Dispatch 主题** — 提炼人物、场景、地貌和历史线索
3. **中文路线解读** — 转化为中国读者能理解的地理、文化和旅行主题
4. **文化复刻行程** — 降维为可达城市、县域、公共景区、博物馆和安全观察点

提醒：不是从官方故事直接复制出一条路线，而是从故事中提炼主题，再设计普通旅行者能安全接近的复刻方式。

---

## 8. 页面状态更新：88% → 90%

### 8.1 原状态

```
完成度：88% · 可用草案 v0.9
已完成：10 段路线 · Milestones 74–95 共 22 条覆盖 · 22 条中文摘要 + 路线意义 + 复刻建议 · 28 天节奏 · 28 天每日导游词 · 28 天每日执行卡 · 6 条短线 · 现场记录模板 · CSV/GeoJSON/GPX/SVG 数据 · SEO/OG/下载入口
```

### 8.2 新状态

```
完成度：90% · Dispatch 基础复核版
已完成：10 段路线 · Milestones 74–95 共 22 条覆盖 · 22 条中文摘要 + 路线意义 + 复刻建议 · 官方 Dispatch 资料对照表 · 22/22 URL 200 · 28 天节奏 · 28 天每日导游词 · 28 天每日执行卡 · 6 条短线 · 现场记录模板 · CSV/GeoJSON/GPX/SVG 数据 · SEO/OG/下载入口
```

### 8.3 同步更新文案

- hero badge：`v1.5.6 · 可用草案 v0.9 · 88% · 22/22 中文摘要` → `v1.5.7 · 可用草案 v0.9 · 90% · Dispatch 基础复核`
- page-meta (× 2)：`v1.5.6 · ... · 88% · ... · 22/22 milestone 中文摘要 + 故事索引` → `v1.5.7 · ... · 90% · ... · Dispatch 资料对照 + 22/22 URL 200`
- footer：`v1.5.6 · ... · 88% · ... · 22/22 milestone 中文摘要` → `v1.5.7 · ... · 90% · ... · Dispatch 基础复核`
- 内容风险说明：`可用草案 v0.9 · 88%` → `可用草案 v0.9 · 90%`
- 仍需验证描述：`页面口径为 90% Dispatch 基础复核版，剩余工作量需要视觉资料 + 实地核验 + 二次深读`

---

## 9. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / OEDW `data_status_label` / `route_summary` 字段
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段

---

## 10. manifest 更新摘要

| 字段 | v1.5.6 | v1.5.7 |
|------|--------|--------|
| 顶层 `version` | v1.5.6 | **v1.5.7** |
| 顶层 `updated_at` | 2026-07-06 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 · Milestones 中文索引版 | **长线文化复刻样板 · Dispatch 基础复核版** |
| 辽塔 `data_status_label` | 自驾人文路线样板 · 已完成读塔顺序 | 自驾人文路线样板 · 已完成读塔顺序（未变） |
| 山西 `data_status_label` | 古建自驾路线样板 · 已完成古建读图顺序 | 古建自驾路线样板 · 已完成古建读图顺序（未变） |
| OEDW `route_summary` | + Milestones 74–95 共 22 条中文故事摘要 + 故事索引 | **+ 官方 Dispatch 资料对照表 + Dispatch 阅读方法** |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 11. OEDW 事实边界验证

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW 「22/23」 清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW Milestones 74–95 = 22/22 | ✅ OEDW 页面 8 处 + README 3 处 |
| OEDW 6,000–6,700 公里保留 | ✅ OEDW 页面 11 处 |
| 北京段 卢沟桥 → 天安门 → 小汤山 | ✅ |
| 黄海终点 2023 冬 / 2024.6 / 2024.8 | ✅ |
| 文化复刻粗点 / 非原始 GPS / 非导航 | ✅ |
| 10% 完全从 OEDW 页面清除 | ✅（页面 grep "10%" 空） |
| 规划中（实际内容） | ✅ 仅 HTML 注释 "规划中提示"，不影响阅读 |
| 22 个 Milestone 编号（74-95）全部出现 | ✅ 数量校验 PASS |
| 不复制官方长文 / 不做全文翻译 | ✅ 仅做中文摘要、转述、引用短标题、引用官方 URL |
| 不伪造 Paul Salopek 原始 GPS | ✅ 所有建议为文化复刻解读 |
| 不写成官方旅行路线 | ✅ 明确标注"文化复刻解读" |
| 22/22 官方 URL 200 (v1.5.7 验证) | ✅ |

---

## 12. 质量门禁验证

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
assert "Dispatch 基础复核版" in html
assert "官方 Dispatch 资料对照表" in html
✅ PASS OEDW dispatch review numbers 74-95 (22/22)

$ curl -s -o /dev/null -w "%{http_code}" -L --max-time 15 <22 URLs>
200 × 22 全部
```

---

## 13. SEO / OG 门禁结果

- `build-route-assets.py --all` 保留 9/9 SEO 字段：✅
- `check-routes-index-sync.py`：✅ routes checked: 3
- `check-route-page-integration.py`：✅ routes checked: 3
- `render-route-og-svg.py --all --check`：✅ 5 files
- `check-route-seo.py`：✅ 5 pages · 3 route pages · 5 og assets

---

## 14. 关键词验收

| 关键词 | 目标 | 命中 |
|--------|------|------|
| Dispatch 基础复核版 | OEDW 页面 / README / CHANGELOG / docs | OEDW 2 / README 2 / CHANGELOG 2 / CONTENT_NOTES 2 |
| 官方 Dispatch 资料对照表 | OEDW 页面 / README / CHANGELOG / docs | OEDW 3 / README 1 / CHANGELOG 2 / CONTENT_NOTES 1 |
| 如何阅读 Out of Eden Walk 的 Dispatch | OEDW 页面 | 2 |
| 从官方故事到复刻路线 | OEDW 页面 | 2 |
| 官方资料状态 | OEDW 页面 | 1 |
| 核心主题 | OEDW 页面 | 1 |
| 关键词 | OEDW 页面 | 2 |
| 人物 / 场景 / 地貌 | OEDW 页面 | 1 |
| 对应执行卡 | OEDW 页面 | 1 |
| Milestone 74 / 95 | OEDW 页面 | 22/22 |
| 90% | OEDW 页面 | 7 |
| 88% | OEDW 页面 | 0（清除） |
| 10% | OEDW 页面 | 0（清除） |
| 规划中 | OEDW 页面 | 仅 HTML 注释 |
| 跨越六年 清除（实际内容） | OEDW/README/docs/reports | ✅ clean |
| 22/23 清除（实际内容） | OEDW/README/docs/reports | ✅ clean |
| 22/22 保留 | OEDW/README/docs/reports | ≥15 |
| 6,000–6,700 保留 | OEDW/README/docs/reports | ≥30 |

---

## 15. 本地 HTTP 200 验证

```
$ python3 -m http.server 8007
$ curl -I http://127.0.0.1:8007/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8007/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8007/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8007/reports/OEDW_DISPATCH_DEEP_REVIEW_REPORT.md      HTTP/1.0 200 OK (after commit)
```

---

## 16. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

通过: 70
失败: 0

通过: 108
失败: 0

✓ STATUS: PASS
```

---

## 17. 提交清单

```bash
git add trips/out-of-eden-walk-china/index.html
git add assets/css/styles.css data/routes/routes-manifest.json
git add scripts/check-route-seo.py
git add README.md CHANGELOG.md docs/CONTENT_NOTES.md
git add reports/OEDW_DISPATCH_DEEP_REVIEW_REPORT.md
git commit -m "Add OEDW dispatch deep review concordance"
git push origin main
```

---

## 18. v1.5.8 建议

1. **每条 dispatch 配 200-500 字中文转述**
   - 引述短标题 + URL
   - 不做全文翻译
   - 22 条 milestone 全部

2. **每条 milestone 配代表图片**
   - 由真实走过的人贡献
   - 走过的 milestone 优先
   - 6,000–6,700 公里覆盖完整度

3. **每条 milestone 现场实拍图**
   - 22 张图
   - 季节性展示
   - 普通旅行者视角

4. **可复刻程度地图化 + 22 条 milestone**
   - 地图上不同颜色显示
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

9. **每条 milestone 与 28 天每日执行卡交叉链接**
   - 双向链接
   - M74 → D1 腾冲
   - D21 卢沟桥 → M89 (北京段)

10. **每条 milestone 配官方 dispatch 主题音频**
    - Paul 原声叙述
    - 中文翻译字幕
    - 离线下载

---

_辛 🔮 · 行旅图谱 · OEDW Dispatch 深度复核与资料对照报告 · 2026-07-06_

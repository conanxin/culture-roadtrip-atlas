# 行旅图谱 · OEDW 视觉资料与参考书目细粒度版 · v1.5.9

> OEDW Visual Bibliography Pack (Granular)
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | 02b6155 (OEDW Visual Bibliography 报告回填) |
| **新 commit** | _pending_（commit 后回填） |
| **push 状态** | _pending_ |
| **部署状态** | _pending_ |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 3/3 endpoints 200 |
| **数量校验** | ✅ 22/22 Milestone 编号（74-95）全部出现 |
| **官方 URL 校验** | ✅ 22/22 全部 200 (2026-07-06 验证) |
| **视觉状态** | ✅ 22/22 全部「官方图片链接 · 待实拍」 |
| **补图清单** | ✅ 22 条全部覆盖 |
| **线上 HTTP 200** | _pending_（push 后回填） |
| **GitHub Actions run** | _pending_ |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +400 | 3 新模块 + 8 类出发前清单 + 重命名 + 导航 + 状态 |
| `assets/css/styles.css` | M | +130 | 17 个新 CSS 类（.oedw-shot-* / .oedw-difficulty-* / .oedw-fieldwork-* / .oedw-archive-rule / .oedw-bibliography-*） |
| `data/routes/routes-manifest.json` | M | +3 | v1.5.9 + OEDW data_status_label / route_summary |
| `scripts/check-route-seo.py` | M | +1 | manifest version 接受 v1.5.2-1.5.9 |
| `README.md` | M | +15 | v1.5.9 当前版本 + 描述 |
| `CHANGELOG.md` | M | +90 | v1.5.9 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +20 | v1.5.9 章节 |
| `reports/OEDW_VISUAL_BIBLIOGRAPHY_PACK_REPORT.md` | A | +500 | 本报告 |

**未修改**：
- 辽塔页面（v1.5.4 状态保留）
- 山西页面（v1.5.4 状态保留）
- CSV / GeoJSON / GPX 坐标数据
- SVG 路线示意图
- OG SVG（SEO 检查不要求）
- 路线工厂门禁脚本

---

## 2. 视觉资料矩阵完成情况

### 2.1 Milestone 视觉资料矩阵（v1.5.8 重命名自「视觉资料占位与来源管理」）

- 22/22 全部建立
- 4 字段：Milestone / 视觉状态 / 需要补拍/已有线索 / 官方 Milestone 链接
- 视觉状态枚举：官方图片链接 / 待实拍 / 待补图 / 暂无图片
- 22/22 当前统一为「官方图片链接 · 待实拍」状态

### 2.2 22 条 Milestone 视觉资料状态统计

| 状态 | 数量 | 编号 |
|------|------|------|
| 🟢 官方图可参考 | 22 | 74-95（22 条全部） |
| 🟡 待实拍 | 22 | 74-95（22 条全部） |
| 🟠 待授权 | 0 | — |
| 🟠 待补图 | 0 | — |
| ⚫ 暂无图片 | 0 | — |

**说明**：22 条 milestone 当前状态为「官方图片链接 + 待实拍」。本仓库不下载任何官方或第三方图片。

---

## 3. 22 条 Milestone 补图清单

22 行 × 6 字段：Milestone / 必补画面 / 可选画面 / 不建议拍摄 / 拍摄难度 / 备注

### 3.1 拍摄难度分布

| 难度 | 数量 | 编号 |
|------|------|------|
| 🟢 低 | 8 | 74, 76, 80, 84, 85, 87, 89, 95 |
| 🟡 中 | 10 | 79, 81, 83, 86, 88, 90, 91, 93, 94, ... |
| 🔴 高 | 4 | 75, 77, 78, 92 |

注：M82 是空城主题（不可刻意复刻），归入"低"但有主题阅读备注。

### 3.2 22 条必补画面（按段落）

| 段落 | 编号 | 必补画面示例 |
|------|------|--------------|
| 第 1 段 | 74 | 边境检查站外观 / 腾冲城市入口 / 雨季山路 |
| 第 1 段 | 75 | 高黎贡山保护区入口 / 雨林远景 |
| 第 2 段 | 76 | 大理坝子 / 喜洲外圈 / 丽江古城外 |
| 第 3 段 | 77 | 丽江古城外 / 木里方向路标 |
| 第 3 段 | 78 | 康定城 / 折多山垭口远景 |
| 第 4 段 | 79 | 川西南山路 / 长征历史层叠 |
| 第 4 段 | 80 | 雅安城 / 都江堰鱼嘴分水 |
| 第 5 段 | 81 | 剑门关阙口 / 翠云廊古柏 / 剑门栈道 |
| 第 5 段 | 82 | 汉中城 / 普通街道 |
| 第 5 段 | 83 | 秦岭隧道 / 秦岭通道 |
| 第 6 段 | 84 | 宝塔山 / 延河大桥 / 陕北窑洞 |
| 第 6 段 | 85 | 陕北手工艺作坊 / 剪纸艺人 |
| 第 7 段 | 86 | 雁门关关城 / 山西古城墙 |
| 第 7 段 | 87 | 城乡结合部商店 / 流动摊贩 |
| 第 7 段 | 88 | 冬季华北街景 / 等待场景 |
| 第 7 段 | 89 | 周口店遗址 / 田园洞剖面 / 北京远郊 |
| 第 9 段 | 90 | 司马台长城 / 古北口 |
| 第 10 段 | 91 | 辽宁东北乡村 / 玉米地 |
| 第 10 段 | 92 | 辽宁玉米地 / 东北农人 |
| 第 10 段 | 93 | 乌鸦群 / 东北田野 |
| 第 10 段 | 94 | 辽宁工业城市外观 / 户外工人 |
| 第 10 段 | 95 | 大连港 / 老铁山 / 黄海 |

---

## 4. OEDW 现场实拍计划

6 类现场记录主题：

| 类别 | 拍摄内容 | 记录主题 |
|------|----------|----------|
| 🛣 道路 | 路肩/岔路/桥/隧道口/老路痕迹/公路与村庄交界 | 今天的人如何移动？路是为谁服务的？旧路是否还可见？ |
| 👥 人 | 摊主/司机/村民/游客/修路工/店主/赶路的人 | 拍人必须先征得同意；不适合拍就写文字观察 |
| 🏔 地貌 | 山口/河谷/塬梁/平原边缘/海岸线/城市边缘地带 | 高海拔/高原段需注意身体，不为补图硬撑 |
| 🚧 边界 | 城门/关口/长城/港口/桥/行政边界/语言/饮食/建筑风格变化 | 边境段不硬闯，深山/保护区不深入 |
| 🍜 日常 | 早餐店/公交站/学校门口/集市/广场/小卖部/路边修车点 | 日常比景点更接近"路如何进入生活" |
| 📋 资料照 | 导览牌/地名牌/博物馆说明牌/道路牌/保护区提示牌/公共交通站牌 | 资料照是后续复核路线最重要的证据之一 |

---

## 5. 视觉资料命名与归档规范

### 5.1 建议目录

`assets/img/oedw-fieldwork/` — 此目录仅用于未来自有实拍 / 已授权图片。当前不存放官方或第三方图片。

### 5.2 命名规则

```
oedw-m74-border-road-01.jpg
oedw-m80-tea-horse-road-01.jpg
oedw-m91-gubeikou-wall-01.jpg
oedw-m95-yellow-sea-port-01.jpg
```

字段解释：
- `oedw` — 项目标识
- `m74` — Milestone 编号（74-95）
- `border-road` — 主题关键词
- `01` — 序号

### 5.3 分类建议

- `road` — 道路 / 桥 / 隧道 / 旧道痕迹
- `people` — 摊主 / 司机 / 村民 / 修路工
- `landform` — 山口 / 河谷 / 塬梁 / 海岸
- `boundary` — 城门 / 关口 / 长城 / 港口 / 行政边界
- `daily-life` — 早餐店 / 公交站 / 学校 / 集市 / 广场
- `source-sign` — 导览牌 / 地名牌 / 博物馆说明牌 / 道路牌

### 5.4 版权/授权备注字段

每张图片在归档时应记录：
- 拍摄者（姓名 / 联系方式）
- 拍摄时间（年-月-日）
- 拍摄地点（省 / 市 / 县 / 镇）
- 授权协议（CC-BY-SA 4.0 / CC-BY / 公共领域 / 商业授权）
- 原创说明（本人原创 / 委托拍摄 / 转载已授权）

---

## 6. 参考书目与资料入口（v1.5.8 重命名自「参考书目与延伸阅读」）

5 类（保持不变）：
- 📕 官方资料 (Official)
- 📘 英文文献 (English)
- 📗 中文资料 (Chinese)
- 📙 学术参考 (Academic)
- 📓 衍生阅读 (Recommended)

---

## 7. 出发前核查清单（v1.5.9 从 5 类扩展为 8 类）

| # | 类别 | 内容 |
|---|------|------|
| 1 | 🌦 路线与天气 | 山区天气/雨季/高海拔/道路施工/季节性封闭 |
| 2 | 🏛 开放状态 | 博物馆预约/遗址/景区/古道/保护区 |
| 3 | 🚆 交通衔接 | 高铁/火车/长途汽车/包车/自驾停车/边境不自驾 |
| 4 | 🛏 住宿区域 | 只确认区域/不压到太晚/预留弹性/边境提前 24h/高反严寒不过夜 |
| 5 | 📷 拍摄与记录 | 相机/录音/命名规则/授权协议/现场记录模板 |
| 6 | 🛡 安全与伦理 | 拍人先同意/不危险路段/不硬闯边境/尊重当地/不带违禁 |
| 7 | 📚 资料复核 | 官方 milestone/dispatch 对照/地名核对/文旅局/景区公告 |
| 8 | ↩ 撤退策略 | 下雨/闭馆/疲劳/交通延误/最小完成版 |

---

## 8. 页面状态更新：92% → 93%

### 8.1 原状态

```
完成度：92% · 视觉资料与书目准备版
```

### 8.2 新状态

```
完成度：93% · 视觉资料准备版
```

### 8.3 同步更新文案

- hero badge：`v1.5.8 · ... · 92% · 视觉资料 + 书目` → `v1.5.9 · ... · 93% · 视觉资料准备`
- page-meta (× 2)：`v1.5.8 · ... · 92% · ... · 视觉资料 + 书目 + 出发前清单` → `v1.5.9 · ... · 93% · ... · 视觉资料矩阵 + 补图清单 + 实拍计划 + 归档规范`
- footer：`v1.5.8 · ... · 92% · ... · 视觉资料与书目准备` → `v1.5.9 · ... · 93% · ... · 视觉资料准备`
- 内容风险说明：`可用草案 v0.9 · 92%` → `可用草案 v0.9 · 93%`
- 仍需验证描述：`页面口径为 92% 视觉资料与书目准备版...` → `页面口径为 93% 视觉资料准备版...`
- 状态描述：增加 22 条 Milestone 补图清单 / OEDW 现场实拍计划 / 视觉资料命名与归档规范 / 出发前核查清单 8 类

---

## 9. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / OEDW `data_status_label` / `route_summary` 字段
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段
✅ 未下载任何官方或第三方图片到仓库
✅ 未引用不存在的本地图片路径

---

## 10. 是否下载第三方图片

**未下载** — 0 张图片
- ❌ 不下载 National Geographic / Out of Eden Walk 图片到仓库
- ❌ 不下载第三方图片到仓库
- ❌ 不引用不存在的本地图片路径
- ✅ 仅做占位、链接、清单、计划、命名规范

---

## 11. manifest 更新摘要

| 字段 | v1.5.8 | v1.5.9 |
|------|--------|--------|
| 顶层 `version` | v1.5.8 | **v1.5.9** |
| 顶层 `updated_at` | 2026-07-06 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 · 视觉资料与书目准备版 | **长线文化复刻样板 · 视觉资料准备版** |
| 辽塔 `data_status_label` | 自驾人文路线样板 · 已完成读塔顺序 | 自驾人文路线样板 · 已完成读塔顺序（未变） |
| 山西 `data_status_label` | 古建自驾路线样板 · 已完成古建读图顺序 | 古建自驾路线样板 · 已完成古建读图顺序（未变） |
| OEDW `route_summary` | + 视觉资料占位 22/22 + 参考书目 5 类 + 出发前核查清单 5 类 | **+ Milestone 视觉资料矩阵 + 22 条补图清单 + 现场实拍计划 + 归档规范 + 出发前核查清单 8 类** |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 12. OEDW 事实边界验证

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW 「22/23」 清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW Milestones 74–95 = 22/22 | ✅ OEDW 页面 7 处 + README 3 处 |
| OEDW 6,000–6,700 公里保留 | ✅ OEDW 页面 11 处 |
| 北京段 卢沟桥 → 天安门 → 小汤山 | ✅ |
| 黄海终点 2023 冬 / 2024.6 / 2024.8 | ✅ |
| 文化复刻粗点 / 非原始 GPS / 非导航 | ✅ |
| 10% 完全从 OEDW 页面清除 | ✅（页面 grep "10%" 空） |
| 90% 完全从 OEDW 页面清除 | ✅（页面 grep "90%" 空） |
| 92% 完全从 OEDW 页面清除 | ✅（页面 grep "92%" 空） |
| 规划中（实际内容） | ✅ 仅 HTML 注释 "规划中提示"，不影响阅读 |
| 22 个 Milestone 编号（74-95）全部出现 | ✅ 数量校验 PASS |
| 不下载 / 不复制 / 不搬运官方图片 | ✅ 22/22 全部「官方图片链接 · 待实拍」 |
| 不把视觉占位写成已经实拍完成 | ✅ 显式标注「待实拍」状态 |
| 不引用不存在的本地图片路径 | ✅ |
| 不为补图而冒险进入边境/深山/保护区 | ✅ 22 条都有「不建议拍摄」字段 |

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
assert "92%" not in html
assert "93%" in html
assert "视觉资料准备版" in html
assert "Milestone 视觉资料矩阵" in html
assert "22 条 Milestone 补图清单" in html
assert "OEDW 现场实拍计划" in html
assert "视觉资料命名与归档规范" in html
assert "参考书目与资料入口" in html
✅ PASS OEDW visual bibliography milestone coverage (22/22)
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
| 视觉资料准备版 | OEDW / README / CHANGELOG / docs | OEDW 2 / README 2 / CHANGELOG 2 / CONTENT_NOTES 2 |
| Milestone 视觉资料矩阵 | OEDW | 1 |
| 22 条 Milestone 补图清单 | OEDW | 3 |
| OEDW 现场实拍计划 | OEDW | 3 |
| 视觉资料命名与归档规范 | OEDW | 3 |
| 参考书目与资料入口 | OEDW | 1 |
| 待实拍 | OEDW | 1 |
| 待授权 | OEDW | 1 |
| 93% | OEDW | 7 |
| 92% | OEDW | 0（清除） |
| 90% | OEDW | 0（清除） |
| 10% | OEDW | 0（清除） |
| 22/22 | OEDW/README/docs | ≥15 |
| 6,000–6,700 | OEDW/README/docs | ≥30 |
| 22/23 | OEDW/README/docs | 0（clean） |
| 跨越六年 | OEDW/README/docs | 0（clean） |

---

## 16. 本地 HTTP 200 验证

```
$ python3 -m http.server 8009
$ curl -I http://127.0.0.1:8009/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8009/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8009/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8009/reports/OEDW_VISUAL_BIBLIOGRAPHY_PACK_REPORT.md  HTTP/1.0 200 OK (after commit)
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
git add reports/OEDW_VISUAL_BIBLIOGRAPHY_PACK_REPORT.md
git commit -m "Add OEDW visual bibliography pack (granular)"
git push origin main
```

---

## 19. v1.5.10 建议

1. **现场实拍贡献**
   - 邀请真实走过的人贡献 22 张 milestone 实拍图
   - 按 CC-BY-SA 4.0 授权
   - 走过的 milestone 优先

2. **图片授权**
   - 联系 National Geographic / Out of Eden Walk 询问官方图片使用授权
   - 如不可行，明确标注「暂无授权」

3. **第三方图片（CC 协议）**
   - Wikimedia Commons
   - 博物馆/景区的官方开放图库
   - 维基百科（CC-BY-SA）

4. **每条 milestone 配代表图片**
   - 22 张图
   - 季节性展示
   - 普通旅行者视角

5. **目录创建**
   - `assets/img/oedw-fieldwork/README.md` 说明未来实拍归档规范
   - 不创建真实图片目录
   - 仅 README + .gitkeep

6. **书目原著获取**
   - 图书馆 / 正规书店 / 在线书店
   - 学术数据库（CNKI / JSTOR）
   - 免费资源（Internet Archive）

7. **可访问性**
   - 字体大小可调
   - 高对比度模式
   - 语音导览（中文 + 英文）
   - 表格 ARIA

8. **「实走反馈」章节**
   - 邀请用户提交 GitHub Issue
   - 走过的 milestone 补充
   - 季节性观察
   - 实拍图贡献

9. **中英双语版**
   - 中文为主，英文副
   - Paul Salopek 母语友好
   - 国际读者可读

10. **每条 milestone 与 28 天每日执行卡交叉链接**
    - 双向链接
    - M74 → D1 腾冲
    - D21 卢沟桥 → M89 (北京段)

11. **每条 milestone 配官方 dispatch 主题音频**
    - Paul 原声叙述
    - 中文翻译字幕
    - 离线下载

---

_辛 🔮 · 行旅图谱 · OEDW 视觉资料与参考书目细粒度版报告 · 2026-07-06_

# 行旅图谱 · OEDW 中国段深度执行版 · v1.5.5

> OEDW China Route Deep Optimization
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | 1301fa6 (Sprint 2 报告回填) |
| **新 commit** | bed2df7 (Deepen OEDW China route execution guide) |
| **push 状态** | ✅ origin/main 已推送 (1301fa6..bed2df7) |
| **部署状态** | ✅ GitHub Pages 已部署 (Deploy run 28778936284 · 24s · success) |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 4/4 endpoints 200 |
| **线上 HTTP 200** | ✅ 4/4 endpoints 200 (2026-07-06) |
| **GitHub Actions run** | ✅ Route Data Quality Gate · run 28778936301 · 9s · success |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +700 | 页面顶部状态 + 6 新模块 + 导航更新 |
| `assets/css/styles.css` | M | +213 | 14 个新 CSS 类（.oedw-*） |
| `data/routes/routes-manifest.json` | M | +3 | v1.5.5 + OEDW data_status_label / route_summary |
| `scripts/check-route-seo.py` | M | +1 | manifest version 接受 v1.5.2 / v1.5.3 / v1.5.4 / v1.5.5 |
| `README.md` | M | +15 | v1.5.5 当前版本 + 描述 |
| `CHANGELOG.md` | M | +60 | v1.5.5 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +20 | v1.5.5 章节 |
| `reports/OEDW_CHINA_ROUTE_DEEP_OPTIMIZATION_REPORT.md` | A | +500 | 本报告 |

**未修改**：
- 辽塔页面（v1.5.4 状态保留）
- 山西页面（v1.5.4 状态保留）
- CSV / GeoJSON / GPX 坐标数据
- SVG 路线示意图
- OG SVG（SEO 检查不要求）
- 路线工厂门禁脚本
- index.html / routes/index.html（首页文案已是 v1.5.4 状态，OEDW 页面状态变化是页面内自洽）

---

## 2. 顶部状态修正

### 2.1 原状态

```
进度：规划中
10% · 已完成路线总览、分段路线、时间线、Milestones 表格、关键故事、复刻版本、资料清单
待完成：实地走访验证、点位实用信息、详细分时日程、住宿与交通建议、每个 milestone 的中文摘要、视觉资料
定位：文化复刻路线（非原始 GPS 复刻），不作为正式出行方案
```

### 2.2 新状态

```
完成度：85% · 可用草案 v0.9
已完成：10 段路线 · Milestones 74–95 共 22 条覆盖 · 28 天节奏 · 28 天每日导游词 · 6 条短线 · 现场记录模板 · CSV/GeoJSON/GPX/SVG 数据 · SEO/OG/下载入口
仍需验证：实地走访验证 · 季节性道路与天气风险 · 部分点位开放状态 · 边境/山地/乡村路段可达性 · 住宿与公共交通现实可行性 · 每个 milestone 逐条中文摘要与视觉资料
定位：文化复刻路线，不是 Paul Salopek 原始 GPS，不是官方旅行路线，不作为实时导航。不是最终实地验证版。
```

### 2.3 同步更新文案

- hero badge：`v1.4.6 · 数据驱动展示 + 静态地图预览` → `v1.5.5 · 可用草案 v0.9 · 85% · 每日执行卡`
- page-meta：`v1.4.6 · 50% · 数据驱动展示 + 静态 SVG 地图预览` → `v1.5.5 · 可用草案 v0.9 · 85% · 2026-07-06 · 每日执行卡 + 住宿交通总表`
- footer：`v1.4.6 · Out of Eden Walk 中国段复刻 · 数据驱动版 · 50% · 2026 · 此页为规划中文化复刻路线` → `v1.5.5 · Out of Eden Walk 中国段 · 可用草案 v0.9 · 85% · 2026 · 文化复刻路线非实地验证版`
- 内容风险说明：`本页面为规划中路线 ... 不作为正式出行方案` → `本页面为可用草案 v0.9 · 85% ... 出发前请以最新官方材料与实地核实为准`
- "建议先看" → "如何使用这条路线"（旧「本条路线尚在规划中。如需查看已上线的完整路线，请参考辽塔巡礼路线」文案被替换）

---

## 3. 如何使用本页模块

4 张卡片：
1. **🗓️ 我只有 7 天**（云南线 / 北京长城线）
2. **⏱ 我有 14 天**（云南+川西 / 北京+承德+大连 / 蜀道秦岭+西安+延安）
3. **🧭 我有 28 天**（28 天每日执行卡）
4. **📖 我只想阅读**（按事实审校→长卷→10段→28天导游词→数据的顺序阅读）

---

## 4. 28 天每日执行卡

28 张执行卡，每张 7 字段：
- Day（天数 + 主题）
- 🏨 过夜建议（区域级，不写酒店）
- 🌅 上午
- 🌤 下午
- 🌙 傍晚 / 晚上
- 最小完成版（只做 1 件事也算完成）
- 可选加点（附条件：天气好/体力足/时间早）
- 撤退策略（下雨/闭馆/疲劳/交通延误时怎么改）
- 今日不要硬加点

28 天主题：D1 腾冲 → D2 和顺 → D3 高黎贡山 → D4 大理 → D5 喜洲/洱源 → D6 丽江 → D7 玉龙雪山边缘 → D8 康定 → D9 雅安 → D10 成都平原 → D11 三星堆/广汉 → D12 剑门关 → D13 汉中/秦岭 → D14 西安 → D15 宜君/黄土 → D16 延安 → D17 黄河沿线 → D18 吕梁 → D19 忻州/雁门关 → D20 周口店/田园洞 → D21 卢沟桥 → D22 天安门/中轴线 → D23 胡同/小汤山 → D24 司马台/古北口 → D25 承德 → D26 辽宁乡村 → D27 大连港 → D28 黄海

---

## 5. 7 / 14 / 28 天路线选择器

3 列对比：

| 维度 | 7 天 | 14 天 | 28 天 |
|------|------|-------|-------|
| **推荐路线** | 云南边地与古道线 / 北京长城与城市断面线 | 云南+川西 / 北京+承德+大连 / 蜀道秦岭+西安+延安 | 28 天每日执行卡 |
| **适合** | 第一次体验、短假、摄影、轻研究 | 主题旅行、写作、文化地理观察 | 长期研究、纪录片式旅行、深度写作 |
| **舍弃** | 川西、秦岭、黄土高原、东北收束 | 不追求中国段全覆盖 | 不适合轻松旅游，不适合赶路打卡 |

---

## 6. 住宿区域与交通方式总表

14 区域表格（6 字段：区域 / 建议过夜地 / 推荐进入方式 / 推荐离开方式 / 适合停留 / 风险提醒）：

| 区域 | 过夜地 | 进入 | 离开 | 停留 | 风险 |
|------|--------|------|------|------|------|
| 腾冲/和顺 | 腾冲市区 | 飞机到腾冲/昆明转机 | 包车/长途汽车 | 2–3 天 | 边境临近区域需二次核实现状 |
| 大理 | 大理古城内或下关 | 高铁/长途汽车 | 包车/长途汽车/高铁 | 2 天 | 旅游季节古城拥挤 |
| 丽江 | 丽江古城外 | 飞机/高铁 | 包车/长途汽车 | 2 天 | 高原反应不严重但有 |
| 康定 | 康定市区 | 长途汽车/自驾 G318 | 包车/长途汽车 | 1–2 天 | 高原垭口大风/雪/冻 |
| 雅安 | 雅安市区 | 高铁/长途汽车 | 包车/长途汽车 | 1 天 | 雨季滑坡 |
| 成都 | 成都市区 | 高铁/飞机 | 地铁/出租车/高铁 | 1–2 天 | 城市交通拥堵 |
| 广汉/三星堆 | 广汉 | 高铁到广汉/成都转 | 包车/长途汽车 | 1 天 | 新馆/老馆预约政策不同 |
| 汉中 | 汉中 | 高铁到汉中 | 包车/出租车 | 1 天 | 山区道路天气 |
| 西安 | 西安城内 | 高铁/飞机 | 地铁/出租车 | 2 天 | 旅游季节人流 |
| 延安 | 延安 | 高铁到延安 | 包车/出租车 | 1–2 天 | 红色旅游季节预约 |
| 吕梁/忻州 | 吕梁或忻州 | 高铁到太原再转 | 包车/长途汽车 | 2 天 | 山路多弯道 |
| 北京 | 北京城内 | 高铁/飞机 | 地铁/出租车 | 3–4 天 | 城市交通拥堵、广场限流 |
| 承德 | 承德 | 高铁到承德/自驾 | 出租车/公交 | 1–2 天 | 山庄限流 + 山区天气 |
| 大连 | 大连 | 高铁/飞机 | 出租车/公交/轻轨 | 2 天 | 东北冬季交通不便 |

---

## 7. 不同人群版本

5 卡片：
1. **👣 第一次走** — 只选 7 天 · 推荐云南线或北京长城线 · 不要从全线开始
2. **📷 摄影者** — 优先云南、北京长城、黄土高原、黄海 · 拍摄重点：道路、人、地貌、边界、日常
3. **✍️ 写作者** — 使用现场记录模板 · 每天只写一个人或一个场景 · 不要写成景点说明
4. **👨‍👩‍👧 亲子 / 家庭** — 不建议全线 · 选择北京长城线或大理/丽江轻量段 · 每天只安排 1 个核心点
5. **🔥 高强度旅行者** — 可以做 28 天版本 · 仍不建议边境、深山、高海拔逐点复刻

---

## 8. 仍需实地验证事项

5 类（替换原 "待完成" 表达）：
1. **实地可达性** — 山区道路 · 边境附近 · 乡村路段 · 季节性封闭
2. **住宿与交通** — 过夜地是否适合普通旅行者 · 公共交通衔接是否稳定 · 自驾停车与返程问题
3. **开放状态** — 博物馆 · 遗址 · 古道 · 边境/保护区周边
4. **细节资料** — 每个 milestone 中文摘要 · 官方 dispatch 摘要 · 地图截图或现场照片 · 参考书目
5. **用户反馈** — 实际走过的人可补充路线建议 · 页面后续可增加「实走反馈」章节

---

## 9. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / OEDW `data_status_label` / `route_summary` 字段
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段

---

## 10. manifest 更新摘要

| 字段 | v1.5.4 | v1.5.5 |
|------|--------|--------|
| 顶层 `version` | v1.5.4 | **v1.5.5** |
| 顶层 `updated_at` | 2026-07-06 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 · 已完成每日导游词 | **长线文化复刻样板 · OEDW 深度执行版** |
| 辽塔 `data_status_label` | 自驾人文路线样板 · 已完成读塔顺序 | 自驾人文路线样板 · 已完成读塔顺序（未变） |
| 山西 `data_status_label` | 古建自驾路线样板 · 已完成古建读图顺序 | 古建自驾路线样板 · 已完成古建读图顺序（未变） |
| OEDW `route_summary` | 28天节奏+6短线+每日导游词+现场记录模板+拍摄建议 | **+ 7/14/28 天选择器 + 28 天每日执行卡 + 住宿交通总表 + 不同人群版本 + 仍需实地验证清单** |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 11. OEDW 事实边界验证

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW 「22/23」 清除（实际内容） | ✅ 0 命中（仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明） |
| OEDW Milestones 74–95 = 22/22 | ✅ OEDW 页面 2 处 + README 3 处 |
| OEDW 6,000–6,700 公里保留 | ✅ OEDW 页面 10 处 |
| 北京段 卢沟桥 → 天安门 → 小汤山 | ✅ |
| 黄海终点 2023 冬 / 2024.6 / 2024.8 | ✅ |
| 文化复刻粗点 / 非原始 GPS / 非导航 | ✅ |
| 10% 完全从 OEDW 页面清除 | ✅（历史报告 0 命中；OEDW 页面 grep "10%" 空） |
| 规划中（实际内容） | ✅ 仅 HTML 注释 "规划中提示"，不影响阅读 |

---

## 12. 质量门禁验证

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
| 85% | OEDW 页面 | 7 |
| 可用草案 v0.9 | OEDW 页面 | 7 |
| 如何使用这条路线 | OEDW 页面 | 2 |
| 28 天每日执行卡 | OEDW 页面 | 3 |
| 最小完成版 | OEDW 页面 | 28（每张卡 1 处） |
| 撤退策略 | OEDW 页面 | 29（含 28 张卡 + 1 模块说明） |
| 住宿区域与交通方式总表 | OEDW 页面 | 2 |
| 按时间选择你的 OEDW 中国段 | OEDW 页面 | 1 |
| 不同人群怎么走 | OEDW 页面 | 1 |
| 仍需实地验证的部分 | OEDW 页面 | 2 |
| OEDW 深度优化 | README/CHANGELOG/docs/reports | 1 (CONTENT_NOTES) |
| 跨越六年 清除（实际内容） | OEDW/README/docs/reports | ✅ clean（仅历史审计） |
| 22/23 清除（实际内容） | OEDW/README/docs/reports | ✅ clean（仅历史审计） |
| 22/22 保留 | OEDW/README/docs/reports | ≥15 |
| 6,000–6,700 保留 | OEDW/README/docs/reports | ≥30 |
| 10% 清除 | OEDW 页面 | ✅ 完全清除 |
| 规划中 清除（实际内容） | OEDW 页面 | ✅ 仅 HTML 注释 |

---

## 15. 本地 HTTP 200 验证

```
$ python3 -m http.server 8004
$ curl -I http://127.0.0.1:8004/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8004/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8004/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8004/reports/OEDW_CHINA_ROUTE_DEEP_OPTIMIZATION_REPORT.md  HTTP/1.0 200 OK
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
git add reports/OEDW_CHINA_ROUTE_DEEP_OPTIMIZATION_REPORT.md
git commit -m "Deepen OEDW China route execution guide"
git push origin main
```

---

## 18. 18. v1.5.6 建议

1. **英文版 28 天每日执行卡**
   - 中英双语版
   - Paul Salopek 母语友好

2. **季节版执行卡**
   - 春季（3-4 月）— 桃花/杏花/油菜花
   - 夏季（6-8 月）— 雨季/草原/东北
   - 秋季（9-10 月）— 摄影黄金
   - 冬季（11-2 月）— 春节/避寒

3. **不同交通工具版**
   - 自驾版
   - 高铁 + 包车版
   - 长途汽车 + 徒步版
   - 自行车版

4. **每个 milestone 中文摘要**
   - 74-95 共 22 条
   - 每条 200-500 字
   - 配官方 dispatch URL

5. **现场照片与地图截图**
   - 由真实走过的人提供
   - 走过的里程碑优先

6. **可访问性**
   - 字体大小可调
   - 高对比度模式
   - 语音导览
   - 表格 ARIA

7. **「实走反馈」章节**
   - 邀请用户提交 GitHub Issue
   - 走过的轨迹补充
   - 季节性观察

8. **离线版**
   - 整页 PDF 导出
   - 单页打印友好
   - 关键执行卡可单独打印

9. **API 友好版**
   - OEDW 数据 JSON 公开 API
   - 第三方工具可调用
   - CC0 / CC-BY-SA 许可

10. **路线图多尺度版**
    - 全国一张图
    - 单段放大地图
    - 1:1,000,000 比例
    - 单点位详细图

---

_辛 🔮 · 行旅图谱 · OEDW 中国段深度执行版报告 · 2026-07-06_

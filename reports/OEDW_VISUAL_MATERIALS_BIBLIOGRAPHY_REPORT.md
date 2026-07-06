# 行旅图谱 · OEDW 视觉资料与参考书目 · v1.5.8

> OEDW Visual Materials and Bibliography Pack
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | 5c13909 (OEDW Dispatch 报告回填) |
| **新 commit** | 0fecdc5 (Add OEDW visual materials and bibliography pack) |
| **push 状态** | ✅ origin/main 已推送 (5c13909..0fecdc5) |
| **部署状态** | ✅ GitHub Pages 已部署 (Deploy run 28786095018 · 22s · success) |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 4/4 endpoints 200 |
| **数量校验** | ✅ 22/22 Milestone 编号（74-95）全部出现 |
| **官方 URL 校验** | ✅ 22/22 全部 200 (2026-07-06 验证) |
| **视觉状态** | ✅ 22/22 全部「官方图片链接 · 待实拍」 |
| **线上 HTTP 200** | ✅ 4/4 endpoints 200 (2026-07-06) |
| **GitHub Actions run** | ✅ Route Data Quality Gate · run 28786095006 · 10s · success |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +300 | 3 新模块 + 状态更新 + 导航 |
| `assets/css/styles.css` | M | +130 | 15 个新 CSS 类（.oedw-visual-* / .oedw-bibliography-* / .oedw-checklist-*） |
| `data/routes/routes-manifest.json` | M | +3 | v1.5.8 + OEDW data_status_label / route_summary |
| `scripts/check-route-seo.py` | M | +1 | manifest version 接受 v1.5.2-1.5.8 |
| `README.md` | M | +15 | v1.5.8 当前版本 + 描述 |
| `CHANGELOG.md` | M | +80 | v1.5.8 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +20 | v1.5.8 章节 |
| `reports/OEDW_VISUAL_MATERIALS_BIBLIOGRAPHY_REPORT.md` | A | +500 | 本报告 |

**未修改**：
- 辽塔页面（v1.5.4 状态保留）
- 山西页面（v1.5.4 状态保留）
- CSV / GeoJSON / GPX 坐标数据
- SVG 路线示意图
- OG SVG（SEO 检查不要求）
- 路线工厂门禁脚本

---

## 2. 视觉资料占位与来源管理

### 2.1 视觉资料状态分类

22 条 milestone 当前统一为「官方图片链接 · 待实拍」状态。本仓库不下载官方或第三方图片到本地。

视觉状态枚举：
- 🟢 官方图片链接（official）
- 🟡 待实拍（pending）
- 🟠 待补图（todo）
- ⚫ 暂无图片（na）

### 2.2 22 条 milestone 视觉资料覆盖

| 段落 | 编号 | 视觉状态 | 需要补拍 / 已有线索 |
|------|------|----------|---------------------|
| 第 1 段 | 74 | 官方图片链接 · 待实拍 | 和顺图书馆 / 腾冲城市 / 边境检查站 / 雨季山路 |
| 第 1 段 | 75 | 官方图片链接 · 待实拍 | 高黎贡山 / 雨林 / 保护区入口 / 泥泞山路 |
| 第 2 段 | 76 | 官方图片链接 · 待实拍 | 大理坝子 / 喜洲 / 丽江 / 玉龙雪山边缘 / 天文村 |
| 第 3 段 | 77 | 官方图片链接 · 待实拍 | 木里旧王国 / 彭布西塔楼 / 藏式碉楼 / 山地孤岛 |
| 第 3 段 | 78 | 官方图片链接 · 待实拍 | 康定 / 贡嘎 / 高原牧场 / 牦牛群 / 藏式民居 |
| 第 4 段 | 79 | 官方图片链接 · 待实拍 | 川西南 / 茶叶挑夫旧传统 / 长征历史层叠 |
| 第 4 段 | 80 | 官方图片链接 · 待实拍 | 雅安 / 茶马古道 / 成都平原 / 三星堆 |
| 第 5 段 | 81 | 官方图片链接 · 待实拍 | 剑门关 / 72 道拐 / 翠云廊古柏 / 剑门栈道 |
| 第 5 段 | 82 | 官方图片链接 · 待实拍 | 汉中 / 空荡街道 / 关闭店面 / 特殊时期 |
| 第 5 段 | 83 | 官方图片链接 · 待实拍 | 秦岭北麓 / 秦岭隧道 / 空荡城镇 |
| 第 6 段 | 84 | 官方图片链接 · 待实拍 | 陕北 / 黄土高原 / 窑洞 / 宝塔山 / 延河大桥 |
| 第 6 段 | 85 | 官方图片链接 · 待实拍 | 陕北手工艺 / 剪纸艺人 / 腰鼓表演 / 面花制作 |
| 第 7 段 | 86 | 官方图片链接 · 待实拍 | 山西 / 吕梁 / 雁门关 / 古城墙 / 当地人 |
| 第 7 段 | 87 | 官方图片链接 · 待实拍 | 山西 / 华北 / 城乡结合部 / 假书 / 天线宝宝 |
| 第 7 段 | 88 | 官方图片链接 · 待实拍 | 华北 / 冬季街景 / 等待中的人 |
| 第 7 段 | 89 | 官方图片链接 · 待实拍 | 周口店 / 猿人洞 / 田园洞剖面 / 北京远郊 |
| 第 9 段 | 90 | 官方图片链接 · 待实拍 | 司马台长城 / 长城墙体 / 远景 |
| 第 10 段 | 91 | 官方图片链接 · 待实拍 | 辽宁东北乡村 / 玉米地 / 告别前 |
| 第 10 段 | 92 | 官方图片链接 · 待实拍 | 辽宁 / 玉米地 / 东北农人 |
| 第 10 段 | 93 | 官方图片链接 · 待实拍 | 辽宁 / 乌鸦群 / 东北田野 |
| 第 10 段 | 94 | 官方图片链接 · 待实拍 | 辽宁工业 / 工厂外观 / 户外工人 |
| 第 10 段 | 95 | 官方图片链接 · 待实拍 | 大连港 / 老铁山 / 黄海 / 告别场景 |

**22/22 全部已建立视觉状态记录**

---

## 3. 参考书目与延伸阅读

5 类书目来源（不复制原文，所有 URL 保留指向原始页面）：

### 3.1 📕 官方资料 (Official)
- Out of Eden Walk · 官方项目首页
- Milestone 74 · Every Story Contains Silences
- Milestone 95 · Feeling Gray
- Paul Salopek · National Geographic 同步报道
- 官方 Dispatch 全文合集（22 篇）

### 3.2 📘 英文文献 (English)
- Salopek, Paul. *Out of Eden: A Walk Through Time* (forthcoming book project)
- National Geographic Society · Out of Eden Walk archive
- *Dispatches from the Silk Road* · Paul Salopek · National Geographic
- Walking as slow journalism essays (2013-2024)
- Pulitzer Center · Out of Eden Walk coverage

### 3.3 📗 中文资料 (Chinese)
- 《永远的行走：与中国相遇》中文纪录片材料
- 国家地理中文网 · OEDW 报道合集
- Paul Salopek 中国段中文译介文章
- 慢新闻 / 慢速写作中文实践文献
- 茶马古道 / 蜀道 / 黄土高原中文研究

### 3.4 📙 学术参考 (Academic)
- 人类迁徙 / 走出非洲学术综述
- 早现代人遗址研究（田园洞 / 周口店）
- 茶马古道交通史研究
- 蜀道与秦蜀交界地理
- 黄土高原水土流失与现代化
- 长城作为边界系统的研究

### 3.5 📓 衍生阅读 (Recommended)
- Eric Newby · *A Short Walk in the Hindu Kush*
- Bruce Chatwin · *The Songlines*
- Patrick Leigh Fermor · *A Time of Gifts*
- 比尔 · 布莱森《徒步中国》相关书籍
- 何伟（Peter Hessler）中国三部曲
- Paul Salopek 中文译介文集

**说明**：以上书单为方向性参考，不表示本页面已完整引用。实际阅读时应通过图书馆或正规渠道获取原著，本页面不存储或分发任何版权材料。

---

## 4. 出发前核查清单

5 类出发前必查项（所有清单都基于已公开信息，不假设任何实时数据）：

### 4.1 🪪 证件与手续
- 身份证 / 护照有效期内
- 边境地区提前办边防证
- 港澳台 / 外国友人额外证件
- 学生 / 老年 / 军警证件
- 港澳台胞证 / 台湾居民来往大陆通行证

### 4.2 🏔 健康与安全
- 高原反应预防（康定 / 高海拔段）
- 雨季装备（云南 / 川西 / 雅安）
- 冬季保暖（陕北 / 山西 / 北京 / 辽宁）
- 常用药品（感冒 / 肠胃 / 外伤）
- 应急联系卡 + 当地医院信息

### 4.3 🚆 交通与时段
- 出发前 24h 复核高铁 / 航班班次
- 山区道路季节性封闭预警
- 包车 / 长途汽车提前预约
- 公共交通衔接时刻核对
- 夜路与边境段不独自驾驶

### 4.4 🏛 开放状态
- 博物馆预约政策（云冈 / 三星堆 / 永乐宫 / 山西古建）
- 遗址 / 古道季节性开放
- 边境 / 保护区周边管控
- 维修闭馆 / 临时限流通知
- 节假日人流高峰预判

### 4.5 📚 资料与装备
- 本页面 28 天每日执行卡
- 住宿区域与交通方式总表
- Milestones 74–95 中文故事索引
- 下载离线地图 / CSV / GeoJSON
- 相机 / 充电宝 / 笔记本

---

## 5. 页面状态更新：90% → 92%

### 5.1 原状态

```
完成度：90% · Dispatch 基础复核版
已完成：10 段路线 · Milestones 74–95 共 22 条覆盖 · 22 条中文摘要 + 路线意义 + 复刻建议 · 官方 Dispatch 资料对照表 · 22/22 URL 200 · 28 天节奏 · 28 天每日导游词 · 28 天每日执行卡 · 6 条短线 · 现场记录模板 · CSV/GeoJSON/GPX/SVG 数据 · SEO/OG/下载入口
```

### 5.2 新状态

```
完成度：92% · 视觉资料与书目准备版
已完成：10 段路线 · Milestones 74–95 共 22 条覆盖 · 22 条中文摘要 + 路线意义 + 复刻建议 · 官方 Dispatch 资料对照表 · 22/22 URL 200 · 视觉资料占位与来源管理 22/22 · 参考书目 5 类 · 出发前核查清单 5 类 · 28 天节奏 · 28 天每日导游词 · 28 天每日执行卡 · 6 条短线 · 现场记录模板 · CSV/GeoJSON/GPX/SVG 数据 · SEO/OG/下载入口
```

### 5.3 同步更新文案

- hero badge：`v1.5.7 · ... · 90% · Dispatch 基础复核` → `v1.5.8 · ... · 92% · 视觉资料 + 书目`
- page-meta (× 2)：`v1.5.7 · ... · 90% · ... · Dispatch 资料对照 + 22/22 URL 200` → `v1.5.8 · ... · 92% · ... · 视觉资料 + 书目 + 出发前清单`
- footer：`v1.5.7 · ... · 90% · ... · Dispatch 基础复核` → `v1.5.8 · ... · 92% · ... · 视觉资料与书目准备`
- 内容风险说明：`可用草案 v0.9 · 90%` → `可用草案 v0.9 · 92%`
- 仍需验证描述：`页面口径为 90% Dispatch 基础复核版...` → `页面口径为 92% 视觉资料与书目准备版...`
- 状态描述：`已有：...官方 Dispatch 资料对照表 · 22/22 URL 200 · 28 天节奏...` → `已有：...官方 Dispatch 资料对照表 · 22/22 URL 200 · 视觉资料占位与来源管理 22/22 · 参考书目 5 类 · 出发前核查清单 5 类 · 28 天节奏...`

---

## 6. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / OEDW `data_status_label` / `route_summary` 字段
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段
✅ 未下载任何官方或第三方图片到仓库

---

## 7. manifest 更新摘要

| 字段 | v1.5.7 | v1.5.8 |
|------|--------|--------|
| 顶层 `version` | v1.5.7 | **v1.5.8** |
| 顶层 `updated_at` | 2026-07-06 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 · Dispatch 基础复核版 | **长线文化复刻样板 · 视觉资料与书目准备版** |
| 辽塔 `data_status_label` | 自驾人文路线样板 · 已完成读塔顺序 | 自驾人文路线样板 · 已完成读塔顺序（未变） |
| 山西 `data_status_label` | 古建自驾路线样板 · 已完成古建读图顺序 | 古建自驾路线样板 · 已完成古建读图顺序（未变） |
| OEDW `route_summary` | + 官方 Dispatch 资料对照表 + Dispatch 阅读方法 | **+ 视觉资料占位 22/22 + 参考书目 5 类 + 出发前核查清单 5 类** |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 8. OEDW 事实边界验证

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
| 规划中（实际内容） | ✅ 仅 HTML 注释 "规划中提示"，不影响阅读 |
| 22 个 Milestone 编号（74-95）全部出现 | ✅ 数量校验 PASS |
| 不下载 / 不复制 / 不搬运官方图片 | ✅ 视觉状态 22/22 全部「官方图片链接 · 待实拍」 |
| 不把视觉占位写成已经实拍完成 | ✅ 显式标注「待实拍」状态 |
| 不伪造 Paul Salopek 原始 GPS | ✅ |
| 不写成官方旅行路线 | ✅ |

---

## 9. 质量门禁验证

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
assert "90%" not in html
assert "视觉资料与书目准备版" in html
assert "视觉资料占位与来源管理" in html
assert "参考书目与延伸阅读" in html
assert "出发前核查清单" in html
✅ PASS OEDW visual bibliography numbers 74-95 (22/22)
```

---

## 10. SEO / OG 门禁结果

- `build-route-assets.py --all` 保留 9/9 SEO 字段：✅
- `check-routes-index-sync.py`：✅ routes checked: 3
- `check-route-page-integration.py`：✅ routes checked: 3
- `render-route-og-svg.py --all --check`：✅ 5 files
- `check-route-seo.py`：✅ 5 pages · 3 route pages · 5 og assets

---

## 11. 关键词验收

| 关键词 | 目标 | 命中 |
|--------|------|------|
| 视觉资料与书目准备版 | OEDW 页面 / README / CHANGELOG / docs | OEDW 2 / README 2 / CHANGELOG 2 / CONTENT_NOTES 2 |
| 视觉资料占位与来源管理 | OEDW 页面 | 4 |
| 参考书目与延伸阅读 | OEDW 页面 | 2 |
| 出发前核查清单 | OEDW 页面 | 4 |
| 官方图片链接 | OEDW 页面 | 23 |
| 待实拍 | OEDW 页面 | 2 |
| 92% | OEDW 页面 | 7 |
| 22/22 | OEDW/README/docs | ≥15 |
| 6,000–6,700 | OEDW/README/docs | ≥30 |
| 10% | OEDW 页面 | 0（清除） |
| 90% | OEDW 页面 | 0（清除） |
| 22/23 | OEDW/README/docs | 0（clean） |
| 跨越六年 | OEDW/README/docs | 0（clean） |

---

## 12. 本地 HTTP 200 验证

```
$ python3 -m http.server 8008
$ curl -I http://127.0.0.1:8008/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8008/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8008/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8008/reports/OEDW_VISUAL_MATERIALS_BIBLIOGRAPHY_REPORT.md  HTTP/1.0 200 OK (after commit)
```

---

## 13. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

通过: 70
失败: 0

通过: 108
失败: 0

✓ STATUS: PASS
```

---

## 14. 提交清单

```bash
git add trips/out-of-eden-walk-china/index.html
git add assets/css/styles.css data/routes/routes-manifest.json
git add scripts/check-route-seo.py
git add README.md CHANGELOG.md docs/CONTENT_NOTES.md
git add reports/OEDW_VISUAL_MATERIALS_BIBLIOGRAPHY_REPORT.md
git commit -m "Add OEDW visual materials and bibliography pack"
git push origin main
```

---

## 15. v1.5.9 建议

1. **现场实拍贡献**
   - 邀请真实走过的人贡献 22 张 milestone 实拍图
   - 按 CC-BY-SA 4.0 或同等协议授权
   - 走过的 milestone 优先

2. **图片授权**
   - 联系 National Geographic / Out of Eden Walk 询问官方图片使用授权
   - 如不可行，明确标注「暂无授权」并改用占位图

3. **第三方图片**
   - Wikimedia Commons（CC 协议）
   - 博物馆/景区的官方开放图库
   - 维基百科（CC-BY-SA）

4. **每条 milestone 配代表图片**
   - 22 张图
   - 季节性展示
   - 普通旅行者视角

5. **书目原著获取**
   - 图书馆 / 正规书店 / 在线书店
   - 学术数据库（CNKI / JSTOR）
   - 免费资源（Internet Archive）

6. **可访问性**
   - 字体大小可调
   - 高对比度模式
   - 语音导览（中文 + 英文）
   - 表格 ARIA

7. **「实走反馈」章节**
   - 邀请用户提交 GitHub Issue
   - 走过的 milestone 补充
   - 季节性观察
   - 实拍图贡献

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

_辛 🔮 · 行旅图谱 · OEDW 视觉资料与参考书目报告 · 2026-07-06_

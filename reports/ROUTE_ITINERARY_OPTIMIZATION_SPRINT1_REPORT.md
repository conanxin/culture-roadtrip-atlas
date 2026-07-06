# 行旅图谱 · 线路优化专项 Sprint 1 · v1.5.3

> Route Itinerary Optimization Sprint 1
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | 4bfb825 (Phase 12 report backfill) |
| **新 commit** | 87183c4 · Optimize route itineraries for three routes（v1.5.3 主交付 · 12 files · 1,087+ lines）|
| **push 状态** | ✅ origin/main 已推送（87183c4）|
| **部署状态** | ✅ GitHub Pages 已部署（Deploy run 28768199695 · 27s · success）|
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 5/5 endpoints 200 |
| **线上 HTTP 200** | ✅ 6/6 endpoints 200 |
| **GitHub Actions run** | ✅ Route Data Quality Gate · run 28768199673 · 10s · success |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +200 | 28 天推荐节奏表 + 6 条短线升级 + OEDW 取舍原则 |
| `trips/liao-tower-roadtrip/index.html` | M | +190 | 9 天优化版 + 5 天压缩版 + 12 天深度版 + 辽塔取舍原则 |
| `trips/shanxi-ancient-architecture-roadtrip/index.html` | M | +200 | 路线总览 4 主题 + 10–12 天标准版 + 7 天压缩版 + 15 天深度版 + 山西取舍原则 |
| `assets/css/styles.css` | M | +195 | .itinerary-optimization-section / .itinerary-table / .route-choice-principles / .route-intensity-badge 等 14 个新类 |
| `data/routes/routes-manifest.json` | M | +12 | v1.5.3 + 3 条路线 data_status_label / route_summary 更新 |
| `index.html` | M | +3 | 路线数据索引入口区增加「压缩版/标准版/深度版」说明 |
| `routes/index.html` | M | +3 | 路线数据资产总览后增加「不同时间预算下的线路版本」说明 |
| `README.md` | M | +12 | v1.5.3 当前版本 + 描述 |
| `CHANGELOG.md` | M | +90 | v1.5.3 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +18 | 线路优化专项章节 |
| `scripts/check-route-seo.py` | M | +2 | manifest version 接受 v1.5.2 / v1.5.3 |
| `reports/ROUTE_ITINERARY_OPTIMIZATION_SPRINT1_REPORT.md` | A | +500 | 本报告 |

---

## 2. OEDW 优化内容

### 2.1 28 天推荐节奏表

- 13 段：腾冲 / 大理 / 丽江 / 康定 / 雅安 / 成都 / 剑门关 / 西安 / 延安 / 吕梁 / 大同 / 北京 / 承德 / 大连
- 字段：天数 / 区域+过夜 / 主要移动 / 当日主题 / 核心看点 / 可压缩（高/中/低 badge）/ 取舍建议
- 标注高风险段：高黎贡山、康定折多山、边境段

### 2.2 6 条短线年度分段完成版本

| 短线 | 天数 | 入口 | 出口 | 难度 |
|------|------|------|------|------|
| 云南线 | 7 | 昆明/腾冲 | 丽江 | 中 |
| 川西线 | 7–8 | 丽江/康定 | 成都 | 高 |
| 蜀道秦岭线 | 5 | 成都/广元 | 西安 | 中 |
| 陕北山西线 | 5 | 西安 | 大同/忻州 | 中 |
| 北京长城线 | 5 | 北京 | 北京/古北水镇 | 低 |
| 东北收束线 | 7 | 北京/承德 | 大连 | 中 |

每条短线补齐：建议天数 / 入口城市 / 出口城市 / 推荐交通 / 适合人群 / 核心看点 / 最佳季节 / 难度 / 不可错过 / 可以删减 / 不建议做法。

### 2.3 OEDW 取舍原则

- 如果只走 7 天：优先云南线或北京长城线
- 如果走 14 天：云南 + 川西，或北京 + 承德 + 大连
- 如果做写作/摄影项目：按"人/路/地貌/边界/城市"五主题
- 核心提示：这条路线的核心不是打卡，而是慢新闻观察

---

## 3. 辽塔优化内容

### 3.1 9 天优化版自驾节奏表

- 9 段：锦州 / 义县 / 北镇 / 朝阳 / 赤峰 / 巴林左旗 / 宁城 / 承德 / 北京
- 字段：Day / 过夜地 / 主要路段 / 核心景点 / 驾驶强度 / 参观强度 / 当日重点 / 备选删减
- 主轴核心：奉国寺、朝阳北塔、庆州白塔、辽上京、大明塔

### 3.2 5 天压缩版

- D1 北京 → 锦州
- D2 义县：奉国寺 + 万佛堂石窟
- D3 朝阳：朝阳北塔 + 北塔博物馆
- D4 赤峰 / 巴林左旗：庆州白塔
- D5 辽上京或大明塔二选一 → 返程衔接

### 3.3 12 天深度版

- D1–D2 锦州 + 义县
- D3–D4 北镇 + 牛河梁
- D5–D7 朝阳三夜
- D8–D9 赤峰 + 巴林左旗
- D10–D11 宁城 + 承德
- D12 承德 → 北京

### 3.4 辽塔路线取舍原则

- 时间不足优先保留：奉国寺、朝阳北塔、庆州白塔、辽上京、大明塔
- 博物馆型旅行者优先保留：北塔博物馆、朝阳博物馆、赤峰辽文化博物馆
- 自然/地理型旅行者可加入：医巫闾山、牛河梁
- 亲子/轻松型不建议连续 9 天高强度换城

---

## 4. 山西优化内容

### 4.1 路线总览 4 主题拆分

- 北部：石窟与辽金木构（大同 / 应县 / 五台山）
- 中部：晋祠与平遥体系（太原 / 晋中）
- 南部：壁画与道教建筑（临汾 / 运城）
- 晋东南：早期木构（长治 / 晋城）

### 4.2 10–12 天标准版

12 段：云冈 / 悬空寺 / 应县 / 五台山 / 太原 / 平遥 / 介休 / 临汾 / 隰县 / 运城 / 长治 / 晋城。

### 4.3 7 天压缩版

7 段：云冈 / 应县 / 五台山 / 太原 / 平遥 / 临汾或运城二选一 / 晋东南。

### 4.4 15 天深度版

9 段：放慢节奏，每 3–4 天安排一个低强度日。

### 4.5 山西古建取舍原则

- 初次山西古建：优先大同、应县、五台山、晋祠、平遥
- 壁画爱好者：永乐宫、小西天、青莲寺
- 木构爱好者：佛光寺、南禅寺、应县木塔、晋祠、镇国寺
- 注意事项：不建议一天塞 5 个以上古建点 / 不建议不查开放状态就跨城赶点

---

## 5. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据  
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / `data_status_label` / `route_summary` 字段  
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段 + 12 字段统计

---

## 6. manifest 更新摘要

| 字段 | v1.5.2 | v1.5.3 |
|------|--------|--------|
| 顶层 `version` | v1.5.2 | **v1.5.3** |
| 顶层 `updated_at` | 2026-07-05 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 | **长线文化复刻样板 · 已完成线路优化** |
| OEDW `route_summary` | 从滇西边境到大连黄海... | ...已补充 28 天推荐节奏 + 6 条年度短线 + 取舍原则 |
| 辽塔 `data_status_label` | 自驾人文路线样板 | **自驾人文路线样板 · 已完成线路优化** |
| 辽塔 `route_summary` | 北京出发的辽塔巡礼... | ...已补充 5 天压缩版 / 9 天优化版 / 12 天深度版 + 取舍原则 |
| 山西 `data_status_label` | 古建自驾路线样板 | **古建自驾路线样板 · 已完成线路优化** |
| 山西 `route_summary` | 串联大同、应县、五台山... | ...已补充 7 天压缩版 / 10–12 天标准版 / 15 天深度版 + 取舍原则 |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 7. 事实边界验证

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除 | ✅ 仅历史审计报告 |
| OEDW 「22/23」 清除 | ✅ 仅历史审计报告 |
| OEDW Milestones 74–95 = 22/22 | ✅ 26 处命中 |
| OEDW 6,000–6,700 公里保留 | ✅ 36 处命中 |
| 三条路线数据声明保留 | ✅ 文化复刻粗点 / 文化自驾粗点 / 非实时导航 / not for navigation |
| 山西路线 3 项声明保留 | ✅ 文化自驾粗点 / 非实时导航 / 不保证开放状态 |

---

## 8. 质量门禁验证

```
$ python3 scripts/build-route-assets.py --all
✅ manifest updated · 9/9 SEO 字段保留

$ python3 scripts/build-route-assets.py --check
✅ PASS · routes: 3

$ python3 scripts/validate-route-data.py --all --manifest-check
✅ PASS · routes: 3

$ python3 scripts/render-route-map-svg.py --all --check
✅ PASS · routes: 3

$ python3 scripts/check-routes-index-sync.py
✅ PASS · routes checked: 3

$ python3 scripts/check-route-page-integration.py
✅ PASS · routes checked: 3

$ python3 scripts/render-route-og-svg.py --all --check
✅ PASS · 5 files

$ python3 scripts/check-route-seo.py
✅ PASS · 5 pages · 3 route pages · 5 og assets

$ bash scripts/verify-site.sh
✅ 108/108 门禁全 PASS
```

---

## 9. 关键词验收

| 关键词 | 目标 | 命中 |
|--------|------|------|
| 28 天推荐节奏 | OEDW | 2 |
| 如何取舍这条长线 | OEDW | 1 |
| 5 天压缩版 | 辽塔 | 3 |
| 9 天优化版自驾节奏 | 辽塔 | 2 |
| 12 天深度版 | 辽塔 | 4 |
| 10–12 天标准版 | 山西 | 2 |
| 7 天压缩版 | 山西 | 2 |
| 15 天深度版 | 山西 | 2 |
| 山西古建取舍原则 | 山西 | 2 |
| 线路优化专项 | README/CHANGELOG/docs | 1+ |
| 跨越六年 清除 | clean | ✅ |
| 22/23 清除 | clean | ✅ |
| 22/22 保留 | ≥20 | 26 |
| 6,000–6,700 保留 | ≥30 | 36 |

---

## 10. SEO / OG 门禁结果

- **build-route-assets.py --all 保留 9/9 SEO 字段**：✅
- **check-routes-index-sync.py**：✅ routes checked: 3
- **check-route-page-integration.py**：✅ routes checked: 3
- **render-route-og-svg.py --all --check**：✅ 5 files
- **check-route-seo.py**：✅ 5 pages · 3 route pages · 5 og assets

---

## 11. 本地 HTTP 200 验证

```
$ python3 -m http.server 8002
$ curl -I http://127.0.0.1:8002/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8002/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8002/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8002/trips/liao-tower-roadtrip/                      HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8002/trips/shanxi-ancient-architecture-roadtrip/    HTTP/1.0 200 OK
```

---

## 12. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

通过: 108
失败: 0

✓ STATUS: PASS
```

---

## 13. 提交清单

```bash
git add trips/out-of-eden-walk-china/index.html
git add trips/liao-tower-roadtrip/index.html
git add trips/shanxi-ancient-architecture-roadtrip/index.html
git add assets/css/styles.css data/routes/routes-manifest.json
git add index.html routes/index.html
git add README.md CHANGELOG.md docs/CONTENT_NOTES.md
git add scripts/check-route-seo.py
git add reports/ROUTE_ITINERARY_OPTIMIZATION_SPRINT1_REPORT.md
git commit -m "Optimize route itineraries for three routes"
git push origin main
```

---

## 14. Sprint 2 建议

1. **OEDW 摄影 / 写作工作流包**
   - 7 个主题点（人 / 路 / 地貌 / 边界 / 城市 / 时令 / 文字）的拍摄 / 写作建议
   - 每段一两个推荐观察位置

2. **辽塔辽代都城体系图**
   - 5 京（上京 / 中京 / 东京 / 南京 / 西京）地理与时间轴
   - 捺钵制度图谱

3. **山西古建朝代轴**
   - 唐 / 五代 / 宋 / 辽 / 金 / 元 / 明 / 清 8 代时间轴
   - 每朝代代表古建与山西位置

4. **跨路线组合包**
   - OEDW 北京段 + 辽塔 5 天压缩版 联动
   - OEDW 陕北山西线 + 山西 5 天压缩版 联动

5. **季节性优化**
   - 春季（杏花 / 油菜花 / 桃花）
   - 夏季（避暑 / 雨季 / 高山草甸）
   - 秋季（彩林 / 稻田 / 胡杨）
   - 冬季（雪景 / 春节 / 寒地文化）

6. **儿童 / 亲子 / 老人版本**
   - 减少每日换城次数
   - 增加博物馆与户外平衡
   - 减少长驾驶段

7. **可持续旅游版**
   - 公共交通衔接优化
   - 当地住宿与饮食建议区域
   - 文化遗产保护建议

---

_辛 🔮 · 行旅图谱 · 线路优化专项 Sprint 1 报告 · 2026-07-06_

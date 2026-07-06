# 行旅图谱 · 线路随身导游手册 Sprint 2 · v1.5.4

> Route Itinerary Field Guide Sprint 2
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | 4e73592 (Sprint 1 报告回填) |
| **新 commit** | _pending_（commit 后回填） |
| **push 状态** | _pending_ |
| **部署状态** | _pending_ |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | ✅ 5/5 endpoints 200 |
| **线上 HTTP 200** | _pending_（push 后回填） |
| **GitHub Actions run** | _pending_ |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `trips/out-of-eden-walk-china/index.html` | M | +180 | 28 天每日导游词 + 现场记录模板 + 拍摄建议 + 今日不要硬加点 |
| `trips/liao-tower-roadtrip/index.html` | M | +200 | 9 天每日导游词 + 核心点停留时长 + 读塔顺序 + 拍摄建议 + 今日不要硬加点 + 错字修正 |
| `trips/shanxi-ancient-architecture-roadtrip/index.html` | M | +210 | 12 天每日导游词 + 核心古建停留时长 + 古建读图顺序 + 拍摄建议 + 今日不要硬加点 |
| `assets/css/styles.css` | M | +213 | .field-guide-section / .field-guide-table / .duration-badge / .reading-sequence / .do-not-add-note 等 14 个新类 |
| `data/routes/routes-manifest.json` | M | +9 | v1.5.4 + 3 路线 data_status_label / route_summary 更新 |
| `scripts/check-route-seo.py` | M | +1 | manifest version 接受 v1.5.2 / v1.5.3 / v1.5.4 |
| `index.html` | M | +3 | 「每日导游词 / 停留时长 / 拍摄点 / 读图顺序」说明 |
| `routes/index.html` | M | +3 | 「现场导览信息 / 每日导游词 / 停留时长」说明 |
| `README.md` | M | +15 | v1.5.4 当前版本 + 描述 |
| `CHANGELOG.md` | M | +88 | v1.5.4 详细变更日志 |
| `docs/CONTENT_NOTES.md` | M | +20 | v1.5.4 章节 + cleanup 说明 |
| `docs/CONTENT_NOTES.md` (cleanup) | M | +1 | 「Phase 13」 → 「线路优化专项 v1.5.3 (Route Itinerary Optimization Sprint 1)」 |
| `reports/ROUTE_ITINERARY_OPTIMIZATION_SPRINT1_REPORT.md` (cleanup) | M | +1 | 「Phase 13 章节」 → 「线路优化专项章节」 |
| `CHANGELOG.md` (cleanup) | M | +1 | 辽塔「辆牲」错字 → 「牺牲」 |
| `reports/ROUTE_ITINERARY_FIELD_GUIDE_SPRINT2_REPORT.md` | A | +500 | 本报告 |

---

## 2. cleanup 结果

### 2.1 Phase 13 误写

- 命中位置：docs/CONTENT_NOTES.md (line 839) · reports/ROUTE_ITINERARY_OPTIMIZATION_SPRINT1_REPORT.md (line 35)
- 修正：
  - `## Phase 13 · 线路优化专项 v1.5.3 (2026-07-06)` → `## 线路优化专项 v1.5.3 (Route Itinerary Optimization Sprint 1) (2026-07-06)`
  - `Phase 13 章节` → `线路优化专项章节`
- 未来建议中的 "Phase 13 建议" 上下文未动（PHASE12 报告中的"Phase 13 建议"是当时对未来工作的预测，本轮 v1.5.4 已经是新的实际工作）

### 2.2 辽塔错字「辆牲」 → 「牺牲」

- 命中位置：trips/liao-tower-roadtrip/index.html (line 3058) · CHANGELOG.md (line 18)
- 修正：
  - 「会辆牲北镇、牛河梁、部分博物馆与部分博物馆型深度」 → 「会牺牲北镇、牛河梁和部分博物馆与部分博物馆型深度」
  - 「辆牲北镇 / 牛河梁 / 部分博物馆」 → 「牺牲北镇 / 牛河梁 / 部分博物馆」
- 其他位置的「辆牲」为本次新增的「修正错字」说明（CHANGELOG/README/CONTENT_NOTES 中明确写"修正「辆牲」错字为「牺牲」"），属正常文档记录

---

## 3. OEDW 优化内容

### 3.1 28 天每日导游词

- 28 段：腾冲 / 和顺 / 高黎贡山 / 大理 / 喜洲·洱源 / 丽江 / 玉龙雪山边缘 / 康定 / 雅安 / 成都平原 / 三星堆·广汉 / 剑门关 / 汉中·秦岭 / 西安 / 宜君·黄土 / 延安 / 黄河沿线 / 吕梁 / 忻州·雁门关 / 周口店·田园洞 / 卢沟桥 / 天安门·中轴线 / 胡同·小汤山 / 司马台·古北口 / 承德 / 辽宁乡村 / 大连港 / 黄海
- 字段：天数 / 今日导游词 / 建议停留（短/中/长 badge）/ 现场观察 / 拍摄记录点 / 今日不要硬加点
- 高风险地带明确提醒：D3 高黎贡山、D7 玉龙雪山边缘、D11 三星堆闪光、D21 卢沟桥宛平城顶、D27 大连港贸易区

### 3.2 OEDW 现场记录模板

8 个问题 checklist：
- 路 · 今天脚下是什么路？
- 人 · 今天遇见了谁？
- 声 · 今天听到最多的声音是什么？
- 动 · 当地人如何移动？
- 旧 · 这里的旧路还在吗？
- 失 · 这里正在失去什么？
- 得 · 这里正在得到什么？
- 主角 · 如果只写一段慢新闻，今天的主角是谁？

### 3.3 OEDW 拍摄 / 记录建议

5 类（不要只拍「景点」，要拍路如何进入人的生活）：
- 道路 · 路肩 / 岔路 / 桥 / 隧道 / 旧道痕迹
- 人 · 摊主 / 司机 / 村民 / 游客 / 修路工
- 地貌 · 山口 / 河谷 / 塬梁 / 海岸
- 边界 · 城门 / 关口 / 长城 / 港口 / 行政边界
- 日常 · 早餐店 / 公交站 / 学校 / 集市 / 广场

---

## 4. 辽塔优化内容

### 4.1 9 天每日导游词

9 段：北京→锦州 / 义县 / 北镇 / 朝阳 / 朝阳→赤峰 / 庆州白塔 / 辽上京 / 辽中京·大明塔·承德 / 承德→北京
- 字段：Day / 今日导游词 / 建议停留 / 拍摄点 / 读图顺序 / 今日不要硬加点

### 4.2 核心点建议停留时长

10 点表格（仅区间，不写门票与实时开放时间）：
- 奉国寺（2–3h）/ 万佛堂石窟（1h）/ 朝阳北塔 + 北塔博物馆（2–3h）/ 庆州白塔（1–2h）/ 辽上京遗址 + 博物馆（半天）/ 大明塔（1h）/ 北镇庙（1–2h）/ 牛河梁国家考古遗址公园（半天）/ 赤峰辽文化博物馆（1–2h）/ 承德避暑山庄（半天）

### 4.3 如何读一座辽塔

6 步读图顺序（不要一到塔前就拍全景）：
1. 看位置：城里 / 山前 / 寺院中 / 旧都城附近
2. 看轮廓：方 / 八角 / 密檐 / 楼阁式 / 混合形态
3. 看基座：须弥座 / 力士 / 莲瓣 / 栏板
4. 看塔身：佛龛 / 胁侍 / 飞天 / 供养人
5. 看檐部：密檐层数 / 出檐 / 斗拱痕迹
6. 看环境：今天它和城市 / 村庄 / 道路的关系

### 4.4 辽塔拍摄与观察建议

6 类：
- 全景 · 远处看塔与城市 / 山体关系
- 中景 · 塔身比例与檐部节奏
- 近景 · 佛龛 / 基座 / 砖雕 / 残损
- 逆光 · 塔轮廓
- 侧光 · 砖雕层次
- 黄昏 · 城市天际线

---

## 5. 山西优化内容

### 5.1 12 天每日导游词

12 段：大同 / 浑源 / 应县 / 五台山 / 太原 / 平遥 / 介休·灵石 / 洪洞·临汾 / 隰县 / 运城·芮城 / 长治 / 晋城·高平
- 字段：Day / 今日导游词 / 建议停留 / 读图顺序 / 拍摄点 / 今日不要硬加点

### 5.2 核心古建建议停留时长

16 点表格：
- 云冈石窟（半天）/ 华严寺（1–2h）/ 善化寺（1h）/ 应县木塔（2–3h）/ 佛光寺（2–3h）/ 南禅寺（1h）/ 晋祠（半天）/ 双林寺（2–3h）/ 镇国寺（1h）/ 广胜寺·飞虹塔（2–3h）/ 隰县小西天（2–3h）/ 永乐宫（2–3h）/ 法兴寺（1h）/ 崇庆寺（1h）/ 青莲寺（1h）/ 府城玉皇庙（1h）

### 5.3 如何读一座山西古建

7 步读图顺序（顺序不对，会看不懂）：
1. 看山门与轴线：入口 / 院落 / 殿堂之间如何组织
2. 看台基与屋顶：等级 / 尺度 / 出檐 / 举折
3. 看梁架：柱网 / 斗拱 / 梁枋 / 屋架关系
4. 看塑像：主尊 / 胁侍 / 供养人 / 动态与表情
5. 看壁画：题材 / 人物关系 / 色彩层次 / 叙事方向
6. 看修缮痕迹：新旧材料如何交接
7. 看环境：和村庄 / 县城 / 山势 / 道路是什么关系

### 5.4 古建拍摄与观察建议

6 类：
- 结构 · 柱网 / 梁架 / 斗拱 / 屋顶侧影
- 空间 · 院落轴线 / 山门到大殿的关系
- 细部 · 彩塑面部 / 衣纹 / 手势 / 莲座
- 壁画 · 整铺关系 / 局部人物 / 边框纹样
- 环境 · 村庄 / 道路 / 山势与寺庙位置
- 修缮 · 新旧材料 / 支护 / 保护提示牌
- 提醒：很多古建内部限制拍摄，必须遵守现场规定；不能拍时就用文字记录空间关系

---

## 6. 是否修改数据文件

✅ **未修改** CSV / GeoJSON / GPX / SVG 坐标数据
✅ 仅修改 `data/routes/routes-manifest.json` 的 `version` / `data_status_label` / `route_summary` 字段
✅ `build-route-assets.py --all` 保留 9/9 SEO 字段

---

## 7. manifest 更新摘要

| 字段 | v1.5.3 | v1.5.4 |
|------|--------|--------|
| 顶层 `version` | v1.5.3 | **v1.5.4** |
| 顶层 `updated_at` | 2026-07-06 | **2026-07-06** |
| OEDW `data_status_label` | 长线文化复刻样板 · 已完成线路优化 | **长线文化复刻样板 · 已完成每日导游词** |
| 辽塔 `data_status_label` | 自驾人文路线样板 · 已完成线路优化 | **自驾人文路线样板 · 已完成读塔顺序** |
| 山西 `data_status_label` | 古建自驾路线样板 · 已完成线路优化 | **古建自驾路线样板 · 已完成古建读图顺序** |
| 3 路线 `route_summary` | 仅含版本描述 | **补齐每日导游词 / 停留时长 / 拍摄点 / 读图顺序** |
| 9 SEO 字段 × 3 路线 | 全部保留 | **全部保留** |

---

## 8. 事实边界验证

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除 | ✅ 仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明 |
| OEDW 「22/23」 清除 | ✅ 仅历史审计报告 + ROUTE_SEO_GUIDE.md 元说明 |
| OEDW Milestones 74–95 = 22/22 | ✅ 28 处命中（+2 from Sprint 1） |
| OEDW 6,000–6,700 公里保留 | ✅ 38 处命中（+2 from Sprint 1） |
| 三条路线数据声明保留 | ✅ 文化复刻粗点 / 文化自驾粗点 / 非实时导航 / not for navigation |
| 山西路线 3 项声明保留 | ✅ 文化自驾粗点 / 非实时导航 / 不保证开放状态 |

---

## 9. 质量门禁验证

```
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
| 28 天每日导游词 | OEDW | 2 |
| OEDW 现场记录模板 | OEDW | 2 |
| OEDW 拍摄 | OEDW | 2 |
| 9 天每日导游词 | 辽塔 | 2 |
| 核心点建议停留时长 | 辽塔 | 2 |
| 如何读一座辽塔 | 辽塔 | 2 |
| 辽塔拍摄 | 辽塔 | 2 |
| 12 天每日导游词 | 山西 | 2 |
| 核心古建建议停留时长 | 山西 | 2 |
| 如何读一座山西古建 | 山西 | 2 |
| 古建拍摄 | 山西 | 2 |
| 今日不要硬加点 | trips (3 路线) | 各 1 |
| 每日导游词 | README/CHANGELOG/docs | 4+7+4+1 |
| 停留时长 | trips/README/docs | 多处 |
| 读图顺序 | trips/README/docs | 多处 |
| 辆牲 错字 | trips 已清 | ✅ |
| 跨越六年 清除 | clean | ✅ |
| 22/23 清除 | clean | ✅ |
| 22/22 保留 | ≥25 | 28 |
| 6,000–6,700 保留 | ≥35 | 38 |

---

## 12. 本地 HTTP 200 验证

```
$ python3 -m http.server 8004
$ curl -I http://127.0.0.1:8004/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8004/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8004/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8004/trips/liao-tower-roadtrip/                      HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8004/trips/shanxi-ancient-architecture-roadtrip/    HTTP/1.0 200 OK
```

---

## 13. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

通过: 108
失败: 0

✓ STATUS: PASS
```

---

## 14. 提交清单

```bash
git add trips/out-of-eden-walk-china/index.html
git add trips/liao-tower-roadtrip/index.html
git add trips/shanxi-ancient-architecture-roadtrip/index.html
git add assets/css/styles.css data/routes/routes-manifest.json
git add index.html routes/index.html
git add README.md CHANGELOG.md docs/CONTENT_NOTES.md
git add scripts/check-route-seo.py
git add reports/ROUTE_ITINERARY_FIELD_GUIDE_SPRINT2_REPORT.md
git commit -m "Add field guide details to route itineraries"
git push origin main
```

---

## 15. Sprint 3 建议

1. **OEDW 跨语言版本**
   - 英文版每日导游词
   - 法文版（Paul 母语）

2. **辽塔 / 山西季节专项**
   - 春季（杏花 / 桃花 / 梨花 vs 辽塔）
   - 夏季（草原 vs 大同气候）
   - 秋季（五台山 + 应县木塔秋色 + 晋祠金秋）
   - 冬季（雪中辽塔 + 春节民俗 vs 山西古建）

3. **行前 7 天学习计划**
   - 文献阅读清单
   - 纪录片 / 视频清单
   - 平台实操清单

4. **现场应急卡**
   - 急救电话
   - 天气应对
   - 古建维修闭馆应对
   - 预约政策变化应对

5. **可持续旅游版**
   - 公共交通衔接
   - 当地住宿与饮食
   - 文化遗产保护建议

6. **儿童 / 亲子 / 老人版本**
   - 减少每日换城
   - 增加博物馆与户外平衡
   - 减少长驾驶段

7. **特殊版本**
   - 反向版（黄海→腾冲）
   - 冬日版
   - 雨季版

8. **可访问性**
   - 路线页语音导览
   - 高对比度模式
   - 字体大小可调

---

_辛 🔮 · 行旅图谱 · 线路随身导游手册 Sprint 2 报告 · 2026-07-06_

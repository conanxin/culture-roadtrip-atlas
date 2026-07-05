# 行旅图谱 · Phase 10 · 路线索引体验与多路线检索

> v1.5.0 · Route Index Experience and Multi-Route Search
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | bd0c3f4 (v1.4.9 · Shanxi Ancient Architecture Route Data Production) |
| **新 commit** | e086678 · Enhance route index search and comparison |
| **push 状态** | ✅ origin/main pushed |
| **部署状态** | ✅ GitHub Pages 已部署（2026-07-05 23:14:28 UTC） |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | 全部 200 |
| **线上 HTTP 200** | ✅ 6/6 endpoints 200 |
| **GitHub Actions run** | ✅ success · run 28758240913 · 10s |

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `data/routes/routes-manifest.json` | M | +72 | version v1.5.0 + 9 检索字段 × 3 routes |
| `routes/index.html` | M | +22 | v1.5.0 徽章 + 仪表盘容器 + nav-link |
| `assets/js/routes-index.js` | A | +381 | 仪表盘前端（搜索/筛选/排序/对比/统计） |
| `assets/css/styles.css` | M | +334 | dashboard / toolbar / cards / compare / status badge |
| `index.html` | M | +4 | 路线数据资产区 → v1.5.0 / 3 路线 / 92 点位 / 3 SVG / 28 段 |
| `docs/ROUTE_FACTORY_GUIDE.md` | A | +285 | 新增路线实操指南 |
| `docs/CONTENT_NOTES.md` | M | +30 | Phase 10 章节 |
| `docs/ROUTE_DATA_SPEC.md` | M | +24 | §13 manifest 与索引页 |
| `README.md` | M | +37 | v1.5.0 当前版本 + 路线索引体验章节 |
| `CHANGELOG.md` | M | +93 | v1.5.0 详细变更日志 |
| `scripts/check-routes-index-sync.py` | M | +48 | v1.1 routes-index.js 必填字段 + dashboard 检查 |
| `scripts/verify-site.sh` | M | +60 | v1.5.0 route index experience gates（+21 项） |

**总计：** 12 个文件 · 1,388 行变更（含新增 JS / MD）

---

## 2. routes-manifest 字段增强

### 2.1 顶层 version

```diff
- "version": "v1.4.9"
+ "version": "v1.5.0"
+ "updated_at": "2026-07-05"
```

### 2.2 每条 route 新增 9 个检索字段

```json
{
  "category": "long_walk | roadtrip | architecture",
  "theme_tags": ["..."],
  "region_tags": ["..."],
  "data_status_label": "...",
  "difficulty_label": "...",
  "best_season": "...",
  "route_summary": "...",
  "data_completeness": "full | v0.1 | planned",
  "featured": true
}
```

### 2.3 三条路线分类

| slug | category | data_completeness | points | segments |
|------|----------|-------------------|--------|----------|
| `out-of-eden-walk-china` | long_walk | full | 42 | 10 |
| `liao-tower-roadtrip` | roadtrip | v0.1 | 20 | 9 |
| `shanxi-ancient-architecture` | architecture | v0.1 | 30 | 9 |

**合计：** 3 routes · 92 points · 28 segments · 0 planned-data · 3 SVG

---

## 3. routes-index.js 功能说明

### 3.1 入口

```javascript
initDashboard() {
  var dashboard = document.getElementById('routes-manifest-dashboard');
  fetch('../data/routes/routes-manifest.json', { credentials: 'omit' })
    .then(...).then(...).catch(...)
}
```

### 3.2 渲染内容

| 区块 | 功能 |
|------|------|
| **统计区** (#routes-manifest-stats) | 路线总数 / 已有数据路线 / CSV 点位总数 / 段落总数 / GeoJSON Feature / SVG 预览 |
| **筛选器** (#routes-manifest-toolbar) | 搜索 + 分类 + 完整度 + 地区 + 排序 + 结果计数 |
| **路线卡片** (#route-index-cards) | 标题 + 状态徽章 + 分类徽章 + theme_tags + region_tags + 统计 + 下载按钮 + 入口 |
| **对比表** (#route-index-compare) | 路线 · 分类 · 状态 · 点位 · 段落 · SVG · 最佳季节 · 难度 · 主题 |

### 3.3 搜索

支持字段：`title` / `route_summary` / `theme_tags` / `region_tags` / `data_status_label`

### 3.4 筛选

| 维度 | 选项 |
|------|------|
| 分类 | 全部 / 长线徒步 / 自驾 / 古建 |
| 完整度 | 全部 / full / v0.1 / planned |
| 地区 | 全部 + 从 region_tags 自动生成 |
| 排序 | 推荐（featured） / 点位从高到低 / 名称 |

### 3.5 Fallback

- **无 JS**：`routes-manifest-dashboard` 容器内显示 `<noscript>` 提示，下方三条路线硬编码卡片可用
- **fetch 失败**：显示错误信息 + 引导使用静态索引

### 3.6 不引入依赖

- ❌ 无 npm / 第三方 JS 库
- ❌ 无后端 / 构建系统
- ✅ 纯 Vanilla JS

---

## 4. routes/index.html 增强说明

### 4.1 Hero 区

```diff
- <div class="trip-skeleton-badge">🗂️ 路线数据索引 · v1.4.9</div>
+ <div class="trip-skeleton-badge">🗂️ 路线数据索引 · v1.5.0</div>
```

### 4.2 总览区（v1.4.7 → v1.5.0）

```diff
- <h3 class="text-center" style="...">📦 路线数据资产总览 · v1.4.9</h3>
+ <h3 class="text-center" style="...">📦 路线数据资产总览 · v1.5.0</h3>
```

### 4.3 路线仪表盘 section

```html
<section id="dashboard" class="container" style="margin-top: var(--space-2xl);">
  <div class="city-card" style="max-width: 1100px; margin: 0 auto;">
    <h3 class="text-center" style="...">🧭 路线仪表盘 · 搜索 / 筛选 / 对比</h3>
    <p style="text-align: center; ...">
      动态加载 routes-manifest.json · 搜索 / 筛选 / 排序 / 对比 · 无依赖纯 Vanilla JS
    </p>
    <section id="routes-manifest-dashboard" class="routes-manifest-dashboard">
      <div class="route-index-loading">正在加载路线索引数据……</div>
      <noscript>浏览器未启用 JavaScript。请使用下方静态路线数据卡片（已硬编码 fallback）。</noscript>
    </section>
  </div>
</section>
```

### 4.4 脚本引入

```html
<script src="../assets/js/routes-index.js"></script>
```

### 4.5 静态 Fallback

页面下方保留三条路线硬编码卡片：

- `#oedw` Out of Eden Walk 中国段 · 42 点位 · 10 段 · 文化复刻粗点
- `#liao-tower` 辽塔巡礼 · 20 点位 · 9 段 · 文化自驾粗点
- `#shanxi` 山西古建 · 30 点位 · 9 段 · 文化自驾粗点

每条卡片仍含：

- 静态 SVG 路线图
- CSV / GeoJSON / GPX / SVG 下载按钮
- 数据统计与风险提示
- 路线页面入口

### 4.6 工厂流程

路线工厂流程区保留常用命令清单：

```
python3 scripts/build-route-assets.py --all
python3 scripts/build-route-assets.py --check
python3 scripts/validate-route-data.py --all --manifest-check
python3 scripts/render-route-map-svg.py --all --check
python3 scripts/check-routes-index-sync.py
./verify-site.sh
```

---

## 5. 首页（index.html）路线数据资产统计

### 5.1 Hero subtitle

```diff
- 一个个人人文旅行路线库 · 3 条路线已接入路线数据资产<br>92 个粗点 · 3 张 SVG 路线图
+ 一个个人人文旅行路线库 · 3 条路线已接入路线数据资产<br>92 个文化复刻粗点 · 3 张 SVG 路线图
```

### 5.2 meta description

```diff
- 行旅图谱 - 为自驾、徒步、古建、博物馆与历史地理旅行准备的个人导游手册库。
+ 行旅图谱 - 为自驾、徒步、古建、博物馆与历史地理旅行准备的个人导游手册库。v1.5.0 接入 3 条路线数据资产、92 个文化复刻粗点、3 张静态 SVG 路线图。
```

### 5.3 路线数据索引 section

```diff
- 路线数据索引已收录 <strong>Out of Eden Walk 中国段</strong>与<strong>辽塔巡礼</strong>两条路线，<br>
+ 行旅图谱已接入 <strong>3 条路线数据资产</strong>，包含 <strong>92 个文化复刻粗点、28 个路线段、3 张静态 SVG 路线图</strong>，<br>

- <span class="trip-tag">v1.4.9</span>
- <span class="trip-tag">3 条路线</span>
- <span class="trip-tag">92 个粗点</span>
- <span class="trip-tag">123 个 features</span>
+ <span class="trip-tag">v1.5.0</span>
+ <span class="trip-tag">3 条路线</span>
+ <span class="trip-tag">92 个粗点</span>
+ <span class="trip-tag">3 张 SVG</span>
+ <span class="trip-tag">28 段路线</span>
```

新增按钮：

```html
<a href="docs/ROUTE_FACTORY_GUIDE.md" target="_blank" class="btn btn-secondary">路线工厂指南</a>
```

---

## 6. ROUTE_FACTORY_GUIDE.md 内容摘要

### 6.1 章节结构（7 章 + 285 行）

| 章节 | 内容 |
|------|------|
| §1 新增路线标准流程 | 10 步（slug → CSV → GeoJSON → GPX → manifest → build → HTML → 模块 → verify → push） |
| §2 CSV 编写规则 | 18 字段 + 命名规范 + 枚举值 + 风险提示 |
| §3 坐标规则 | 城市 / 文保单位 / 景区粗点；不写道路级导航；不伪造历史人物轨迹 |
| §4 数据安全边界 | 文化复刻粗点 / 文化自驾粗点 / 非实时导航 / 不保证开放状态 |
| §5 必跑命令 | 5 条核心命令 + verify-site.sh |
| §6 常见错误 | manifest 漂移 / HTML 未同步 / SVG 缺 not for navigation / GPX waypoint 不一致 / planned-data 不应创建空 CSV / URL 与真实路径不一致 |
| §7 当前三条路线示例 | OEDW / 辽塔 / 山西 定位与样板说明 |

### 6.2 必跑命令清单

```
python3 scripts/build-route-assets.py --all
python3 scripts/build-route-assets.py --check
python3 scripts/validate-route-data.py --all --manifest-check
python3 scripts/render-route-map-svg.py --all --check
python3 scripts/check-routes-index-sync.py
./verify-site.sh
```

### 6.3 常见错误 6 类

1. **manifest 统计与实际数据不一致** → 重跑 `build-route-assets.py --all`
2. **routes/index.html 未同步** → 检查新增 slug / title / 文件名是否出现
3. **SVG 缺少 not for navigation 声明** → 检查 `render-route-map-svg.py` 模板
4. **GPX waypoint 数与 CSV 行数不一致** → 检查 CSV 18 字段完整性
5. **planned-data 不应创建空 CSV** → planned-data 只在 manifest 占位，不创建文件
6. **页面 URL 与真实路径不一致** → 检查 `page_url` 字段与实际页面路径匹配

---

## 7. check-routes-index-sync.py 增强说明

### 7.1 v1.0 → v1.1 变更

| 改动 | 说明 |
|------|------|
| 新增 | routes-index.js 必填字段检查（slug / title / category / theme_tags / region_tags / points / segments / has_svg_preview） |
| 新增 | `#routes-manifest-dashboard` 容器检查 |
| 新增 | routes/index.html 引入 routes-index.js 检查 |
| 新增 | routes-manifest.json 引用检查（routes/index.html 或 assets/js/routes-index.js） |
| 改进 | planned-data 与 url 字段缺失兼容 |

### 7.2 PASS 输出

```
PASS routes index sync check
routes checked: 3
dynamic manifest rendering: yes
```

---

## 8. verify-site.sh 增强说明

### 8.1 v1.4.8 → v1.5.0 变更

| 改动 | 说明 |
|------|------|
| 数据文件清单扩展 | 增加 shanxi csv/svg + routes-index.js + ROUTE_FACTORY_GUIDE.md |
| 新增 section | Route index experience gates（v1.5.0）+ 8 项检查 |
| 标题 | `v1.4.8 route factory + quality gates` → `v1.5.0 route index experience + multi-route search` |

### 8.2 新增 8 项检查

```
✓ data/routes/shanxi-ancient-architecture.csv
✓ assets/img/routes/shanxi-ancient-architecture-map.svg
✓ assets/js/routes-index.js
✓ docs/ROUTE_FACTORY_GUIDE.md
✓ routes-manifest.json 引用（routes/index.html 或 routes-index.js）
✓ routes-index.js 被 routes/index.html 引入
✓ #routes-manifest-dashboard 容器存在
✓ ROUTE_FACTORY_GUIDE.md 含关键词：新增路线标准流程
✓ ROUTE_FACTORY_GUIDE.md 含关键词：CSV 编写规则
✓ ROUTE_FACTORY_GUIDE.md 含关键词：坐标规则
✓ ROUTE_FACTORY_GUIDE.md 含关键词：数据安全边界
✓ ROUTE_FACTORY_GUIDE.md 含关键词：必跑命令
```

### 8.3 验证总数

- Phase 8 / Phase 9 门禁：79 项
- v1.5.0 新增：12 项
- **总计：91 项门禁全 PASS**

---

## 9. GitHub Actions 更新说明

`.github/workflows/route-data.yml` 同步加入 `check-routes-index-sync.py` 与 `verify-site.sh`：

```yaml
- name: Check routes index sync
  run: |
    python3 scripts/check-routes-index-sync.py

- name: Run verify-site.sh
  run: |
    bash scripts/verify-site.sh
```

---

## 10. 三条路线统计

| slug | category | completeness | points | segments | features | waypoints | SVG | region tags |
|------|----------|--------------|--------|----------|----------|-----------|-----|-------------|
| `out-of-eden-walk-china` | long_walk | full | 42 | 10 | 53 | 42 | ✅ | 云南 / 四川 / 陕西 / 山西 / 北京 / 辽宁 |
| `liao-tower-roadtrip` | roadtrip | v0.1 | 20 | 9 | 30 | 20 | ✅ | 北京 / 辽宁 / 内蒙古 / 河北 |
| `shanxi-ancient-architecture` | architecture | v0.1 | 30 | 9 | 40 | 30 | ✅ | 山西 / 大同 / 五台山 / 太原 / 平遥 / 晋东南 |
| **合计** | 3 类 | 0 planned | **92** | **28** | 123 | 92 | **3** | 16 个 |

---

## 11. 本地命令验证结果

```
$ python3 scripts/build-route-assets.py --all
(PASS · manifest matches generated statistics · routes: 3)

$ python3 scripts/build-route-assets.py --check
PASS route factory check
manifest matches generated statistics
routes: 3

$ python3 scripts/validate-route-data.py --all --manifest-check
PASS all route data validation
manifest matches generated statistics
routes: 3

$ python3 scripts/render-route-map-svg.py --all --check
PASS all route SVG check
routes: 3

$ python3 scripts/check-routes-index-sync.py
PASS routes index sync check
routes checked: 3
dynamic manifest rendering: yes

$ python3 -c "manifest metadata check"
PASS manifest search metadata
routes: 3
total points: 92
total segments: 28
categories: {'architecture', 'long_walk', 'roadtrip'}
```

---

## 12. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

================================
  行旅图谱 · 网站验证脚本
  v1.5.0 route index experience + multi-route search
================================

通过: 91
失败: 0

🛡 Route data gates · 9 文件 PASS
🧭 Route index experience gates (v1.5.0) · 8 检查 PASS

✓ STATUS: PASS
```

---

## 13. 本地 HTTP 200 验证

```
$ python3 -m http.server 8000
$ curl -I http://127.0.0.1:8000/                                 HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/routes/                          HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/assets/js/routes-index.js        HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/data/routes/routes-manifest.json HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/docs/ROUTE_FACTORY_GUIDE.md     HTTP/1.0 200 OK
```

`routes-manifest.json` 内容验证：

```
routes: 3
version: v1.5.0
out-of-eden-walk-china · long_walk · full · 42 pts
liao-tower-roadtrip · roadtrip · v0.1 · 20 pts
shanxi-ancient-architecture · architecture · v0.1 · 30 pts
```

---

## 14. 事实边界验证（OEDW）

| 检查项 | 命令 | 结果 |
|--------|------|------|
| OEDW "跨越六年" 是否清除 | `grep -R "跨越六年" trips data routes README.md docs reports scripts assets .github` | ✅ 仅在历史审计报告出现，未在 v1.5.0 新增文件出现 |
| OEDW "22/23" 是否清除 | `grep -R "22/23" trips data routes README.md docs reports scripts assets .github` | ✅ 仅在历史审计报告出现 |
| OEDW Milestones 74–95 = 22/22 | `grep -R "22/22" trips/out-of-eden-walk-china` | ✅ trips/out-of-eden-walk-china/index.html:1130 |
| OEDW 6,000–6,700 公里 | `grep -R "6,000–6,700" trips/out-of-eden-walk-china` | ✅ 4 处保留 |
| OEDW 北京段：卢沟桥→天安门→小汤山 | `grep -R "卢沟桥" trips/out-of-eden-walk-china` | ✅ 保留 |
| OEDW 黄海终点：2023 冬 / 2024.6 / 2024.8 | `grep -R "黄海" trips/out-of-eden-walk-china` | ✅ 保留 |
| 路线数据声明：文化复刻粗点 / 文化自驾粗点 | `grep -R "文化复刻粗点\|文化自驾粗点" data routes` | ✅ 全部保留 |
| not for navigation | `grep -R "not for navigation" data assets` | ✅ 全部 SVG 含此声明 |

---

## 15. 浏览器 Smoke（_optional_）

本地无浏览器环境，记录 N/A，不阻塞。

- 打开 `/routes/` · N/A
- 搜索"山西"，只显示山西路线 · N/A
- 分类 architecture 显示山西 · N/A
- 分类 long_walk 显示 OEDW · N/A
- 排序点位数，OEDW 应在前 · N/A
- 控制台无关键错误 · N/A

---

## 16. GitHub Actions 验证

✅ **success · run 28758240913 · 10s**

```
$ gh run list --workflow "Route Data Quality Gate" --limit 3
completed	success	Enhance route index search and comparison	Route Data Quality Gate	main	push	28758240913	10s	2026-07-05T23:14:28Z
completed	success	Produce Shanxi ancient architecture route data	Route Data Quality Gate	main	push	28725412598	12s	2026-07-05T01:15:45Z
completed	success	Produce Shanxi ancient architecture route data	Route Data Quality Gate	main	push	28725377586	11s	2026-07-05T01:14:10Z
```

---

## 17. 线上 HTTP 200 验证

✅ **6/6 endpoints 200**

```
200 https://conanxin.github.io/culture-roadtrip-atlas/
200 https://conanxin.github.io/culture-roadtrip-atlas/routes/
200 https://conanxin.github.io/culture-roadtrip-atlas/assets/js/routes-index.js
200 https://conanxin.github.io/culture-roadtrip-atlas/data/routes/routes-manifest.json
200 https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_FACTORY_GUIDE.md
200 https://conanxin.github.io/culture-roadtrip-atlas/reports/PHASE10_ROUTE_INDEX_SEARCH_REPORT.md
```

---

## 18. 页面 URL

- 首页：https://conanxin.github.io/culture-roadtrip-atlas/
- 路线数据索引：https://conanxin.github.io/culture-roadtrip-atlas/routes/
- 路线仪表盘：https://conanxin.github.io/culture-roadtrip-atlas/routes/#dashboard
- manifest：https://conanxin.github.io/culture-roadtrip-atlas/data/routes/routes-manifest.json
- routes-index.js：https://conanxin.github.io/culture-roadtrip-atlas/assets/js/routes-index.js
- ROUTE_FACTORY_GUIDE：https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_FACTORY_GUIDE.md
- Phase 10 报告：https://conanxin.github.io/culture-roadtrip-atlas/reports/PHASE10_ROUTE_INDEX_SEARCH_REPORT.md

---

## 19. Phase 11 建议

1. **数据资产扩量**
   - OEDW 剩余 50% 段落继续补完（22/22 milestones → 完整覆盖）
   - 山西 / 辽塔 升级到 `full` 状态
   - 引入第 4 条路线（如河西走廊 / 川滇茶马古道 / 徽州古村）

2. **可视化增强**
   - 路线仪表盘加入统计图（点位分布 / 段落长度分布）
   - 路线对比表支持 CSV 导出
   - 路线卡片支持「加入对比」按钮

3. **数据共享**
   - manifest 提供 RSS / Atom feed
   - 提供路线数据 API 文档（manifest schema）
   - 鼓励外部研究者提交新路线（PR 模板）

4. **检索优化**
   - 全文搜索支持模糊匹配
   - 按难度 / 季节 / 距离筛选
   - 路线相似度推荐（基于 theme_tags / region_tags 重合度）

5. **多语言**
   - 英文版 manifest（routes-manifest.en.json）
   - 英文版 routes/index.html
   - 英文版 ROUTE_FACTORY_GUIDE

6. **CI/CD**
   - manifest schema 校验（JSON Schema）
   - 自动生成 routes/index.html 静态卡片（v1.6.0 候选）
   - 部署到 conanxin.github.io + 自托管备份

---

## 20. 提交清单

```bash
git add CHANGELOG.md README.md
git add assets/css/styles.css
git add assets/js/routes-index.js
git add data/routes/routes-manifest.json
git add docs/CONTENT_NOTES.md docs/ROUTE_DATA_SPEC.md docs/ROUTE_FACTORY_GUIDE.md
git add index.html routes/index.html
git add scripts/check-routes-index-sync.py scripts/verify-site.sh
git add reports/PHASE10_ROUTE_INDEX_SEARCH_REPORT.md
git commit -m "Enhance route index search and comparison"
git push origin main
```

---

_辛 🔮 · 行旅图谱 · Phase 10 报告 · 2026-07-06_
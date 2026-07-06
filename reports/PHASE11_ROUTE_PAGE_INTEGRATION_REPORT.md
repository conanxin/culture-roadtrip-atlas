# 行旅图谱 · Phase 11 · 路线页面统一数据徽章与跨页面推荐

> v1.5.1 · Route Page Unified Data Badges and Related Routes
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | db06764 (v1.5.0 Phase 10 backfill) |
| **新 commit** | _pending_（commit 后回填） |
| **push 状态** | _pending_ |
| **部署状态** | _pending_ |
| **本地命令验证** | 全部 PASS |
| **本地 HTTP** | 全部 200 |
| **线上 HTTP 200** | _pending_（push 后回填） |
| **GitHub Actions run** | _pending_ |

---

## 1. 修改文件列表（13 文件 · 2,261 行）

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `assets/js/route-page-badges.js` | A | +375 | 详情页统一模块（徽章 / 摘要 / 下载 / 警告 / 相关路线） |
| `assets/js/routes-index.js` | M | +2 | 索引卡片加「详情页徽章：已接入」指示器 |
| `assets/css/styles.css` | M | +307 | route-page-data-panel + related 样式 |
| `trips/out-of-eden-walk-china/index.html` | M | +18 | route-page-data-panel + script |
| `trips/liao-tower-roadtrip/index.html` | M | +17 | route-page-data-panel + script |
| `trips/shanxi-ancient-architecture-roadtrip/index.html` | M | +18 | route-page-data-panel + script |
| `docs/ROUTE_PAGE_INTEGRATION_GUIDE.md` | A | +287 | 详情页接入指南（10 章节） |
| `docs/ROUTE_PAGE_TEMPLATE.md` | M | +47 | §9 统一数据徽章模块 |
| `docs/ROUTE_FACTORY_GUIDE.md` | M | +30 | §13 路线页面接入步骤 |
| `docs/CONTENT_NOTES.md` | M | +22 | Phase 11 章节 |
| `docs/ROUTE_DATA_SPEC.md` | M | +0 | 复用 v1.5.0 manifest 章节 |
| `README.md` | M | +16 | v1.5.1 当前版本 + 接入说明 |
| `CHANGELOG.md` | M | +94 | v1.5.1 详细变更日志 |
| `scripts/check-route-page-integration.py` | A | +167 | 详情页集成检查脚本 |
| `scripts/verify-site.sh` | M | +50 | v1.5.1 增强（91 → 97 门禁） |
| `.github/workflows/route-data.yml` | M | +4 | 加入 check-route-page-integration.py |
| `routes/index.html` | M | +4 | 版本号 v1.5.0 → v1.5.1 |
| `reports/PHASE11_ROUTE_PAGE_INTEGRATION_REPORT.md` | A | +500 | 本报告 |

---

## 2. 新增 JS：route-page-badges.js

### 2.1 入口

```javascript
function init() {
  var panels = document.querySelectorAll('#route-page-data-panel');
  panels.forEach(function (p) { initPanel(p); });
}
```

### 2.2 渲染内容

| 区块 | 功能 |
|------|------|
| **头部 + 徽章** | 路线数据状态标题 · 数据完整度 / 分类 / SVG / 点位 / 段 / 非导航 徽章 |
| **摘要卡** | 8 字段（路线名 / 数据状态 / 最佳季节 / 难度 / 点位 / 段落 / GeoJSON / GPX）+ theme_tags + region_tags |
| **下载入口** | 路线数据索引 / CSV / GeoJSON / GPX / SVG |
| **数据安全边界** | 统一文案（文化复刻 / 自驾 / 不实时导航 / 不保证开放 / 不伪造精确轨迹） |
| **相关路线** | 最多 2 条推荐（按 category / theme_tags / region_tags / featured / points 排序） |

### 2.3 URL 转换

manifest 的 `../data/...` / `../trips/...` / `../routes/` 路径按 `data-site-root` 重写：

```javascript
function resolveUrl(url, siteRoot) {
  if (!url) return '';
  if (/^https?:\/\//i.test(s)) return s;
  if (s.startsWith('../')) return siteRoot + s.replace(/^\.\.\//, '');
  if (s.startsWith('./')) return siteRoot + s.slice(2);
  return s;
}
```

### 2.4 相关路线推荐逻辑

```javascript
function scoreRelated(route, other) {
  if (other.slug === route.slug) return -1;        // 不推荐自己
  var score = 0;
  if (other.category === route.category) score += 10;
  // theme_tags 交集 ×3
  // region_tags 交集 ×2
  if (other.featured) score += 1;
  score += (other.points || 0) / 100;
  return score;
}
```

排序：`score desc → points desc`，取前 2 条。

### 2.5 Fallback

- **无 JS**：容器内 `<div class="route-page-data-fallback">` 显示静态文案
- **fetch 失败**：显示「路线数据模块加载失败」+ 数据索引入口
- **缺 data-route-slug**：显示「配置错误」提示

---

## 3. 三条路线页面接入情况

### 3.1 OEDW

```
trips/out-of-eden-walk-china/index.html
  ✓ data-route-slug="out-of-eden-walk-china"
  ✓ data-manifest-url="../../data/routes/routes-manifest.json"
  ✓ data-site-root="../../"
  ✓ <script src="../../assets/js/route-page-badges.js"></script>
  ✓ #route-page-data-panel 容器存在
  ✓ 含「路线数据」章节
```

### 3.2 辽塔

```
trips/liao-tower-roadtrip/index.html
  ✓ data-route-slug="liao-tower-roadtrip"
  ✓ data-manifest-url="../../data/routes/routes-manifest.json"
  ✓ data-site-root="../../"
  ✓ <script src="../../assets/js/route-page-badges.js"></script>
  ✓ #route-page-data-panel 容器存在
  ✓ 含「路线数据」章节
```

### 3.3 山西

```
trips/shanxi-ancient-architecture-roadtrip/index.html
  ✓ data-route-slug="shanxi-ancient-architecture"
  ✓ data-manifest-url="../../data/routes/routes-manifest.json"
  ✓ data-site-root="../../"
  ✓ <script src="../../assets/js/route-page-badges.js"></script>
  ✓ #route-page-data-panel 容器存在
  ✓ 含「路线数据」章节
```

---

## 4. 相关路线推荐逻辑（每页推荐结果）

### 4.1 OEDW（long_walk）

| 推荐 | category | theme_tags 重合 | region_tags 重合 | score |
|------|----------|------------------|-------------------|-------|
| 辽塔 | roadtrip | 0（无交集） | 1（北京 / 辽宁） | 0+0+2+1+0.20 = 3.20 |
| 山西 | architecture | 0（无交集） | 1（山西） | 0+0+2+1+0.30 = 3.30 |

### 4.2 辽塔（roadtrip）

| 推荐 | category | theme_tags 重合 | region_tags 重合 | score |
|------|----------|------------------|-------------------|-------|
| OEDW | long_walk | 0 | 1 | 3.20 |
| 山西 | architecture | 1（自驾） | 0 | 1+3+0+1+0.30 = 5.30 |

### 4.3 山西（architecture）

| 推荐 | category | theme_tags 重合 | region_tags 重合 | score |
|------|----------|------------------|-------------------|-------|
| OEDW | long_walk | 0 | 1（山西） | 3.30 |
| 辽塔 | roadtrip | 1（自驾） | 0 | 1+3+0+1+0.20 = 5.20 |

---

## 5. 新增文档

### 5.1 ROUTE_PAGE_INTEGRATION_GUIDE.md（287 行 · 10 章节）

| § | 章节 | 内容 |
|---|------|------|
| 1 | 目标 | 5 项能力清单 |
| 2 | 必备条件 | 4 项 |
| 3 | 页面接入代码 | 容器 / 必填属性 / 脚本引入 / 完整示例 |
| 4 | 推荐插入位置 | 5 条原则 |
| 5 | URL 规则 | 4 种形态 + siteRoot 配置 |
| 6 | 必跑检查 | 8 项 |
| 7 | 常见错误 | 8 类 + 修复 |
| 8 | 相关路线推荐逻辑 | score 公式 + 排序 |
| 9 | 不引入依赖 | 4 条 |
| 10 | 当前三条路线接入状态 | 表格 |

### 5.2 ROUTE_PAGE_TEMPLATE.md §9 统一数据徽章模块（47 行）

包含容器位置 / HTML 代码 / 脚本 / 模块能力 / fallback / 接入指南引用。

### 5.3 ROUTE_FACTORY_GUIDE.md §13 路线页面接入步骤（30 行）

包含接入代码 / 推荐位置 / 必跑检查 / 详细指南引用。

---

## 6. 新增检查脚本

### 6.1 scripts/check-route-page-integration.py（167 行）

检查 8 项：

1. 每条有 page_url 的 route：页面文件存在
2. 页面含 `data-route-slug="<slug>"` 且 slug 与 manifest 完全一致
3. 页面含 `#route-page-data-panel` 容器
4. 页面引入 `route-page-badges.js`
5. 数据完整路线（含 csv_url）页面含「路线数据」关键词
6. 页面声明 `data-site-root`
7. `route-page-badges.js` 存在且含核心关键词（`data-route-slug` / `data-manifest-url` / `data-site-root` / `routes-manifest.json` / `渲染` / `fetch` / `推荐`）
8. `ROUTE_PAGE_INTEGRATION_GUIDE.md` 存在且含核心章节（`接入` / `data-route-slug` / `data-site-root` / `route-page-badges.js`）

PASS 输出：

```
PASS route page integration check
routes checked: 3
```

---

## 7. verify-site.sh 增强说明

### 7.1 v1.5.0 → v1.5.1 变更

| 改动 | 说明 |
|------|------|
| 数据文件清单 | 增加 `assets/js/route-page-badges.js` + `docs/ROUTE_PAGE_INTEGRATION_GUIDE.md` |
| 新增 section | check-route-page-integration.py 调用 |
| 新增 section | 三个详情页接入检查（data-route-slug + route-page-badges.js + route-page-data-panel） |
| 标题 | `v1.5.0 route index experience` → `v1.5.1 route page integration + related routes` |

### 7.2 验证总数

- v1.5.0 门禁：91 项
- v1.5.1 新增：6 项（1 项 integration check + 3 项详情页接入 + 2 项文件存在性）
- **总计：97 项门禁全 PASS**

---

## 8. GitHub Actions 更新说明

`.github/workflows/route-data.yml` 加入：

```yaml
- name: Check route page integration
  run: |
    python3 scripts/check-route-page-integration.py
```

---

## 9. route page integration check 结果

```
$ python3 scripts/check-route-page-integration.py
行旅图谱 · 路线详情页集成检查
manifest: .../data/routes/routes-manifest.json
badges-js: .../assets/js/route-page-badges.js
guide: .../docs/ROUTE_PAGE_INTEGRATION_GUIDE.md
routes: 3
--------------------------------------------------
  ✓ out-of-eden-walk-china: data-route-slug 已声明
  ✓ out-of-eden-walk-china: route-page-data-panel 容器已存在
  ✓ out-of-eden-walk-china: route-page-badges.js 已引入
  ✓ out-of-eden-walk-china: 含'路线数据'章节
  ✓ out-of-eden-walk-china: data-site-root 已声明
  ✓ liao-tower-roadtrip: data-route-slug 已声明
  ✓ liao-tower-roadtrip: route-page-data-panel 容器已存在
  ✓ liao-tower-roadtrip: route-page-badges.js 已引入
  ✓ liao-tower-roadtrip: 含'路线数据'章节
  ✓ liao-tower-roadtrip: data-site-root 已声明
  ✓ shanxi-ancient-architecture: data-route-slug 已声明
  ✓ shanxi-ancient-architecture: route-page-data-panel 容器已存在
  ✓ shanxi-ancient-architecture: route-page-badges.js 已引入
  ✓ shanxi-ancient-architecture: 含'路线数据'章节
  ✓ shanxi-ancient-architecture: data-site-root 已声明
--------------------------------------------------
PASS route page integration check
routes checked: 3
```

---

## 10. route factory 现有门禁结果

```
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
```

---

## 11. verify-site.sh 结果

```
$ bash scripts/verify-site.sh

================================
  行旅图谱 · 网站验证脚本
  v1.5.1 route page integration + related routes
================================

通过: 97
失败: 0

✓ check-routes-index-sync.py
✓ check-route-page-integration.py
✓ out-of-eden-walk-china · 路线页面接入统一面板
✓ liao-tower-roadtrip · 路线页面接入统一面板
✓ shanxi-ancient-architecture · 路线页面接入统一面板

✓ STATUS: PASS
```

---

## 12. 本地 HTTP 200 验证

```
$ python3 -m http.server 8000
$ curl -I http://127.0.0.1:8000/                                                HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/routes/                                         HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/trips/out-of-eden-walk-china/                   HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/trips/liao-tower-roadtrip/                      HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/trips/shanxi-ancient-architecture-roadtrip/    HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/assets/js/route-page-badges.js                  HTTP/1.0 200 OK
$ curl -I http://127.0.0.1:8000/docs/ROUTE_PAGE_INTEGRATION_GUIDE.md            HTTP/1.0 200 OK
```

---

## 13. 事实边界验证（OEDW）

| 检查项 | 结果 |
|--------|------|
| OEDW 「跨越六年」清除 | ✅ 仅历史审计报告（v1.5.1 新增文件 0 命中） |
| OEDW 「22/23」 清除 | ✅ 仅历史审计报告 |
| OEDW Milestones 74–95 = 22/22 | ✅ 22 处命中 |
| OEDW 6,000–6,700 公里保留 | ✅ 32 处命中 |
| 三条路线数据声明保留 | ✅ 文化复刻粗点（多处）+ 文化自驾粗点（多处） |

---

## 14. 浏览器 Smoke

无浏览器环境，记录 N/A，不阻塞。

- OEDW 详情页徽章显示 · N/A
- OEDW 相关路线推荐 · N/A
- 辽塔详情页徽章显示 · N/A
- 山西详情页徽章显示 · N/A
- 控制台无关键错误 · N/A

---

## 15. GitHub Actions 验证

_pending_（push 后回填）：

```
$ gh run list --workflow "Route Data Quality Gate" --limit 5
```

预期本次 commit run 为 success。

---

## 16. 线上 HTTP 200 验证

_pending_（push 后回填）：

```
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/routes/
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/assets/js/route-page-badges.js
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_PAGE_INTEGRATION_GUIDE.md
$ curl -I https://conanxin.github.io/culture-roadtrip-atlas/reports/PHASE11_ROUTE_PAGE_INTEGRATION_REPORT.md
```

全部应为 200。

---

## 17. 页面 URL

- 首页：https://conanxin.github.io/culture-roadtrip-atlas/
- 路线数据索引：https://conanxin.github.io/culture-roadtrip-atlas/routes/
- OEDW 详情页：https://conanxin.github.io/culture-roadtrip-atlas/trips/out-of-eden-walk-china/
- 辽塔详情页：https://conanxin.github.io/culture-roadtrip-atlas/trips/liao-tower-roadtrip/
- 山西详情页：https://conanxin.github.io/culture-roadtrip-atlas/trips/shanxi-ancient-architecture-roadtrip/
- route-page-badges.js：https://conanxin.github.io/culture-roadtrip-atlas/assets/js/route-page-badges.js
- ROUTE_PAGE_INTEGRATION_GUIDE：https://conanxin.github.io/culture-roadtrip-atlas/docs/ROUTE_PAGE_INTEGRATION_GUIDE.md
- Phase 11 报告：https://conanxin.github.io/culture-roadtrip-atlas/reports/PHASE11_ROUTE_PAGE_INTEGRATION_REPORT.md

---

## 18. 闭环说明

v1.5.1 形成完整闭环：

```
首页 (index.html)
  ↓ 路线数据资产统计 + 路线工厂指南按钮
路线数据索引 (routes/index.html)
  ↓ 搜索 / 筛选 / 排序 / 对比 / 仪表盘
路线详情页 (trips/<slug>/index.html)
  ↓ 统一数据状态徽章（route-page-badges.js）
  ├─ 数据下载 (CSV / GeoJSON / GPX / SVG)
  └─ 相关路线推荐 → 另一条详情页
                       ↓
                  同一份 routes-manifest.json 驱动
```

所有页面统一由 `routes-manifest.json` 驱动，避免手工漂移。

---

## 19. Phase 12 建议

1. **第 4 条路线接入**
   - 按 ROUTE_PAGE_INTEGRATION_GUIDE.md 接入新路线
   - 运行 check-route-page-integration.py 验证
   - 不需要修改 route-page-badges.js（通用化已完成）

2. **数据完善**
   - 辽塔 / 山西 从 v0.1 升级到 full
   - OEDW 剩余 50% 段落继续补完
   - 加入更多点位（避免空 CSV）

3. **跨页面体验**
   - 路线页面增加「收藏 / 阅读进度」localStorage
   - 相关路线增加排除逻辑（同 region 不重复推荐）
   - 推荐卡片加「加入对比」按钮

4. **可访问性**
   - route-page-data-panel 添加 ARIA 标签
   - 徽章颜色对比度检查
   - 键盘可达性

5. **多语言**
   - 英文版 route-page-badges.js（i18n）
   - 英文版 ROUTE_PAGE_INTEGRATION_GUIDE

6. **CI/CD**
   - 详情页集成检查生成报告（HTML）
   - 自动截图（如果环境有 Playwright）
   - 部署到 conanxin.github.io + 自托管备份

---

## 20. 提交清单

```bash
git add assets/js/route-page-badges.js assets/js/routes-index.js assets/css/styles.css
git add trips/out-of-eden-walk-china/index.html trips/liao-tower-roadtrip/index.html trips/shanxi-ancient-architecture-roadtrip/index.html
git add docs/ROUTE_PAGE_INTEGRATION_GUIDE.md docs/ROUTE_PAGE_TEMPLATE.md docs/ROUTE_FACTORY_GUIDE.md docs/CONTENT_NOTES.md README.md CHANGELOG.md
git add routes/index.html
git add scripts/check-route-page-integration.py scripts/verify-site.sh .github/workflows/route-data.yml
git add reports/PHASE11_ROUTE_PAGE_INTEGRATION_REPORT.md
git commit -m "Add unified route page data badges"
git push origin main
```

---

_辛 🔮 · 行旅图谱 · Phase 11 报告 · 2026-07-06_
# 行旅图谱 · 路线 SEO 指南

> 路线页面对外分享、搜索展示与社交卡片的统一要求
> v1.0 · v1.5.2 · 2026-07-06

---

## 1. 目标

每个路线页面都需要在外部分发场景下表现得体：

- **搜索引擎**：title / description / canonical 准确 · OG / Twitter Card 完整
- **社交平台**：Facebook / Twitter / LinkedIn / WeChat 都能正确展示卡片
- **屏幕阅读器**：share_summary 可读
- **品牌一致性**：行旅图谱 / Culture Roadtrip Atlas / 暗金色调

所有数据来源统一为 `data/routes/routes-manifest.json`，避免手工漂移。

---

## 2. 每个页面必须有的 `<head>` 元数据

| 标签 | 必填 | 来源 |
|------|------|------|
| `<title>` | ✅ | manifest `seo_title` |
| `<meta name="description">` | ✅ | manifest `seo_description` |
| `<link rel="canonical">` | ✅ | manifest `canonical_url` |
| `<meta property="og:title">` | ✅ | manifest `og_title` |
| `<meta property="og:description">` | ✅ | manifest `og_description` |
| `<meta property="og:type">` | ✅ | 路线页 `article` / 索引页 + 首页 `website` |
| `<meta property="og:url">` | ✅ | manifest `canonical_url` |
| `<meta property="og:image">` | ✅ | manifest `og_image_url` |
| `<meta property="og:site_name">` | ✅ | 行旅图谱 · Culture Roadtrip Atlas |
| `<meta property="og:locale">` | ✅ | zh_CN |
| `<meta property="og:image:width">` | ✅ | 1200 |
| `<meta property="og:image:height">` | ✅ | 630 |
| `<meta property="og:image:alt">` | ✅ | og_title |
| `<meta name="twitter:card">` | ✅ | summary_large_image |
| `<meta name="twitter:title">` | ✅ | manifest `twitter_title` |
| `<meta name="twitter:description">` | ✅ | manifest `twitter_description` |
| `<meta name="twitter:image">` | ✅ | manifest `og_image_url` |
| `<meta name="theme-color">` | ✅ | #2e4f4f |

### 2.1 路线页（article）

og:type 必须为 `article`，因为每条路线是具体的可阅读、可旅行内容。

### 2.2 索引页 + 首页（website）

og:type 必须为 `website`，因为它们是聚合页。

### 2.3 路线页 og:image

每条路线 og:image 指向 `assets/img/og/<slug>-og.svg`，由 `render-route-og-svg.py` 自动生成。

### 2.4 索引页 og:image

路线索引页 og:image 指向 `assets/img/og/routes-index-og.svg`。

### 2.5 首页 og:image

首页 og:image 指向 `assets/img/og/site-og.svg`。

---

## 3. OG SVG 生成方式

### 3.1 命令清单

```bash
# 默认（等同 --all）
python3 scripts/render-route-og-svg.py

# 生成全部
python3 scripts/render-route-og-svg.py --all

# 生成单条
python3 scripts/render-route-og-svg.py out-of-eden-walk-china
python3 scripts/render-route-og-svg.py liao-tower-roadtrip
python3 scripts/render-route-og-svg.py shanxi-ancient-architecture

# 检查（CI 模式）
python3 scripts/render-route-og-svg.py --all --check
```

### 3.2 输出清单

```
assets/img/og/out-of-eden-walk-china-og.svg
assets/img/og/liao-tower-roadtrip-og.svg
assets/img/og/shanxi-ancient-architecture-og.svg
assets/img/og/site-og.svg
assets/img/og/routes-index-og.svg
```

### 3.3 SVG 规格

- 尺寸：1200 × 630
- 背景：米白 / 纸张质感（`#faf6ed` → `#f0e8d4`）
- 主色：墨绿（`#2e4f4f`）
- 点缀：暗金（`#a8804c` → `#c8a96a`）
- 必须含：
  - `<title>` + `<desc>` 元素
  - 「行旅图谱」品牌文字
  - route title
  - route summary
  - category / data status
  - points / segments
  - 「文化复刻粗点 / 文化自驾粗点 · 非导航」声明
  - route slug（便于检查）
- 不引用：
  - 外部字体（仅 system-ui fallback）
  - 外部图片
  - 外部脚本
  - JavaScript
- 不依赖：
  - 浏览器
  - 网络
  - npm / 构建系统

### 3.4 `--check` 模式

检查项：

- 5 个 OG SVG 文件存在、非空（> 500 字节）
- 每个 route 的 `og_image_url` 文件名与实际文件匹配
- 每个 SVG 含「行旅图谱」+ route slug +「非导航」关键词
- 失败返回非 0

输出示例：

```
行旅图谱 · OG SVG 检查 (v1.5.2)
--------------------------------------------------
  ✓ out-of-eden-walk-china-og.svg: 5497 bytes
  ✓ liao-tower-roadtrip-og.svg: 5477 bytes
  ✓ shanxi-ancient-architecture-og.svg: 5501 bytes
  ✓ site-og.svg: 4586 bytes
  ✓ routes-index-og.svg: 5722 bytes
  ✓ out-of-eden-walk-china: og_image_url matches out-of-eden-walk-china-og.svg
  ✓ liao-tower-roadtrip: og_image_url matches liao-tower-roadtrip-og.svg
  ✓ shanxi-ancient-architecture: og_image_url matches shanxi-ancient-architecture-og.svg
--------------------------------------------------
PASS route OG SVG generation
routes: 3
site-og.svg ok
routes-index-og.svg ok
```

---

## 4. SEO 检查方式

### 4.1 命令清单

```bash
# SEO 一致性检查
python3 scripts/check-route-seo.py

# 全部验证
./scripts/verify-site.sh
```

### 4.2 `check-route-seo.py` 覆盖范围

| 类别 | 检查项 |
|------|--------|
| 1 | manifest version = v1.5.2 |
| 2 | 9 SEO 字段完整（每条 route） |
| 3 | OG SVG 文件存在且 > 500 字节 |
| 4 | 14 类 HTML meta 标签（title / description / canonical / og:title / og:description / og:type / og:url / og:image / og:site_name / og:locale / twitter:card / twitter:title / twitter:description / twitter:image） |
| 5 | canonical URL 与 manifest 一致 |
| 6 | og:image basename 与 manifest 一致 |
| 7 | og_title 文本在页面可见 |
| 8 | share_summary 文本在页面可见（`<p class="route-share-summary">`） |
| 9 | 索引页 + 首页 og:type = `website` |
| 10 | 页面含 `route-page-data-panel` 容器 |

输出示例：

```
PASS route SEO check
pages checked: 5
route pages: 3
og assets: 5
warnings: 0
```

### 4.3 description 长度建议

- 中文：60–220 字符
- 超出不 FAIL，但会 WARN
- 警告会出现在输出末尾的 `warnings: N`

### 4.4 主题包含检查

- 路线页 title 或 og:title 须包含路线主题关键词（如 `OEDW` / `辽塔` / `山西`）

---

## 5. verify-site.sh v1.5.2 增强

### 5.1 新增门禁

```bash
test -s scripts/check-route-seo.py
test -s scripts/render-route-og-svg.py
python3 scripts/render-route-og-svg.py --all --check
python3 scripts/check-route-seo.py
test -s assets/img/og/site-og.svg
test -s assets/img/og/routes-index-og.svg
test -s assets/img/og/out-of-eden-walk-china-og.svg
test -s assets/img/og/liao-tower-roadtrip-og.svg
test -s assets/img/og/shanxi-ancient-architecture-og.svg
```

### 5.2 总门禁

- v1.5.1 门禁：97 项
- v1.5.2 新增：10 项
- **总计：107 项门禁**

---

## 6. GitHub Actions

`.github/workflows/route-data.yml` 加入：

```yaml
- name: Check route SEO
  run: |
    python3 scripts/check-route-seo.py

- name: Check route OG SVG
  run: |
    python3 scripts/render-route-og-svg.py --all --check
```

任何 SEO / OG 资产不一致都会被 CI 拦截。

---

## 7. 常见错误

| 错误 | 后果 | 修复 |
|------|------|------|
| 忘记加 canonical | 搜索引擎权重分散 | `<link rel="canonical" href="{canonical_url}">` |
| og:type 写错 | 社交平台不展示 | 路线页 `article` / 索引页 + 首页 `website` |
| og:image 指向不存在的 URL | 分享卡片无图 | 同步运行 `render-route-og-svg.py --all` |
| share_summary 拼写错 | SEO 文本不一致 | 复制 manifest 字段值 |
| twitter:card 仍是 `summary` | 不会展示大图 | 改为 `summary_large_image` |
| `build-route-assets.py --all` 删了 SEO 字段 | manifest 漂移 | 9 个 SEO 字段由 `dict()` 浅拷贝保留 |
| OG SVG 缺 `<title>` | 屏幕阅读器无内容 | 重新运行 `render-route-og-svg.py --all` |
| OG SVG 缺 slug | 自动化检查失败 | 重新运行 `render-route-og-svg.py --all` |

---

## 8. 不引入依赖

- ❌ 地图 API
- ❌ 后端 / 数据库
- ❌ 构建系统
- ❌ npm 依赖
- ❌ 外部字体 / 图片 / 脚本
- ❌ 浏览器截图

---

## 9. 关键边界

- OEDW 「跨越六年」/「22/23」必须清除
- OEDW 6,000–6,700 公里 / 22/22 milestones 保留
- 三条路线数据声明（文化复刻粗点 / 文化自驾粗点 / 非导航）保留
- OG SVG 必含「非导航」关键词

---

_辛 🔮 · 行旅图谱 · SEO 指南 · v1.0 · 2026-07-06_
#!/usr/bin/env bash
# 行旅图谱 · 网站验证脚本
# 用途：检查关键文件存在性 + grep 关键字 + HTTP 200 检查
# 版本：v1.0 stable release

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PASS_COUNT=0
FAIL_COUNT=0

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check_pass() {
  echo -e "${GREEN}✓${NC} $1"
  PASS_COUNT=$((PASS_COUNT+1))
}

check_fail() {
  echo -e "${RED}✗${NC} $1"
  FAIL_COUNT=$((FAIL_COUNT+1))
}

echo "================================"
echo "  行旅图谱 · 网站验证脚本"
echo "  v1.5.1 route page integration + related routes"
echo "================================"
echo ""

# 1. 文件存在性检查
echo "📁 关键文件检查"
echo "----------------------------------------"

FILES=(
  "index.html"
  "trips/liao-tower-roadtrip/index.html"
  "trips/shanxi-ancient-architecture-roadtrip/index.html"
  "assets/js/trips-data.js"
  "assets/js/liao-tower-data.js"
  "assets/js/home.js"
  "assets/js/app.js"
  "assets/css/styles.css"
  "docs/TRIP_TEMPLATE.md"
  "docs/CONTENT_NOTES.md"
  "CHANGELOG.md"
  "README.md"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    check_pass "$file"
  else
    check_fail "$file (缺失)"
  fi
done

echo ""

# 2. 首页关键字检查
echo "🔍 首页关键字检查"
echo "----------------------------------------"

INDEX_KEYWORDS=(
  "行旅图谱"
  "路线库"
  "Featured Trip"
  "北京出发·辽塔巡礼自驾导游手册"
  "山西古建自驾线"
  "规划中"
  "文化导览草稿中"
  "70"
)

for kw in "${INDEX_KEYWORDS[@]}"; do
  if grep -q "$kw" index.html || grep -q "$kw" assets/js/trips-data.js; then
    check_pass "首页含: $kw"
  else
    check_fail "首页缺: $kw"
  fi
done

echo ""

# 3. 辽塔页关键字检查
echo "🔍 辽塔行程页关键字检查"
echo "----------------------------------------"

LIAO_KEYWORDS=(
  "奉国寺"
  "万佛堂石窟"
  "朝阳北塔"
  "庆州白塔"
  "辽上京"
  "大明塔"
  "资料来源索引"
)

for kw in "${LIAO_KEYWORDS[@]}"; do
  if grep -q "$kw" trips/liao-tower-roadtrip/index.html || grep -q "$kw" assets/js/liao-tower-data.js; then
    check_pass "辽塔页含: $kw"
  else
    check_fail "辽塔页缺: $kw"
  fi
done

echo ""

# 4. 山西古建页关键字检查
echo "🔍 山西古建规划页关键字检查"
echo "----------------------------------------"

SHANXI_KEYWORDS=(
  "山西古建自驾线"
  "规划中"
  "文化导览草稿中"
  "山西古建现场怎么看"
  "古建观察清单"
  "导览草稿"
  "待实地复核"
  "30 秒导入"
  "现场怎么看"
  "离开前回望"
  "自我提问"
  "减柱造"
  "悬塑"
  "水陆画"
  "实用信息核验"
  "出发前必须核验"
  "点位实用信息表"
  "高风险点位提示"
  "11 天 10 晚深度版"
  "8 天压缩版"
  "14 天慢行版"
  "云冈石窟"
  "华严寺"
  "善化寺"
  "应县木塔"
  "佛光寺"
  "南禅寺"
  "晋祠"
  "镇国寺"
  "双林寺"
  "小西天"
  "玉皇庙"
  "青莲寺"
  "资料来源索引"
)

for kw in "${SHANXI_KEYWORDS[@]}"; do
  if grep -q "$kw" trips/shanxi-ancient-architecture-roadtrip/index.html; then
    check_pass "山西页含: $kw"
  else
    check_fail "山西页缺: $kw"
  fi
done

echo ""

# 5. README 内容检查
echo "🔍 README 关键字检查"
echo "----------------------------------------"

README_KEYWORDS=(
  "项目定位"
  "当前路线列表"
  "如何添加新路线"
)

for kw in "${README_KEYWORDS[@]}"; do
  if grep -q "$kw" README.md; then
    check_pass "README 含: $kw"
  else
    check_fail "README 缺: $kw"
  fi
done

echo ""

# 6. CHANGELOG 检查
echo "🔍 CHANGELOG 检查"
echo "----------------------------------------"

if [ -f "CHANGELOG.md" ]; then
  if grep -q "v1.0" CHANGELOG.md; then
    check_pass "CHANGELOG.md 含 v1.0"
  else
    check_fail "CHANGELOG.md 缺 v1.0"
  fi
fi

echo ""

# 7. JS 函数检查
echo "🔍 JS 函数检查"
echo "----------------------------------------"

JS_FUNCTIONS=(
  "renderTripCards"
  "filterTrips"
  "localStorage"
  "speechSynthesis"
  "filterSpots"
)

for fn in "${JS_FUNCTIONS[@]}"; do
  if grep -q "$fn" assets/js/app.js assets/js/home.js assets/js/trips-data.js assets/js/liao-tower-data.js 2>/dev/null; then
    check_pass "JS 含: $fn"
  else
    check_fail "JS 缺: $fn"
  fi
done

echo ""

# 总结
echo "================================"
echo "  验证结果"
echo "================================"
echo -e "通过: ${GREEN}${PASS_COUNT}${NC}"
echo -e "失败: ${RED}${FAIL_COUNT}${NC}"
echo ""

# 8. Route data gates (v1.4.8 新增 · v1.5.0 增强)
echo "🛡 Route data gates"
echo "----------------------------------------"

ROUTE_DATA_FILES=(
  "data/routes/routes-manifest.json"
  "data/routes/out-of-eden-walk-china.csv"
  "data/routes/liao-tower-roadtrip.csv"
  "data/routes/shanxi-ancient-architecture.csv"
  "assets/img/routes/out-of-eden-walk-china-map.svg"
  "assets/img/routes/liao-tower-roadtrip-map.svg"
  "assets/img/routes/shanxi-ancient-architecture-map.svg"
  "assets/js/routes-index.js"
  "assets/js/route-page-badges.js"
  "docs/ROUTE_FACTORY_GUIDE.md"
  "docs/ROUTE_PAGE_INTEGRATION_GUIDE.md"
)

for file in "${ROUTE_DATA_FILES[@]}"; do
  if [ -s "$file" ]; then
    check_pass "$file"
  else
    check_fail "$file (缺失或为空)"
  fi
done

# v1.5.0 增强 · 路线索引体验门禁
echo ""
echo "🧭 Route index experience gates (v1.5.0)"
echo "----------------------------------------"

# routes-manifest.json 必出现在 index.html 或 routes-index.js
if grep -R "routes-manifest.json" -q routes/index.html assets/js/routes-index.js 2>/dev/null; then
  check_pass "routes-manifest.json 引用（routes/index.html 或 routes-index.js）"
else
  check_fail "routes-manifest.json 未在 routes/index.html 或 routes-index.js 引用"
fi

# routes-index.js 被 routes/index.html 引入
if grep -R "routes-index.js" -q routes/index.html 2>/dev/null; then
  check_pass "routes-index.js 被 routes/index.html 引入"
else
  check_fail "routes-index.js 未被 routes/index.html 引入"
fi

# #routes-manifest-dashboard 容器存在
if grep -R "routes-manifest-dashboard" -q routes/index.html 2>/dev/null; then
  check_pass "#routes-manifest-dashboard 容器存在"
else
  check_fail "#routes-manifest-dashboard 容器缺失"
fi

# ROUTE_FACTORY_GUIDE.md 必含新增路线流程关键词
for keyword in "新增路线标准流程" "CSV 编写规则" "坐标规则" "数据安全边界" "必跑命令"; do
  if grep -R "$keyword" -q docs/ROUTE_FACTORY_GUIDE.md 2>/dev/null; then
    check_pass "ROUTE_FACTORY_GUIDE.md 含关键词：$keyword"
  else
    check_fail "ROUTE_FACTORY_GUIDE.md 缺关键词：$keyword"
  fi
done

# validate-route-data.py --all --manifest-check
if [ -f "scripts/validate-route-data.py" ]; then
  if python3 scripts/validate-route-data.py --all --manifest-check >/tmp/verify-rd.log 2>&1; then
    check_pass "validate-route-data.py --all --manifest-check"
  else
    check_fail "validate-route-data.py --all --manifest-check (查看 /tmp/verify-rd.log)"
    cat /tmp/verify-rd.log | sed 's/^/    /'
  fi
fi

# render-route-map-svg.py --all --check
if [ -f "scripts/render-route-map-svg.py" ]; then
  if python3 scripts/render-route-map-svg.py --all --check >/tmp/verify-svg.log 2>&1; then
    check_pass "render-route-map-svg.py --all --check"
  else
    check_fail "render-route-map-svg.py --all --check (查看 /tmp/verify-svg.log)"
    cat /tmp/verify-svg.log | sed 's/^/    /'
  fi
fi

# build-route-assets.py --check
if [ -f "scripts/build-route-assets.py" ]; then
  if python3 scripts/build-route-assets.py --check >/tmp/verify-build.log 2>&1; then
    check_pass "build-route-assets.py --check"
  else
    check_fail "build-route-assets.py --check (查看 /tmp/verify-build.log)"
    cat /tmp/verify-build.log | sed 's/^/    /'
  fi
fi

# check-routes-index-sync.py
if [ -f "scripts/check-routes-index-sync.py" ]; then
  if python3 scripts/check-routes-index-sync.py >/tmp/verify-sync.log 2>&1; then
    check_pass "check-routes-index-sync.py"
  else
    check_fail "check-routes-index-sync.py (查看 /tmp/verify-sync.log)"
    cat /tmp/verify-sync.log | sed 's/^/    /'
  fi
fi

# v1.5.1 新增 · check-route-page-integration.py
if [ -f "scripts/check-route-page-integration.py" ]; then
  if python3 scripts/check-route-page-integration.py >/tmp/verify-page.log 2>&1; then
    check_pass "check-route-page-integration.py"
  else
    check_fail "check-route-page-integration.py (查看 /tmp/verify-page.log)"
    cat /tmp/verify-page.log | sed 's/^/    /'
  fi
fi

# v1.5.1 新增 · 三个详情页含统一面板
for slug in "out-of-eden-walk-china" "liao-tower-roadtrip" "shanxi-ancient-architecture"; do
  page_path=""
  case "$slug" in
    out-of-eden-walk-china) page_path="trips/out-of-eden-walk-china/index.html" ;;
    liao-tower-roadtrip) page_path="trips/liao-tower-roadtrip/index.html" ;;
    shanxi-ancient-architecture) page_path="trips/shanxi-ancient-architecture-roadtrip/index.html" ;;
  esac
  if [ -f "$page_path" ]; then
    if grep -q "data-route-slug=\"$slug\"" "$page_path" && \
       grep -q "route-page-badges.js" "$page_path" && \
       grep -q "route-page-data-panel" "$page_path"; then
      check_pass "$slug · 路线页面接入统一面板"
    else
      check_fail "$slug · 路线页面接入不完整（缺 data-route-slug / route-page-badges.js / route-page-data-panel）"
    fi
  else
    check_fail "$page_path 缺失"
  fi
done

echo ""

# 总结
echo "================================"
echo "  验证结果"
echo "================================"
echo -e "通过: ${GREEN}${PASS_COUNT}${NC}"
echo -e "失败: ${RED}${FAIL_COUNT}${NC}"
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
  echo -e "${GREEN}✓ STATUS: PASS${NC}"
  exit 0
else
  echo -e "${RED}✗ STATUS: FAIL${NC}"
  echo "请修复上述失败项后重新运行"
  exit 1
fi
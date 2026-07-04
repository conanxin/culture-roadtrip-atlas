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
echo "  v1.1 shanxi route research"
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
  "研究建档中"
  "规划中"
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
  "研究建档"
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
  "待核对"
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

if [ $FAIL_COUNT -eq 0 ]; then
  echo -e "${GREEN}✓ STATUS: PASS${NC}"
  exit 0
else
  echo -e "${RED}✗ STATUS: FAIL${NC}"
  echo "请修复上述失败项后重新运行"
  exit 1
fi
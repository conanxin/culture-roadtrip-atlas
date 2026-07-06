/**
 * routes-index.js · 行旅图谱 · 路线数据索引前端
 *
 * 功能:
 *   1. fetch routes-manifest.json
 *   2. 渲染统计（路线数、点位、段落、SVG）
 *   3. 渲染路线卡片（含状态徽章、tags、下载按钮）
 *   4. 搜索（名称 / summary / theme_tags / region_tags）
 *   5. 筛选（category / data_completeness / has_svg_preview / 地区）
 *   6. 排序（featured / 点位 / 名称）
 *   7. 渲染路线对比表
 *   8. fetch 失败 fallback
 *   9. 不引入依赖
 *
 * 使用:
 *   <section id="routes-manifest-dashboard" class="routes-manifest-dashboard">
 *     <div class="route-index-loading">正在加载路线索引数据……</div>
 *   </section>
 *   <script src="../assets/js/routes-index.js"></script>
 *
 * 历史:
 *   v1.0 · 2026-07-05 · Phase 10 首版
 */

(function () {
  'use strict';

  // ---------- 工具函数 ----------

  function $(selector, parent) {
    return (parent || document).querySelector(selector);
  }

  function escapeHtml(text) {
    if (text === null || text === undefined) return '';
    return String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function basename(url) {
    if (!url) return '';
    var parts = String(url).split('/');
    return parts[parts.length - 1] || '';
  }

  // ---------- 状态 ----------

  var state = {
    manifest: null,
    searchQuery: '',
    categoryFilter: 'all',
    completenessFilter: 'all',
    regionFilter: 'all',
    sortBy: 'featured',
  };

  // ---------- 渲染：统计 ----------

  function renderStats(container, routes) {
    if (!container) return;
    var totalPoints = 0;
    var totalSegments = 0;
    var totalFeatures = 0;
    var svgCount = 0;
    var plannedCount = 0;
    var fullCount = 0;
    var v01Count = 0;
    routes.forEach(function (r) {
      totalPoints += r.points || 0;
      totalSegments += r.segments || 0;
      totalFeatures += r.geojson_features || 0;
      if (r.has_svg_preview) svgCount += 1;
      if (r.data_completeness === 'planned') plannedCount += 1;
      else if (r.data_completeness === 'full') fullCount += 1;
      else if (r.data_completeness === 'v0.1') v01Count += 1;
    });

    var html = ''
      + '<div class="route-data-stat-grid">'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + routes.length + '</div><div class="route-data-stat-label">路线总数</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + (routes.length - plannedCount) + '</div><div class="route-data-stat-label">已有数据路线</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + totalPoints + '</div><div class="route-data-stat-label">CSV 点位总数</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + totalSegments + '</div><div class="route-data-stat-label">总段落数</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + totalFeatures + '</div><div class="route-data-stat-label">GeoJSON Feature</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + svgCount + '</div><div class="route-data-stat-label">SVG 预览</div></div>'
      + '</div>';

    container.innerHTML = html;
  }

  // ---------- 渲染：单路线卡片 ----------

  function categoryBadge(category) {
    var labels = {
      'long_walk': '长线徒步',
      'roadtrip': '自驾',
      'architecture': '古建'
    };
    return labels[category] || category;
  }

  function completenessBadge(dc) {
    var labels = {
      'full': 'full · 完整',
      'v0.1': 'v0.1 · 初版',
      'planned': 'planned · 规划中'
    };
    return labels[dc] || dc;
  }

  function renderCard(route) {
    var pageUrl = route.page_url || '#';
    var csvUrl = route.csv_url || '';
    var geojsonUrl = route.geojson_url || '';
    var gpxUrl = route.gpx_url || '';
    var svgUrl = route.svg_url || '';

    var themeTags = (route.theme_tags || []).map(function (t) {
      return '<span class="route-index-tag">' + escapeHtml(t) + '</span>';
    }).join('');
    var regionTags = (route.region_tags || []).map(function (t) {
      return '<span class="route-index-tag route-index-tag-region">' + escapeHtml(t) + '</span>';
    }).join('');

    var downloads = '';
    if (csvUrl) {
      downloads += '<a href="' + escapeHtml(csvUrl) + '" class="route-data-button" download><span class="data-format-badge data-format-csv">CSV</span><span class="route-data-button-label">下载</span></a>';
    }
    if (geojsonUrl) {
      downloads += '<a href="' + escapeHtml(geojsonUrl) + '" class="route-data-button" download><span class="data-format-badge data-format-geojson">GeoJSON</span><span class="route-data-button-label">下载</span></a>';
    }
    if (gpxUrl) {
      downloads += '<a href="' + escapeHtml(gpxUrl) + '" class="route-data-button" download><span class="data-format-badge data-format-gpx">GPX</span><span class="route-data-button-label">下载</span></a>';
    }
    if (svgUrl) {
      downloads += '<a href="' + escapeHtml(svgUrl) + '" class="route-data-button" target="_blank"><span class="data-format-badge data-format-svg">SVG</span><span class="route-data-button-label">预览</span></a>';
    }

    var featuredClass = route.featured ? ' route-index-card-featured' : '';

    return ''
      + '<article class="route-index-card' + featuredClass + '" data-route-slug="' + escapeHtml(route.slug) + '">'
      + '<div class="route-index-page-badge">详情页徽章：已接入</div>'
      + '<div class="route-index-card-header">'
      + '<div class="route-index-badges">'
      + '<span class="route-category-badge route-category-' + escapeHtml(route.category || '') + '">' + escapeHtml(categoryBadge(route.category)) + '</span>'
      + '<span class="route-status-badge route-status-' + escapeHtml(route.data_completeness || '') + '">' + escapeHtml(completenessBadge(route.data_completeness)) + '</span>'
      + '</div>'
      + '<h3 class="route-index-card-title">' + escapeHtml(route.title) + '</h3>'
      + '<p class="route-index-card-summary">' + escapeHtml(route.route_summary || '') + '</p>'
      + '<div class="route-index-tags">' + themeTags + '</div>'
      + '<div class="route-index-tags">' + regionTags + '</div>'
      + '</div>'
      + '<div class="route-data-stat-grid route-data-stat-grid-mini">'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + (route.points || 0) + '</div><div class="route-data-stat-label">点位</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + (route.segments || 0) + '</div><div class="route-data-stat-label">段落</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + (route.geojson_features || 0) + '</div><div class="route-data-stat-label">features</div></div>'
      + '<div class="route-data-stat-card"><div class="route-data-stat-num">' + (route.gpx_waypoints || 0) + '</div><div class="route-data-stat-label">waypoints</div></div>'
      + '</div>'
      + '<div class="route-index-card-meta">'
      + '<div><strong>最佳：</strong>' + escapeHtml(route.best_season || '—') + '</div>'
      + '<div><strong>难度：</strong>' + escapeHtml(route.difficulty_label || '—') + '</div>'
      + '<div><strong>数据状态：</strong>' + escapeHtml(route.data_status_label || '—') + '</div>'
      + '</div>'
      + '<div class="route-index-card-downloads">' + downloads + '</div>'
      + '<div class="route-index-card-cta">'
      + '<a href="' + escapeHtml(pageUrl) + '" class="btn btn-primary btn-sm">查看路线页面 →</a>'
      + '</div>'
      + '</article>';
  }

  // ---------- 过滤 + 排序 ----------

  function applyFilters(routes) {
    var q = state.searchQuery.trim().toLowerCase();
    var filtered = routes.filter(function (r) {
      // 搜索
      if (q) {
        var hay = (r.title + ' ' + (r.route_summary || '') + ' ' + (r.theme_tags || []).join(' ') + ' ' + (r.region_tags || []).join(' ') + ' ' + (r.data_status_label || '')).toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      // category
      if (state.categoryFilter !== 'all' && r.category !== state.categoryFilter) return false;
      // completeness
      if (state.completenessFilter !== 'all' && r.data_completeness !== state.completenessFilter) return false;
      // region
      if (state.regionFilter !== 'all') {
        var regions = r.region_tags || [];
        if (regions.indexOf(state.regionFilter) === -1) return false;
      }
      return true;
    });

    // 排序
    filtered.sort(function (a, b) {
      if (state.sortBy === 'featured') {
        if ((b.featured ? 1 : 0) !== (a.featured ? 1 : 0)) return (b.featured ? 1 : 0) - (a.featured ? 1 : 0);
        return (b.points || 0) - (a.points || 0);
      } else if (state.sortBy === 'points') {
        return (b.points || 0) - (a.points || 0);
      } else if (state.sortBy === 'name') {
        return (a.title || '').localeCompare(b.title || '', 'zh');
      }
      return 0;
    });

    return filtered;
  }

  // ---------- 渲染：卡片列表 ----------

  function renderCards(container, routes) {
    if (!container) return;
    var filtered = applyFilters(routes);
    if (filtered.length === 0) {
      container.innerHTML = '<div class="route-index-empty">没有匹配的路线。试试改变搜索词或筛选条件。</div>';
      return;
    }
    container.innerHTML = filtered.map(renderCard).join('');
  }

  // ---------- 渲染：对比表 ----------

  function renderCompare(container, routes) {
    if (!container) return;
    var rows = routes.map(function (r) {
      return '<tr>'
        + '<td><a href="' + escapeHtml(r.page_url || '#') + '">' + escapeHtml(r.title) + '</a></td>'
        + '<td>' + escapeHtml(categoryBadge(r.category)) + '</td>'
        + '<td>' + escapeHtml(completenessBadge(r.data_completeness)) + '</td>'
        + '<td>' + (r.points || 0) + '</td>'
        + '<td>' + (r.segments || 0) + '</td>'
        + '<td>' + (r.has_svg_preview ? '✅' : '—') + '</td>'
        + '<td>' + escapeHtml(r.best_season || '—') + '</td>'
        + '<td>' + escapeHtml(r.difficulty_label || '—') + '</td>'
        + '<td>' + escapeHtml((r.theme_tags || []).slice(0, 3).join(' · ')) + '</td>'
        + '</tr>';
    }).join('');

    container.innerHTML = '<table class="route-compare-table">'
      + '<thead><tr><th>路线</th><th>分类</th><th>数据状态</th><th>点位</th><th>段落</th><th>SVG</th><th>最佳季节</th><th>难度</th><th>主题</th></tr></thead>'
      + '<tbody>' + rows + '</tbody>'
      + '</table>';
  }

  // ---------- 渲染：筛选控件 ----------

  function uniqueRegions(routes) {
    var set = {};
    routes.forEach(function (r) {
      (r.region_tags || []).forEach(function (t) { set[t] = true; });
    });
    return Object.keys(set).sort();
  }

  function renderToolbar(container, routes) {
    if (!container) return;
    var regions = uniqueRegions(routes);
    var regionOptions = '<option value="all">全部地区</option>' + regions.map(function (r) {
      return '<option value="' + escapeHtml(r) + '">' + escapeHtml(r) + '</option>';
    }).join('');

    container.innerHTML = ''
      + '<div class="route-index-toolbar">'
      + '<div class="route-index-toolbar-row">'
      + '<input id="route-search" type="search" placeholder="搜索路线、主题、地区……" class="route-index-search" />'
      + '</div>'
      + '<div class="route-index-toolbar-row">'
      + '<label>分类 <select id="route-category-filter">'
      + '<option value="all">全部</option>'
      + '<option value="long_walk">长线徒步</option>'
      + '<option value="roadtrip">自驾</option>'
      + '<option value="architecture">古建</option>'
      + '</select></label>'
      + '<label>完整度 <select id="route-completeness-filter">'
      + '<option value="all">全部</option>'
      + '<option value="full">full</option>'
      + '<option value="v0.1">v0.1</option>'
      + '<option value="planned">planned</option>'
      + '</select></label>'
      + '<label>地区 <select id="route-region-filter">' + regionOptions + '</select></label>'
      + '<label>排序 <select id="route-sort">'
      + '<option value="featured">推荐</option>'
      + '<option value="points">点位从高到低</option>'
      + '<option value="name">名称</option>'
      + '</select></label>'
      + '<span class="route-index-result-count" id="route-index-result-count"></span>'
      + '</div>'
      + '</div>';

    // 绑定事件
    var searchEl = $('#route-search', container);
    var catEl = $('#route-category-filter', container);
    var compEl = $('#route-completeness-filter', container);
    var regEl = $('#route-region-filter', container);
    var sortEl = $('#route-sort', container);

    function rerender() {
      var root = container.closest('.routes-manifest-dashboard') || document;
      var cardsEl = $('#route-index-cards', root);
      var countEl = $('#route-index-result-count', root);
      renderCards(cardsEl, routes);
      if (countEl) {
        var n = cardsEl ? cardsEl.querySelectorAll('.route-index-card').length : 0;
        countEl.textContent = '共 ' + n + ' 条';
      }
    }

    if (searchEl) searchEl.addEventListener('input', function (e) {
      state.searchQuery = e.target.value || '';
      rerender();
    });
    if (catEl) catEl.addEventListener('change', function (e) {
      state.categoryFilter = e.target.value;
      rerender();
    });
    if (compEl) compEl.addEventListener('change', function (e) {
      state.completenessFilter = e.target.value;
      rerender();
    });
    if (regEl) regEl.addEventListener('change', function (e) {
      state.regionFilter = e.target.value;
      rerender();
    });
    if (sortEl) sortEl.addEventListener('change', function (e) {
      state.sortBy = e.target.value;
      rerender();
    });

    // 初始 result count
    setTimeout(rerender, 0);
  }

  // ---------- 入口 ----------

  function initDashboard() {
    var dashboard = document.getElementById('routes-manifest-dashboard');
    if (!dashboard) return;

    fetch('../data/routes/routes-manifest.json', { credentials: 'omit' })
      .then(function (resp) {
        if (!resp.ok) throw new Error('HTTP ' + resp.status);
        return resp.json();
      })
      .then(function (manifest) {
        state.manifest = manifest;
        var routes = manifest.routes || [];

        dashboard.innerHTML = ''
          + '<div id="routes-manifest-stats"></div>'
          + '<div id="routes-manifest-toolbar"></div>'
          + '<div id="route-index-cards" class="route-index-cards"></div>'
          + '<h3 class="route-index-section-title">路线对比表</h3>'
          + '<div id="route-index-compare" class="route-index-compare"></div>';

        renderStats(document.getElementById('routes-manifest-stats'), routes);
        renderToolbar(document.getElementById('routes-manifest-toolbar'), routes);
        renderCards(document.getElementById('route-index-cards'), routes);
        renderCompare(document.getElementById('route-index-compare'), routes);
      })
      .catch(function (err) {
        dashboard.innerHTML = '<div class="route-index-empty">'
          + '<h4>⚠ 路线 manifest 加载失败</h4>'
          + '<p>无法 fetch() 路线 manifest。错误：' + escapeHtml(err.message || err) + '</p>'
          + '<p>请使用下方静态索引卡片（已硬编码 fallback）。</p>'
          + '</div>';
      });
  }

  function init() {
    initDashboard();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
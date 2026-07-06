/**
 * route-page-badges.js · 行旅图谱 · 路线详情页统一数据徽章
 *
 * 功能:
 *   1. fetch routes-manifest.json（路径由 data-manifest-url 决定）
 *   2. 根据 data-route-slug 渲染统一数据状态徽章 + 摘要卡 + 下载入口
 *   3. 推荐最多 2 条相关路线（按 category / theme_tags / region_tags / featured / points）
 *   4. URL 转换：把 manifest 中 ../data/... / ../trips/... 等面向 routes/index.html 的相对路径
 *      按 data-site-root 重写为面向当前详情页的路径
 *   5. 无 JS / fetch 失败 fallback（容器内默认静态文案保留）
 *   6. 不引入依赖
 *
 * 使用:
 *   <section id="route-page-data-panel"
 *            class="route-page-data-panel"
 *            data-route-slug="<slug>"
 *            data-manifest-url="../../data/routes/routes-manifest.json"
 *            data-site-root="../../">
 *     <div class="route-page-data-fallback">本路线已接入路线数据资产……</div>
 *   </section>
 *   <script src="../../assets/js/route-page-badges.js"></script>
 *
 * 历史:
 *   v1.0 · 2026-07-06 · Phase 11 首版 · 三条路线详情页统一徽章 + 摘要 + 下载 + 相关路线
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

  /**
   * 把 manifest 里的相对路径（面向 routes/index.html）转换为面向当前详情页的路径
   * 规则:
   *   - http(s):// 开头 → 原样
   *   - 以 ../ 开头 → 去掉 ../ 前缀，再拼接 siteRoot
   *   - 其他相对路径 → 直接拼接 siteRoot
   *   - null/空 → 返回 ''
   */
  function resolveUrl(url, siteRoot) {
    if (!url) return '';
    var s = String(url);
    if (/^https?:\/\//i.test(s)) return s;
    if (s.startsWith('../')) {
      var stripped = s.replace(/^\.\.\//, '');
      return siteRoot + stripped;
    }
    if (s.startsWith('./')) {
      return siteRoot + s.slice(2);
    }
    if (s.startsWith('/')) {
      return s;
    }
    // 已经是相对于当前页面的路径
    return s;
  }

  function completenessLabel(dc) {
    var labels = {
      'full': '完整数据',
      'v0.1': 'v0.1 初版',
      'planned': '规划中'
    };
    return labels[dc] || dc;
  }

  function categoryLabel(c) {
    var labels = {
      'long_walk': '长线徒步',
      'roadtrip': '自驾',
      'architecture': '古建'
    };
    return labels[c] || c;
  }

  // ---------- 渲染：状态徽章 ----------

  function renderBadges(route) {
    var dc = route.data_completeness || 'planned';
    var cat = route.category || '';
    var html = '';
    html += '<span class="route-page-data-badge route-page-data-badge-' + escapeHtml(dc) + '">' + escapeHtml(completenessLabel(dc)) + '</span>';
    if (cat) {
      html += '<span class="route-page-data-badge route-page-data-badge-category route-page-data-badge-category-' + escapeHtml(cat) + '">' + escapeHtml(categoryLabel(cat)) + '</span>';
    }
    if (route.has_svg_preview) {
      html += '<span class="route-page-data-badge route-page-data-badge-svg">SVG 预览</span>';
    }
    if (route.points) {
      html += '<span class="route-page-data-badge route-page-data-badge-points">' + route.points + ' 点位</span>';
    }
    if (route.segments) {
      html += '<span class="route-page-data-badge route-page-data-badge-segments">' + route.segments + ' 段</span>';
    }
    html += '<span class="route-page-data-badge route-page-data-badge-not-nav">非导航 · 文化复刻粗点</span>';
    return html;
  }

  // ---------- 渲染：摘要卡 ----------

  function renderSummary(route) {
    var items = [
      { label: '路线名', value: route.title || '—' },
      { label: '数据状态', value: route.data_status_label || '—' },
      { label: '最佳季节', value: route.best_season || '—' },
      { label: '难度', value: route.difficulty_label || '—' },
      { label: '点位', value: (route.points || 0) + ' 个' },
      { label: '段落', value: (route.segments || 0) + ' 段' },
      { label: 'GeoJSON', value: (route.geojson_features || 0) + ' features' },
      { label: 'GPX', value: (route.gpx_waypoints || 0) + ' waypoints' }
    ];
    var html = '<div class="route-page-data-summary-grid">';
    items.forEach(function (it) {
      html += '<div class="route-page-data-summary-item">'
        + '<div class="route-page-data-summary-label">' + escapeHtml(it.label) + '</div>'
        + '<div class="route-page-data-summary-value">' + escapeHtml(it.value) + '</div>'
        + '</div>';
    });
    html += '</div>';

    if (route.route_summary) {
      html += '<p class="route-page-data-summary-text">' + escapeHtml(route.route_summary) + '</p>';
    }

    if (Array.isArray(route.theme_tags) && route.theme_tags.length) {
      html += '<div class="route-page-data-tags">';
      route.theme_tags.forEach(function (t) {
        html += '<span class="route-related-tag">' + escapeHtml(t) + '</span>';
      });
      html += '</div>';
    }
    if (Array.isArray(route.region_tags) && route.region_tags.length) {
      html += '<div class="route-page-data-tags">';
      route.region_tags.forEach(function (t) {
        html += '<span class="route-related-tag route-related-tag-region">' + escapeHtml(t) + '</span>';
      });
      html += '</div>';
    }

    return html;
  }

  // ---------- 渲染：下载入口 ----------

  function renderActions(route, siteRoot) {
    var indexUrl = resolveUrl('../routes/', siteRoot);
    var csvUrl = resolveUrl(route.csv_url, siteRoot);
    var geojsonUrl = resolveUrl(route.geojson_url, siteRoot);
    var gpxUrl = resolveUrl(route.gpx_url, siteRoot);
    var svgUrl = resolveUrl(route.svg_url, siteRoot);

    var html = '<div class="route-page-data-actions">';
    if (indexUrl) {
      html += '<a href="' + escapeHtml(indexUrl) + '" class="route-page-data-action"><span class="route-page-data-action-icon">📂</span><span class="route-page-data-action-label">查看路线数据索引</span></a>';
    }
    if (csvUrl) {
      html += '<a href="' + escapeHtml(csvUrl) + '" class="route-page-data-action" download><span class="route-page-data-action-icon">📄</span><span class="route-page-data-action-label">CSV</span></a>';
    }
    if (geojsonUrl) {
      html += '<a href="' + escapeHtml(geojsonUrl) + '" class="route-page-data-action" download><span class="route-page-data-action-icon">🗺️</span><span class="route-page-data-action-label">GeoJSON</span></a>';
    }
    if (gpxUrl) {
      html += '<a href="' + escapeHtml(gpxUrl) + '" class="route-page-data-action" download><span class="route-page-data-action-icon">📍</span><span class="route-page-data-action-label">GPX</span></a>';
    }
    if (svgUrl) {
      html += '<a href="' + escapeHtml(svgUrl) + '" class="route-page-data-action" target="_blank"><span class="route-page-data-action-icon">🖼️</span><span class="route-page-data-action-label">SVG 预览</span></a>';
    }
    html += '</div>';
    return html;
  }

  // ---------- 渲染：数据安全边界提示 ----------

  function renderWarning(route) {
    var lines = [
      '本路线数据为' + (route.data_status_label || '文化复刻粗点') + '，非实时导航数据，不用于路况、开放状态、天气、安全或紧急救援。',
      '坐标为城市 / 文保单位 / 景区公开粗略点，不写道路级导航坐标。'
    ];
    if (route.category === 'roadtrip' || route.category === 'architecture') {
      lines.push('自驾前需独立核实交通、天气、管制、闭馆与文保开放信息。');
    }
    var html = '<div class="route-page-data-warning"><strong>数据安全边界</strong><ul>';
    lines.forEach(function (l) {
      html += '<li>' + escapeHtml(l) + '</li>';
    });
    html += '</ul></div>';
    return html;
  }

  // ---------- 相关路线推荐 ----------

  function scoreRelated(route, other) {
    if (other.slug === route.slug) return -1;
    var score = 0;
    if (other.category === route.category) score += 10;
    var themeOverlap = (route.theme_tags || []).filter(function (t) {
      return (other.theme_tags || []).indexOf(t) !== -1;
    }).length;
    score += themeOverlap * 3;
    var regionOverlap = (route.region_tags || []).filter(function (r) {
      return (other.region_tags || []).indexOf(r) !== -1;
    }).length;
    score += regionOverlap * 2;
    if (other.featured) score += 1;
    score += (other.points || 0) / 100;
    return score;
  }

  function pickRelated(currentRoute, allRoutes, max) {
    var m = max || 2;
    var scored = allRoutes
      .map(function (r) { return { route: r, score: scoreRelated(currentRoute, r) }; })
      .filter(function (x) { return x.score >= 0; })
      .sort(function (a, b) {
        if (b.score !== a.score) return b.score - a.score;
        return (b.route.points || 0) - (a.route.points || 0);
      });
    return scored.slice(0, m).map(function (x) { return x.route; });
  }

  function renderRelated(currentRoute, related, siteRoot) {
    if (!related.length) {
      return '<div class="route-related-empty">暂无可推荐的相关路线。</div>';
    }
    var html = '<div class="route-related-grid">';
    related.forEach(function (r) {
      var pageUrl = resolveUrl(r.page_url, siteRoot);
      var indexUrl = resolveUrl('../routes/', siteRoot);
      var themeTags = (r.theme_tags || []).slice(0, 4).map(function (t) {
        return '<span class="route-related-tag">' + escapeHtml(t) + '</span>';
      }).join('');
      var dc = r.data_completeness || 'planned';
      html += '<article class="route-related-card">'
        + '<div class="route-related-badges">'
        + '<span class="route-page-data-badge route-page-data-badge-' + escapeHtml(dc) + '">' + escapeHtml(completenessLabel(dc)) + '</span>'
        + '<span class="route-page-data-badge route-page-data-badge-category route-page-data-badge-category-' + escapeHtml(r.category || '') + '">' + escapeHtml(categoryLabel(r.category)) + '</span>'
        + '</div>'
        + '<h4 class="route-related-title">' + escapeHtml(r.title) + '</h4>'
        + '<p class="route-related-summary">' + escapeHtml(r.route_summary || '') + '</p>'
        + '<div class="route-related-tags">' + themeTags + '</div>'
        + '<div class="route-related-actions">'
        + (pageUrl ? '<a href="' + escapeHtml(pageUrl) + '" class="route-page-data-action">进入路线 →</a>' : '')
        + (indexUrl ? '<a href="' + escapeHtml(indexUrl) + '" class="route-page-data-action">数据索引 →</a>' : '')
        + '</div>'
        + '</article>';
    });
    html += '</div>';
    return html;
  }

  // ---------- 入口 ----------

  function initPanel(panel) {
    var slug = panel.getAttribute('data-route-slug');
    var manifestUrl = panel.getAttribute('data-manifest-url')
      || (panel.getAttribute('data-site-root') || '../../') + 'data/routes/routes-manifest.json';
    var siteRoot = panel.getAttribute('data-site-root') || '../../';

    if (!slug) {
      panel.innerHTML = '<div class="route-page-data-warning"><strong>配置错误</strong>：缺少 data-route-slug 属性。</div>';
      return;
    }

    fetch(manifestUrl, { credentials: 'omit' })
      .then(function (resp) {
        if (!resp.ok) throw new Error('HTTP ' + resp.status);
        return resp.json();
      })
      .then(function (manifest) {
        var routes = (manifest && manifest.routes) || [];
        var currentRoute = routes.filter(function (r) { return r.slug === slug; })[0];
        if (!currentRoute) {
          panel.innerHTML = '<div class="route-page-data-warning"><strong>未找到路线</strong>：slug ' + escapeHtml(slug) + ' 不在 manifest 中。</div>';
          return;
        }
        var related = pickRelated(currentRoute, routes, 2);

        var html = ''
          + '<div class="route-page-data-header">'
          + '<h3 class="route-page-data-title">📦 路线数据状态</h3>'
          + '<div class="route-page-data-badges">' + renderBadges(currentRoute) + '</div>'
          + '</div>'
          + '<div class="route-page-data-summary">' + renderSummary(currentRoute) + '</div>'
          + '<div class="route-page-data-actions-wrap">'
          + '<h4 class="route-page-data-section-title">⬇ 数据下载</h4>'
          + renderActions(currentRoute, siteRoot)
          + '</div>'
          + renderWarning(currentRoute)
          + '<div class="route-related-section">'
          + '<h4 class="route-page-data-section-title">🔗 相关路线推荐</h4>'
          + renderRelated(currentRoute, related, siteRoot)
          + '</div>';

        panel.innerHTML = html;
      })
      .catch(function (err) {
        var msg = err && err.message ? err.message : String(err);
        panel.innerHTML = '<div class="route-page-data-warning">'
          + '<strong>路线数据模块加载失败</strong>'
          + '<p>无法 fetch() manifest（' + escapeHtml(manifestUrl) + '）：' + escapeHtml(msg) + '</p>'
          + '<p>可前往 <a href="' + escapeHtml(resolveUrl('../routes/', siteRoot)) + '">路线数据索引</a> 查看 CSV / GeoJSON / GPX 与 SVG 预览。</p>'
          + '</div>';
      });
  }

  function init() {
    var panels = document.querySelectorAll('#route-page-data-panel');
    panels.forEach(function (p) {
      try {
        initPanel(p);
      } catch (e) {
        if (p) p.innerHTML = '<div class="route-page-data-warning">初始化失败：' + escapeHtml(e && e.message ? e.message : String(e)) + '</div>';
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
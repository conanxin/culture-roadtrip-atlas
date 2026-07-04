/**
 * route-data-viewer.js · 行旅图谱 · 路线数据前端查看器
 *
 * 功能:
 *   1. fetch() 加载 GeoJSON 文化复刻粗点数据
 *   2. 自动生成总点位数 / 段落数 / 省份数 / 可复刻性统计 / 难度统计
 *   3. 提供 4 个筛选器（段落 / 省份 / 难度 / 可复刻性）
 *   4. 渲染点位表格（序号 / 段落 / 点位 / 省份 / 地区 / 坐标精度 / 难度 / 可复刻性 / 风险提示）
 *   5. fetch 失败时显示 fallback（直接下载 CSV / GeoJSON / GPX）
 *   6. 无依赖、纯 Vanilla JS
 *
 * 使用:
 *   <section id="route-data-viewer"
 *            data-route-geojson="../../data/routes/out-of-eden-walk-china.geojson"
 *            data-route-name="Out of Eden Walk 中国段">
 *     <div class="route-data-loading">正在加载路线数据……</div>
 *     <noscript>浏览器未启用 JavaScript。请直接下载 CSV / GeoJSON / GPX 文件查看路线数据。</noscript>
 *   </section>
 *
 * 历史:
 *   v1.0 · 2026-07-04 · Phase 6 首版
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

  function badgeClass(value, prefix) {
    var p = prefix || 'route-data-badge';
    var v = String(value || '').toLowerCase();
    if (v === 'high') return p + ' ' + p + '-high';
    if (v === 'medium') return p + ' ' + p + '-medium';
    if (v === 'low' || v === 'n/a') return p + ' ' + p + '-low';
    if (v === 'not_recommended' || v === 'reading_only') return p + ' ' + p + '-caution';
    if (v === 'hard') return p + ' ' + p + '-caution';
    if (v === 'easy') return p + ' ' + p + '-high';
    return p + ' ' + p + '-medium';
  }

  function badgeLabel(value) {
    var map = {
      'high': '高',
      'medium': '中',
      'low': '低',
      'not_recommended': '不推荐',
      'reading_only': '仅阅读',
      'easy': '易',
      'hard': '难',
      'n/a': 'N/A',
      'city': '城市级',
      'landmark': '地标级',
      'region': '区域级',
      'approximate': '近似',
      'unknown': '未知'
    };
    return map[value] || value;
  }

  // ---------- 渲染：摘要 ----------

  function renderSummary(points, container) {
    var segments = {};
    var provinces = {};
    var feasibility = {};
    var difficulty = {};
    points.forEach(function (p) {
      var props = p.properties || {};
      var seg = props.segment_id || 'unknown';
      segments[seg] = (segments[seg] || 0) + 1;
      var prov = props.province || 'unknown';
      provinces[prov] = (provinces[prov] || 0) + 1;
      var rf = props.replication_feasibility || 'unknown';
      feasibility[rf] = (feasibility[rf] || 0) + 1;
      var diff = props.difficulty || 'unknown';
      difficulty[diff] = (difficulty[diff] || 0) + 1;
    });

    var html = '<div class="route-data-summary-grid">';
    html += '<div class="route-data-summary-card"><div class="route-data-summary-num">' + points.length + '</div><div class="route-data-summary-label">点位总数</div></div>';
    html += '<div class="route-data-summary-card"><div class="route-data-summary-num">' + Object.keys(segments).length + '</div><div class="route-data-summary-label">段落数</div></div>';
    html += '<div class="route-data-summary-card"><div class="route-data-summary-num">' + Object.keys(provinces).length + '</div><div class="route-data-summary-label">省份数</div></div>';
    html += '<div class="route-data-summary-card"><div class="route-data-summary-num">' + (feasibility['high'] || 0) + '</div><div class="route-data-summary-label">高复刻性点位</div></div>';
    html += '<div class="route-data-summary-card"><div class="route-data-summary-num">' + (feasibility['medium'] || 0) + '</div><div class="route-data-summary-label">中复刻性点位</div></div>';
    html += '<div class="route-data-summary-card"><div class="route-data-summary-num">' + (feasibility['low'] || 0) + '</div><div class="route-data-summary-label">低复刻性点位</div></div>';
    html += '</div>';

    // 段落分布
    html += '<h4 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-family: serif; font-weight: 600;">段落分布</h4>';
    html += '<div class="route-data-summary-grid">';
    Object.keys(segments).sort().forEach(function (seg) {
      html += '<div class="route-data-summary-card"><div class="route-data-summary-num">' + segments[seg] + '</div><div class="route-data-summary-label">' + escapeHtml(seg) + '</div></div>';
    });
    html += '</div>';

    container.innerHTML = html;
  }

  // ---------- 渲染：筛选器 ----------

  function renderFilters(points, container, onFilterChange) {
    var segments = {};
    var provinces = {};
    var difficulties = {};
    var feasibilities = {};
    points.forEach(function (p) {
      var props = p.properties || {};
      if (props.segment_id) segments[props.segment_id] = true;
      if (props.province) provinces[props.province] = true;
      if (props.difficulty) difficulties[props.difficulty] = true;
      if (props.replication_feasibility) feasibilities[props.replication_feasibility] = true;
    });

    function buildSelect(id, label, values, allLabel) {
      var sorted = Object.keys(values).sort();
      var html = '<div class="route-data-filter">';
      html += '<label for="' + id + '">' + label + '</label>';
      html += '<select id="' + id + '" class="route-data-filter-select">';
      html += '<option value="all">' + allLabel + '</option>';
      sorted.forEach(function (v) {
        html += '<option value="' + escapeHtml(v) + '">' + escapeHtml(badgeLabel(v)) + ' (' + v + ')</option>';
      });
      html += '</select>';
      html += '</div>';
      return html;
    }

    var html = '<div class="route-data-filters">';
    html += buildSelect('rdv-filter-segment', '段落', segments, '全部段落');
    html += buildSelect('rdv-filter-province', '省份', provinces, '全部省份');
    html += buildSelect('rdv-filter-difficulty', '难度', difficulties, '全部难度');
    html += buildSelect('rdv-filter-feasibility', '可复刻性', feasibilities, '全部可复刻性');
    html += '</div>';

    container.innerHTML = html;

    // 绑定事件
    ['segment', 'province', 'difficulty', 'feasibility'].forEach(function (kind) {
      var sel = document.getElementById('rdv-filter-' + kind);
      if (sel) sel.addEventListener('change', onFilterChange);
    });
  }

  function getFilterValues() {
    return {
      segment: $('#rdv-filter-segment') ? $('#rdv-filter-segment').value : 'all',
      province: $('#rdv-filter-province') ? $('#rdv-filter-province').value : 'all',
      difficulty: $('#rdv-filter-difficulty') ? $('#rdv-filter-difficulty').value : 'all',
      feasibility: $('#rdv-filter-feasibility') ? $('#rdv-filter-feasibility').value : 'all',
    };
  }

  // ---------- 渲染：表格 ----------

  function renderTable(points, container) {
    var filters = getFilterValues();
    var filtered = points.filter(function (p) {
      var props = p.properties || {};
      if (filters.segment !== 'all' && props.segment_id !== filters.segment) return false;
      if (filters.province !== 'all' && props.province !== filters.province) return false;
      if (filters.difficulty !== 'all' && props.difficulty !== filters.difficulty) return false;
      if (filters.feasibility !== 'all' && props.replication_feasibility !== filters.feasibility) return false;
      return true;
    });

    var sorted = filtered.slice().sort(function (a, b) {
      return (a.properties.sequence || 999) - (b.properties.sequence || 999);
    });

    if (sorted.length === 0) {
      container.innerHTML = '<div class="route-data-empty">没有符合筛选条件的点位。请放宽筛选器。</div>';
      return;
    }

    var html = '<div class="route-data-table-wrap"><table class="route-data-viewer-table">';
    html += '<thead><tr>';
    html += '<th>序号</th><th>段落</th><th>点位</th><th>省份</th><th>地区</th><th>精度</th><th>难度</th><th>可复刻性</th><th>风险提示</th>';
    html += '</tr></thead><tbody>';
    sorted.forEach(function (f) {
      var props = f.properties || {};
      html += '<tr>';
      html += '<td>' + escapeHtml(props.sequence || '-') + '</td>';
      html += '<td>' + escapeHtml(props.segment_id || '-') + '</td>';
      html += '<td>' + escapeHtml(props.point_name || '-') + '</td>';
      html += '<td>' + escapeHtml(props.province || '-') + '</td>';
      html += '<td>' + escapeHtml(props.city_or_area || '-') + '</td>';
      html += '<td><span class="' + badgeClass(props.coordinate_precision) + '">' + escapeHtml(badgeLabel(props.coordinate_precision)) + '</span></td>';
      html += '<td><span class="' + badgeClass(props.difficulty) + '">' + escapeHtml(badgeLabel(props.difficulty)) + '</span></td>';
      html += '<td><span class="' + badgeClass(props.replication_feasibility) + '">' + escapeHtml(badgeLabel(props.replication_feasibility)) + '</span></td>';
      html += '<td class="route-data-risk">' + escapeHtml(props.risk_note || '-') + '</td>';
      html += '</tr>';
    });
    html += '</tbody></table></div>';
    html += '<div class="route-data-table-meta">显示 ' + sorted.length + ' / ' + points.length + ' 个点位</div>';
    container.innerHTML = html;
  }

  // ---------- Fallback ----------

  function renderFallback(container, error) {
    var msg = error ? String(error.message || error) : '未知错误';
    container.innerHTML = '<div class="route-data-fallback">'
      + '<h4>⚠ 数据表加载失败</h4>'
      + '<p>无法 fetch() GeoJSON 数据。错误：' + escapeHtml(msg) + '</p>'
      + '<p>本页仍然可正常阅读。请直接下载 CSV / GeoJSON / GPX 文件查看路线数据：</p>'
      + '<ul>'
      + '<li><a href="../../data/routes/out-of-eden-walk-china.csv" download>下载 CSV</a></li>'
      + '<li><a href="../../data/routes/out-of-eden-walk-china.geojson" download>下载 GeoJSON</a></li>'
      + '<li><a href="../../data/routes/out-of-eden-walk-china.gpx" download>下载 GPX</a></li>'
      + '</ul>'
      + '<p><strong>所有数据均为文化复刻粗点，非 Paul Salopek 原始 GPS 轨迹，不用于导航。</strong></p>'
      + '</div>';
  }

  // ---------- 初始化 ----------

  function initViewer(container) {
    var geoUrl = container.getAttribute('data-route-geojson');
    var routeName = container.getAttribute('data-route-name') || '路线数据';

    container.innerHTML = '<h3 class="route-data-viewer-title">📊 ' + escapeHtml(routeName) + ' · 数据驱动路线表</h3>'
      + '<div class="route-data-summary" id="rdv-summary"></div>'
      + '<div class="route-data-filters-wrap" id="rdv-filters"></div>'
      + '<div class="route-data-table" id="rdv-table"></div>';

    if (!geoUrl) {
      renderFallback(container, new Error('缺少 data-route-geojson 属性'));
      return;
    }

    fetch(geoUrl, { credentials: 'omit' })
      .then(function (resp) {
        if (!resp.ok) throw new Error('HTTP ' + resp.status);
        return resp.json();
      })
      .then(function (geo) {
        var features = (geo.features || []);
        var points = features.filter(function (f) {
          return f.geometry && f.geometry.type === 'Point';
        });

        renderSummary(points, document.getElementById('rdv-summary'));

        renderFilters(points, document.getElementById('rdv-filters'), function () {
          renderTable(points, document.getElementById('rdv-table'));
        });

        renderTable(points, document.getElementById('rdv-table'));
      })
      .catch(function (err) {
        renderFallback(container, err);
      });
  }

  function init() {
    var containers = document.querySelectorAll('#route-data-viewer');
    containers.forEach(function (c) {
      try {
        initViewer(c);
      } catch (e) {
        renderFallback(c, e);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
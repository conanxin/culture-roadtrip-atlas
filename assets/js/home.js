/**
 * 行旅图谱 · 首页脚本 (v0.8)
 * 负责路线卡片渲染、筛选、Featured Trip 展示
 */

(function () {
  'use strict';

  // ============ 工具函数 ============

  function getStorage(key, defaultValue) {
    try {
      const value = localStorage.getItem(key);
      return value ? JSON.parse(value) : defaultValue;
    } catch (e) {
      return defaultValue;
    }
  }

  function setStorage(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
      // localStorage 不可用时静默失败
    }
  }

  // ============ 路线卡片渲染 ============

  /**
   * 渲染路线卡片
   */
  function renderTripCards(trips) {
    const grid = document.getElementById('trips-grid');
    if (!grid) return;

    if (trips.length === 0) {
      grid.innerHTML = '<div class="trips-empty">暂无符合条件的路线</div>';
      return;
    }

    let html = '';
    trips.forEach(trip => {
      const statusClass = trip.isLive ? 'status-live' : 'status-planning';
      const buttonHtml = trip.isLive
        ? `<a href="${trip.url}" class="btn btn-primary">进入行程 →</a>`
        : trip.url && trip.url !== '#'
          ? `<a href="${trip.url}" class="btn btn-outline">查看规划 →</a>`
          : `<button class="btn btn-outline" disabled>规划中</button>`;

      const progressHtml = trip.isLive
        ? `<div class="trip-progress"><div class="trip-progress-bar" style="width: ${trip.progress}%"></div></div><div class="trip-progress-label">已上线 · v0.7</div>`
        : `<div class="trip-progress"><div class="trip-progress-bar" style="width: ${trip.progress}%"></div></div><div class="trip-progress-label">规划进度 ${trip.progress}%</div>`;

      html += `
        <article class="trip-card${trip.isFeatured ? ' trip-card-featured' : ''}" data-trip-id="${trip.id}">
          ${trip.isFeatured ? '<div class="trip-featured-tag">⭐ Featured Trip</div>' : ''}
          <div class="trip-card-header">
            <h3 class="trip-card-title">${trip.name}</h3>
            <p class="trip-card-subtitle">${trip.oneLine}</p>
          </div>

          <div class="trip-tags">
            ${trip.tags.map(t => `<span class="trip-tag">${t}</span>`).join('')}
          </div>

          <div class="trip-meta">
            <div class="trip-meta-item">
              <span class="trip-meta-label">天数</span>
              <span class="trip-meta-value">${trip.days}</span>
            </div>
            <div class="trip-meta-item">
              <span class="trip-meta-label">起终点</span>
              <span class="trip-meta-value">${trip.route}</span>
            </div>
            <div class="trip-meta-item">
              <span class="trip-meta-label">核心主题</span>
              <span class="trip-meta-value">${trip.themes.join(' · ')}</span>
            </div>
            <div class="trip-meta-item">
              <span class="trip-meta-label">适合人群</span>
              <span class="trip-meta-value">${trip.suitableFor.join(' · ')}</span>
            </div>
          </div>

          ${progressHtml}

          <div class="trip-card-footer">
            <span class="trip-status ${statusClass}">${trip.status}</span>
            ${buttonHtml}
          </div>
        </article>
      `;
    });

    grid.innerHTML = html;
  }

  /**
   * 渲染 Featured Trip 区块
   */
  function renderFeaturedTrip() {
    const featured = TRIPS_DATA.find(t => t.isFeatured);
    if (!featured) return;

    const container = document.getElementById('featured-trip');
    if (!container) return;

    container.innerHTML = `
      <article class="featured-trip-card">
        <div class="featured-trip-badge">⭐ Featured Trip · 当前主推</div>
        <h3 class="featured-trip-title">${featured.name}</h3>
        <p class="featured-trip-subtitle">${featured.oneLine}</p>

        <div class="featured-trip-meta">
          <div class="featured-trip-meta-item">
            <span class="featured-trip-meta-label">天数</span>
            <span class="featured-trip-meta-value">${featured.days}</span>
          </div>
          <div class="featured-trip-meta-item">
            <span class="featured-trip-meta-label">主题</span>
            <span class="featured-trip-meta-value">${featured.themes.slice(0, 3).join(' · ')}</span>
          </div>
          <div class="featured-trip-meta-item">
            <span class="featured-trip-meta-label">状态</span>
            <span class="featured-trip-meta-value trip-status status-live">${featured.status}</span>
          </div>
        </div>

        <div class="featured-trip-tags">
          ${featured.tags.map(t => `<span class="trip-tag">${t}</span>`).join('')}
        </div>

        <div class="featured-trip-footer">
          <a href="${featured.url}" class="btn btn-primary btn-lg">进入行程 →</a>
          <p class="featured-trip-note">完整 9 天路线 · 现场导游 · 知识图谱 · 资料来源 · 视觉文物图录</p>
        </div>
      </article>
    `;
  }

  /**
   * 筛选路线
   */
  function filterTrips(category) {
    const filtered = category === 'all'
      ? TRIPS_DATA
      : TRIPS_DATA.filter(t => t.categories.includes(category));

    renderTripCards(filtered);
    updateFilterButtons(category);
  }

  /**
   * 更新筛选按钮状态
   */
  function updateFilterButtons(activeCategory) {
    const buttons = document.querySelectorAll('.trip-filter-btn');
    buttons.forEach(btn => {
      if (btn.dataset.category === activeCategory) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  // ============ 初始化 ============

  function initFilterButtons() {
    const buttons = document.querySelectorAll('.trip-filter-btn');
    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const category = btn.dataset.category;
        filterTrips(category);
      });
    });
  }

  function init() {
    renderFeaturedTrip();
    renderTripCards(TRIPS_DATA);
    initFilterButtons();
  }

  // 等待 DOM 加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
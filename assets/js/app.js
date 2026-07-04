/**
 * 行旅图谱 · 交互脚本
 * 功能：景点筛选、卡片展开/收起、朗读讲解、进度保存、地图跳转
 */

(function() {
  'use strict';

  // ============ 工具函数 ============

  /**
   * 获取 localStorage 数据
   */
  function getStorage(key, defaultValue = []) {
    try {
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : defaultValue;
    } catch (e) {
      console.warn('localStorage read error:', e);
      return defaultValue;
    }
  }

  /**
   * 保存 localStorage 数据
   */
  function setStorage(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
      console.warn('localStorage write error:', e);
    }
  }

  /**
   * 切换数组中的元素
   */
  function toggleArrayItem(arr, item) {
    const index = arr.indexOf(item);
    if (index > -1) {
      arr.splice(index, 1);
    } else {
      arr.push(item);
    }
    return arr;
  }

  /**
   * 复制文本到剪贴板
   */
  function copyToClipboard(text) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(() => {
        showToast('已复制：' + text);
      }).catch(() => {
        fallbackCopy(text);
      });
    } else {
      fallbackCopy(text);
    }
  }

  function fallbackCopy(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    showToast('已复制：' + text);
  }

  /**
   * 显示 Toast 提示
   */
  function showToast(message, duration = 2000) {
    let toast = document.querySelector('.toast-message');
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'toast-message';
      toast.style.cssText = `
        position: fixed;
        bottom: 80px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(26, 58, 42, 0.9);
        color: #faf8f2;
        padding: 10px 20px;
        border-radius: 20px;
        font-size: 0.9rem;
        z-index: 1000;
        transition: opacity 0.3s;
      `;
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.style.opacity = '1';
    setTimeout(() => {
      toast.style.opacity = '0';
    }, duration);
  }

  // ============ 朗读功能 ============

  // 语音朗读状态
  let isSpeaking = false;

  /**
   * 朗读文本
   */
  function speakText(text, btn) {
    if (!('speechSynthesis' in window)) {
      showToast('当前浏览器不支持语音朗读');
      return;
    }

    // iOS Safari 需要用户交互才能触发
    if (navigator.userAgent.match(/(iPhone|iPad|iPod)/i)) {
      // iOS 设备，先尝试 unlock
      var unlockAudio = function() {
        var audio = new window.Audio();
        audio.play().catch(function() {});
        document.removeEventListener('touchstart', unlockAudio, true);
      };
      document.addEventListener('touchstart', unlockAudio, true);
    }

    // 停止之前的朗读
    stopSpeech();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'zh-CN';
    utterance.rate = 0.9;
    utterance.pitch = 1;

    // 按钮状态
    if (btn) {
      btn.classList.add('listened');
      btn.textContent = '🔊 朗读中...';
      isSpeaking = true;
      updateStopButtons(true);
    }

    utterance.onend = function() {
      if (btn) {
        btn.classList.remove('listened');
        btn.textContent = '🔊 朗读讲解';
        isSpeaking = false;
        updateStopButtons(false);
      }
    };

    utterance.onerror = function() {
      if (btn) {
        btn.classList.remove('listened');
        btn.textContent = '🔊 朗读讲解';
        isSpeaking = false;
        updateStopButtons(false);
      }
      showToast('朗读出错，请重试');
    };

    window.speechSynthesis.speak(utterance);
  }

  /**
   * 停止朗读
   */
  function stopSpeech() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    isSpeaking = false;
    updateStopButtons(false);
    // 重置所有朗读按钮状态
    document.querySelectorAll('[data-speak-btn]').forEach(function(btn) {
      btn.classList.remove('listened');
      btn.textContent = '🔊 朗读讲解';
    });
  }

  /**
   * 更新停止按钮状态
   */
  function updateStopButtons(speaking) {
    document.querySelectorAll('.stop-speak-btn').forEach(function(btn) {
      if (speaking) {
        btn.classList.add('active');
        btn.textContent = '⏹ 停止';
      } else {
        btn.classList.remove('active');
        btn.textContent = '⏹ 停止';
      }
    });
  }

  // ============ 地图跳转 ============

  /**
   * 打开高德地图搜索
   */
  function openGaodeMap(spotName) {
    const url = `https://restapi.amap.com/v3/place/text?keywords=${encodeURIComponent(spotName)}&city=全国&output=json&key=YOUR_KEY`;
    // 直接使用网页版搜索（不需要key）
    const webUrl = `https://www.amap.com/search?query=${encodeURIComponent(spotName)}`;
    window.open(webUrl, '_blank');
    showToast('正在打开高德地图网页版...');
  }

  /**
   * 打开百度地图搜索
   */
  function openBaiduMap(spotName) {
    const webUrl = `https://map.baidu.com/search/${encodeURIComponent(spotName)}/@`;
    window.open(webUrl, '_blank');
    showToast('正在打开百度地图...');
  }

  // ============ 景点卡片功能 ============

  /**
   * 切换景点卡片展开/收起
   */
  function toggleSpotCard(card) {
    const body = card.querySelector('.spot-card-body');
    const toggle = card.querySelector('.spot-toggle');

    if (body.classList.contains('visible')) {
      body.classList.remove('visible');
      toggle.classList.remove('expanded');
    } else {
      body.classList.add('visible');
      toggle.classList.add('expanded');
    }
  }

  /**
   * 更新景点状态按钮
   */
  function updateSpotButtons(spotId) {
    const visited = getStorage('visited_spots');
    const wanted = getStorage('wanted_spots');
    const listened = getStorage('listened_spots');

    document.querySelectorAll(`[data-spot-btn="${spotId}"]`).forEach(btn => {
      const type = btn.dataset.btnType;

      if (type === 'visited') {
        btn.classList.toggle('visited', visited.includes(spotId));
        btn.textContent = visited.includes(spotId) ? '✅ 已去' : '📍 已去';
      } else if (type === 'wanted') {
        btn.classList.toggle('visited', wanted.includes(spotId));
        btn.textContent = wanted.includes(spotId) ? '⭐ 想去' : '☆ 想去';
      } else if (type === 'listened') {
        btn.classList.toggle('listened', listened.includes(spotId));
      }
    });
  }

  /**
   * 处理景点操作
   */
  function handleSpotAction(spotId, action) {
    let data, key;

    switch (action) {
      case 'visited':
        key = 'visited_spots';
        break;
      case 'wanted':
        key = 'wanted_spots';
        break;
      case 'listened':
        key = 'listened_spots';
        break;
      default:
        return;
    }

    data = getStorage(key);
    toggleArrayItem(data, spotId);
    setStorage(key, data);
    updateSpotButtons(spotId);
    updateProgress();
    showToast(action === 'visited' ? '已标记去过' : action === 'wanted' ? '已标记想去' : '已标记已听');
  }

  // ============ 资料包功能 ============

  /**
   * 处理资料操作
   */
  function handleResourceAction(resourceName, action) {
    const key = 'read_materials';
    let data = getStorage(key);
    toggleArrayItem(data, resourceName);
    setStorage(key, data);

    // 更新按钮状态
    document.querySelectorAll(`[data-resource-btn]`).forEach(btn => {
      const btnResource = btn.dataset.resourceName;
      const btnType = btn.dataset.btnType;
      if (btnResource === resourceName && btnType === action) {
        btn.classList.toggle('visited', data.includes(resourceName));
        btn.textContent = data.includes(resourceName) ? '✅ 已读' : '📖 已读';
      }
    });

    updateProgress();
    showToast(data.includes(resourceName) ? '已标记已读' : '已取消已读');
  }

  // ============ 进度统计 ============

  /**
   * 更新进度显示
   */
  function updateProgress() {
    const totalSpots = document.querySelectorAll('.spot-card').length;
    const visitedSpots = getStorage('visited_spots').length;
    const totalResources = document.querySelectorAll('.resource-card').length;
    const readResources = getStorage('read_materials').length;

    // 更新顶部进度条
    const spotProgress = document.getElementById('spot-progress');
    const resourceProgress = document.getElementById('resource-progress');

    if (spotProgress) {
      const percent = totalSpots > 0 ? Math.round((visitedSpots / totalSpots) * 100) : 0;
      spotProgress.style.width = percent + '%';
      const countEl = spotProgress.closest('.progress-bar').querySelector('.progress-count');
      if (countEl) countEl.textContent = `${visitedSpots}/${totalSpots} 景点`;
    }

    if (resourceProgress) {
      const percent = totalResources > 0 ? Math.round((readResources / totalResources) * 100) : 0;
      resourceProgress.style.width = percent + '%';
      const countEl = resourceProgress.closest('.progress-bar').querySelector('.progress-count');
      if (countEl) countEl.textContent = `${readResources}/${totalResources} 资料`;
    }

    // 更新打卡区域统计
    const spotCountEl = document.getElementById('checkin-spots');
    const resourceCountEl = document.getElementById('checkin-resources');
    if (spotCountEl) spotCountEl.textContent = visitedSpots;
    if (resourceCountEl) resourceCountEl.textContent = readResources;
  }

  // ============ 筛选功能 ============

  /**
   * 筛选景点
   */
  function filterSpots(filterValue) {
    const cards = document.querySelectorAll('.spot-card');
    const filterBtns = document.querySelectorAll('.filter-btn');

    // 更新按钮状态
    filterBtns.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.filter === filterValue);
    });

    cards.forEach(card => {
      const types = card.dataset.types ? card.dataset.types.split(',') : [];
      const tags = card.dataset.tags ? card.dataset.tags.split(',') : [];

      if (filterValue === 'all' || types.includes(filterValue) || tags.includes(filterValue)) {
        card.style.display = '';
        card.style.animation = 'fadeIn 0.3s ease';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // ============ 初始化 ============

  function init() {
    // 初始化导航
    initNavigation();

    // 初始化景点卡片点击
    initSpotCards();

    // 初始化筛选按钮
    initFilterButtons();

    // 初始化朗读按钮
    initSpeakButtons();

    // 初始化停止朗读按钮
    initStopSpeakButtons();

    // 初始化操作按钮
    initActionButtons();

    // 初始化地图按钮
    initMapButtons();

    // 初始化资料按钮
    initResourceButtons();

    // 初始化语音状态检测
    initSpeechStatus();

    // 更新进度
    updateProgress();

    // v0.3 现场使用版
    initV3();
    initArrivalButtons();
    showSpeechNotice();

    // 平滑滚动到锚点
    initSmoothScroll();
  }

  /**
   * 初始化导航
   */
  function initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id], div[id]');

    // 滚动监听
    window.addEventListener('scroll', () => {
      let current = '';
      const scrollY = window.scrollY + 100;

      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
          current = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
          link.classList.add('active');
        }
      });
    });
  }

  /**
   * 初始化景点卡片
   */
  function initSpotCards() {
    document.querySelectorAll('.spot-card-header').forEach(header => {
      header.addEventListener('click', function(e) {
        // 不触发如果点击的是按钮
        if (e.target.closest('.spot-action-btn')) return;
        const card = this.closest('.spot-card');
        toggleSpotCard(card);
      });
    });
  }

  /**
   * 初始化筛选按钮
   */
  function initFilterButtons() {
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        filterSpots(btn.dataset.filter);
      });
    });
  }

  /**
   * 初始化朗读按钮
   */
  function initSpeakButtons() {
    document.querySelectorAll('[data-speak-btn]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const spotId = btn.dataset.speakBtn;
        const spotCard = document.querySelector(`.spot-card[data-spot-id="${spotId}"]`);
        const guideText = spotCard.querySelector('.guide-text');

        if (guideText) {
          // 停止当前朗读
          if (window.speechSynthesis.speaking) {
            stopSpeech();
            btn.classList.remove('listened');
            btn.textContent = '🔊 朗读讲解';
          } else {
            const text = guideText.innerText;
            speakText(text, btn);

            // 标记已听
            const listened = getStorage('listened_spots');
            if (!listened.includes(spotId)) {
              toggleArrayItem(listened, spotId);
              setStorage('listened_spots', listened);
              updateSpotButtons(spotId);
            }
          }
        }
      });
    });
  }

  /**
   * 初始化操作按钮
   */
  function initActionButtons() {
    document.querySelectorAll('[data-spot-btn]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const spotId = btn.dataset.spotBtn;
        const action = btn.dataset.btnType;
        handleSpotAction(spotId, action);
      });
    });
  }

  /**
   * 初始化地图按钮
   */
  function initMapButtons() {
    document.querySelectorAll('[data-map-gaode]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        openGaodeMap(btn.dataset.mapGaode);
      });
    });

    document.querySelectorAll('[data-map-baidu]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        openBaiduMap(btn.dataset.mapBaidu);
      });
    });

    document.querySelectorAll('[data-copy]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        copyToClipboard(btn.dataset.copy);
      });
    });
  }

  /**
   * 初始化资料按钮
   */
  function initResourceButtons() {
    document.querySelectorAll('[data-resource-btn]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const resourceName = btn.dataset.resourceName;
        const action = btn.dataset.btnType;
        handleResourceAction(resourceName, action);
      });
    });
  }

  /**
   * 初始化平滑滚动
   */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          const headerOffset = 80;
          const elementPosition = target.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

          window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  /**
   * 初始化停止朗读按钮
   */
  function initStopSpeakButtons() {
    document.querySelectorAll('.stop-speak-btn').forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.stopPropagation();
        stopSpeech();
        showToast('已停止朗读');
      });
    });
  }

  /**
   * 初始化语音状态检测
   */
  function initSpeechStatus() {
    const speechStatusEl = document.getElementById('speech-status');
    if (!speechStatusEl) return;

    const dot = speechStatusEl.querySelector('.speech-status-dot');
    const text = speechStatusEl.querySelector('.speech-status-text');

    if ('speechSynthesis' in window) {
      dot.classList.add('supported');
      dot.classList.remove('unsupported');
      text.textContent = '语音朗读: 支持';
    } else {
      dot.classList.add('unsupported');
      dot.classList.remove('supported');
      text.textContent = '语音朗读: 不支持';
    }
  }


  // ============ v0.3 现场使用版功能 ============

  /**
   * 初始化今日模式
   */
  function initTodayMode() {
    const dayBtns = document.querySelectorAll('.today-day-btn');
    const todayContents = document.querySelectorAll('.today-content');

    dayBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const day = btn.dataset.day;

        // 更新按钮状态
        dayBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // 切换内容
        todayContents.forEach(content => {
          content.classList.remove('active');
          if (content.dataset.day === day) {
            content.classList.add('active');
          }
        });
      });
    });
  }

  /**
   * 初始化行前 7 天学习计划打卡
   */
  function initPrepPlan() {
    const prepChecks = document.querySelectorAll('.prep-plan-check');
    const completedDays = getStorage('prep_plan_completed', []);

    // 恢复已打卡状态
    prepChecks.forEach(btn => {
      const day = parseInt(btn.dataset.day);
      if (completedDays.includes(day)) {
        btn.classList.add('checked');
        btn.textContent = '✅ 已完成';
        const item = btn.closest('.prep-plan-item');
        if (item) item.classList.add('completed');
      }

      btn.addEventListener('click', () => {
        const dayNum = parseInt(btn.dataset.day);
        let completed = getStorage('prep_plan_completed', []);

        if (completed.includes(dayNum)) {
          completed = completed.filter(d => d !== dayNum);
          btn.classList.remove('checked');
          btn.textContent = '✅ 标记完成';
          const item = btn.closest('.prep-plan-item');
          if (item) item.classList.remove('completed');
          showToast('已取消打卡');
        } else {
          completed.push(dayNum);
          btn.classList.add('checked');
          btn.textContent = '✅ 已完成';
          const item = btn.closest('.prep-plan-item');
          if (item) item.classList.add('completed');
          showToast('已打卡');
        }

        setStorage('prep_plan_completed', completed);
        updateProgressDashboard();
      });
    });
  }

  /**
   * 更新进度面板
   */
  function updateProgressDashboard() {
    const dashSpots = document.getElementById('dash-spots');
    const dashListened = document.getElementById('dash-listened');
    const dashResources = document.getElementById('dash-resources');
    const dashPrep = document.getElementById('dash-prep');

    if (dashSpots) {
      const total = document.querySelectorAll('.spot-card').length;
      const visited = getStorage('visited_spots').length;
      dashSpots.textContent = visited + ' / ' + total;
    }

    if (dashListened) {
      const total = document.querySelectorAll('[data-speak-btn]').length;
      const listened = getStorage('listened_spots').length;
      dashListened.textContent = listened + ' / ' + total;
    }

    if (dashResources) {
      const total = document.querySelectorAll('.resource-card').length;
      const read = getStorage('read_materials').length;
      dashResources.textContent = read + ' / ' + total;
    }

    if (dashPrep) {
      const total = document.querySelectorAll('.prep-plan-check').length;
      const completed = getStorage('prep_plan_completed', []).length;
      dashPrep.textContent = completed + ' / 7';
    }
  }

  /**
   * 初始化现场模式底部导航
   */
  function initFieldNav() {
    const fieldNav = document.getElementById('field-nav');
    if (!fieldNav) return;

    // 只在移动端显示
    function checkMobile() {
      if (window.innerWidth <= 768) {
        fieldNav.classList.add('show');
        document.body.classList.add('has-field-nav');
      } else {
        fieldNav.classList.remove('show');
        document.body.classList.remove('has-field-nav');
      }
    }

    checkMobile();
    window.addEventListener('resize', checkMobile);

    // 点击导航项
    const navItems = fieldNav.querySelectorAll('.field-nav-item');
    navItems.forEach(item => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const target = item.dataset.target;
        if (target) {
          const targetEl = document.querySelector(target);
          if (targetEl) {
            const offset = 70;
            const top = targetEl.getBoundingClientRect().top + window.pageYOffset - offset;
            window.scrollTo({ top, behavior: 'smooth' });

            // 更新活动状态
            navItems.forEach(n => n.classList.remove('active'));
            item.classList.add('active');
          }
        }
      });
    });
  }

  /**
   * 初始化 v0.3 功能
   */
  function initV3() {
    initTodayMode();
    initPrepPlan();
    updateProgressDashboard();
    initFieldNav();
  }


  

  /**
   * 朗读到达前导入
   */
  function speakArrivalIntro(spotId) {
    const spot = SPOT_DATA.spots.find(s => s.id === spotId);
    if (!spot || !spot.arrivalIntro) {
      showToast('暂无导入内容');
      return;
    }
    if (!('speechSynthesis' in window)) {
      showToast('当前浏览器不支持朗读');
      return;
    }

    speechSynthesis.cancel();
    const text = `【到达前导入】${spot.arrivalIntro}`;
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'zh-CN';
    u.rate = 0.9;
    u.onend = () => {
      // 标记为已听
      let listened = getStorage('listened_spots');
      if (!listened.includes(spotId + '_arrival')) {
        listened.push(spotId + '_arrival');
        setStorage('listened_spots', listened);
      }
    };
    speechSynthesis.speak(u);
  }

  /**
   * 初始化到达前按钮
   */
  function initArrivalButtons() {
    document.querySelectorAll('[data-arrival-btn]').forEach(btn => {
      btn.addEventListener('click', () => {
        const spotId = btn.dataset.arrivalBtn;
        speakArrivalIntro(spotId);
      });
    });
  }

  /**
   * 显示语音不支持提示
   */
  function showSpeechNotice() {
    if (!('speechSynthesis' in window)) {
      const notice = document.createElement('div');
      notice.className = 'speech-notice';
      notice.textContent = '⚠️ 当前浏览器不支持朗读，可直接阅读导游词。';
      const heroSection = document.querySelector('.hero');
      if (heroSection) {
        heroSection.appendChild(notice);
      }
    }
  }


    // 页面加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // 页面可见性变化时停止朗读
  document.addEventListener('visibilitychange', () => {
    if (document.hidden && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
  });

})();

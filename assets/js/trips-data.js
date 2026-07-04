/**
 * 行旅图谱 · 路线库数据 (v0.8)
 * 包含所有路线的元数据和卡片信息
 */

const TRIPS_DATA = [
  {
    id: 'liao-tower-roadtrip',
    name: '北京出发·辽塔巡礼自驾导游手册',
    shortName: '辽塔巡礼',
    oneLine: '从辽西走廊到契丹草原腹地，一条关于佛塔、捺钵与辽代都城的自驾路线',
    status: '已上线',
    days: '9天8晚',
    route: '北京 → 锦州 → 义县 → 北镇 → 朝阳 → 赤峰 → 巴林左旗 → 宁城/承德 → 北京',
    themes: ['辽代佛塔', '都城遗址', '草原文明', '契丹', '捺钵', '五京制度'],
    tags: ['辽塔', '契丹', '捺钵', '石窟', '博物馆', '自驾'],
    suitableFor: ['自驾爱好者', '历史人文旅行者', '建筑爱好者'],
    progress: 100,
    categories: ['古建', '博物馆', '自驾', '边疆史'],
    url: 'trips/liao-tower-roadtrip/index.html',
    isFeatured: true,
    isLive: true
  },
  {
    id: 'shanxi-ancient-buildings',
    name: '山西古建自驾线',
    shortName: '山西古建',
    oneLine: '从大同到晋祠，沿途寻找中国古建筑的半部历史——唐、五代、宋、辽、金、元、明、清的木构遗产',
    status: '规划中',
    days: '10-12天',
    route: '北京 → 大同 → 朔州 → 太原 → 平遥 → 临汾 → 运城 → 北京',
    themes: ['唐宋木构', '辽金建筑', '彩塑壁画', '寺观祠庙'],
    tags: ['古建', '自驾', '山西', '唐宋', '辽金'],
    suitableFor: ['古建爱好者', '自驾爱好者', '深度历史旅行者'],
    progress: 20,
    categories: ['古建', '自驾'],
    url: '#',
    isFeatured: false,
    isLive: false
  },
  {
    id: 'beijing-liao-jin-buildings',
    name: '北京周边辽金古建线',
    shortName: '北京辽金',
    oneLine: '以北京为起点，向周边寻找辽金时代的石窟、佛塔与寺庙遗存',
    status: '规划中',
    days: '3-4天',
    route: '北京 → 门头沟（戒台寺/潭柘寺）→ 房山（云居寺/石经山）→ 河北涞源（阁院寺）→ 北京',
    themes: ['辽代石经', '辽金佛塔', '北京周边'],
    tags: ['北京', '辽金', '石窟', '短途', '古建'],
    suitableFor: ['北京居民', '周末出行', '古建入门'],
    progress: 30,
    categories: ['古建', '徒步', '城市史'],
    url: '#',
    isFeatured: false,
    isLive: false
  },
  {
    id: 'hexi-corridor',
    name: '河西走廊文化线',
    shortName: '河西走廊',
    oneLine: '从兰州到敦煌，沿祁连山北麓的河西走廊，看石窟、关隘、长城与丝绸之路的千年回响',
    status: '规划中',
    days: '12-14天',
    route: '兰州 → 武威 → 张掖 → 嘉峪关 → 敦煌',
    themes: ['丝路文化', '石窟艺术', '汉唐关隘', '佛教东传'],
    tags: ['丝路', '石窟', '敦煌', '河西', '自驾'],
    suitableFor: ['丝路文化爱好者', '自驾爱好者', '深度旅行者'],
    progress: 10,
    categories: ['古建', '石窟', '博物馆', '自驾', '边疆史'],
    url: '#',
    isFeatured: false,
    isLive: false
  },
  {
    id: 'dian-vietnam-railway',
    name: '滇越铁路文化线',
    shortName: '滇越铁路',
    oneLine: '从昆明到河口，沿着 100 年前法国人修建的米轨铁路，穿越滇南的山水与历史',
    status: '规划中',
    days: '7-8天',
    route: '昆明 → 蒙自 → 碧色寨 → 个旧 → 河口',
    themes: ['工业遗产', '近代史', '跨国铁路', '滇南人文'],
    tags: ['铁路', '近代史', '云南', '工业遗产'],
    suitableFor: ['铁路文化爱好者', '近代史爱好者', '小众旅行者'],
    progress: 5,
    categories: ['博物馆', '城市史'],
    url: '#',
    isFeatured: false,
    isLive: false
  },
  {
    id: 'via-francigena',
    name: 'Via Francigena 徒步线',
    shortName: 'Via Francigena',
    oneLine: '从 Canterbury 到 Rome，沿着中世纪朝圣者走过 1900 公里的古道，穿过英格兰、法国、瑞士、意大利',
    status: '规划中',
    days: '40-90天',
    route: 'Canterbury → Calais → Reims → Lausanne → Aosta → Rome',
    themes: ['中世纪朝圣', '欧洲古道', '罗马式教堂', '跨国徒步'],
    tags: ['徒步', '欧洲', '中世纪', '朝圣'],
    suitableFor: ['深度徒步爱好者', '欧洲文化爱好者', '长程旅行者'],
    progress: 0,
    categories: ['徒步', '边疆史'],
    url: '#',
    isFeatured: false,
    isLive: false
  }
];

// 导出为全局变量
window.TRIPS_DATA = TRIPS_DATA;
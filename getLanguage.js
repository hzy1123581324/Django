/** 
 * 获取浏览器语言
*/
function getLanguage() {
    // 根据浏览器语言转化为后台约定的语言
    const localToBrowser = {
        'zh-CN': 'zh_CN',
        en: 'en_US',
        ko: 'ko_KR',
        ru: 'ru_RU',
        'zh-TW': 'zh_TW',
        ja: 'ja_JP',
        ms: 'ms_MY',
    };
    const currentLan = localToBrowser[navigator.language || navigator.userLanguage] || 'en_US';
    let lan = getCookie('lan') || localStorage.getItem('lan');
    if (currentLan && !lan) {
        localStorage.setItem('lan', currentLan);
        setCookie('lan', currentLan);
    }

    function setCookie(name, value, times) {
        times = times || 36500;
        let exp = new Date();
        exp.setTime(exp.getTime() + times * 24 * 60 * 60 * 1000);
        let domain = `.${location.host.split('.')[1]}.${location.host.split('.')[2]}`;
        if (location.host.split('.')[2]) {
            document.cookie = `${name}=${escape(value)};expires=${exp.toGMTString()};domain=${domain};path=/`;
        } else {
            document.cookie = `${name}=${escape(value)};expires=${exp.toGMTString()};path=/`;
        }
    }
    function getCookie(name) {
        let arrd = null
        let reg = new RegExp('(^| )' + name + '=([^;]*)(;|$)')
        if (document.cookie.match(reg)) {
            arrd = document.cookie.match(reg)
            return unescape(arrd[2])
        } else {
            return null
        }
    }
    return currentLan;
}
getLanguage();

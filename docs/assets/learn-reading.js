/* ═══════════════════════════════════════════════════════════════
   StudyMate · 阅读条（跨页面共用）
   ═══════════════════════════════════════════════════════════════
   这一条做两件事，都挂在每页顶部：

   1. **字号调节（A− / A+）**：改 `--learn-font-scale`（定义在 learn-theme.css），
      全站字号都是 rem，所以整页等比缩放。选择记进 localStorage，下次打开还是这个字号。
   2. **术语表版本切换（大白话版 ↔ 规范版）+ 首次进入的引导**：只在术语表的两个页面上出现。
      学生第一次打开时，用一个气泡说明这两个版本的区别与建议，点过就记住、不再打扰。

   依赖：无。主题开关复用 Sayo 的 `LearnTheme.set`（learn-theme.js 已提供）。
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var SCALE_KEY = 'learn-font-scale';
  var GLOSSARY_HINT_KEY = 'learn-glossary-hint-seen';
  var MIN = 0.8, MAX = 2.0, STEP = 0.1;

  /* ── 字号 ───────────────────────────────────────────────── */

  function readScale() {
    var v = parseFloat(localStorage.getItem(SCALE_KEY));
    if (isNaN(v)) return 1;
    return Math.min(MAX, Math.max(MIN, v));
  }

  function applyScale(v) {
    v = Math.min(MAX, Math.max(MIN, Math.round(v * 10) / 10));
    document.documentElement.style.setProperty('--learn-font-scale', v);
    try { localStorage.setItem(SCALE_KEY, String(v)); } catch (e) { /* 隐私模式忽略 */ }
    syncScaleUI(v);
    return v;
  }

  function syncScaleUI(v) {
    var out = document.getElementById('learn-scale-value');
    if (out) out.textContent = Math.round(v * 100) + '%';
    var down = document.getElementById('learn-scale-down');
    var up = document.getElementById('learn-scale-up');
    if (down) down.disabled = v <= MIN + 1e-6;
    if (up) up.disabled = v >= MAX - 1e-6;
  }

  /* ── 主题（复用 Sayo 的逻辑，这里是条上的那个开关） ────────── */

  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }

  function syncThemeUI() {
    var cb = document.getElementById('learn-reading-theme');
    if (cb) cb.checked = currentTheme() === 'dark';
  }

  function setTheme(theme) {
    if (window.LearnTheme && typeof window.LearnTheme.set === 'function') {
      window.LearnTheme.set(theme);
    } else {
      document.documentElement.setAttribute('data-theme', theme);
      try { localStorage.setItem('learn-theme', theme); } catch (e) {}
    }
    syncThemeUI();
  }

  /* ── 术语表版本切换与首次引导 ───────────────────────────── */

  function glossaryInfo() {
    var bar = document.getElementById('learn-reading-bar');
    var other = bar && bar.getAttribute('data-glossary-other');
    if (!other) return null;
    return {
      other: other,
      otherLabel: bar.getAttribute('data-glossary-other-label') || '另一种版本'
    };
  }

  function showGlossaryHint() {
    var info = glossaryInfo();
    if (!info) return;
    var seen = false;
    try { seen = localStorage.getItem(GLOSSARY_HINT_KEY) === '1'; } catch (e) {}
    if (seen) return;

    var tip = document.createElement('div');
    tip.className = 'learn-glossary-hint';
    tip.setAttribute('role', 'note');
    tip.innerHTML =
      '<p class="learn-glossary-hint__title">这里有两个版本的术语表，都讲同一批词</p>' +
      '<ul class="learn-glossary-hint__list">' +
      '<li><b>大白话版</b>：每个词都拿生活里的东西打比方——完全没接触过计算机的话，先看这份。</li>' +
      '<li><b>规范版</b>：定义更精确，还标了「不要用哪个说法代替它」——学过几章、想确认准确说法时看。</li>' +
      '</ul>' +
      '<p class="learn-glossary-hint__foot">' +
      '想换的时候，点上面的「' + info.otherLabel + '」按钮就行。' +
      '<button type="button" class="learn-glossary-hint__ok">知道了</button>' +
      '</p>';

    var dismiss = function () {
      try { localStorage.setItem(GLOSSARY_HINT_KEY, '1'); } catch (e) {}
      if (tip.parentNode) tip.parentNode.removeChild(tip);
    };
    tip.querySelector('.learn-glossary-hint__ok').addEventListener('click', dismiss);

    var host = document.getElementById('learn-reading-bar');
    if (host && host.parentNode) host.parentNode.insertBefore(tip, host.nextSibling);
  }

  /* ── 装配 ───────────────────────────────────────────────── */

  function build() {
    var bar = document.getElementById('learn-reading-bar');
    if (!bar) return;

    applyScale(readScale());

    var down = document.getElementById('learn-scale-down');
    var up = document.getElementById('learn-scale-up');
    if (down) down.addEventListener('click', function () { applyScale(readScale() - STEP); });
    if (up) up.addEventListener('click', function () { applyScale(readScale() + STEP); });

    var themeCb = document.getElementById('learn-reading-theme');
    if (themeCb) {
      syncThemeUI();
      themeCb.addEventListener('change', function () {
        setTheme(themeCb.checked ? 'dark' : 'light');
      });
      // 与页面上原有的主题开关双向同步：那边改了，这边跟着变
      document.addEventListener('change', function (e) {
        if (e.target && /theme/.test(e.target.id || '') &&
            e.target.id !== 'learn-reading-theme') {
          syncThemeUI();
        }
      });
    }

    showGlossaryHint();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();

/* ═══════════════════════════════════════════════════════════════
   KTSSD ERP — Accessibility & Visual Alert Helpers
   FIX: Was empty stub. Full deaf-learner accessibility helpers.
   ═══════════════════════════════════════════════════════════════ */

/* ── High Contrast ── */
function toggleHighContrast() {
  document.body.classList.toggle('high-contrast');
  const on = document.body.classList.contains('high-contrast');
  localStorage.setItem('ktssd_hc', on ? '1' : '0');
}

/* ── Large Font ── */
function toggleLargeFont() {
  document.body.classList.toggle('large-font');
  const on = document.body.classList.contains('large-font');
  localStorage.setItem('ktssd_lf', on ? '1' : '0');
}

/* ── Visual Flash Alert (for deaf users — no sound) ── */
function visualFlash(color) {
  color = color || '#EF4444';
  const flash = document.createElement('div');
  flash.style.cssText = `
    position:fixed;inset:0;z-index:99999;
    background:${color};opacity:0;
    pointer-events:none;transition:opacity 0.1s;
  `;
  document.body.appendChild(flash);
  requestAnimationFrame(() => {
    flash.style.opacity = '0.25';
    setTimeout(() => {
      flash.style.opacity = '0';
      setTimeout(() => flash.remove(), 200);
    }, 220);
  });
}

/* ── Border pulse for alerts ── */
function borderPulse(el, color) {
  if (!el) return;
  color = color || '#EF4444';
  const orig = el.style.outline;
  let count = 0;
  const interval = setInterval(() => {
    el.style.outline = count % 2 === 0 ? `3px solid ${color}` : 'none';
    if (++count >= 6) { clearInterval(interval); el.style.outline = orig; }
  }, 180);
}

/* ── Visual notification banner (top) ── */
function showVisualBanner(msg, color) {
  const b = document.getElementById('alert-banner');
  if (!b) return;
  b.textContent = '🚨 ' + msg;
  b.style.background = color || '#DC2626';
  b.classList.remove('hidden');
  visualFlash(color || '#DC2626');
  setTimeout(() => b.classList.add('hidden'), 6000);
}

/* ── Keyboard nav enhancement ── */
function enhanceKeyboardNav() {
  document.addEventListener('keydown', (e) => {
    // Alt+D → Dashboard, Alt+L → Library, Alt+S → Students, Alt+M → Messages
    if (!e.altKey) return;
    const map = { d: '/dashboard', l: '/library', s: '/students', m: '/communication', r: '/results' };
    if (map[e.key]) { e.preventDefault(); window.location.href = map[e.key]; }
  });
}

/* ── Restore saved accessibility preferences ── */
document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('ktssd_hc') === '1') document.body.classList.add('high-contrast');
  if (localStorage.getItem('ktssd_lf') === '1') document.body.classList.add('large-font');
  // Sync toggle buttons
  ['toggle-hc', 'toggle-lf'].forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    const key = id === 'toggle-hc' ? 'ktssd_hc' : 'ktssd_lf';
    if (localStorage.getItem(key) === '1') el.classList.add('on');
  });
  enhanceKeyboardNav();
});

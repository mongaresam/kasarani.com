/* ═══════════════════════════════════════════════════════════════════
   KTSSD ERP — Main JavaScript
   Kasarani Treeside Secondary School for the Deaf
   ═══════════════════════════════════════════════════════════════════ */

/* ── Theme ── */
function toggleTheme() {
  const body = document.body;
  const btn  = document.getElementById('theme-btn');
  const isDark = body.dataset.theme === 'dark';
  body.dataset.theme = isDark ? 'light' : 'dark';
  if (btn) btn.textContent = isDark ? '🌙' : '☀️';
  localStorage.setItem('ktssd_theme', body.dataset.theme);
}

/* ── Sidebar ── */
function toggleSidebar() {
  const sb = document.getElementById('sidebar');
  const mw = document.getElementById('main-wrap');
  if (!sb) return;
  sb.classList.toggle('collapsed');
  localStorage.setItem('ktssd_sidebar', sb.classList.contains('collapsed') ? '1' : '0');
}

/* ── Toast ── */
function showToast(msg, type = 'success') {
  const t = document.getElementById('toast');
  if (!t) return;
  t.textContent = msg;
  t.className = `toast ${type} show`;
  clearTimeout(window._toastTimer);
  window._toastTimer = setTimeout(() => { t.classList.remove('show'); }, 3200);
}

/* ── Alert Banner ── */
function showAlert(msg) {
  const b = document.getElementById('alert-banner');
  if (!b) return;
  b.textContent = '🚨 ' + msg;
  b.classList.remove('hidden');
  setTimeout(() => b.classList.add('hidden'), 5000);
}

/* ── Chip filter ── */
function chipFilter(el, group, callback) {
  document.querySelectorAll(`.chip[data-group="${group}"]`).forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  if (callback) callback(el.dataset.val);
}

/* ── Tab system ── */
function switchTab(btn, tabId) {
  const parent = btn.closest('.tab-bar').parentElement;
  parent.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  parent.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  const pane = document.getElementById(tabId);
  if (pane) pane.classList.add('active');
}

/* ── Toggle switch ── */
function toggleSwitch(el) {
  el.classList.toggle('on');
  const label = el.dataset.label || 'Setting';
  showToast(`${label} ${el.classList.contains('on') ? 'enabled' : 'disabled'}`, 'info');
}

/* ── Message read ── */
function readMessage(id, el) {
  document.querySelectorAll('.msg-item').forEach(m => m.classList.remove('active'));
  el.classList.add('active');
  el.classList.remove('unread');
  // fetch and show (demo: just show placeholder)
  fetch('/api/messages')
    .then(r => r.json())
    .then(msgs => {
      const m = msgs.find(x => x.id == id);
      if (!m) return;
      const view = document.getElementById('msg-view');
      if (!view) return;
      view.innerHTML = `
        <div class="msg-sender">
          <div class="sender-avi">${m.from[0]}</div>
          <div>
            <div style="font-weight:700;font-size:14px;color:var(--text)">${m.from}</div>
            <div style="color:var(--text-sec);font-size:11px">${m.date} · ${m.time}</div>
          </div>
          ${m.priority === 'high' ? '<span class="badge badge-red" style="margin-left:auto">⚡ HIGH PRIORITY</span>' : ''}
        </div>
        <div class="msg-view-title">${m.subject}</div>
        <div class="msg-body">${m.body}</div>
        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <button class="btn btn-primary btn-sm" onclick="showToast('Reply sent!','success')">↩ Reply</button>
          <button class="btn btn-outline btn-sm" onclick="showToast('Forwarded!','info')">→ Forward</button>
          <button class="btn btn-outline btn-sm" onclick="showToast('Marked important!','warning')">⭐ Mark Important</button>
        </div>`;
    });
}

/* ── Student search ── */
function searchStudents(q) {
  const rows = document.querySelectorAll('.student-row');
  q = q.toLowerCase();
  rows.forEach(r => {
    r.style.display = r.dataset.name.toLowerCase().includes(q) ? '' : 'none';
  });
}

/* ── Inventory search & filter ── */
function searchInventory(q) {
  const rows = document.querySelectorAll('.inv-row');
  q = q.toLowerCase();
  rows.forEach(r => {
    const match = r.dataset.name.toLowerCase().includes(q) || r.dataset.cat.toLowerCase().includes(q);
    r.style.display = match ? '' : 'none';
  });
}

function filterInventory(cat) {
  const rows = document.querySelectorAll('.inv-row');
  rows.forEach(r => {
    r.style.display = (cat === 'All' || r.dataset.cat === cat) ? '' : 'none';
  });
}

/* ── Chart helpers ── */
function chartDefaults() {
  return {
    color: getComputedStyle(document.body).getPropertyValue('--text-sec').trim() || '#64748B',
    grid: getComputedStyle(document.body).getPropertyValue('--border').trim() || '#BFDBFE',
  };
}

function makeLineChart(id, labels, data, label = 'Mean Grade') {
  const ctx = document.getElementById(id);
  if (!ctx) return;
  const d = chartDefaults();
  return new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        label,
        data,
        borderColor: '#0EA5E9',
        backgroundColor: 'rgba(14,165,233,0.10)',
        borderWidth: 2.5,
        pointBackgroundColor: '#0EA5E9',
        pointRadius: 4,
        tension: 0.4,
        fill: true,
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { color: d.grid }, ticks: { color: d.color, font: { size: 10 } } },
        y: { grid: { color: d.grid }, ticks: { color: d.color, font: { size: 10 } } }
      }
    }
  });
}

function makeBarChart(id, labels, data, colors) {
  const ctx = document.getElementById(id);
  if (!ctx) return;
  const d = chartDefaults();
  return new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        data,
        backgroundColor: colors || Array(labels.length).fill('rgba(14,165,233,0.75)'),
        borderRadius: 6,
        borderSkipped: false,
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { color: d.color, font: { size: 10 } } },
        y: { grid: { color: d.grid }, ticks: { color: d.color, font: { size: 10 } } }
      }
    }
  });
}

function makeDoughnutChart(id, labels, data) {
  const ctx = document.getElementById(id);
  if (!ctx) return;
  return new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels,
      datasets: [{
        data,
        backgroundColor: ['#38BDF8','#0EA5E9','#1D4ED8','#0F2D5E'],
        borderWidth: 2,
        borderColor: getComputedStyle(document.body).getPropertyValue('--card').trim(),
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { font: { size: 10 }, color: chartDefaults().color, padding: 10 }
        }
      },
      cutout: '65%'
    }
  });
}

/* ── Print / Download stub ── */
function downloadPDF(name) {
  showToast(`📄 Downloading ${name}…`, 'success');
}

/* ── Emergency alert ── */
function sendEmergencyAlert() {
  showAlert('Emergency alert dispatched to all staff and students!');
  showToast('🚨 Emergency alert sent!', 'error');
}

/* ── Approve/Reject resource ── */
function approveRequest(name) {
  showToast(`✅ ${name} — Request Approved!`, 'success');
}
function reorderItem(name) {
  showToast(`📦 Reorder request for ${name} sent to supplier!`, 'warning');
}

/* ── Init ── */
document.addEventListener('DOMContentLoaded', () => {
  // Restore theme
  const savedTheme = localStorage.getItem('ktssd_theme');
  if (savedTheme) {
    document.body.dataset.theme = savedTheme;
    const btn = document.getElementById('theme-btn');
    if (btn) btn.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
  }
  // Restore sidebar state
  const sb = document.getElementById('sidebar');
  if (sb && localStorage.getItem('ktssd_sidebar') === '1') {
    sb.classList.add('collapsed');
  }
  // Animate cards in
  document.querySelectorAll('.card,.stat-card,.announcement-card').forEach((el, i) => {
    el.style.animationDelay = `${i * 0.04}s`;
    el.classList.add('fade-in');
  });
});

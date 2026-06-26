/* ═══════════════════════════════════════════════════════════════
   KTSSD ERP — Dashboard Chart Helpers
   FIX: Was empty stub. Chart functions live in main.js.
        This file adds extra chart types not in main.js.
   ═══════════════════════════════════════════════════════════════ */

/* makeLineChart, makeBarChart, makeDoughnutChart, chartDefaults
   are all defined in main.js and available globally. */

/** Radar chart — used by Academic CBC page */
function makeRadarChart(id, labels, data) {
  const ctx = document.getElementById(id);
  if (!ctx) return null;
  const d = chartDefaults();
  return new Chart(ctx, {
    type: 'radar',
    data: {
      labels,
      datasets: [{
        label: 'Performance',
        data,
        borderColor: '#0EA5E9',
        backgroundColor: 'rgba(14,165,233,0.18)',
        borderWidth: 2,
        pointBackgroundColor: '#0EA5E9',
        pointRadius: 4,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        r: {
          grid: { color: d.grid },
          ticks: { color: d.color, font: { size: 9 }, backdropColor: 'transparent' },
          pointLabels: { color: d.color, font: { size: 10 } }
        }
      }
    }
  });
}

/** Side-by-side bar chart — used by Academic CAT comparison */
function makeComparisonBarChart(id, labels, dataset1, dataset2, label1, label2) {
  const ctx = document.getElementById(id);
  if (!ctx) return null;
  const d = chartDefaults();
  return new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [
        { label: label1, data: dataset1, backgroundColor: 'rgba(56,189,248,0.6)',  borderRadius: 4, borderSkipped: false },
        { label: label2, data: dataset2, backgroundColor: 'rgba(15,45,94,0.75)',   borderRadius: 4, borderSkipped: false }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { labels: { color: d.color, font: { size: 10 } } } },
      scales: {
        x: { grid: { display: false }, ticks: { color: d.color, font: { size: 9 } } },
        y: { grid: { color: d.grid },  ticks: { color: d.color, font: { size: 10 } }, min: 0, max: 10 }
      }
    }
  });
}

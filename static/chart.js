// ================================
// Click EA Tool Pro - chart.js
// （損益チャート表示の準備用）
// ================================

// Chart.jsを使用してプレビューを表示する例
// ※ index.html に <canvas id="profitChart"></canvas> を追加したときのみ動作します

document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("profitChart");
  if (!ctx) return;

  const chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["エントリー", "損切り", "利確"],
      datasets: [
        {
          label: "価格ライン",
          data: [150.0, 149.0, 151.0],
          borderColor: "rgb(75, 192, 192)",
          tension: 0.3,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: true },
        title: {
          display: true,
          text: "損益ラインプレビュー",
        },
      },
      scales: {
        y: {
          title: { display: true, text: "価格" },
        },
      },
    },
  });
});

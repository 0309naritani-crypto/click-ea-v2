
// ================================
// Click EA Tool Pro - app.js
// （UIと通信制御のベース）
// ================================

// RRスライダーと入力欄の連動
const rrRange = document.getElementById("rrRange");
const rrInput = document.getElementById("rrInput");
if (rrRange && rrInput) {
  rrRange.addEventListener("input", () => (rrInput.value = rrRange.value));
  rrInput.addEventListener("input", () => (rrRange.value = rrInput.value));
}

// リスク割合スライダーと入力欄の連動
const riskRange = document.getElementById("riskRange");
const riskInput = document.getElementById("riskInput");
if (riskRange && riskInput) {
  riskRange.addEventListener("input", () => (riskInput.value = riskRange.value));
  riskInput.addEventListener("input", () => (riskRange.value = riskInput.value));
}

// OANDA送信テスト
const sendBtn = document.getElementById("sendTestBtn");
if (sendBtn) {
  sendBtn.addEventListener("click", async () => {
  const entry = parseFloat(document.getElementById("entry").value);
  const sl = parseFloat(document.getElementById("sl").value);
  const rr = parseFloat(document.getElementById("rrInput").value);
  const risk = parseFloat(document.getElementById("riskInput").value);

  // ★ BUY/SELLの方向判定をここで実施
  const direction = sl < entry ? "BUY" : "SELL";

  try {
    const response = await fetch("/api/order/send-test", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ direction, entry, sl, rr, risk }),
    });

    const result = await response.json();

    const pipDiff = Math.abs(entry - sl);
    const lossYen = (100 * risk).toFixed(2);
    const profitYen = (lossYen * rr).toFixed(2);

    const box = document.getElementById("resultBox");
    box.style.display = "block";
    box.innerHTML = `
      <h5>📊 損益計算プレビュー</h5>
      <div>方向：${direction}</div>
      <div>エントリー：${entry.toFixed(3)}</div>
      <div>損切り：${sl.toFixed(3)}</div>
      <div>利確：${result.tp.toFixed(3)} pips/div>
      <div>RR：${rr}</div>
      <div>リスク割合：${risk}%</div>
      <div>ロット数：${result.units}</div>
      <div class="mt-2">損失金額：${lossYen}円</div>
      <div>利益金額：${profitYen}円</div>
    `;
  } catch (error) {
    console.error(error);
  }
});

}

// 全決済ボタン
const closeBtn = document.getElementById("closeAllBtn");
if (closeBtn) {
  closeBtn.addEventListener("click", async () => {
    const res = await fetch("/api/positions/close-all", { method: "POST" });
    const data = await res.json();
    alert(data.closed ? "全ポジションをクローズしました" : "失敗しました");
  });
}

// リセットボタン
const resetBtn = document.getElementById("resetBtn");
if (resetBtn) {
  resetBtn.addEventListener("click", () => {
    document.getElementById("entry").value = "";
    document.getElementById("sl").value = "";
    rrRange.value = 1.3;
    rrInput.value = 1.3;
    riskRange.value = 1;
    riskInput.value = 1;
    document.getElementById("resultBox").style.display = "none";
  });
}

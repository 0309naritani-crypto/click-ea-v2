from flask import Flask, render_template, request, jsonify
import os  # ← ここを追加！

app = Flask(__name__)

# ===============================
# トップページ
# ===============================
@app.route("/")
def index():
    return render_template("index.html")

# ===============================
# OANDA送信テスト
# ===============================
@app.post("/api/order/send-test")
def send_test_order():
    data = request.get_json()
    direction = data.get("direction", "BUY")
    entry_price = float(data.get("entry", 0))
    sl_price = float(data.get("sl", 0))
    rr = float(data.get("rr", 1.3))
    risk = float(data.get("risk", 1))

    # 仮のロジック（本番ではOANDA計算に差し替え）
    if direction.upper() == "BUY":
        tp_price = entry_price + (entry_price - sl_price) * rr
    else:
        tp_price = entry_price - (sl_price - entry_price) * rr

    # 損切り幅
    pip_diff = abs(entry_price - sl_price)

    # 仮口座残高
    account_balance = 100000  

    # リスク金額（例：1% → 1000円）
    risk_amount = account_balance * (risk / 100)

    # ロット（仮計算）
    lot = risk_amount / pip_diff  

    # 損失金額と利益金額
    loss_yen = risk_amount
    profit_yen = risk_amount * rr

    return jsonify({
        "direction": direction,
        "entry": entry_price,
        "sl": sl_price,
        "tp": tp_price,
        "pipDiff": pip_diff,
        "rr": rr,
        "risk": risk,
        "units": lot,
        "lossYen": loss_yen,
        "profitYen": profit_yen
    })


# ===============================
# 全ポジションクローズ（テスト用）
# ===============================
@app.post("/api/positions/close-all")
def close_all_positions():
    return jsonify({"closed": True})

# ===============================
# Render用 起動設定
# ===============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

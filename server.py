from flask import Flask, render_template, request, jsonify

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
    tp_price = entry_price + (entry_price - sl_price) * rr
    lot = 1000

    return jsonify({
        "direction": direction,
        "entry": entry_price,
        "sl": sl_price,
        "tp": tp_price,
        "units": lot
    })

# ===============================
# 全ポジションクローズ（テスト用）
# ===============================
@app.post("/api/positions/close-all")
def close_all_positions():
    return jsonify({"closed": True})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)



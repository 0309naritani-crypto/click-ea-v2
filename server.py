from flask import Flask, render_template, request, jsonify
import os

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

    # フロントから送られたdirectionを使用
    direction = data.get("direction", "")
    entry = float(data.get("entry", 0))
    sl = float(data.get("sl", 0))
    rr = float(data.get("rr", 1))
    risk = float(data.get("risk", 1))

    # 利確を自動計算（BUY/SELLで分岐）
    if direction == "BUY":
        tp = entry + abs(entry - sl) * rr
    else:
        tp = entry - abs(entry - sl) * rr

    pip_diff = abs(entry - sl)
    loss_yen = 100 * risk
    profit_yen = loss_yen * rr

    return jsonify({
        "direction": direction,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "pipDiff": pip_diff,
        "rr": rr,
        "risk": risk,
        "units": 1000,
        "lossYen": loss_yen,
        "profitYen": profit_yen
    })


# ===============================
# 全ポジションクローズ（テスト用）
# ===============================
@app.post("/api/positions/close-all")
def close_all_positions():
    return jsonify({"closed": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


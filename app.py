from flask import Flask, request
import os, requests

TOKEN = os.getenv("BOT_TOKEN")  # לא צריך CHAT_ID

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "ok"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    msg = data.get("message") or data.get("edited_message") or {}
    chat = msg.get("chat") or {}
    chat_id = chat.get("id")
    text = msg.get("text", "")

    if not chat_id:
        return {"ok": True}

    reply = f"🤖 קיבלתי: {text}" if text else "🤖 קיבלתי הודעה."
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": reply}
    )
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

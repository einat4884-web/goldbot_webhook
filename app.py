import os
import requests
from flask import Flask, request, jsonify

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    r = requests.post(url, json=payload, timeout=10)
    return r.json()

@app.route("/", methods=["GET"])
def health():
    return jsonify(status="ok", message="Bot is alive")

@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json(silent=True) or {}
    message = (update.get("message")
               or update.get("edited_message")
               or {})
    chat = message.get("chat") or {}
    chat_id = chat.get("id")
    text = message.get("text", "")

    if not chat_id:
        return jsonify(ok=True)

    if text == "/start":
        reply = "שלום! הבוט מחובר ועובד ✅"
    else:
        reply = f"קיבלתי: {text}"

    send_message(chat_id, reply)

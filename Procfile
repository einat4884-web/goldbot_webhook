import os
import requests
from flask import Flask, request, jsonify

TOKEN = os.getenv("BOT_TOKEN", "")
API = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

def send_message(chat_id: int, text: str, keyboard: bool = True):
    url = f"{API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }
    if keyboard:
        # מקלדת מהירה עם כפתורים
        payload["reply_markup"] = {
            "keyboard": [
                [{"text": "✅ מצב בוט"}, {"text": "ℹ️ עזרה"}],
                [{"text": "✨ התחלה"}, {"text": "❌ ביטול"}]
            ],
            "resize_keyboard": True,
            "one_time_keyboard": False
        }
    # שליחה
    r = requests.post(url, json=payload, timeout=10)
    return r.json()

@app.get("/")
def health():
    return jsonify(status="ok", message="bot is alive")

@app.post("/")
def webhook():
    update = request.get_json(silent=True) or {}
    message = update.get("message") or update.get("edited_message") or {}
    chat = message.get("chat") or {}
    chat_id = chat.get("id")
    text = (message.get("text") or "").strip()

    if not chat_id:
        return jsonify(ok=True)

    # לוגיקה פשוטה לשיחה
    if text in ("/start", "✨ התחלה"):
        reply = "שלום! הבוט מחובר ועובד ✅\nשלחי אחת מהאפשרויות:"
    elif text in ("✅ מצב בוט",):
        reply = "מצב: פעיל ✅\nאם לא מגיעות תשובות, בדקי שהטוקן נכון ושיש Webhook."
    elif text in ("ℹ️ עזרה",):
        reply = "פקודות: /start • מצב בוט • עזרה • ביטול"
    elif text in ("❌ ביטול",):
        reply = "בוטל. אני כאן כשתצטרכי 🙂"
    elif text.startswith("/"):
        reply = "לא זיהיתי את הפקודה הזאת. נסי /start"
    else:
        reply = f"קיבלתי: {text}"

    send_message(chat_id, reply, keyboard=True)
    return jsonify(ok=True)

from flask import Flask, request
import requests
import os

# קבלת משתני הסביבה (הטוקן וה־CHAT ID)
TOKEN = os.getenv("BOT_TOKEN", "PUT-YOUR-BOT-TOKEN-HERE")
CHAT_ID = os.getenv("CHAT_ID", "PUT-YOUR-CHAT-ID-HERE")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/send', methods=['GET', 'POST'])
def send_message():
    if request.method == 'GET':
        return {"status": "ok", "message": "GET request received"}

    data = request.json
    message = data.get("message", "Hello from Flask bot!")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    r = requests.post(url, json=payload)
    return r.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

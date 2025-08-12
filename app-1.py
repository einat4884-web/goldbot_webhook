from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def receive_message():
    data = request.get_json()
    return jsonify({
        "ok": True,
        "message_received": data
    })

if __name__ == "__main__":
    # להרצה מקומית
    app.run(host="0.0.0.0", port=5000)

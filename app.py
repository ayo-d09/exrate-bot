from decouple import config
import requests
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app, path="/metrics")

API_KEY = config("KEY")
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def get_conversion(source_currency, target_currency, source_amount):
    response = requests.get(
        f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{source_currency}/{target_currency}/{source_amount}",
        timeout=10
    )
    context = response.json()
    return context["conversion_result"]

def send_message(chat_id, text):
    requests.post(f"{TELEGRAM_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', {})
    chat_id = message['chat']['id']
    text = message.get('text', '').upper().strip()
    if text == '/START':
        send_message(chat_id, "Welcome. Send me a conversion like:\n100 USD to NGN\n50 EUR to GBP")
        return jsonify({"status": "ok"})
    try:
        parts = text.split()
        amount = float(parts[0])
        from_currency = parts[1]
        to_currency = parts[3]
        result = get_conversion(from_currency, to_currency, amount)
        send_message(chat_id, f"{amount} {from_currency} = {round(result, 2)} {to_currency}")
    except:
        send_message(chat_id, "Format: 100 USD to NGN")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
    
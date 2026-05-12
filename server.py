from flask import Flask, request
from strategy import analyze_market
from signals import send_signal

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    symbol = data['symbol']
    price = float(data['price'])

    result = analyze_market(price)

    message = f"""
📊 SIGNAL {symbol}

{result['signal']}

Entry: {price}

TP: {result['tp']}

SL: {result['sl']}
"""

    send_signal(message)

    return {"status": "success"}

@app.route('/')
def home():
    return "Trading Bot Running"

if __name__ == '__main__':
    app.run()

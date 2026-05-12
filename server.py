from flask import Flask, request
import os  # Ajouté pour récupérer le port de Render
from strategy import analyze_market
from signals import send_signal

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Sécurité simple pour éviter les erreurs si data est vide
    if not data:
        return {"status": "error", "message": "No data received"}, 400

    symbol = data.get('symbol', 'N/A')
    price = float(data.get('price', 0))

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
    # Récupère le port via la variable d'environnement 'PORT' (par défaut 5000)
    # L'hôte '0.0.0.0' est INDISPENSABLE pour que Render puisse accéder à l'app
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

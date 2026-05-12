def analyze_market(price):

    if price > 3300:
        return {
            "signal": "BUY",
            "tp": price + 10,
            "sl": price - 5
        }

    else:
        return {
            "signal": "SELL",
            "tp": price - 10,
            "sl": price + 5
        }

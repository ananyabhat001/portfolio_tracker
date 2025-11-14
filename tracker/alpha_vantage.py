import os
import requests

def get_stock_price(symbol):
    api_key = os.environ.get('ALPHA_VANTAGE_API_KEY', '0C4MY258GEB8F466')  # Prefer environment variable for security!
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price_str = data.get('Global Quote', {}).get('05. price')
        if price_str is not None:
            return float(price_str)
    except Exception as e:
        print(f'Error fetching price for {symbol}: {e}')
    return None

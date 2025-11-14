import os
import requests

def get_stock_price(symbol):
    api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    print(data)  # This will write the Alpha Vantage API's raw response to your Render log
    try:
        price = float(data['Global Quote']['05. price'])
        return price
    except (KeyError, ValueError):
        return None

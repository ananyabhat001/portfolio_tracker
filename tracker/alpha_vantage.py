import requests

API_KEY = '0C4MY258GEB8F466'

def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url).json()
    try:
        price = float(response['Global Quote']['05. price'])
        return price
    except (KeyError, ValueError):
        return None

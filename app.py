import requests
import json

def get_keys(path):
    with open(path) as f:
        return json.load(f)
keys = get_keys("./apikey.json")
api_key = keys['api_key']


def getStockPrice(stock, api_key):
    price = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}').json()
    price = ((price['Global Quote']['05. price']))
    print(f'The price of ${stock} is {price}')

stock_symbol = str(input("What stock symbol would you like the price of: "))
getStockPrice(stock_symbol, api_key)
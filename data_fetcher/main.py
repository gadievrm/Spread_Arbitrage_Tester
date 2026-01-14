import requests
import json

r = requests.get("https://api.bybit.com/v5/market/kline?symbol=BTCUSDT&interval=1&limit=500")
print (r.json())

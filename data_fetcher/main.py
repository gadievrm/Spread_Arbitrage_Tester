import requests
import csv
import json


def bybit(url, symbol, interval, limit, start, end):
    params = f'?symbol={symbol}&interval={interval}&limit={limit}&start={start}&end={end}'
    req = url + params
    print(req)
    return requests.get(req)

def sep(rJson):
    result = []
    for item in rJson['result']['list']:
        result.append([item[0],item[4]])
        
    return result


                                                           #Symbol  interv limit   start            end
#test                                                     BTCUSDT    1    2000    1670601600000    1670608800000
r = bybit('https://api.bybit.com/v5/market/kline', 'BTCUSDT', '1', '2000', '1670601600000', '1670608800000')


responseJson = r.json()
twoRows = sep(responseJson)

with open('new_file.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(twoRows) 
print(twoRows[0])



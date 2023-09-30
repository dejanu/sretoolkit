#!/usr/bin/env python

# call API https://api.coindesk.com/v1/bpi/currentprice.json
# get the current price of bitcoin in USD
# print the price

import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)
data = response.json()
print(data['bpi']['USD']['rate'])

if __name__ == '__main__':
    
    #call API
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    
import json
import requests
import os
from tabulate import tabulate



def api_call():
    response = requests.get('https://api.coincap.io/v2/assets')
    data = response.json() if response and response.status_code == 200 else None
    
    return data


def create_pairs(data):
    pairs = []
    for c in data['data']:
        pairs.append([c['rank'], c['name'], c['priceUsd'], c['changePercent24Hr'], c['supply'], c['marketCapUsd']])
        
    return pairs


def generate_table(pairs):
    print(tabulate(pairs, headers=['Rank', 'Asset', 'Price (USD)', 'Change in % (24Hr)', 'Supply', 'Market Cap (USD)'], floatfmt=".6f", tablefmt="grid"))


def run():
    os.system('clear')
    data = api_call()
    pairs = create_pairs(data)
    generate_table(pairs)


if __name__ == '__main__':
    run()
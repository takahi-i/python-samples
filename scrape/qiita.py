import requests
from bs4 import BeautifulSoup
import json


def get_trend_items():
    r = requests.get('https://qiita.com/') 
    soup = BeautifulSoup(r.text, "html.parser")
    target_div = soup.select('div[data-hyperapp-app="Trend"]')[0]
    trend_items = json.loads(target_div.get('data-hyperapp-props'))
    return trend_items

items = get_trend_items()
for item in items['trend']['edges']:
    print(item['node']['title'])

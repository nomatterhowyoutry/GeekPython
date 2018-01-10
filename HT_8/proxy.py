import requests
import json
import random

proxy_url = 'https://gimmeproxy.com/api/getProxy?get=true&supportsHttps=true&anonymityLevel=1&maxCheckPeriod=3600'
proxy_list = []
for x in range(0, 20):
    if proxy_list:
        proxy = requests.get(proxy_url, timeout=5, proxies = random.choice(proxy_list))
    else:
        proxy = requests.get(proxy_url, timeout=5)
    if proxy:
        proxy_json = proxy.json()
        proxy_data = {proxy_json['type']: proxy_json['ipPort']}
        proxy_list.append(proxy_data)

print(proxy_list)

if proxy_list:
    with open('proxy_list.json', 'w') as f:
        json.dump(proxy_list, f)
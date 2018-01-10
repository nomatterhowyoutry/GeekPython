import bs4
import requests
import time
from lxml import html
import random
import json
import xlsxwriter
import csv
from fake_useragent import UserAgent

start = time.time()

json_data = open('proxy_list.json').read()
proxy_list = json.loads(json_data)

url = 'https://www.expireddomains.net'
list = []
next_page = '/deleted-tel-domains'


def get_user_agent():

    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'

    try:
        ua = UserAgent().random
    except Exception:
        return {'User-Agent': ua}
    else:
        return {'User-Agent': ua}


def get_proxy():

    global proxy_list

    return random.choice(proxy_list)

# main loop
while True:
    print(url + next_page)
    r = requests.get(url=url + next_page, proxies=get_proxy(),
                     headers=get_user_agent())
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', class_='base1')
    content = table.select('tbody')[0].select('tr')
    for part in content:
        domain_name = part.select('td.field_domain')[
            0].select('a.namelinks')[0].text
        list.append(domain_name)
    try:
        next_page = soup.select('a.next')[0].get('href')
        time.sleep(random.uniform(3, 5))
    except:
        break

# writing data into files
with open('domain.json', 'w') as outfile:
    json.dump(list, outfile)

with open('domain.txt', 'w') as outfile:
    outfile.writelines(['{}\n'.format(i) for i in list])

workbook = xlsxwriter.Workbook('domain.xlsx')
worksheet = workbook.add_worksheet()
row = 0
worksheet.write(row, 0, 'domain-name')
for i in list:
    row += 1
    worksheet.write(row, 0, i)
workbook.close()

with open('domain.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=('domain-name', ))
    writer.writeheader()
    for i in list:
        writer.writerow({'domain-name': i})

# output with time elapsed
print('application ended up, time: {:.3f} sec,'.format(time.time() - start))

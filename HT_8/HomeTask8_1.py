import requests
import bs4
import time
import csv
import time
import json
import xlsxwriter

start = time.time()

url = 'http://quotes.toscrape.com'
r = requests.get(url=url)
soup = bs4.BeautifulSoup(r.content, 'lxml')
quotes = soup.select('div.quote')
quote = quotes[0]
next_page_url = ''
has_next = True
fnames = ('text', 'author-url', 'author-title', 'born-date',
          'born-place', 'about', 'tag-names', 'tag-urls', 'id', 'id-url')
file = open('quotes.csv', 'w')
writer = csv.DictWriter(file, fieldnames=fnames)
writer.writeheader()
data = []
while has_next:
    r = requests.get(url=url + next_page_url)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    quotes = soup.select('div.quote')
    for quote in quotes:
        text = quote.select('span.text')[0].text[1:-1]
        text = text.replace(";", "")  # ';' breakes structure in csv file
        author = quote.select('small.author')[0].text
        author_url = url + quote.select('span > a')[0].get('href')
        r2 = requests.get(url=author_url)
        soup2 = bs4.BeautifulSoup(r2.content, 'lxml')
        details = soup2.select('div.container')[0]
        born_date = details.select('span.author-born-date')[0].string
        born_place = details.select('span.author-born-location')[0].string
        about = details.select('div.author-description')[0].string
        tag_name = [i.string for i in quote.select('.tags > a')]
        tag_url = [i.get("href") for i in quote.select('.tags > a')]
        id = author_url.split('/')[-1].lower()
        data.append({'author': (author_url, author, born_date, born_place, about),
                     'tags': (tag_name, tag_url, text, author, author_url) })
        writer.writerow({
            fnames[0]: text,
            fnames[1]: author_url,
            fnames[2]: author,
            fnames[3]: born_date,
            fnames[4]: born_place,
            fnames[5]: about,
            fnames[6]: tag_name,
            fnames[7]: tag_url,
            fnames[8]: id,
            fnames[9]: author_url
        })
    try:
        next_page_url = soup.select('ul.pager')[0].select(
            'li.next a')[0].get('href')
    except:
        has_next = False

with open('quotes.json', 'w') as f:
    json.dump(data, f)

with open('quotes.txt', 'w') as f:
    f.writelines(['{}\n'.format(i) for i in data])

workbook = xlsxwriter.Workbook('quotes.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for i in data:
    worksheet.write(row, 0, '{}'.format(i['author']))
    worksheet.write(row, 1, '{}'.format(i['tags']))
    row += 1
workbook.close()

print('application ended up, time: {:.3f} sec,'.format(time.time() - start))
file.close()

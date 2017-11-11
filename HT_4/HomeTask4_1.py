import re
import csv

f1 = open('openerp-server.log')
pattern = re.compile('(.*\d.-\d.-\d.*\d.:\d.:\d.).*(ERROR|WARNING|CRITICAL) (\pg|\?|\None) (.*)\r')

ans = []
with open('openerp-server.log', 'r') as file:
        for line, text in enumerate(file):
            if re.findall(pattern, text):
                row = re.findall(pattern, text)
                row = (line,) + row[0]
                ans.append(row)

with open('all_data.csv','wb') as file:
    writer = csv.DictWriter(file, fieldnames = ('line_id', 'marker', 'date_time', 'description'))
    writer.writeheader()
    writer.writerows({'line_id': row[0], 'marker': row[2], 'date_time': row[1],
                      'description': row[4]} for row in ans)
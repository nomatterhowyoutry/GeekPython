import re
import csv

pattern = re.compile('(.*\d.-\d.-\d.*\d.:\d.:\d.).*(ERROR|WARNING|CRITICAL) (\pg|\?|\None) (.*)\r')
file1 = open('openerp-server.log', 'r')
file2 = open('all_data.csv','wb')
writer = csv.DictWriter(file2, fieldnames = ('line_id', 'marker', 'date_time', 'description'))
writer.writeheader()

for line, text in enumerate(file1):
    if re.findall(pattern, text):
        row = re.findall(pattern, text)
        writer.writerow({'line_id': line, 'marker': row[0][1], 'date_time': row[0][0],'description': row[0][3]})
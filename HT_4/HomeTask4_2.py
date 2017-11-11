import re
import csv

f1 = open('openerp-server.log')
pattern = re.compile('(.*\d.-\d.-\d.*\d.:\d.:\d.).*(ERROR|WARNING|CRITICAL) (\pg|\?|\None) (.*)\r')

ans = []
with open('openerp-server.log', 'r') as file:
        for text in file:
            if re.findall(pattern, text):
                row = re.findall(pattern, text)
                in_list = False
                for i in range(0, len(ans)):
                    if row[0][3] in ans[i]:
                        if row[0][1] in ans[i]:
                            ans[i][0] += 1
                            in_list = True
                            break
                if not in_list:
                    ans.append([1] + list(row[0]))

with open('unique.csv','wb') as file:
    writer = csv.DictWriter(file, fieldnames = ('count', 'marker', 'date_time', 'description'))
    writer.writeheader()
    writer.writerows({'count': row[0], 'marker': row[2], 'date_time': row[1], 'description': row[4]} for row in ans)
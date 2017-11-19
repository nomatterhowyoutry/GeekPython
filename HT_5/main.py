import argparse
from urllib.request import urlopen
import logging
import json
import re
import csv
import os
import time
from config import *

start = time.time()

# Preparing logger parameters
logger = logging.getLogger("main.py")
logger.setLevel(logging.INFO)
fh = logging.FileHandler(folder_name + log_output)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info(u'Application started!')

#Creating directory
if os.path.isdir(os.path.abspath(os.curdir)+folder_name):
    os.mkdir(folder_name)

# Preparing argparser
parser = argparse.ArgumentParser(
    description='You can choose between askstories, showstories, newstories, jobstories')
parser.add_argument('--tag','-t', type=str, default='newstories', help='tag of field to parse')
parser.add_argument('--limit','-limit', type=int, default=5, help='limit of parsed ID')
args = parser.parse_args()
tag = args.tag
limit = args.limit

# Getting array of text ID's
logger.info(u"Getting ID's with {0} tag".format(tag))
if tag in choices:
    url = 'https://hacker-news.firebaseio.com/v0/' + tag + '.json?print=pretty'
    response = urlopen(url, timeout=5)
    data = json.loads(response.read().decode('utf8'))
else:
    print('Wrong tag name!')
    logger.error(u'Application terminated: Wrong tag name!')
    quit()

# Getting data from every ID
logger.info(u"Getting data from ID's")
untag = re.compile('<[^>]*>')
data1 = []
max = []
for i in data[:limit]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(i) + '.json?print=pretty'
    response = urlopen(url, timeout=5)
    line = json.loads(response.read().decode('utf8'))
    data1.append(line)
    if 'text' in line.keys():
        # Remove useless tags
        line['text'] = untag.sub('', line['text'])
    fnames = [k for k, v in line.items()]
    if len(max) < len(fnames):
        max = fnames

# Creating 'reports.csv'
logger.info(u'Writing into reports.csv')
file = open(os.path.abspath(os.curdir)+'/'+folder_name+csv_output, 'w')
fnames = max
writer = csv.DictWriter(file, fieldnames = fnames)
writer.writeheader()
for i in data1:
    row = {}
    for j in fnames:
        if j in i.keys():
            row.update({j:i[j]})
        else:
            row.update({j:''})
    writer.writerow(row)

print('main.py ended up, time: {:.3f} sec,'.format(time.time() - start),
      'with {0} objects created'.format(len(data1)))
file.close()
logger.info(u'Application ended up correctly!')
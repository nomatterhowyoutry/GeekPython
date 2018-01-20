from urllib.request import urlopen
import argparse
import json
import pickle
import re
import time
import os
import logging
import psycopg2
from datetime import datetime
from config import *

# Creating directory
if not os.path.isdir(os.path.abspath(os.curdir) + folder_name):
    os.mkdir(os.path.abspath(os.curdir) + folder_name)

# Preparing argparser
parser = argparse.ArgumentParser(
    description='You can choose between askstories, showstories, newstories, jobstories or all')
parser.add_argument('--tag', '-t', type=str,
                    default='showstories', help='tag of field to parse')
args = parser.parse_args()
tag = args.tag


class Main(object):
    """docstring for Main"""

    # Starting point of counting time
    start = time.time()

    # Connecting to DataBase
    conn = psycopg2.connect("dbname=HomeTask10 user=postgres")
    cur = conn.cursor()

    # Preparing logger parameters
    logger = logging.getLogger("HomeTask9.py")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(os.path.abspath(
        os.curdir) + folder_name + log_output)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info(u'Application started!')

    def __init__(self):
        super(Main, self).__init__()

    def into_html(self):
        # Creating 'index.html' with all data
        body = ''
        start = '''<!DOCTYPE html>
        <html>
        <head>
            <link href="style.css" rel="stylesheet">
            <title>''' + str(datetime.now()) + '''</title>
        </head>
        <body>
        '''
        end = '''
        </body>
        </html>'''
        for i in choices:
            body += str(self.get_table(i))
        with open(os.path.abspath(os.curdir) + folder_name + html_output, 'w') as f:
            f.write(start + body + end)
        print('Script ended up, time: {:.3f} sec,'.format(
            time.time() - self.start))
        self.logger.info(u'Application ended up correctly!')
        self.cur.close()
        self.conn.close()

    def get_table(self, part):
        # Wrapping into <table> each table
        try:
            self.cur.execute("SELECT data as data FROM {};".format(part))
            data = self.cur.fetchall()
        except:
            self.logger.error(u'No {} table to read data from!'.format(part))
            return ''
        self.logger.info(u'Wrapping into html {} tag data'.format(part))
        fnames = max([list(i[0].keys()) for i in data])
        string = '<tr>\n'
        for key in fnames:
            string += '<td><b>' + str(key) + '</b></td>'
        string += '\n</tr>\n'
        for item in data:
            string += '<tr>\n'
            for key in fnames:
                if key in item[0].keys():
                    string += '<td>' + str(item[0][key]) + '</td>'
                else:
                    string += '<td> </td>'
            string += '\n</tr>\n'
        return '''<a class="main-item" href="javascript:void(0);" >''' + part + '''</a>
        <ul class="sub-menu">
        <li>\n<table>''' + string + '''\n</table>
        </li>  
        </ul><br>'''

    def get_data(self, tag):
        # Getting data from every ID
        print("Getting data with {} tag".format(tag))
        self.logger.info(u"Getting data from ID's")
        untag = re.compile("<[^>]*>|'")  # remove html tags in text
        self.cur.execute("""CREATE TABLE IF NOT EXISTS {} ( ID serial NOT NULL PRIMARY KEY, data json NOT NULL )""".format(tag))
        self.cur.execute("SELECT data -> 'id' as id FROM {};".format(tag))
        query = """INSERT INTO {} (data) VALUES ('%s');""".format(tag)
        Uids = self.cur.fetchall()
        ids = self.get_ids(tag)
        for i in ids:
            if (i,) not in Uids:
                url = 'https://hacker-news.firebaseio.com/v0/item/' + \
                    str(i) + '.json?print=pretty'
                try:
                    response = urlopen(url, timeout=5)
                except ConnectionError:
                    self.logger.warning(u"Connection timed out")
                    continue
                line = json.loads(response.read().decode('utf8'))
                if line:
                    if 'text' in list(line.keys()):
                        line['text'] = untag.sub('', line['text'])
                    line = json.dumps(line).translate(str.maketrans({"'": " "}))
                    self.cur.execute(query % line)
                    self.conn.commit()

    def get_ids(self, tag):
        # Getting array of text ID's
        if tag in choices:
            self.logger.info(u"Getting ID's with {0} tag".format(tag))
            url = 'https://hacker-news.firebaseio.com/v0/' + tag + '.json?print=pretty'
            response = urlopen(url, timeout=5)
            data = json.loads(response.read().decode('utf8'))
            return data
        else:
            print('Wrong tag name!')
            self.logger.error(u'Application terminated: Wrong tag name!')
            quit()

if __name__ == '__main__':
    main = Main()
    if tag == 'all':
        for tag in choices:
            main.get_data(tag)
        main.into_html()
    else:
        main.get_data(tag)
        main.into_html()

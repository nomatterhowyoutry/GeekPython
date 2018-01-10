from urllib.request import urlopen
import argparse
import json
import pickle
import re
import time
import os
import logging
from datetime import datetime
from config import *

# Creating directory
if not os.path.isdir(os.path.abspath(os.curdir) + folder_name):
    os.mkdir(folder_name)

# Preparing argparser
parser = argparse.ArgumentParser(
    description='You can choose between askstories, showstories, newstories, jobstories or all')
parser.add_argument('--tag', '-t', type=str,
                    default='jobstories', help='tag of field to parse')
args = parser.parse_args()
tag = args.tag


class Main(object):
    """docstring for Main"""

    # Starting point of counting time
    start = time.time()

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

    def save_data(self, tag):
        # Creating pickle file with unique elements
        data = self.get_data(tag)
        self.logger.info(u'Writing into pickle file')
        with open(os.path.abspath(os.curdir) + folder_name + '/' + str(tag) + '.pkl', 'wb') as f:
            pickle.dump(data, f)

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
            body += str(self.get_table(str(i)))
        with open(os.path.abspath(os.curdir) + folder_name + html_output, 'w') as f:
            f.write(start + body + end)
        print('Script ended up, time: {:.3f} sec,'.format(
            time.time() - self.start))
        self.logger.info(u'Application ended up correctly!')

    def get_table(self, part):
        # Wrapping into <table> each pickle file
        try:
            with open(os.path.abspath(os.curdir) + folder_name + '/' + str(part) + '.pkl', 'rb') as f:
                data = pickle.load(f)
        except:
            self.logger.error(u'No pkl file to read from!')
            return ''
        self.logger.info(u'Wrapping into html {} tag data'.format(part))
        fnames = max([list(i.keys()) for i in data])
        string = '<tr>\n'
        for key in fnames:
            string += '<td><b>' + str(key) + '</b></td>'
        string += '\n</tr>\n'
        for item in data:
            string += '<tr>\n'
            for key in fnames:
                if key in item.keys():
                    string += '<td>' + str(item[key]) + '</td>'
                else:
                    string += '<td> </td>'
            string += '\n</tr>\n'
        return '''<a class="main-item" href="javascript:void(0);" >''' + part + '''</a>
        <ul class="sub-menu">
        <li>\n<table>''' + string + '''\n</table>
        </li>  
        </ul><br>'''

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

    def get_data(self, tag):
        # Getting data from every ID
        self.logger.info(u"Getting data from ID's")
        untag = re.compile('<[^>]*>')  # remove html tags in text
        data = []
        ids = self.get_ids(tag)
        for i in ids:
            url = 'https://hacker-news.firebaseio.com/v0/item/' + \
                str(i) + '.json?print=pretty'
            try:
                response = urlopen(url, timeout=5)
            except ConnectionError:
                self.logger.warning(u"Connection timed out")
                continue
            line = json.loads(response.read().decode('utf8'))
            if 'text' in line.keys():
                line['text'] = untag.sub('', line['text'])
            data.append(line)
        return data

if __name__ == '__main__':
    main = Main()
    if tag == 'all':
        for tag in choices:
            # main.save_data(tag)
        main.into_html()
        quit()
    else:
        # main.save_data(tag)
        main.into_html()

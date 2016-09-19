#!/usr/bin/env 

from __future__ import unicode_literals
import sys
import numpy as np
import pandas as pd
import sqlite3
import urllib, urllib2
from bs4 import BeautifulSoup ## To install do - conda install beautifulsoup4
import re
import json
import requests
import hidden
import datetime


# conda create --name Env_Python2712 python=2.7.12

# activate Env_Python2712


#### Connect to (or Create) Database for the job postings from Indeed ####

conn = sqlite3.connect('guardiancrawl_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Tables ####

## Drop tables if need to restart
# cur.execute('DROP TABLE IF EXISTS JobPost_Parse_HTML ')


## Create tables JobPost_Parse_HTML 
# cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_Parse_HTML
#	(jp_parse_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
#	, jp_url_id int)''')

####

##################################################################
##################################################################
				## Parse HTML from database
##################################################################
##################################################################

# select HTML to parse
# parse html
# enter parse html into database



#### Select HTML to Parse

# url_status_ok = 200
# has_HTML_been_parsed_already = 0
# cur.execute('SELECT jp_url_id FROM JobPost_URLs where url_status = ? and parsed = ?', (str(url_status_ok), str(has_HTML_been_parsed_already), ))
# jp_url_id_all = cur.fetchall()
# print(type(jp_url_id_all)) # is a list
# for item in jp_url_id_all:

#### Scrape HTML



cur.execute('SELECT HTML FROM JobPost_HTML WHERE jp_url_id = ? ', (1, ))
html = cur.fetchone()[0]

print(html[0:2000])





# soup = BeautifulSoup(html, "html.parser")
# 
# header = soup('h1')
# 
# print(header)['title']# 
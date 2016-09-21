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


#### Create Stock Price Table ####

## Drop tables if need to restart
# cur.execute('DROP TABLE IF EXISTS JobPost_URLs ')
# cur.execute('DROP TABLE IF EXISTS JobPost_HTML ')


## Create tables JobPost_URL_Scrapped
cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_URLs
  (jp_url_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
  , guardian_job_id int
  , url_date DATE
  , url TEXT UNIQUE
  , url_status int
  , parsed TEXT DEFAULT 0)''')

cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_HTML
  (jp_html_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
  , jp_url_id INTEGER
  , HTML TEXT)''')

####

##################################################################
##################################################################
				## Crawl the guardian jobs site
##################################################################
##################################################################


#### Use the base URL to get the actual job spec ####

	## Job titles
		# Python Data Engineer

# go through each job on theguardian website using 6386547 plus 1
# check the html text for keywords: sql python analyst
# store url
# dump html as text
# add 1 
# continue


base_url = 'https://jobs.theguardian.com/job/'
url_headers = { 'User-Agent': 'Mozilla/5.0' }

job_count = 0
while job_count < 10:
	job_count = job_count + 1
	# guardian_job_id = 6377990 + 1	# starting job id, will become max job id from the database.
	
	cur.execute('SELECT max(guardian_job_id) FROM JobPost_URLs')
	guardian_job_id = cur.fetchone()[0] + 1 # Adds 1 to the max guardian job id
	print(guardian_job_id)

	url = base_url + str(guardian_job_id)
	r = requests.get(url, headers=url_headers)
	print(r.url)
	print(r.status_code)

	cur.execute('''INSERT INTO JobPost_URLs (guardian_job_id, url_date, url, url_status) VALUES (?, ?, ?, ?)''', 
		(guardian_job_id, datetime.datetime.now().strftime ("%Y%m%d"), r.url, r.status_code, ) )

	#### Scrape HTML

	cur.execute('SELECT jp_url_id FROM JobPost_URLs WHERE guardian_job_id = ? ', (guardian_job_id, ))
	jp_url_id = cur.fetchone()[0]

	html = r.content

	cur.execute('''INSERT INTO JobPost_HTML (jp_url_id, HTML) VALUES (?, ?)''', 
		(jp_url_id, html) )

	conn.commit()

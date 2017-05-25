#!/usr/bin/env
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys		# sys.exit()
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

conn = sqlite3.connect('harnhamcrawl_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Tables ####

## Drop tables if need to restart
# cur.execute('DROP TABLE IF EXISTS JobPost_URLs ')
# cur.execute('DROP TABLE IF EXISTS JobPost_HTML ')


## Create tables JobPost_URL_Scrapped
cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_URLs
  (jp_url_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
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
				## Crawl the harnham jobs site
##################################################################
##################################################################


#### Use the query site to get the actual job specs ####

	# Python
	# London

# go through each job result on harnham search query
# the go to the job spec of that job result
# store url
# dump html as text

h_url_pyldn = '?s=1&o4=&q=python&o1=&matchany=0&o2=893&ij=0&ds=&e=&page=1&lang=&referral=0&sortdir=desc&st=0&o3=&sortby=WebsiteDate&pagesize=10'
h_url_ldn =   '?s=1&o4=&q=&o1=&matchany=0&o2=652&ij=0&ds=&e=&page=1&lang=&referral=0&sortdir=desc&st=0&o3=&sortby=WebsiteDate&pagesize=100'

base_url = 'http://www.harnham.com/jobs/'
url_headers = { 'User-Agent': 'Mozilla/5.0' }

url = base_url + str(h_url_ldn)
r = requests.get(url, headers=url_headers)
print(r.url)
# print(r.status_code)

soup = BeautifulSoup(r.content, "html.parser")

#print(soup)

# <table cellspacing="0" class="vacancyResults"> == $0
for table in soup.findAll('table', attrs={'class': 'vacancyResults'}):
	for a in table.findAll('a', attrs={'class': 'jobResultsTitle'}):
		print('')
		print('')
		print((a.contents[0]).encode('utf8'))
		print(a.get('href'))
		job_url = a.get('href')

#### Try putting URL into table, if can't then it's already in there. URL must be unique.
		try:
			cur.execute('''INSERT INTO JobPost_URLs (url_date, url) VALUES (?, ?)''', 
				(datetime.datetime.now().strftime ("%Y%m%d"), job_url, ) )
			print('inserting url (job) into table as not there already.')

		except:
			print('URL (job) already in database')
			continue

#### Update the URL status
		job_r = requests.get(job_url, headers=url_headers)
		#print(job_r.url)
		print(job_r.status_code)
		cur.execute('''UPDATE JobPost_URLs SET url_status = (?) WHERE url = (?)''', 
				(job_r.status_code, job_r.url, ) )
			
#### Insert HTML into table

		cur.execute('SELECT jp_url_id FROM JobPost_URLs WHERE url = ? ', (job_r.url, ))
		jp_url_id = cur.fetchone()[0]

		html = r.content

		cur.execute('''INSERT INTO JobPost_HTML (jp_url_id, HTML) VALUES (?, ?)''', 
			(jp_url_id, html) )	


		conn.commit()

cur.close()
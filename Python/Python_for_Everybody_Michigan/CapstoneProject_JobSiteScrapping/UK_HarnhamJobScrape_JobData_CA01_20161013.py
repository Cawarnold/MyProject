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

http://www.harnham.com/jobs/?s=1&o4=&q=python&o1=&matchany=0&o2=893&ij=0&ds=&e=&page=1&lang=&referral=0&sortdir=desc&st=0&o3=&sortby=WebsiteDate&pagesize=10


base_url = 'https://jobs.theguardian.com/job/'
url_headers = { 'User-Agent': 'Mozilla/5.0' }

## Get maximum guardian_job_id

cur.execute('SELECT max(guardian_job_id) FROM JobPost_URLs')
guardian_job_id = cur.fetchone()[0]

# If restarting database from scratch, then need starter guardian_job_id.
if not guardian_job_id:
	guardian_job_id = 6377990 	# guardian_job_id = 6377990 # starting job id, will become max job id from the database.

print('Current max guardian job id:  ' + str(guardian_job_id))

job_count = 0
while job_count < 10:
	job_count = job_count + 1	
	guardian_job_id = int(guardian_job_id) + int(1)

	url = base_url + str(guardian_job_id)
	r = requests.get(url, headers=url_headers)
	print(r.url)

#### Skip URLs where the status_code is not 200.
	if r.status_code != 200:
		print('     URL Status :'+str(r.status_code)+'  ...   URL skipped')
		continue

#### If Date Posted was yesterday stop running query

	soup = BeautifulSoup(r.content, "html.parser")

	dt_items = []
	dd_items = []
	for item in soup.findAll('div', attrs={'class': 'grid'}):
		for dts in item.findAll("dt"):
			dt_items.append(re.sub('[^A-Za-z0-9\-]+', '', dts.contents[0]))
		for dds in item.findAll("dd"):
			dd_items.append(re.sub('[^A-Za-z0-9\-]+', '', dds.contents[0]))

	job_posted = ''

	count_dt_items = 0
	while count_dt_items < 15:
		count_dt_items = count_dt_items + 1
		if dt_items[count_dt_items] == 'Posted': job_posted 				= dd_items[count_dt_items]

	span_items = []
	for item in soup.findAll('div', attrs={'class': 'grid'}):
		for dds in item.findAll("dd"):
			for spans in dds.findAll("span"):
				#print(spans.attrs['itemprop'])
				#print(spans.contents[0])
				if spans.attrs['itemprop'] == 'datePosted' and job_posted == '': job_posted = re.sub('[^A-Za-z0-9\-]+', '',spans.contents[0])


	yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d%b%Y') 

	print(job_posted)
	print(yesterday)

	if job_posted == yesterday:
		print('Job posts up to date: ' + str(yesterday))
		print('Quitting program...')
		sys.exit()


#### Insert job ID and URLs into JobPost_URLs

	cur.execute('''INSERT INTO JobPost_URLs (guardian_job_id, url_date, url, url_status) VALUES (?, ?, ?, ?)''', 
		(guardian_job_id, datetime.datetime.now().strftime ("%Y%m%d"), r.url, r.status_code, ) )

#### Scrape HTML

	cur.execute('SELECT jp_url_id FROM JobPost_URLs WHERE guardian_job_id = ? ', (guardian_job_id, ))
	jp_url_id = cur.fetchone()[0]

	html = r.content

	cur.execute('''INSERT INTO JobPost_HTML (jp_url_id, HTML) VALUES (?, ?)''', 
		(jp_url_id, html) )

	conn.commit()
cur.close()
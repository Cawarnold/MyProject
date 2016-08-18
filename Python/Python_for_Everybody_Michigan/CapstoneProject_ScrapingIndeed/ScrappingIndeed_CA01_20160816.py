#!/usr/bin/env Env_Python2712

import numpy as np
import pandas as pd
import sqlite3
import urllib
from bs4 import BeautifulSoup ## To install do - conda install beautifulsoup4
import re



# conda create --name Env_Python2712 python=2.7.12
# activate Env_Python2712

## Program Setup
	# Create database and tables
	# Get first page of job postings. 
	# Scrape all hrefs. Store in table.
	# Scrape individual job posting for the HTML, clean up, output list of words.
	# Manage URLs to access via the job postings 
# 


#### Connect to (or Create) Database for the job postings from Indeed ####

conn = sqlite3.connect('indeed_job_postings.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Stock Price Table ####

## Drop tables if need to restart
#cur.execute('DROP TABLE IF EXISTS Stock_EOD_Prices ')
cur.execute('DROP TABLE IF EXISTS JobPost_URL_Scrapped ')

## Create tables JobPost_URL_Scrapped
cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_URL_Scrapped
	(url_id INTEGER PRIMARY KEY, url_date DATE,  url TEXT UNIQUE
	,scrapped INTEGER DEFAULT 0)''')

--- creata other table for job title, company, salary, key words...
####



#### Always page 1, for now ####

url = 'http://www.indeed.co.uk/jobs?q=data+scientist&l=London'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a') ## 'a' is an HTML tag <a linkstuff <\a>

for tag in tags:
	print tag.get('href', None)



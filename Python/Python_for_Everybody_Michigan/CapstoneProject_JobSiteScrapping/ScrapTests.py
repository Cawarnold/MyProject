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

h_url = '?s=1&o4=&q=python&o1=&matchany=0&o2=893&ij=0&ds=&e=&page=1&lang=&referral=0&sortdir=desc&st=0&o3=&sortby=WebsiteDate&pagesize=10'


base_url = 'http://www.harnham.com/jobs/'
url_headers = { 'User-Agent': 'Mozilla/5.0' }

url = base_url + str(h_url)
r = requests.get(url, headers=url_headers)
print(r.url)
# print(r.status_code)

soup = BeautifulSoup(r.content, "html.parser")

#print(soup)

# <table cellspacing="0" class="vacancyResults"> == $0
for table in soup.findAll('table', attrs={'class': 'vacancyResults'}):
	for a in table.findAll('a', attrs={'class': 'jobResultsTitle'}):
		print(a.contents[0])
		print(a.get('href'))
		job_url = a.get('href')

		try:
			print('Trying url (job)')
			cur.execute('''INSERT INTO JobPost_URLs (url_date, url) VALUES (?, ?,)''', 
				(datetime.datetime.now().strftime ("%Y%m%d"), r.url, ) )
			print('URL inserted')

		except:
			print('URL (job) already in database')


		job_r = requests.get(job_url, headers=url_headers)
		print(job_r.url)
		print(job_r.status_code)
		soup = BeautifulSoup(job_r.content, "html.parser")






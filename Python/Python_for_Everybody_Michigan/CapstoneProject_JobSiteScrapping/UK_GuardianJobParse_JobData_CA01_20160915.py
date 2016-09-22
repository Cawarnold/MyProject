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
# cur.execute('DROP TABLE IF EXISTS JobPost_Details ')


## Create tables JobPost_Parse_HTML 
cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_Details
	(jp_parse_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
	, jp_url_id int)''')

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


cur.execute('SELECT HTML FROM JobPost_HTML WHERE jp_url_id = ? ', (3, ))
html = cur.fetchone()[0]

#print(html[0:2000])


soup = BeautifulSoup(html, "html.parser")

#########################################
#### Method for extracting Job Title ####

#for item in soup.findAll('div', attrs={'class': 'grid'}):
#	print(item.text)
#	print(type(item.text))
#	print(item)
#	print(type(item))

#### Gets Header -- Job Title
#for item in soup.findAll('div', attrs={'class':'grid'}):
#	print(item.h1.contents[0])
#	print(type(item.h1.contents[0]))

for item in soup.findAll('div', attrs={'class':'grid'}):
	for h1 in item.findAll('h1', attrs={'itemprop':'title'}):
		job_title = str(h1.contents[0])

# print(job_title)

#########################################
#### Recruiter ####

recruiter_list = []
for item in soup.findAll('div', attrs={'class': 'grid'}):
	for span in item.findAll('span', attrs={'itemprop':'name'}):
		for line in span:
			recruiter_list.append(line)
recruiter = recruiter_list[0]

#########################################
#### job_details ####

dt_items = []
dd_items = []
for item in soup.findAll('div', attrs={'class': 'grid'}):
	for dts in item.findAll("dt"):
		dt_items.append(re.sub('[^A-Za-z0-9\-]+', '', dts.contents[0]))
	for dds in item.findAll("dd"):
		dd_items.append(re.sub('[^A-Za-z0-9\-]+', '', dds.contents[0]))

#if dt_items[2] == 'Salary': job_salary = dd_items[2]
#	if re.match('[0-9][0-9][0-9]+[\-][0-9][0-9][0-9]+[a-zA-Z]+',job_salary): # 3 or more digits
#		salary_high = (re.split('[\-](.*?)[a-zA-Z]+',job_salary))[1]
#		salary_low = (re.split('[\-](.*?)[a-zA-Z]+',job_salary))[0]
#job_salary = (int(salary_high) + int(salary_low))/2



if dt_items[1] == 'Location': job_location 			= dd_items[1]
if dt_items[2] == 'Salary': job_salary 				= dd_items[2]
if dt_items[3] == 'Posted':	job_posted 				= dd_items[3]
if dt_items[4] == 'JobLevel': job_joblevel			= dd_items[4]
if dt_items[5] == 'Hours': job_hours 				= dd_items[5]
if dt_items[6] == 'Contract': job_contract 			= dd_items[6]	
if dt_items[7] == 'ListingType': job_listingtype	= dd_items[7]	


print(dt_items)


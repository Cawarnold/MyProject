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
#cur.execute('DROP TABLE IF EXISTS JobPost_Details ')


## Create tables JobPost_Parse_HTML 
cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_Details
	(jp_details_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
	, jp_url_id int
	, job_title text
	, recruiter text
	, job_location text
	, job_salary text
	, job_posted text
	, job_closes text
	, job_ref text
	, job_industry text
	, job_joblevel text
	, job_hours text
	, job_contract text
	, job_listingtype text)''')



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

#count_jobs = 1
#while count_jobs < 10:

jp_url_id = 0
cur.execute('SELECT h.jp_url_id FROM JobPost_HTML h LEFT OUTER JOIN JobPost_Details d ON h.jp_url_id = d.jp_url_id WHERE d.jp_url_id is null')
jp_url_id = cur.fetchone()[0]
print('Processing jp_url_id: ' + str(jp_url_id))

if jp_url_id == 0:
	print('Program Exiting ...') 
	sys.exit()

cur.execute('SELECT HTML FROM JobPost_HTML WHERE jp_url_id = ? ', (jp_url_id, ))
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

job_title = ''
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

recruiter = ''
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


job_location = ''
job_salary = ''
job_posted = ''
job_joblevel = ''
job_hours = ''
job_contract = ''
job_listingtype = ''

count_dt_items = 0
while count_dt_items < 15:
	count_dt_items = count_dt_items + 1
	if dt_items[count_dt_items] == 'Location': job_location 			= dd_items[count_dt_items] ## Location starts at [1]
	if dt_items[count_dt_items] == 'Salary': job_salary 				= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Posted':	job_posted 				= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Closes': job_closes					= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Ref': job_ref						= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Industry': job_industry				= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'JobLevel': job_joblevel				= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Hours': job_hours 					= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Contract': job_contract 			= dd_items[count_dt_items]	
	if dt_items[count_dt_items] == 'ListingType': job_listingtype		= dd_items[count_dt_items]


#print(job_title)
#print(recruiter)
#print(job_location)
#print(job_salary)
#print(job_posted)
#print(job_closes)
#print(job_ref)
#print(job_industry)
#print(job_joblevel)
#print(job_hours)
#print(job_contract)
#print(job_listingtype)


#########################################
#### Insert Job Post Details into JobPost_Details database
#########################################



cur.execute('''INSERT OR IGNORE INTO JobPost_Details 
		(jp_url_id, job_title, recruiter, job_location
			, job_salary, job_posted, job_closes, job_ref
			, job_industry, job_joblevel, job_hours
			, job_contract, job_listingtype) 
		VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', 
		( jp_url_id, job_title, recruiter, job_location
			, job_salary, job_posted, job_closes, job_ref
			, job_industry, job_joblevel, job_hours
			, job_contract, job_listingtype , ) )

print('Commiting Job details to database')
conn.commit()


cur.close()
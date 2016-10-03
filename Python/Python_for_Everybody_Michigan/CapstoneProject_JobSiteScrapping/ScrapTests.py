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

## Print URL
cur.execute('SELECT u.url FROM JobPost_URLs u where u.jp_url_id = ? ', ('115', ))
print(cur.fetchone()[0])

## Fetch the HTML for the jp_url_id
cur.execute('SELECT HTML FROM JobPost_HTML h where jp_url_id = ? ', ('115', ))

html = cur.fetchone()[0]

soup = BeautifulSoup(html, "html.parser")

dt_items = []
dd_items = []
for item in soup.findAll('div', attrs={'class': 'grid'}):
	for dts in item.findAll("dt"):
		dt_items.append(re.sub('[^A-Za-z0-9\-]+', '', dts.contents[0]))
	for dds in item.findAll("dd"):
		dd_items.append(re.sub('[^A-Za-z0-9\-]+', '', dds.contents[0]))


print(dt_items)
print(dd_items)

count_dt_items = 0
while count_dt_items < (len(dd_items)-1):
	count_dt_items = count_dt_items + 1
	print(dt_items[count_dt_items])
	if dt_items[count_dt_items] == 'Location': job_location 			= dd_items[count_dt_items] ## Location starts at [1]
	if dt_items[count_dt_items] == 'Salary': job_salary 				= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Posted': job_posted 				= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Closes': job_closes					= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Ref': job_ref						= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Industry': industry					= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'JobFunction': job_function			= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'JobLevel': job_level				= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Hours': job_hours 					= dd_items[count_dt_items]
	if dt_items[count_dt_items] == 'Contract': job_contract 			= dd_items[count_dt_items]	
	if dt_items[count_dt_items] == 'ListingType': job_listingtype		= dd_items[count_dt_items]


## sometime Posted is in an HTML span:
for item in soup.findAll('div', attrs={'class': 'grid'}):
	for dds in item.findAll("dd"):
		for spans in dds.findAll("span"):
			#print(spans.attrs['itemprop'])
			#print(spans.contents[0])
			if spans.attrs['itemprop'] == 'datePosted' and job_posted == '': job_posted = re.sub('[^A-Za-z0-9\-]+', '',spans.contents[0])


###############################################################
####### Category Lists #######

#### Types of Job Industry ####

types_Industry = ['Arts & heritage','Charities','Construction','Design','Engineering','Environment'
,'Finance & Accounting','Further Education','General','Government & Politics','Health'
,'Higher Education','Hospitality','Housing','Legal','Leisure','Marketing & PR','Media'
,'Recruitment','Retail & FMCG','Schools','Science','Skilled Trade','Social care'
,'Social Enterprise','Technology','Travel & transport']


#### Types of Job Level ####

types_Job_Function = ['Administration', 'Consultant', 'Customer service', 'Finance', 'HR & Training'
, 'IT', 'Legal', 'Marketing/PR', 'Sales', 'Secretarial']


#### Types of Job Level ####

types_Job_Level = ['Apprenticeship', 'Entry Level', 'Graduate', 'Experienced (non manager)', 'Management', 'Senior Executive']


#### Types of Job Contract ####

types_Job_Contract = ['Permanent', 'Temp', 'Contract', 'Job share']


#### Types of Job Hours ####

types_Job_Hours = ['Full Time', 'Part Time']


#### Types of Job Listing Type ####

types_Job_ListingType = ['Job vacancy', 'Course', 'Graduate scheme', 'Internship']
###############################################################



#### Collect up all the href fields ####

for item in soup.findAll('div', attrs={'class': 'grid'}):
	for dds in item.findAll("dd"):
		for aas in dds.findAll("a"):
			#print(aas.attrs['href'])
			#print(aas.contents[0])
			if aas.contents[0] in types_Industry: industry = aas.contents[0]
			if aas.contents[0] in types_Job_Function: job_function = aas.contents[0]
			if aas.contents[0] in types_Job_Level: job_level = aas.contents[0]
			if aas.contents[0] in types_Job_Contract: job_contract = aas.contents[0]
			if aas.contents[0] in types_Job_Hours: job_hours = aas.contents[0]
			if aas.contents[0] in types_Job_ListingType: job_listingtype = aas.contents[0]










print(job_location)
print(job_salary)
print(job_posted)
print(job_closes)
print(job_ref)
print(industry)
print(job_function)
print(job_level)
print(job_hours)
print(job_contract)
print(job_listingtype)







cur.close()
#!/usr/bin/env 

from __future__ import unicode_literals
import sys			# sys.exit()
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

count_jobs = 0
while count_jobs < 0:
	count_jobs = count_jobs + 1
	## Get jp_url_id which has not been processed yet.
	jp_url_id = 0
	cur.execute('SELECT h.jp_url_id FROM JobPost_HTML h INNER JOIN JobPost_URLs u ON h.jp_url_id = u.jp_url_id LEFT OUTER JOIN JobPost_Details d ON h.jp_url_id = d.jp_url_id WHERE d.jp_url_id is null and u.url_status = ?',('200',))
	
	## Catch errors with try / except.
	try:
		jp_url_id = cur.fetchone()[0]

	except:
		print('Program Exiting ...')
		continue

	print('Processing jp_url_id: ' + str(jp_url_id))

	cur.execute('SELECT u.guardian_job_id FROM JobPost_HTML h inner join JobPost_URLs u on h.jp_url_id = u.jp_url_id WHERE h.jp_url_id = ? ', (jp_url_id, ))
	guardian_job_id = cur.fetchone()[0]
	print('Printing guardian job url: https://jobs.theguardian.com/job/' + str(guardian_job_id))


	## Fetch the HTML for the jp_url_id
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
			job_title = str(h1.contents[0].encode('utf-8'))

# print(job_title)

#########################################
#### Recruiter ####

	recruiter_list = []
	for item in soup.findAll('div', attrs={'class': 'grid'}):
		for span in item.findAll('span', attrs={'itemprop':'name'}):
			for line in span:
				recruiter_list.append(line)

	if len(recruiter_list) > 1:
		recruiter = recruiter_list[0]
	else:
		print(recruiter_list)

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
	job_closes = ''
	job_ref = ''
	industry = ''
	job_level = ''
	job_hours = ''
	job_contract = ''
	job_listingtype = ''

	count_dt_items = 0
	while count_dt_items < 15:
		count_dt_items = count_dt_items + 1
		if dt_items[count_dt_items] == 'Location': job_location 			= dd_items[count_dt_items] ## Location starts at [1]
		if dt_items[count_dt_items] == 'Salary': job_salary 				= dd_items[count_dt_items]
		if dt_items[count_dt_items] == 'Posted': job_posted 				= dd_items[count_dt_items]
		if dt_items[count_dt_items] == 'Closes': job_closes					= dd_items[count_dt_items]
		if dt_items[count_dt_items] == 'Ref': job_ref						= dd_items[count_dt_items]
		if dt_items[count_dt_items] == 'JobFunction': job_function			= dd_items[count_dt_items]
		if dt_items[count_dt_items] == 'JobLevel': job_level				= dd_items[count_dt_items]
		if dt_items[count_dt_items] == 'Hours': job_hours 					= dd_items[count_dt_items]
		if dt_items[count_dt_items] == 'Contract': job_contract 			= dd_items[count_dt_items]	
		if dt_items[count_dt_items] == 'ListingType': job_listingtype		= dd_items[count_dt_items]


## sometime Posted is in an HTML span:
	span_items = []
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
				if aas.contents[0] in types_Job_Function: job_function = aas.contents[0]
				if aas.contents[0] in types_Job_Level: job_level = aas.contents[0]
				if aas.contents[0] in types_Job_Hours: job_hours = aas.contents[0]
				if aas.contents[0] in types_Job_Contract: job_contract = aas.contents[0]
				if aas.contents[0] in types_Job_ListingType: job_listingtype = aas.contents[0]

#### Getting the list of industries associated with the Organisation ####

	## need to build out industries hierarchy
	industry = []
	for item in soup.findAll('div', attrs={'class': 'grid'}):
		for dds in item.findAll("dd"):
			for aas in dds.findAll("a"):
				print(aas.contents[0])
				if aas.contents[0] in types_Industry: industry.append(aas.contents[0])		## will need some adjusting
	#print(industry)

	#job_industry = ''
	ind_counts = dict()
	for ind in industry:
		ind_counts[ind] = ind_counts.get(ind,0) + 1
	#print(ind_counts)

	job_industry = ''
	for key in ind_counts:
		if job_industry == '':
			job_industry = job_industry + key
		else:
			job_industry = job_industry + ', ' + key

	print(job_industry)

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
				, job_industry, job_level, job_hours
				, job_contract, job_listingtype , ) )

	print('Commiting Job details to database')
	print('')
	print('')
	
	conn.commit()


cur.close()
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

conn = sqlite3.connect('harnhamcrawl_database.sqlite')
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
	, job_location text
	, job_salary text
	, job_contract text
	, job_sector text
	, recruitment_consultant text
	, recruitment_number text
	, recruitment_email text)''')



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

count_jobs = 0
while count_jobs < 1:
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

	cur.execute('SELECT url FROM JobPost_URLs WHERE jp_url_id = ? ', (jp_url_id, ))
	url = cur.fetchone()[0]
	print(url)

	## Fetch the HTML for the jp_url_id
	cur.execute('SELECT HTML FROM JobPost_HTML WHERE jp_url_id = ? ', (jp_url_id, ))
	html = cur.fetchone()[0]

	soup = BeautifulSoup(html, "html.parser")
	#soup = BeautifulSoup(html, "lxml")


#########################################
#### Extract Job Details from HTML
#########################################
	
#### List of sectors
	sectors = ['Credit Risk', 'Data & Technology', 'Data Science', 'Digital', 'Marketing & Insight', 'Internal']


#<div class="vacancyDetailsDescription">
#		<h1 class="jobDetailsHeader">Manager- Data Analytics- Consultancy</h1>
	div_main = soup.find("div", attrs = {"id": "main"})
	print(type(div_main))
	vacancyDetails = div_main.find("div", attrs = {"class": "vacancyDetailsDescription"})
	print(str(vacancyDetails))
	print(type(vacancyDetails))
	for div in div_main.findAll("div", attrs = {"class": "vacancyDetailsDescription"}):
		print(type(div))
		print(div)
	vacancyDetails = div_main.find("div.vacancyDetailsDescription")
	print(vacancyDetails)














#####

#	job_location = ''
#	job_salary = ''
#	job_contract = ''
#
## <div class="infoContainer">
#	# <div class="contract icon"></div>
#	# <div class="location icon"></div>
#	# <div class="salary icon"></div>
#	div_main = soup.find("div", {"id": "main"})
#	for infoContainer in div_main.findAll('div', attrs={'class': 'infoContainer'}):
#		for con in infoContainer.findAll('div', attrs={'class': 'location icon'}):
#			job_location = job_location + (infoContainer.get_text())
#		for con in infoContainer.findAll('div', attrs={'class': 'salary icon'}):
#			job_salary = job_location + (infoContainer.get_text())
#		for con in infoContainer.findAll('div', attrs={'class': 'contract icon'}):
#			job_contract = job_location + (infoContainer.get_text())
#
#	print(job_location)
#	print(job_salary)
#	print(job_contract)
#
## <div id="vacancyDetails">
#	div_vacancyDetails = soup.find("div", {"id": "vacancyDetails"})
#	print(div_vacancyDetails)
#
#	#sector = div_vacancyDetails.findAll('h2')
#	#print(sector)
#
#	jobDetailsHeader = soup.find('h2').get_text()
#	print(jobDetailsHeader)

	print('End')


#	, jp_url_id int
#	, job_title text
#	, job_location text
#	, job_salary text
#	, job_contract text
#	, job_sector text
#	, recruitment_consultant text
#	, recruitment_number text
#	, recruitment_email text







#########################################
#### Insert Job Post Details into JobPost_Details database
#########################################



#	cur.execute('''INSERT OR IGNORE INTO JobPost_Details 
#			(jp_url_id, job_title, recruiter, job_location
#				, job_salary, job_posted, job_closes, job_ref
#				, job_industry, job_joblevel, job_hours
#				, job_contract, job_listingtype) 
#			VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', 
#			( jp_url_id, job_title, recruiter, job_location
#				, job_salary, job_posted, job_closes, job_ref
#				, job_industry, job_level, job_hours
#				, job_contract, job_listingtype , ) )
#
#	print('Commiting Job details to database')
#	print('')
#	print('')
	
	conn.commit()


cur.close()
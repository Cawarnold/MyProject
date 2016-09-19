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


# conda create --name Env_Python2712 python=2.7.12

# activate Env_Python2712


## Srape and App

# https://www.quora.com/Is-it-possible-to-scrape-data-from-mobile-apps

#### Overview
## Glassdoor uses specific URLs to search for job queries
## https://www.glassdoor.co.uk/Job/london-analyst-python-jobs-SRCH_IL.0,6_IC2671300_KO7,21.htm
## which means that we will have store our inital glassdoor job queries in a database 
## so that we can call on themn at a later time to retrieve the job post.



##################################################################
			## Create initial job query database
##################################################################

#### Connect to (or Create) Database ####

conn = sqlite3.connect('glassdoorcrawl_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####

#### Create job query Tables ####

## Drop tables if need to restart
#cur.execute('DROP TABLE IF EXISTS GD_C_JobQueries')
#cur.execute('DROP TABLE IF EXISTS GD_Employer_Rating')
#cur.execute('DROP TABLE IF EXISTS GD_Employer_Seach_Query')


## Create tables
cur.execute('''CREATE TABLE IF NOT EXISTS GDC_JobQueries
	(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
	, gdc_jq_id TEXT
	, jobquery TEXT
	, location TEXT
	, url TEXT)''')




cur.execute('''INSERT INTO GDC_JobQueries (jobquery, location, url) VALUES (?, ?, ?)''', 
	('python analyst', 'london', 'https://www.glassdoor.co.uk/Job/london-analyst-python-jobs-SRCH_IL.0,6_IC2671300_KO7,21.htm') )

cur.execute('''INSERT INTO GDC_JobQueries (jobquery, location, url) VALUES (?, ?, ?)''', 
	('python SQL analyst', 'london', 'https://www.glassdoor.co.uk/Job/london-sql-analyst-python-jobs-SRCH_IL.0,6_IC2671300_KO7,25.htm') )




##################################################################
##################################################################
				## Crawl the Glassdoor site
##################################################################
##################################################################


## Laying out the foundations for the 

#### Always page 1, for now ####

url = 'http://www.glassdoor.co.uk/'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

print(soup)

#tags = soup('a') ## 'a' is an HTML tag <a linkstuff <\a>


#base_url = 'http://www.glassdoor.co.uk/'




## base URL
base_url = 'https://www.glassdoor.co.uk/Job/jobs.htm?'

## The parameters for the GET request ##
payload = {
	'suggestCount': '0'		
	, 'suggestChosen': 'false'
	, 'useragent': 'Mozilla'
	, 'clickSource': 'searchBtn'
	, 'typedKeyword': 'analyst+python'
	, 'sc.keyword': 'analyst+python'
	, 'locT': 'C'
	, 'locId': '2671300'
}

## Avoids API's mod_security by setting useragent to known browser ##
		#http://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
url_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}

url = 'https://www.glassdoor.co.uk/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=analyst+python&sc.keyword=analyst+python&locT=C&locId=2671300'

url2 = 'https://www.glassdoor.co.uk/Job/london-analyst-jobs-SRCH_IL.0,6_IC2671300_KO7,14.htm'

url3 = 'https://www.glassdoor.com/partner/jobListing.htm?pos=101&ao=131089&s=182&guid=000001572703a0d3b21f305b6dbf4cb3&src=GD_JOB_AD&t=JF&extid=12&exst=L&ist=O&ast=OL&vt=e&uido=D159BF4C9A7F87329696E4887EF1123D&slr=false&rtp=0&cb=1473828332246&jobListingId=1950455272&utm_medium=email&utm_source=jobfeed&utm_campaign=jobfeed-ol&utm_content=jf-ol-jobtitle&encryptedUserId=D159BF4C9A7F87329696E4887EF1123D'

req = urllib2.Request(url3, headers=url_headers)

#try:
#    page = urllib2.urlopen(req)
#except urllib2.HTTPError, e:
#    print e.fp.read()
#
#content = page.read()
#print content

#  !!! HEAVILY GUARDED !!! NO ACCESS :(
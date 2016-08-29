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








#### GET Request to Glassdoor API ####

# The Glassdoor API is a simple, lightweight REST API that responds 
# to http requests with JSON (future support for XML is planned). 
# Because it is a REST API, it is completely stateless. 
# Requests are expected to be made in the form of a simple HTTP GET.

## base URL of API
base_url = 'http://api.glassdoor.com/api/api.htm?'

## The parameters for the GET request ##
payload = {
	'v': '1'		# Version
	, 'format': 'json'
	, 'useragent': 'Mozilla'
	, 't.p': hidden.GlassdoorAPI()[0]
	, 't.k': hidden.GlassdoorAPI()[1]
	, 'userip': hidden.GlassdoorAPI()[2]
	, 'action': 'employers'
	, 'q': 'pharmaceutical'		# Query phrase
	, 'l': 'london'				# Location,  city, state, or country
	, 'country': 'UK'			# Country
}

## Avoids API's mod_security by setting useragent to known browser ##
		#http://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
url_headers = {
	'User-Agent': 'Mozilla/5.0'
}

r = requests.get(base_url, params=payload, headers=url_headers)

## Check request status
if r.status_code == '200':
	print(r.url)
	json_data = r.json()

## Exit script if json data status not OK ##
if 'status' not in js or json_data['status'] != 'OK': 
	sys.exit()
else:
	print('Successful api call')


#### Connect to (or Create) Database ####

conn = sqlite3.connect('my_lse_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Stock Price Table ####

## Drop tables if need to restart
#cur.execute('DROP TABLE IF EXISTS Stock_EOD_Prices ')
cur.execute('DROP TABLE IF EXISTS My_Current_Stocks ')

## Create tables
cur.execute('''CREATE TABLE IF NOT EXISTS Stock_EOD_Prices
	(Date DATE, Stock_Symbol TEXT, Price_EOD TEXT
	, UNIQUE(Date, Stock_Symbol) ON CONFLICT REPLACE)''')

cur.execute('''CREATE TABLE IF NOT EXISTS My_Current_Stocks
	(Stock_Symbol TEXT, Number_of_Shares INT)''')
####





print(json_data['response']['currentPageNumber'])
print(json_data['response']['totalNumberOfPages'])
print(json_data['response']['totalRecordCount'])



while count < 10:

print(json_data['response']['employers'][0]['id'])
print(json_data['response']['employers'][0]['name'])
print(json_data['response']['employers'][0]['website'])
print(json_data['response']['employers'][0]['industry'])


print(json_data['response']['employers'][0]['numberOfRatings'])
print(json_data['response']['employers'][0]['overallRating'])
print(json_data['response']['employers'][0]['ratingDescription'])







'''
count = 0
while count < 10:
	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ====' 
		print data
		continue
	print json.dumps(js, indent=4)
	
	lat = js["results"][0]["geometry"]["location"]["lat"] 
	lng = js["results"][0]["geometry"]["location"]["lng"] 
	print 'lat',lat,'lng',lng
	location = js['results'][0]['formatted_address'] 
	print location
'''
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

## Example URL
# http://api.glassdoor.com/api/api.htm?q=pharmaceutical&action=employers&t.p=89958&v=1&userip=159.220.75.4&useragent=Python&format=json&t.k=gBpvHITc7jO

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

conn = sqlite3.connect('glassdoor_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Employers Tables ####

## Drop tables if need to restart
cur.execute('DROP TABLE IF EXISTS GD_Employers ')
cur.execute('DROP TABLE IF EXISTS My_Current_Stocks ')

## Create tables
cur.execute('''CREATE TABLE IF NOT EXISTS GD_Employers
	(gde_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
	, employer_id INTEGER, employer_name TEXT
	, website TEXT, industry TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Employer_Rating
	(employer_id INTEGER, numberOfRatings INT
	, overallRating REAL, ratingDescription TEXT)''')
####



print(json_data['response']['currentPageNumber'])
print(json_data['response']['totalNumberOfPages'])
print(json_data['response']['totalRecordCount'])

print(json_data['response']['employers'][0]['id'])
print(json_data['response']['employers'][0]['name'])
print(json_data['response']['employers'][0]['website'])
print(json_data['response']['employers'][0]['industry'])

print(json_data['response']['employers'][0]['numberOfRatings'])
print(json_data['response']['employers'][0]['overallRating'])
print(json_data['response']['employers'][0]['ratingDescription'])

count = 0
while count < 10:
	employer_id = json_data['response']['employers'][count]['id']
	employer_name = json_data['response']['employers'][count]['name']
	website = json_data['response']['employers'][count]['website']
	industry = json_data['response']['employers'][count]['industry']

	numberOfRatings = json_data['response']['employers'][count]['numberOfRatings']
	overallRating = json_data['response']['employers'][count]['overallRating']
	ratingDescription = json_data['response']['employers'][count]['ratingDescription']

	


	
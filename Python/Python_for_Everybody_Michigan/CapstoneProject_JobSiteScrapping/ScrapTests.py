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
	, 'q': 'analytic'		# Query phrase
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
if 'status' not in json_data or json_data['status'] != 'OK': 
	sys.exit()
else:
	print('Successful api call')

print(r.url)

count = 0
while count < 9:
	count = count + 1

## Check vital information is available, if not skip employer.

	if json_data['response']['employers'][count]['id'] is None: continue
	if json_data['response']['employers'][count]['name'] is None: continue
	if json_data['response']['employers'][count]['website'] is None: continue
	if json_data['response']['employers'][count]['industry'] is None: continue

	print(json_data['response']['employers'][count]['id'])
	print(json_data['response']['employers'][count]['name'])
	print(json_data['response']['employers'][count]['website'])
	print(json_data['response']['employers'][count]['industry'])

	print(json_data['response']['employers'][count]['numberOfRatings'])
	print(json_data['response']['employers'][count]['overallRating'])
	print(json_data['response']['employers'][count]['ratingDescription'])

	#employer_id = json_data['response']['employers'][count]['id']
	#employer_name = json_data['response']['employers'][count]['name']
	#website = json_data['response']['employers'][count]['website']
	#industry = json_data['response']['employers'][count]['industry']
#
	#numberOfRatings = json_data['response']['employers'][count]['numberOfRatings']
	#overallRating = json_data['response']['employers'][count]['overallRating']
	#ratingDescription = json_data['response']['employers'][count]['ratingDescription']


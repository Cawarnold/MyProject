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
#  

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
	, 'action': 'jobs-prog'
	, 'jobTitle': 'Data Analyst'			# Job Title
	, 'countryId': '1'					# Country Id - only 1 (US) is supported right now.
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


#### Connect to (or Create) Database ####

conn = sqlite3.connect('glassdoor_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####

print(json_data['response']['results'][0]['nextJobTitle'])
print(json_data['response']['results'][0]['frequency'])
print(json_data['response']['results'][0]['frequencyPercent'])
print(json_data['response']['results'][0]['nationalJobCount'])
print(json_data['response']['results'][0]['medianSalary'])






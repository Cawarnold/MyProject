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
#  http://api.glassdoor.com/api/api.htm?t.p=5317&t.k=n07aR34Lk3Y&userip=0.0.0.0&useragent=&format=json&v=1&action=jobs-stats&returnStates=true&admLevelRequested=1

## base URL of API
base_url = 'http://api.glassdoor.com/api/api.htm?'

## The parameters for the GET request ##
payload = {
	'v': '1.1'		# Version
	, 'format': 'json'
	, 'useragent': 'Mozilla'
	, 't.p': hidden.GlassdoorAPI()[0]
	, 't.k': hidden.GlassdoorAPI()[1]
	, 'userip': hidden.GlassdoorAPI()[2]
	, 'action': 'jobs-stats'

	## The following parameters are optional.
	, 'q': 'analytic'		# Query phrase.
	, 'l': 'london'				# Location,  city, state, or country.
	, 'country': 'UK'			# Country.
	#, 'e': 'ThomsonReuters'	# Employer.
	#, 'city': 'London'		# City.
	, 'fromAge': '30'		# Age of job ad in days, -1 = all jobs (default), 5 = 5 days.
	#, 'jobType': 'all'		# Job Type, all (default), fulltime, parttime, internship, contract, internship, temporary.
	#, 'minRating': '0'		# Min Rating (0 = returns all (default), 1 = more than 1 star..
	#, 'radius': '3'		# Radius in miles of the location specified.
	#, 'jt': 'Analyst'		# Job Title, if you want to specify job title.
	#, 'jc': '3'			# Job Category, if you want to specify job category. 3 = Analyst, 29 = Software Development / IT.

	## The following parameters return beakdowns of the data.
	#, 'returnCities'			# Results will include geographical data (job counts) broken down by city.
	#, 'returnStates'			# Results will include geographical data (job counts, score) broken down by the type of geographical district specified in parameter admLevelRequested.
	#, 'returnJobTitles'			# Results will include job data broken down by job title.
	#, 'returnEmployers'			# Results will include job data broken down by employer.
	#, 'admLevelRequested'			# Geographic district type requested when returnStates is true (1 = states, 2 = counties)
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


#### Print useful information from this query ####

print(json_data['response']['countReturned'])
print(json_data['response']['totalNumberOfPages'])
print(json_data['response']['totalRecordCount'])




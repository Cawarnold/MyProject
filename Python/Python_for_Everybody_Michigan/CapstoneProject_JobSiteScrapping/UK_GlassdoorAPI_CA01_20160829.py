#!/usr/bin/env

from __future__ import unicode_literals
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

####
# The Glassdoor API is a simple, lightweight REST API that responds 
# to http requests with JSON (future support for XML is planned). 
# Because it is a REST API, it is completely stateless. 
# Requests are expected to be made in the form of a simple HTTP GET.

def test_glassdoor_api():
	x = 1



#test_url = 'http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=89958&t.k=gBpvHITc7jO&action=employers&q=pharmaceuticals&userip=149.72.61.234&useragent=Mozilla/%2F4.0'

#r = requests.get(test_url)
#print(r)

#data = json.load(urllib2.urlopen(test_url))
#print(data)



base_url = 'http://api.glassdoor.com/api/api.htm?'



#### The parameters for the GET request ####
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

#### Avoids API's mod_security by setting useragent to known browser ####
#http://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
url_headers = {
	'User-Agent': 'Mozilla/5.0'
}

r = requests.get(base_url, params=payload, headers=url_headers)
print(r.url)
if r.status_code == '200':
	print(r.url)
	print('Successful api call')
json_data = r.json()

print(json_data['status'])


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
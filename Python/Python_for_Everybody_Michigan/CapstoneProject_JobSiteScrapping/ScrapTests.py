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



base_url = 'https://jobs.theguardian.com/job/'
url_headers = { 'User-Agent': 'Mozilla/5.0' }

job_count = 0
while job_count < 1:
	job_count = job_count + 1
	guardian_job_id = 6377990 	# starting job id, will become max job id from the database.
	url = base_url + str(guardian_job_id + job_count)
	r = requests.get(url, headers=url_headers)
	print(r.url)
	print(r.status_code)
	html = r.content
	#print(html[0:30000])

	soup = BeautifulSoup(html, "html.parser")
	
	for item in soup.findAll('div', {'class': 'grid'}):
		

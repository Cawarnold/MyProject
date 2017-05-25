#!/usr/bin/env
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys		# sys.exit()
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

guardian_job_id = 6401001
url = 'https://jobs.theguardian.com/job/6401001/experiential-senior-account-manager/'

cur.execute('SELECT guardian_job_id FROM JobPost_URLs where url = ?', (url, ))
try:
	print('The URL' + str(cur.fetchone()[0]) + 'is already in table')
	print('continue')
except:
	print('continue with code')




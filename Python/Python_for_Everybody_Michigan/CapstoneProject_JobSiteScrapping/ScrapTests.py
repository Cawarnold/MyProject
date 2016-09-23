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


#### Connect to (or Create) Database for the job postings from Indeed ####

conn = sqlite3.connect('guardiancrawl_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


cur.execute('SELECT h.jp_url_id FROM JobPost_HTML h LEFT OUTER JOIN JobPost_Details d ON h.jp_url_id = d.jp_url_id WHERE d.jp_url_id is null')
jp_url_id = cur.fetchone()[0]

print(jp_url_id)
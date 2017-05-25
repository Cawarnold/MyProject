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


#### Query the DB ####

cursor.execute("select top 1 * from [vMDB_Test].dbo.[JF_Websubs_Data_Hierarchy]")
row = cursor.fetchone()
while row is not None:
	if row > 0 : print('CONNECTION WORKS')
	row = cursor.fetchone()




	
#### Connect to (or Create) Database ####

conn = sqlite3.connect('enterprise_hierarchy_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Employers Tables ####

## Drop tables if need to restart
cur.execute('DROP TABLE IF EXISTS Enterprises ')

## Create tables
cur.execute('''CREATE TABLE IF NOT EXISTS Companies
	(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
	, enterprise_id INTEGER, enterprise_name TEXT
	, website TEXT, industry TEXT)''')
####
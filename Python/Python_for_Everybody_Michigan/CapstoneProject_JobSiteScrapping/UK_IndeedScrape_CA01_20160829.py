#!/usr/bin/env Env_Python2712
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import numpy as np
import pandas as pd
import sqlite3
import urllib
from bs4 import BeautifulSoup ## To install do - conda install beautifulsoup4
import re



# conda create --name Env_Python2712 python=2.7.12
# activate Env_Python2712

## https://jessesw.com/Data-Science-Skills/  

## Program Setup
  # Create database and tables
  # Get first page of job postings. 
  # Scrape all hrefs. Store in table.
  # Scrape individual job posting for the HTML, clean up, output list of words.
  # Manage URLs to access via the job postings 
# 


#### Connect to (or Create) Database for the job postings from Indeed ####

conn = sqlite3.connect('indeed_job_postings.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Stock Price Table ####

## Drop tables if need to restart
cur.execute('DROP TABLE IF EXISTS JobPost_URL_Scrapped ')
cur.execute('DROP TABLE IF EXISTS Job_Details ')

## Create tables JobPost_URL_Scrapped
cur.execute('''CREATE TABLE IF NOT EXISTS JobPost_URL_Scrapped
  (url_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
  , url_date DATE,  url TEXT UNIQUE
  ,scrapped INTEGER DEFAULT 0)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Job_Details
  (job_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
  , url_id INTEGER, job_title TEXT
  ,company TEXT, salary TEXT, keywords Text)''')

####




s



#### Always page 1, for now ####

url = 'http://www.indeed.co.uk/jobs?q=data+scientist&l=London'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a') ## 'a' is an HTML tag <a linkstuff <\a>


base_url = 'http://www.indeed.co.uk/'



count = 0
for tag in tags:
  if tag.get('data-tn-element') != "jobTitle": continue
  while count < 1:
    count = count + 1
    url_href = tag.get('href')
    print(url_href)
    job_html = urllib.urlopen(base_url+url_href).read()
    job_soup = BeautifulSoup(job_html, "html.parser")
    job_tags = job_soup('li')
    for tag in job_tags:
      print(tag.get('p'))





print(count)
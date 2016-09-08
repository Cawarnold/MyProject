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


## Srape and App

# https://www.quora.com/Is-it-possible-to-scrape-data-from-mobile-apps





#### Always page 1, for now ####

url = 'http://www.glassdoor.co.uk/'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

print(soup)

#tags = soup('a') ## 'a' is an HTML tag <a linkstuff <\a>


#base_url = 'http://www.glassdoor.co.uk/'



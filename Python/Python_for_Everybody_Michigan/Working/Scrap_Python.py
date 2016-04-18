#!/usr/bin/env Env3_Python276_Django171_djangoextensions

## http://www.pythonlearn.com/book_009.pdf

# The program will use urllib to read the HTML
# from the data files below, 
# extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position 
# from the top and follow that link, 
# repeat the process a number of times, 
# and report the last name you find.

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/known_by_Fox.html"

repeat = 0
while repeat < 7:
	print url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')
	list_urls = []
	for tag in tags:
		list_urls.append(tag.get('href', None))
	url = list_urls[17]
	repeat = repeat + 1

print "Last name in sequence:", re.findall("known_by_(.+).html",url)[0]




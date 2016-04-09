#!/usr/bin/env Env3_Python276_Django171_djangoextensions


import urllib
from BeautifulSoup import *
url = 'http://www.crummy.com/software/' #raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	print tag.get('href', None)

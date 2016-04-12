#!/usr/bin/env Env3_Python276_Django171_djangoextensions


#### Exercises 12.5



import re
import urllib
import socket
from bs4 import BeautifulSoup

url = 'http://www.pythonlearn.com/code/intro-short.txt'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

hostname = re.findall( '.*(www.+?)/',url)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mysock.connect((hostname[0], 80))
	mysock.send('GET ' + url + ' HTTP/1.0\n\n')
except:
	print 'Please enter valid url'
	exit()

while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) :
		break
	print data
mysock.close()
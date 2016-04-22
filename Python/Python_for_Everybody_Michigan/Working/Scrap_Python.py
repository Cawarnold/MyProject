#!/usr/bin/env Env3_Python276_Django171_djangoextensions

## http://www.pythonlearn.com/book_009.pdf



count_manually = 100+99+86+85+84+82+82+81+78+78+78+77+76+68+67+67+65+65+63+63+61+58+54+53+51+50+50+48+47+42+41+38+38+35+34+33+32+26+24+24+15+14+13+13+11+10+7+7+4

count_maually2 = 100+99+86+85+84+82+82+81+78+78+78+77+76+68+67+67+65+65+63+63+61+58+54+53+51+50+50+48+47+42+41+38+38+38+35+34+33+32+26+24+24+15+14+13+13+11+10+7+7+4

import urllib
import xml.etree.ElementTree as ET

#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_234596.xml'

url_open = urllib.urlopen(url)
data = url_open.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

#print data

#comments = tree.findall('comments')
#print comments[0].find('comment').find('count').text

##  you can use an XPath selector string to look 
## through the entire tree of XML for any tag named 'count'
counts = tree.findall('.//count')

#print type(counts) ## list
#print type(counts[0])

sums = 0
count = 0
for element in counts:
	count = count + 1
	sums = sums + int(element.text)

print count
print sums
print count_manually
print count_maually2

############
'''
import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
    '''
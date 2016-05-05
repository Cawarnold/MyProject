#!/usr/bin/env Env3_Python276_Django171_djangoextensions

## https://apps.twitter.com

## https://apps.twitter.com/app/12234901/keys

import urllib
import twurl
import json
import sqlite3

print 'People'


conn = sqlite3.connect('friends.sqlitesqlite3')
cur = conn.cursor()
cur.execute('''SELECT * FROM People''')
count = 0
for row in cur :
	print row
	count = count + 1
print count, 'rows.'

print 'Follows'

cur.execute('''SELECT * FROM Follows''')
count = 0
for row in cur :
	print row
	count = count + 1
print count, 'rows.'

cur.close()


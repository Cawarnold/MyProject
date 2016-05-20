#!/usr/bin/env Env3_Python276_Django171_djangoextensions

## http://www.pythonlearn.com/book_009.pdf
import xml.etree.ElementTree as ET
import sqlite3

import urllib


conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name    TEXT UNIQUE
);

CREATE TABLE Genre (
	id 	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name 	TEXT UNIQUE
);

CREATE TABLE Album (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id  INTEGER,
	title   TEXT UNIQUE
);

CREATE TABLE Track (
	id  INTEGER NOT NULL PRIMARY KEY 
		AUTOINCREMENT UNIQUE,
	title TEXT  UNIQUE,
	album_id  INTEGER,
	genre_id  INTEGER,
	len INTEGER, 
	rating INTEGER, 
	count INTEGER
);
''')

url = 'http://www.pythonlearn.com/code/tracks/Library.xml'
fhand = urllib.urlopen(url)


##fname = raw_input('Enter file name: ')
##if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
	found = False
	for child in d:
		if found : return child.text
		if child.tag == 'key' and child.text == key : 
			found = True
	return None

#### Lookup function - my explanation ####
## The d attribute will be the list of dicts that contain the track info.
## The key attribute will be the 'key' of the tag.
	## the 'key' tag is <key>Name</key>, the key attibute is 'Name'.
	## he says it would have been better if they weren't named the same thing.

## When the function is used:
	## for child in dictionary -- ie any of the items (tags) in the dict
		## found is false, so skips 'if found : return child.text'
		## then asks if child tag is 'key'  and if child text is key.
			## eg. child tag = <key>Name</key>, and child text = Name. then found turns to true.
		## so the function is still on the same tag and runs through another iteration of the for loop.
		## but this time found = True.
			## this executes: if found : return child.text
	## rememer return exits the function (def lookup(d,key))
	## if not found then return None -- a very pythonic way of doing things.


stuff = ET.parse(fhand)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entry in all:
	if ( lookup(entry, 'Track ID') is None ) : continue

	name = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')
	count = lookup(entry, 'Play Count')
	rating = lookup(entry, 'Rating')
	length = lookup(entry, 'Total Time')

	if name is None or artist is None or album is None or genre is None: 
		continue

	print name, artist, album, genre, count, rating, length

	cur.execute('''INSERT OR IGNORE INTO Artist (name) 
		VALUES ( ? )''', ( artist, ) )
	cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
	artist_id = cur.fetchone()[0]

## insert artist if it isn't there already or ignore artist if it is already there.

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
		VALUES ( ?, ? )''', ( album, artist_id ) )
	cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
	album_id = cur.fetchone()[0]

## Copy above but for Genre

	cur.execute('''INSERT OR IGNORE INTO Genre (name) 
		VALUES ( ? )''', ( genre, ) )
	cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
	genre_id = cur.fetchone()[0]

##add genre to the insert statement, Values ?, and tuple.

	cur.execute('''INSERT OR REPLACE INTO Track
		(title, album_id, genre_id, len, rating, count) 
		VALUES ( ?, ?, ?, ?, ?, ? )''', 
		( name, album_id, genre_id, length, rating, count ) )

	conn.commit()
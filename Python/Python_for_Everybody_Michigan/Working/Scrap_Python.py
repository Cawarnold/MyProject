#!/usr/bin/env Env3_Python276_Django171_djangoextensions

## http://www.pythonlearn.com/book_009.pdf

import sqlite3
conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',( 'Thunderstruck', 20 ) )
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',( 'My Way', 15 ) )
conn.commit()

print 'Tracks:'
cur.execute('SELECT title, plays FROM Tracks')

for row in cur :
	print row

cur.execute('DELETE FROM Tracks WHERE plays < 100')

conn.commit()
cur.close()

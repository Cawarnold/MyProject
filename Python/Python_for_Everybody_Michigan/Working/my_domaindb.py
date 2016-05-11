#### Exercise Chuck -- Counting Email in a Database

#### http://www.pythonlearn.com/code/

import urllib
import sqlite3


	#### URL Connection

url = 'http://www.pythonlearn.com/code/mbox.txt'
# url = 'http://www.pythonlearn.com/code/mbox-short.txt'

fhand = urllib.urlopen(url)

	#### SQLite connection

## Open connection to a sqlite database domaindb
sqlite_conn = sqlite3.connect('domaindb.sqlite')
## Then create a cursor through which you can talk to the db
cur = sqlite_conn.cursor()

	#### Drop and Create the database

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

	#### Extract Domains and insert or update the database

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From': continue
	domain = words[1].split('@')[1]
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain, ))
	row = cur.fetchone() 
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count) 
			VALUES ( ?, 1 )''', ( domain, ) )
	else : 
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (domain, ))
	sqlite_conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

print
print "Counts:"
for row in cur.execute(sqlstr) :
	print str(row[0]), row[1]

cur.close()


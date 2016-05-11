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
DROP TABLE IF EXISTS Domain_Counts''')

cur.execute('''
CREATE TABLE Domain_Counts (domain TEXT, count INTEGER)''')

	#### Extract Domains and insert or update the database

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From': continue
	domain = words[1].split('@')[1]
	print domain
	cur.execute('SELECT count FROM Domain_Counts WHERE domain = ? ', (domain, ))
	row = cur.fetchone() 
	if row is None:
		cur.execute('''INSERT INTO Domain_Counts (domain, count) 
			VALUES ( ?, 1 )''', ( domain, ) )
	else : 
		cur.execute('UPDATE Domain_Counts SET count=count+1 WHERE domain = ?', (domain, ))
	sqlite_conn.commit()


sqlstr = 'SELECT domain, count FROM Domain_Counts ORDER BY count DESC'

print
print "Counts:"
for row in cur.execute(sqlstr) :
	print str(row[0]), row[1]

cur.close()


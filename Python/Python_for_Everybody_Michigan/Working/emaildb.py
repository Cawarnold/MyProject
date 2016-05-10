import sqlite3

#### http://www.pythonlearn.com/code/

## Open connection to a sqlite database
conn = sqlite3.connect('emaildb.sqlite')
## Then create a cursor through which you can talk to the db
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

cur.execute('''DROP TABLE IF EXISTS help''')
cur.execute('''CREATE TABLE help (stuff TEXT)''')
cur.execute('''INSERT INTO help (stuff) VALUES (?)''', ('abc', ) )

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: ') : continue
	pieces = line.split()
	email = pieces[1]
	print email
	cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
	row = cur.fetchone() 
	if row is None:
		cur.execute('''INSERT INTO Counts (email, count) 
			VALUES ( ?, 1 )''', ( email, ) )
	else : 
		cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email, ))
	# This statement commits outstanding changes to disk each 
	# time through the loop - the program can be made faster 
	# by moving the commit so it runs only after the loop completes
	#### Chuck had a different version on his video
	####try:
	####	count = cur.fetchone()[0]
	####	cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email, ))
	####except:
	####	cur.execute('''INSERT INTO Counts (email, count) 
	####			VALUES ( ?, 1 )''', ( email, ) )
	####	conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
	print str(row[0]), row[1]

cur.close()

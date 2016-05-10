#!/usr/bin/env Env3_Python276_Django171_djangoextensions

## http://www.pythonlearn.com/book_009.pdf


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    print email
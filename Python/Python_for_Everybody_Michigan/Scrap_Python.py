#!/usr/bin/env Env3_Python276_Django171_djangoextensions


## Just Scrap stuff


file_name = open('mbox-short.txt','r')


for line in file_name:
	if not line[0:5] == 'From ':
		continue
	else:
		day = line.split(' ')[2]
		print(day)



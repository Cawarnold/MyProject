#!/usr/bin/env Env3_Python276_Django171_djangoextensions


## Just Scrap stuff

#### 7.1
#file_name = raw_input('Enter a file name:')
#file_connection = open(file_name, 'r')
#for line in file_connection:
#	print(line.upper())

#### 7.2 and 7.3
file_name = raw_input('Enter a file name:')
#file_name = 'mbox-short.txt'
if file_name == 'na na boo boo':
	print('you child!')
	exit()
else:
	try:
		file_connection = open(file_name, 'r')
	except:
		print('Please Enter valid file name')
		exit()


counter = 0
total_conf = 0.0
for line in file_connection:
	if line.upper()[:len('X-DSPAM-CONFIDENCE:')] == 'X-DSPAM-CONFIDENCE:':
		counter = counter + 1
		total_conf = total_conf + float(line.rstrip()[len('X-DSPAM-CONFIDENCE:')+1:])

average_spam_confidence = total_conf / counter

print(average_spam_confidence)
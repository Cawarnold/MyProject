#### Scrap file to run random python


#### 7.1
#file_name = raw_input('Enter a file name:')
#file_connection = open(file_name, 'r')
#for line in file_connection:
#	print(line.upper().rstrip())

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
	if not line.upper().startswith('X-DSPAM-CONFIDENCE:'):
		continue
	else:
		counter = counter + 1
		total_conf = total_conf + float(line.rstrip()[len('X-DSPAM-CONFIDENCE:')+1:])

average_spam_confidence = float(total_conf) / float(counter)

print(('Average spam confidence: ')+ str(average_spam_confidence)) 


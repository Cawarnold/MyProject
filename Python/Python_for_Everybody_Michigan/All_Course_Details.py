#### Python for Everybody Specialization ####


## Getting Started with Python
	# From the "Python for Informatics book"

# Course 1: Getting Started with Python
# Course 2: Python Data Structures
# Course 3: Using Python to Access Web Data
# Course 4: Using Databases with Python
# Capstone: Retrieving, Processing and Visualizing Data with Python







#####################################################################
#####################################################################
			# Notes on the book -- Python for Informatics #
#####################################################################
#####################################################################

# Python Reserved words

# and 
# as 
# assert
# break 
# class 
# continue
# def 
# del 	
# elif 	
# else 	
# except 
# exec 	 (not in python 3.0)
# finally
# for 	
# from 
# global
# if 	
# import
# in 	
# is 	
# lambda
# not 	
# or 		
# pass 	
# print
# raise
# return
# try
# while
# with
# yield
 
## Simple program to find the most common word in a text file.

name = raw_input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print bigword, bigcount


## User input
	>>> name = raw_input('What is your name?\n')
	Chuck
	>>> print(name)
	Chuck

## Placeholder for code you haven't written yet.

	if x < 0:
		pass


## The try / except feature is a trial and error statement.
	#try these things, if they dont work print (except) print error message.
	
	inp = raw_input('Enter Fahrenheit Temperature:')
	try:
		fahr = float(inp)
		cel = (fahr - 32.0) * 5.0 / 9.0
		print cel
	except:
		print 'Please enter a number'




#### 20160114: now at Chapter 3.   http://do1.dr-chuck.com/py4inf/EN-us/book.pdf


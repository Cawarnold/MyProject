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

#####
#		To run snippets of code go to
#		the Scrap_Python.py file to write your python
#		Then run the file from the terminal
#####


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

## Built-in Functions should also be treated as reserved words.
	#eg. max, min, len



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


## Random function: returns a float between 0.0 and 1.0 (including 0.0 but not 1.0)
	# Each time you call random you get the next number in a long series.

	import random
	for i in range(10):
		x = random.random()
		print x


## Raw input: takes a user input assigns it to variable

	hours = raw_input('How many hours have you worked this week?')
	rate = 12.5
	pay = float(hours) * float(rate)	

	print("You will be paid $" + str(pay) + " this week.")


## End a program at certain point
	
	try:
		blah
	except:
		print("Error")
		quit()


## The pay rate example with try except and definition

def computepay(h,r):
    if h > 40:
    	overtime = h - 40
    	return (40 * r) + (overtime * r * 1.5)
    else:
    	return (h * r)
try:
	hrs = raw_input("Enter Hours:")
	rate = raw_input("Enter Rate:")
except:
	print("Please only enter numerical values. Eg. 45")
	quit()

h = float(hrs)
r = float(rate)

p = computepay(h,r)
print "Pay",p

## Finding Larget and smallest numbers from raw input.

largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done" :
		break
	#print(smallest, largest)	
	try:
		num = int(num)
		if largest is None or num > largest:
			largest = num
		if smallest is None or num < smallest:
			smallest = num
	except:
		print("Invalid input")


print "Maximum is", largest
print "Minimum is", smallest




## Remember to close the connection to the file after writing to it.

fout = open('output','w')
print fout

line1 = "Debugging whitespaces can be made easier,\n"
fout.write(line1)
line2 = "by using the repr() function.\n"
fout.write(line2)

# Test this by commenting fout.close()
fout.close()

file = open('output','r')
for line in file:
	print line

print('>print repr(' + repr('a 2\t 3\n 4') + ')')
print(repr('a 2\t 3\n 4'))

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


## List operations
	#Concatenate
		>a = [1, 2, 3]
		>b = [4, 5, 6]
		>c = a + b
		>print(c)
		[1, 2, 3, 4, 5, 6]

	#Multi
		>[0]*4
		[0,0,0,0]
		>[1,2,3]*3
		[1, 2, 3, 1, 2, 3, 1, 2, 3]

	#Slice
		> t = ['a', 'b', 'c', 'd', 'e', 'f']
		> t[1:3]
		['b','c']

	#Changing ontents of list
		>t = ['a', 'b', 'c', 'd', 'e', 'f']
		>t[1:3] = ['x', 'y']
		print t
		>['a', 'x', 'y', 'd', 'e', 'f']

## List methods
	#Append
		> t = ['a', 'b', 'c']
		> t.append('d')
		> print t
		['a', 'b', 'c', 'd']

	#Extend
		> t1 = ['a', 'b', 'c']
		> t2 = ['d', 'e']
		> t1.extend(t2)
		> print t1
		['a', 'b', 'c', 'd', 'e']

	#Sort
		> t = ['d', 'c', 'e', 'b', 'a']
		> t.sort()
		> print t

## Deleting Elements
	#pop - modifies list and returns element that was removed
		> t = ['a', 'b', 'c']
		> x = t.pop(1)
		> print t
		['a', 'c']
		> print x
		b

	#remove - if you know the element but not the index
		> t = ['a', 'b', 'c']
		> t.remove('b')
		> print t
		['a', 'c']

	#del - just removes the values
		> t = ['a', 'b', 'c', 'd', 'e', 'f']
		> del t[1:5]
		> print t
		['a', 'f']

## Using lists
	# writing a program that averages the numbers you give it.
		> numlist = list()
		> while ( True ) :
			inp = raw_input('Enter a number: ')
			if inp == 'done' : break
			value = float(inp)
			numlist.append(value)
		> average = sum(numlist) / len(numlist)
		> print 'Average:', average

	# Convert a string of characters into a list of values.
		> s = 'spam'
		> t = list(s)
		> print t
		['s', 'p', 'a', 'm']

	# split a string into list of words (use join to do the opposite)
		> s = 'pining for the fjords'
		> t = s.split()
		> print t
		['pining', 'for', 'the', 'fjords']

	# split a sting on the deliminator
		> s = 'spam-spam-spam'
		> delimiter = '-'
		> s.split(delimiter)
		['spam', 'spam', 'spam']






#### 20160215: Readings -> 6.1   http://do1.dr-chuck.com/py4inf/EN-us/book.pdf

 


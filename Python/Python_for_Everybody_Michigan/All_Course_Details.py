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

## Can find the methods of functions using dir
x = list()
dir(x)


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
	if not line.upper().startswith('X-DSPAM-CONFIDENCE:'):
		continue
	else:
		counter = counter + 1
		total_conf = total_conf + float(line.rstrip()[len('X-DSPAM-CONFIDENCE:')+1:])

average_spam_confidence = float(total_conf) / float(counter)

print(('Average spam confidence: ')+ str(average_spam_confidence)) 



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

	#Function
		> nums = [3, 41, 12, 9, 74, 15]
		> print len(nums)
		6
		> print max(nums)
		74
		> print min(nums)
		3
		> print sum(nums)  ## Only works when elements are all numbers.
		154
		> print sum(nums)/len(nums)
		25


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


## Parsing lines
	file_name = open('mbox-short.txt','r')


	for line in file_name:
		if not line[0:5] == 'From ':
			continue
		else:
			day = line.split(' ')[2]
			print(day)

## Objects and values
	# Comparing Strings, Python creates one string object and both a and b refer to it.
		> a = 'banana'
		> b = 'banana'
		> a is b
		True
		# these strings are identical and therefore equivalent

	# Comparing Lists, Pyhon creates two list objects.
		> a = [1,2,3]
		> b = [1,2,3]
		> a is b
		False
		# these lists are equivalent but not identical

	# Creating a reference means one object is aliased to another.
		> a = [1,2,3]
		> b = a
		> b is a
		True
		# If the aliase object is mutable, changes made to one alias affects the other.
		> b[0] = 17
		> print a
		[17,2,3]

## List arguements (things you can do to lists)
	# It is important to distinguish between operations that modify lists
		# and operations that create new lists.

	# append -- modifies the list
		> t1 = [1, 2]
		> t2 = t1.append(3)
		> print t1
		[1, 2, 3]
		> print t2
		None
		
	# the + operator -- creates a new list
		> t3 = t1 + [3]
		> print t3
		[1, 2, 3]
		> t2 is t3
		False

	# Comparing functions
	## The parameter t and the variable letters are aliases for the same object.

	# 1. A new list is not created, the list is modified.
	def delete_head(t):
		del t[0]
	letters = ['a', 'b', 'c']
	delete_head(letters)
	print letters
	['b', 'c']

	# 2. A new list is not created and the list is not modified. 
	def bad_delete_head(t):
		t = t[1:]

	letters = ['a', 'b', 'c']
	bad_delete_head(letters)
	print letters
	['a', 'b', 'c']

	# 3. A new list is created, the old list is not modified.
	def tail(t):
		return t[1:]
	
	letters = ['a', 'b', 'c']
	rest = tail(letters)
	print letters
	['a', 'b', 'c']
	print rest
	['b', 'c']


#### 8.1a Remove first and last elements from list and return None.
		# A new list is not created, the list is modified.
def chop(t):
	del t[0]
	del t[len(t)-1]
	return None

letters = ['a', 'b', 'c','d','e','f']
print chop(letters)
print letters

#### 8.1b Create new list containing all but the first and last element.
		# A new list is created, the list is not modified.

def middle(t):
	return t[1:len(t)-1]

letters = ['a', 'b', 'c','d','e','f']
print middle(letters)
print letters	


# Debugging -- helpful tips:
	# Don’t forget that most list methods modify the argument and return None.
	# This is the opposite of the string methods, which return a new string and
	# leave the original alone.

		# If you are used to writing string code like this:
		word = word.strip()
		# It is tempting to write list code like this:
		t = t.sort() # WRONG!


	# Pick an idiom and stick with it.

		# don’t forget that these are right:
		t.append(x)
		t = t + [x]
		# And these are wrong:
		t.append([x]) # WRONG!
		t = t.append(x) # WRONG!
		t + [x] # WRONG!
		t = t + x # WRONG!


	# Make copies to avoid aliasing.

		# make the copy before applying the method
		orig = t[:]
		t.sort()

	# Lists, split, and files

		#  Use the "Guardian" pattern when reading through files.
		fhand = open('mbox-short.txt')
		for line in fhand:
			words = line.split()
			print 'Debug:',words
			if len(words) == 0 : continue 	#Guardian
			if words[0] != 'From' : continue	#Guardian becuase of blank lines
			print words[2]


#### 8.2 More guardians:

fhand = open('mbox-short.txt')
for line in fhand:
	words = line.split()
	print 'Debug:',words
	if len(words) == 0 : continue
	if words[0] != 'From ' : continue
	if len(words) < 3 : continue
	print words[2]

#### 8.3 rewrite guardian code without if statements.
			#instead use a compound logical expression with a sinlge if.

fhand = open('mbox-short.txt')
for line in fhand:
	words = line.split()
	print 'Debug:',words
	if len(words) == 0 and words[0] != 'From ' and len(words) < 3: continue
	print words[2]			

#### 8.4 Romeo
# For each line, split line into words, 
# for each word check if it's in a list, if not add to list.

fhand = open('romeo.txt')
t = list()
for line in fhand:
	line = line.split()
	for word in line:
		if word in t : continue
		t.append(word)

romeo_orig = t[:]
t.sort()
print(t)


#### 8.5 mbox-short
# We are interested in the email addresses of the people who sent mail.
# provide list of emails.

fhand = open('mbox-short.txt')
counter = 0
for line in fhand:
	line = line.split()
	if len(line) == 0 or line[0] != 'From': continue
	counter = counter + 1
	print(line[1])
print(counter)



#### 8.6 Max and min from user input
# Store the numbers the user enters in a list
# Use max() and min() to compute max and min.
list_numbers = list()
while (True):
	user_number = raw_input('Enter a number: ')
	if user_number == 'done' or user_number == '': break
	else:
		user_number = float(user_number)
		if user_number not in list_numbers:
			list_numbers.append(user_number)

print('Maximum: ' + str(max(list_numbers)))
print 'Minimum: ', min(list_numbers)



#### 20160303: Readings -> 8.1   http://do1.dr-chuck.com/py4inf/EN-us/book.pdf


 


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

#########################################################
#########################################################
				# Powerful Python idioms # 


#### Count letters in string using a dictionary.

word = 'brontosaurus'
d = dict()
for c in word:
	d[c] = d.get(c,0) + 1
	print d
print 'finished dict', d

# get returns the corresponding value; otherwise it returns the default value

#### Turn dict into list
x = { 'a' : 1, 'b' : 2, 'c': 3}
list_of_tuples_stuff = x.items()
print list_of_tuples_stuff
>>> [('a', 1), ('c', 3), ('b', 2)]

#### Regex Cheatsheet
	https://www.debuggex.com/cheatsheet/regex/python

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('\S+@\S+', line)
	if len(x) > 0 :
		print x

#### Regex Quick Guide

	# ^	Matches the beginning of a line
	# $	Matches the end of the line
	# .	Matches any character
	# \s	Matches whitespace
	# \S	Matches any non-whitespace character
	# *	Repeats a character zero or more times
	# *?	Repeats a character zero or more times (non-greedy)
	# +	Repeats a character one or more times
	# +?	Repeats a character one or more times (non-greedy)
	# [aeiou]	Matches a single character in the listed set
	# [^XYZ]	Matches a single character not in the listed set
	# [a-z0-9]	The set of characters can include a range
	# (	Indicates where string extraction is to start
	# )	Indicates where string extraction is to end


#########################################################
#########################################################


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



######### Lists

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



<<<<<<< HEAD
=======
#### 20160303: Readings -> 8.1   http://do1.dr-chuck.com/py4inf/EN-us/book.pdf

>>>>>>> be09384e34f864364a6c19c916ad77a5631214af

######### Dictionaries 


## Dictionaries
	create_a_dictionary = dict()
	create_a_dictionary = {}

	# Adding items (Key:Value)
		create_a_dictionary[one] = 'uno'
		create_a_dictionary[two] = 'duo'
		create_a_dictionary = {'one':'uno', 'two':'duo'}

	# Exracting Vlaues
		print(create_a_dictionary[one])
		> 'uno'

	# Does key exist?
		'one' in create_a_dictionary
		>True

	# does value exist?
		'uno' in create_a_dictionary.values()
		>True

#### 9.1 Dictionary as set of counters

word = 'brontosaurus'
d = dict()
for c in word:
	if c not in d:
		d[c] = 1
	else:
		d[c] = d[c] + 1
print d
print d.get('z')

# Can reduce this to 4 lines using the get method.
	# get returns the corresponding value;
		# otherwise it returns the default value.
word = 'brontosaurus'
d = dict()
for c in word:
	d[c] = d.get(c,0) + 1
print d	


## Open file, iterate through lines and count words

fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
print counts



## Sorting values of a dictionary.

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = counts.keys()
lst.sort()
for key in lst:
	print key, counts[key]


## Removing the punctuation from the list before makeing the counts

import string # New Code
fhand = open('romeo.txt')

countA = dict()
countB = dict()

for line in fhand:
	line = line.translate(None, string.punctuation) # New Code
	line = line.lower() # New Code
	words = line.split()
	
	for word in words:
		countA[word] = countA.get(word,0)+1

		if word not in countB:
			countB[word] = 1
		else:
			countB[word] += 1

print countA
print countB


## Dealing with Large datasets
	
	## Scale down input
		# eg. use top 10 rows

	## Check summaries and types
		# eg. number of items, many errors are cause by the type of values

	## Write self -checks
		# writing tests to check your code works.

	## Print pretty output
		# Build debugging error messages into code.

#### Exercise 9.2

	# write a program that counts frequency of days of the week.

fhand = open('mbox-short.txt')

day_list = list()
day_dict = dict()

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From': continue
	day_list.append(words[2])

	for day in day_list:
		if day not in day_dict:
			day_dict[day] = 1
		else:
			day_dict[day] = day_dict[day] + 1

print(day_dict)



#### Exercise 9.3

	# write a program that counts frequency of emails.

fhand = open('mbox-short.txt')

email_list = list()
email_dict = dict()

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From': continue
	email_list.append(words[1])

	for item in email_list:
		if item not in email_dict:
			email_dict[item] = 1
		else:
			email_dict[item] = email_dict[item] + 1

print(email_dict)


#### Exercise 9.4

	# write a program that counts frequency of emails.

fhand = open('mbox-short.txt')

day_list = list()
day_dict = dict()

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From': continue
	day_list.append(words[1])

	for day in day_list:
		if day not in day_dict:
			day_dict[day] = 1
		else:
			day_dict[day] = day_dict[day] + 1

vals = day_dict.values()
vals.sort(reverse = True)
max_val = vals[0]

for key, value in day_dict.iteritems():
	if value == max_val:
		print key, value


#### Exercise 9.5

	# write a program that counts frequency of email domains.

fhand = open('mbox-short.txt')

dom_list = list()
domain_dict = dict()

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From': continue
	dom_list.append(words[1].split('@')[1])
	for item in dom_list:
		if item not in domain_dict:
			domain_dict[item] = 1
		else:
			domain_dict[item] = domain_dict[item] + 1

print(domain_dict)


#### Exercise 9.6 (Chuck)

	# write a program that prints more common word in text file.

fhand = open('mbox-short.txt')
text = fhand.read()
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None

for word, count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount

#### Assignment 9.4

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
	if line[:5] != 'From ': continue
	email = line.split()[1]
	counts[email] = counts.get(email,0)+1

bigcount = None
bigword = None

for word, count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount


######### Tuples

dir(tuple())
>> ['count','index']

## Tuples -- immutable, comparable, hashable

	# created using brackets ()
	t = tuple()
	t = ('a', 'b', 'c', 'd', 'e')


	# if the argument is a sting with no commas.
	>>> t = tuple('lupins')
	>>> print t
	('l', 'u', 'p', 'i', 'n', 's')
	>>> print t[2]
	'p'


## Comparing tuples
	# compares first element of sequence, 
	# then next until it finds one which differs.
	>>> (0, 1, 2) == (0, 3, 4)
	False
	>>> (0, 1, 2) < (0, 3, 4)
	True
	>>> (0, 1, 2000000) < (0, 3, 4)
	True

## The DSU pattern
	## building a list of tuples, sorting, and extracting part of the result

	# Decorate - a sequence by building a list of tuples with one 
		# or more sort keys preceding the elements from the sequence,
	# Sort the - list of tuples using the Python built-in sort,
	# Undecorate - by extracting the sorted elements of the sequence.

	## Sort list of words longest to shortest:
		txt = 'but soft what light in yonder window breaks'
		words = txt.split()
		t = list()
			# builds list of tuples.
		for word in words:
			t.append((len(word), word))  
		t.sort(reverse=True)
		res = list()
		for length, word in t:
			res.append(word)
		print res
		['yonder', 'window', 'breaks', 'light', 'what','soft', 'but', 'in']

## Tuple assignment

	# In this example we have a two-element list (which is a sequence) 
	# and assign the first and second elements of the sequence 
	# to the variables x and y in a single statement.

		>>> m = [ 'have', 'fun' ]
		>>> x, y = m
		>>> x
		'have'
		>>> y
		'fun'

	# Tuples translats the tuple assignement and does this

		>>> m = [ 'have', 'fun' ]
		>>> x = m[0]
		>>> y = m[1]

	# A particularly clever application of tuple assignment allows us 
	# to swap the values of two variables in a single statement:
	>>> a, b = b, a

	# The right side can be any kind of sequence (string, list, or tuple).
	# For example, to split an email address into 
	# a user name and a domain:

	>>> addr = 'monty@python.org'
	>>> uname, domain = addr.split('@')


## Dictionaries and Tuples
	# Dictionaries have a method called items() 
	# it returns a list of tuples, key, value.
	>>> d = {'a':10, 'b':1, 'c':22}
	>>> t = d.items()
	>>> print t
	[('a', 10), ('c', 22), ('b', 1)]

	# items from a dictionary are inherently not ordered
	# but since the list of tuples is a list, and tuples are comparable,
	# we can now sort the list of tuples.

	>>> d = {'a':10, 'b':1, 'c':22}
	>>> t = d.items()
	>>> t
	[('a', 10), ('c', 22), ('b', 1)]
	>>> t.sort()
	>>> t
	[('a', 10), ('b', 1), ('c', 22)]

## Print out the contents of a dictionary sorted by the value.

	# get dictionary, make list of tuples, sort by value.
	>>> d = {'a':10, 'b':1, 'c':22}
	>>> l = list()
	>>> for key, val in d.items() :
			l.append( (val, key) )
	
	>>> l
	[(10, 'a'), (22, 'c'), (1, 'b')]
	>>> l.sort(reverse=True)
	>>> l
	[(22, 'c'), (10, 'a'), (1, 'b')]


## The most common words -- Romeo and Juliet example
	import string
	fhand = open('romeo.txt')
	
	counts = dict()
	for line in fhand:
		line = line.translate(None, string.punctuation)
		line = line.lower()
		words = line.split()
		for word in words:
			if word not in counts:
				counts[word] = 1
			else:
				counts[word] = counts[word] + 1
	
	# sort the dictionary by value
	lst = list()
	for key, val in counts.items():
		lst.append( (val, key) )
	
	lst.sort(reverse = True)
	
	for key, val in lst[:10]:
		print key, val

	# First part of the program - reads the file and 
	# computes the dictionary that maps each word to the count of words in the document.
	# second part constructs a list of (val, key) tuples then sorts them.

## Using tuples as keys in dictionaries
	
	# Because tuples are hashable and lists are not, 
	# if we want to create a composite key to use in a dictionary
	# we must use a tuple as the key.

	directory[last,first] = number
	
	for last, first in directory:
		print first, last, directory[last,first]

	# the loop traverses the keys in directory, which are tuples.
	# it assigns the elements of each tuple to last and first, 
	# then prints the name and corresponding telephone number.


## From the video: list comprehension

c = {'a':10, 'b':1, 'c':22}

print sorted( [ (v,k) for k,v in c.items() ] )

	# (v,k) is a list of tuples.
	# sorted is a function




#### Exercise 10.1

	# write a program that counts frequency of emails.
		# using a list of (count, email) tuples from a dictionary. 

fhand = open('mbox-short.txt', 'r')

emails = list()
count_email = dict()

for line in fhand:
	list_of_words = line.split()
	if len(list_of_words) == 0: continue
	if list_of_words[0] != 'From': continue
	emails.append(list_of_words[1])

for email in emails:
	count_email[email] = count_email.get(email,0) + 1

list_of_tuples = list()

for key, val in count_email.items():
	list_of_tuples.append( (val, key)  )

list_of_tuples.sort(reverse = True)

for val, key in list_of_tuples[:1]:
	print key, val


#### Exercise 10.2

	# count frequency of hour of commits (in 'from' line).
		# sort by hour, print one per line.

fhand = open('mbox-short.txt', 'r')

hours_of_day = list()
count_hour = dict()

for line in fhand:
	list_of_words = line.split()
	if len(list_of_words) == 0: continue
	if list_of_words[0] != 'From': continue
	hours_of_day.append(list_of_words[5].split(':')[0])

for hour in hours_of_day:
	count_hour[hour] = count_hour.get(hour,0) + 1

list_of_tuples = list()

for key, val in count_hour.items():
	list_of_tuples.append( (key, val)  )

list_of_tuples.sort()

for val, key in list_of_tuples:
	print val, key


#### Exercise 10.3

	# read a text file. print letters in decreasing order.

import string

fhand = open('romeo.txt', 'r')

list_of_letters = list()
count_letters = dict()

for line in fhand:
	line = line.translate(None, string.punctuation)
	line = line.lower()
	words = line.split()
	for word in words:
		for letter in word:
			list_of_letters.append(letter)

# put into count dictionary
for letter in list_of_letters:
	count_letters[letter] = count_letters.get(letter,0) + 1

# put into list of tuples for sorting
list_of_tuples = list()

for key, val in count_letters.items():
	list_of_tuples.append( (val, key) )

list_of_tuples.sort(reverse = True)

for val, key in list_of_tuples:
	print key, val


#### Exercise 10.2 (Chuck Coursera)

# its the hour problem Exercise 10.2 copies directly in.


 #################################################################
 #################################################################
 ########        Using Python to Access Web Data       ###########
 #################################################################
 #################################################################

## Scrape, Parse and Read Web Data as well as access data using web APIs.
	# Work with HTML, XML, JSON data formats in python.


#### Regluar Expressions ####

# The task of searching and extracting is so common that Python
 # has a very powerful library called regular expressions that
 # handles many of these tasks quite elegantly

## To import the re package use 'import re'

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:', line) :
		print line

## The caret character is used in regular expressions to match 
	# “the beginning” of a line

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('ˆFrom:', line) :
		
## The period (or fullstop) character is used to match any character.
	# “F..m:” matches any of “From:”, “Fxxm:”, “F12m:”, or “F!@m:”

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('ˆF..m:', line) :
		print line

## The asterisk character indicates that the previous character 
	# can be repeated zero or more times.
	# Use plus sign for one or more times.

# here we have any number of any characters until an @ sign.

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('ˆF..m:.*@', line) :
		print line

# beware this will match lines such as
#'From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu' # up to the last @ sign in 'cwen @iupui.edu'


# The search string “ˆFrom:.+@” will successfully match lines that start with
# “From:”, followed by one or more characters (“.+”), followed by an at-sign.


## Extracting data using regular expressions

	# Use the findall() method 

import re
s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
lst = re.findall('\S+@\S+', s)
print lst

# The output of the program would be:
	['csev@umich.edu', 'cwen@iupui.edu']

## re.findall('\S+@\S+', s) means: 
	# we are looking for substrings that have at least 
	# one non-whitespace character, followed by an at-sign, 
	# followed by at least one more non-whitespace character

## We can use this regular expression in a program 
	# to read all the lines in a file and 
	# print out anything that looks like an
	# email address as follows:

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('\S+@\S+', line)
	if len(x) > 0 :
		print x

## Some of our email addresses have incorrect characters 
	# like “<” or “;” at the beginning or end. 
	# Let’s declare that we are only interested in 
	# the portion of the string that starts and ends 
	# with a letter or a number.

import re
hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
	x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
	if len(x) > 0 :
		print x

## Translating this regular expression, [a-zA-Z0-9]\S*@\S*[a-zA-Z]:
	# we are looking for substrings that start with 
	# a single lowercase letter, uppercase letter, 
	# or number “[a-zA-Z0-9]”, followed by 
	# zero or more non-blank characters (“\S*”), followed by 
	# an at-sign, followed by 
	# zero or more non-blank characters (“\S*”), followed by 
	# an uppercase or lowercase letter "[a-zA-Z]". 

## Note that we switched from “+” to “*” 
	# to indicate zero or more non-blank characters 
	# since “[azA-Z0-9]” is already one non-blank character. 

# Remember that the “*” or “+” applies to the single character 
	# immediately to the left of the plus or asterisk.


#### Combining searching and extracting
	
## Match lines like:
	# X-DSPAM-Confidence: 0.8475
	# X-DSPAM-Probability: 0.0000

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('ˆX\S*: [0-9.]+', line) :
		print line

# we want lines that start with “X-”, followed by 
# zero or more characters (“.*”), followed by 
# a colon (“:”) and then a space. 
# After the space we are looking for one or more 
# characters that are either a digit (0-9)
# or a period “[0-9.]+”. 

# Note that inside the square brackets, the period matches an
# actual period (ie. not a wildcard).








#### 20160321: Readings -> 11   http://do1.dr-chuck.com/py4inf/EN-us/book.pdf

 ###############################################
########        General Notes       ###########
 ###############################################

 #10.8 Sequences: strings, lists, and tuples—Oh My!
#I have focused on lists of tuples, but almost all of the examples in this chapter also
#work with lists of lists, tuples of tuples, and tuples of lists. To avoid enumerating
#the possible combinations, it is sometimes easier to talk about sequences of
#sequences.
#In many contexts, the different kinds of sequences (strings, lists, and tuples) can
#be used interchangeably. So how and why do you choose one over the others?
#To start with the obvious, strings are more limited than other sequences because
#the elements have to be characters. They are also immutable. If you need the
#ability to change the characters in a string (as opposed to creating a new string),
#you might want to use a list of characters instead.
#Lists are more common than tuples, mostly because they are mutable. But there
#are a few cases where you might prefer tuples:
#1. In some contexts, like a return statement, it is syntactically simpler to
#create a tuple than a list. In other contexts, you might prefer a list.
#2. If you want to use a sequence as a dictionary key, you have to use an immutable
#type like a tuple or string.
#3. If you are passing a sequence as an argument to a function, using tuples
#reduces the potential for unexpected behavior due to aliasing.
#10.9. Debugging 125
#Because tuples are immutable, they don’t provide methods like sort and reverse,
#which modify existing lists. However Python provides the built-in functions
#sorted and reversed, which take any sequence as a parameter and return a new
#sequence with the same elements in a different order.
#10.9 Debugging
#Lists, dictionaries and tuples are known generically as data structures; in this
#chapter we are starting to see compound data structures, like lists of tuples, and
#dictionaries that contain tuples as keys and lists as values. Compound data structures
#are useful, but they are prone to what I call shape errors; that is, errors
#caused when a data structure has the wrong type, size, or composition, or perhaps
#you write some code and forget the shape of your data and introduce an error.
#For example, if you are expecting a list with one integer and I give you a plain old
#integer (not in a list), it won’t work.
#When you are debugging a program, and especially if you are working on a hard
#bug, there are four things to try:
#reading: Examine your code, read it back to yourself, and check that it says what
#you meant to say.
#running: Experiment by making changes and running different versions. Often
#if you display the right thing at the right place in the program, the problem
#becomes obvious, but sometimes you have to spend some time to build
#scaffolding.
#ruminating: Take some time to think! What kind of error is it: syntax, runtime,
#semantic? What information can you get from the error messages, or from
#the output of the program? What kind of error could cause the problem
#you’re seeing? What did you change last, before the problem appeared?
#retreating: At some point, the best thing to do is back off, undoing recent
#changes, until you get back to a program that works and that you understand.
#Then you can start rebuilding.
#Beginning programmers sometimes get stuck on one of these activities and forget
#the others. Each activity comes with its own failure mode.
#For example, reading your code might help if the problem is a typographical error,
#but not if the problem is a conceptual misunderstanding. If you don’t understand
#what your program does, you can read it 100 times and never see the error, because
#the error is in your head




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

	# ^			Matches the beginning of a line
	# $			Matches the end of the line
	# .			Matches any character
	# \s		Matches whitespace
	# \S		Matches any non-whitespace character
	# *			Repeats a character zero or more times
	# *?		Repeats a character zero or more times (non-greedy)
	# +			Repeats a character one or more times
	# +?		Repeats a character one or more times (non-greedy)
	# [aeiou]	Matches a single character in the listed set
	# [^XYZ]	Matches a single character not in the listed set
	# [a-z0-9]	The set of characters can include a range
	# (			Indicates where string extraction is to start
	# )			Indicates where string extraction is to end
	# \b 		Matches the empty string, but only at the start or end of a word.
	# \B 		Matches the empty string, but not at the start or end of a word.


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



##################################################################################################################################
##################################################################################################################################
########################################       Using Python to Access Web Data       #############################################
##################################################################################################################################
##################################################################################################################################



## Scrape, Parse and Read Web Data as well as access data using web APIs.
	# Work with HTML, XML, JSON data formats in python.



###############################################################################################
###############################################################################################
###############################################################################################

#### Chapter 11 : Regular expressions ####

## CheatSheet

import re
re.search() # returns True/False depending if string matches (or not)
re.findall() # returns the matching strings


# ^			Matches the beginning of a line
# $			Matches the end of the line
# .			Matches any character
# \s		Matches whitespace
# \S		Matches any non-whitespace character
# *			Repeats a character zero or more times
# *?		Repeats a character zero or more times (non-greedy)
# +			Repeats a character one or more times
# +?		Repeats a character one or more times (non-greedy)
# [aeiou]	Matches a single character in the listed set
# [^XYZ]	Matches a single character not in the listed set
# [a-z0-9]	The set of characters can include a range
# (			Indicates where string extraction is to start
# )			Indicates where string extraction is to end



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

		## Equivalent to 
		hand = open('mbox-short.txt')
		for line in hand:
			line = line.rstrip()
			if line.find('From:') >=0:
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
	# And "*?" / "+?" are non-greedy forms of the same.


#### Combining searching and extracting
	
## If we want to find numbers on lines that 
## start with the string “X-” such as::
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


	## Parentheses and findall() -- Extracting data

## But now we have to extract the numbers.
	# Parentheses are another special character in regular expressions

import re
hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
	x = re.findall('ˆX\S*: ([0-9.]+)', line)
	if len(x) > 0 :
		print x

# The numbers are still in a list 
# and need to be converted from strings to floating point, 
# but we have used the power of regular expressions to 
# both search and extract the information we found interesting.

	## extract all of the revision numbers from lines like:
		# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('ˆDetails:.*rev=([0-9]+)', line)
	if len(x) > 0:
		print x

# Translating our regular expression, 
# we are looking for lines that start with “Details:”, followed by 
# any number of characters (“.*”), followed by 
# “rev=”, and then by one or more digits. 
# We want to find lines that match the entire expression but
# we only want to extract the integer number at the end of the line, 
# so we surround “[0-9]+” with parentheses.

	## extract hour of day from lines like:
		# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

## My effort
import re
hand = open('mbox-short.txt','r')
for line in hand:
	line = line.strip() #strips extra \n when printing lines.
	x = re.findall('^From.*?([0-9][0-9]):' , line)
	if len(x) > 0:
		print x

## Correct Answer
import re
hand = open('mbox-short.txt','r')
for line in hand:
	line = line.strip() #strips extra \n when printing lines.
	x = re.findall('^From .* ([0-9][0-9]):' , line)
	if len(x) > 0:
		print x

## Escape character \

	# We need a way to match the actual character.
	# such as the character $.
	# To do this we use the backslash character \.

import re
x = 'We have just received $10.00 for cookies.'
y = re.findall('\$[0-9]+',x)
z = re.findall('[$][0-9]+',x)
print 'Are \$ and [$] equivalent?', y == z
print 'Are \$ and [$] the same?', y in z


## Unix

# There is a command-line program built into Unix called 
# grep(Generalized Regular Expression Parser) 
# it does pretty much the same as the search() examples in this chapter


#### Exercise 11  -- Chuck

## Copy & Paste from mac.


## Using List Comprehension:

import re
print sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_234594.txt', 'r' ).read())])

# Answer is 524320


#### Exercise 11.1

# Ask the user to enter a regular expression and count the number of
# lines that matched the regular expression:
	$ python grep.py
	Enter a regular expression: ˆAuthor
	mbox.txt had 1798 lines that matched ˆAuthor

import re

user_input = raw_input('Enter a regular expression:')
fhand = open('mbox-short.txt', 'r')

counter = 0
for line in fhand:
	line = line.strip()
	x = re.findall(user_input, line)
	if len(x) > 0:
		counter = counter + 1

print 'mbox.txt had ', counter, 'lines that matched', user_input


#### Exercise 11.2

# Write a program to look for lines of the form
	New Revision: 39772

# and extract the number from each of the lines 
# using a regular expression and the findall() method. 
# Compute the average of the numbers and print out the average.

import re
fhand = open('mbox-short.txt', 'r')

numbers_list = list()
counter = 0
for line in fhand:
	line = line.strip()
	x = re.findall('^New Revision: ([0-9]+)', line)
	for number in x:
		numbers_list.append(number)
		counter = counter + 1

total = float(sum(int(i) for i in numbers_list))

print float(total/ counter)



###############################################################################################
###############################################################################################
###############################################################################################


#### Chapter 12 : Networked programs ####
 

## In this chapter we will pretend to be a web browser 
# and retrieve web pages using 
# the HyperText Transport Protocol (HTTP). 
# Then we will read through the web
# page data and parse it.

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) :
		break
	print data
mysock.close()

# First the program makes a connection to port 80 
# on the server www.py4inf.com.
# Since our program is playing the role of the “web browser”, 
# the HTTP protocol says we must send the GET command 
# followed by a blank line.

# Once we send that blank line, we write a loop 
# that receives data in 512-character chunks 
# from the socket and prints the data out
# until there is no more data to read
#(i.e., the recv() returns an empty string).

# The output starts with headers which 
# the web server sends to describe the document.

# For example, the Content-Type header indicates 
# that the document is a plain text document (text/plain).

# After the server sends us the headers, 
# it adds a blank line to indicate the end of the headers, 
# and then sends the actual data of the file romeo.txt.


#### 12.3 Retrieving an image over HTTP

# In the above example, we retrieved a plain text file 
# which had newlines in the file and we simply copied 
# the data to the screen as the program ran.
# We can use a similar program to retrieve an image 
# across using HTTP. Instead of copying the data to the screen 
# as the program runs, we accumulate the data in a string, trim off
# the headers, and then save the image data to a file as follows:

import socket
import time
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
count = 0
picture = ""; # picture equals empty string
while True:
	data = mysock.recv(5120)
	if ( len(data) < 1 ) : break
	# time.sleep(0.25) # Allows the server to get ahead of us in the data sending.
	count = count + len(data)
	print len(data),count
	picture = picture + data
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n"); ## \r\n is newline for networks. \r is carriage return, \n is newline.
print 'Header length',pos
print picture[:pos]

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("Picture_from_web.jpg","wb")
fhand.write(picture);
fhand.close()


#### 12.4 Retrieving web pages with urllib

# Using urllib, you can treat a web page much like a file. 
# You simply indicate which web page you would like to retrieve 
# and urllib handles all of the HTTP protocol and header details.


# The equivalent code to read the romeo.txt file 
# from the web using urllib is as follows:
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	print line.strip()

# As an example, we can write a program to retrieve the data for romeo.txt 
# and compute the frequency of each word in the file as follows:
import urllib
counts = dict()
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
print counts


#### Parsing HTML and scraping the web

# One of the common uses of the urllib capability 
# in Python is to scrape the web.

# Web scraping is when we write a program that 
# pretends to be a web browser and retrieves pages, 
# then examines the data in those pages looking for patterns.

# As an example, a search engine such as Google will 
# look at the source of one web page and extract 
# the links to other pages and retrieve those pages, 
# extracting links, and so on. 
# Using this technique, Google spiders its way 
# through nearly all of the pages on the web.
# Google also uses the frequency of links from pages it finds 
# to a particular page as one measure of how “important” 
# a page is and how high the page should appear in its search results.


#### Parsing HTML using regular expressions

# One simple way to parse HTML is to use regular expressions 
# to repeatedly search for and extract substrings that match 
# a particular pattern.

# Here is a simple web page:

<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>

# We can construct a well-formed regular expression
# to match and extract the link values from the above text 
# as follows:

href="http://.+?"


## Our regex:

import urllib
import re
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
	print link


# Regular expressions work very nicely when your HTML 
# is well formatted and predictable. 
# But since there are a lot of “broken” HTML pages out there, 
# a solution only using regular expressions might either 
# miss some valid links or end up with bad data.
# This can be solved by using a robust HTML parsing library.


#### 12.7 Parsing HTML using BeautifulSoup

# As an example, we will simply parse some HTML input 
# and extract links using the BeautifulSoup library. 

# You can download and install the BeautifulSoup code from:
		# http://www.crummy.com/software/
# You can download and “install” BeautifulSoup or 
# you can simply place the BeautifulSoup.py file 
# in the same folder as your application.

## BeautifulSoup is now called bs4

# We will use urllib to read the page and then 
# use BeautifulSoup to extract the
# href attributes from the anchor (a) tags.

import urllib
from bs4 import BeautifulSoup
url = 'http://www.crummy.com/software/' #raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a') ## 'a' is an HTML tag <a linkstuff <\a>

for tag in tags:
	print tag.get('href', None) ## gets what is inside of the href


# You can use BeautifulSoup to pull out various parts of each tag as follows:

import urllib
from BeautifulSoup import *
url =  'http://www.dr-chuck.com/page2.htm' #raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	# Look at the parts of a tag
	print 'TAG:',tag
	print 'URL:',tag.get('href', None)
	print 'Content:',tag.contents[0]
	print 'Attrs:',tag.attrs

# These examples only begin to show the power of BeautifulSoup 
# when it comes # to parsing HTML. 
# See the documentation and samples at 
# http://www.crummy.com/software/BeautifulSoup/ for more detail.


#### 12.8 Reading binary files  using urllib

# Sometimes you want to retrieve a non-text (or binary) file 
# such as an image or  video file. 
# The data in these files is generally not useful to print out, 
# but you can easily make a copy of a URL to a local file 
# on your hard disk using urllib.


# The pattern is to open the URL and use read to download 
# the entire contents of the document into a string variable (img) 
# then write that information to a local file
# as follows:
img = urllib.urlopen('http://www.py4inf.com/cover.jpg').read()
fhand = open('cover.jpg', 'w')
fhand.write(img)
fhand.close()

# This program reads all of the data in at once across the network 
# and stores it in the variable img in the main memory of your computer, 
# then opens the file cover.jpg and writes the data out to your disk. 
# This will work if the size of the file is less than 
#  the size of the memory of your computer.

# However if this is a large audio or video file, 
# this program may crash or at least run extremely slowly 
# when your computer runs out of memory. 
# In order to avoid running out of memory, 
# we retrieve the data in blocks (or buffers) and then write
# each block to your disk before retrieving the next block. 
# This way the program can read any size file 
# without using up all of the memory you have in your computer.

import urllib
img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover.jpg', 'wb') 
## open('cover.jpg', 'w') doeesn't work when trying to open the image
size = 0
while True:
	info = img.read(100000)
	if len(info) < 1 : break
	size = size + len(info)
	fhand.write(info)
print size,'characters copied.'
fhand.close()


#### Exercises 12.1 
	# Change the socket program socket1.py to prompt the user 
	#	for the URL so it can read any web page. 
	# You can use split(’/’) to break the URL into
	# its component parts so you can extract the host 
	# name for the socket connect call.
	# Add error checking using try and except to handle the condition 
	# where the user enters an improperly formatted or non-existent URL.


import socket
import re

#url = 'http://www.py4inf.com/code/romeo.txt'
url = raw_input( 'Enter url:')

hostname = re.findall( '.*(www.+?)/',url)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mysock.connect((hostname[0], 80))
	mysock.send('GET ' + url + ' HTTP/1.0\n\n')
except:
	print 'Please enter valid url'
	exit()

while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) :
		break
	print data
mysock.close()



#### Exercises 12.2 
	#Change your socket program so that it 
	# counts the number of characters it has received and 
	# stops displaying any text after it has shown 3000 characters.
	# The program should retrieve the entire document and 
	# count the total number of characters and display 
	# the count of the number of characters at the end of the
	# document. 

import socket
import re

#url = 'http://www.py4inf.com/code/romeo.txt'
url = 'http://www.py4inf.com/code/mbox-short.txt'
#url = 'http://www.py4inf.com/code/mbox.txt'
#url = raw_input( 'Enter url:')

hostname = re.findall( '.*(www.+?)/',url)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mysock.connect((hostname[0], 80))
	mysock.send('GET ' + url + ' HTTP/1.0\n\n')
except:
	print 'Please enter valid url'
	exit()

count = 0
text = ""
while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) : break
	#for char in data:
	#	counter = counter + len(char)
	count = count + len(data)
	text = text + data

print text[:3000]
print 'Text above has', len(text[:3000]), 'characters.'
print 'Entire document has', count, 'characters.'

mysock.close()


#### Exercises 12.3 
	# Use urllib to replicate the previous exercise of 
	# (1) retrieving the document from a URL, 
	# (2) displaying up to 3000 characters, and 
	# (3) counting the overall number of characters in the document. 
	# Dont worry about the headers for this exercise, 
	# simply show the first 3000 characters of the document contents.

###########
import urllib
import re
from bs4 import BeautifulSoup

#url = 'http://www.py4inf.com/code/romeo.txt'
url = 'http://www.py4inf.com/code/mbox-short.txt'
#url = 'http://www.py4inf.com/code/mbox.txt'
#url = raw_input( 'Enter url:')

html = urllib.urlopen(url).read()

print html[:3000]
print 'Text above has', len(html[:3000]), 'characters.'
print 'Entire document has', len(html), 'characters.'


#### Exercises 12.4
	# Change the urllinks.py program to extract 
	# and count paragraph (p) tags from the retrieved 
	# HTML document and display the count of the paragraphs
	# as the output of your program. 
	# Do not display the paragraph text, only count them. 
	# Test your program on several small web pages 
	# as well as some larger web pages

import urllib
import re
from bs4 import BeautifulSoup

#url = 'http://www.crummy.com/software/'
url = 'http://www.pythonforbeginners.com/'
url = 'https://en.wikipedia.org/wiki/Main_Page'
#url = raw_input( 'Enter url:')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

count = 0
tags = soup('p')
for tag in tags:
	count = count + 1
print count
## Tested by going to wiki page, inspect element, search <p> -- total is 6. :)


#### Chuck Exercise -Scraping HTML data with Beautiful Soup

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from bs4 import BeautifulSoup
#from BeautifulSoup import *

#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_234599.html'

#print 'reading url: ', url
html = urllib.urlopen(url).read()
#print(type(html))

soup = BeautifulSoup(html)
#print type(soup)

# Retrieve all of the anchor tags
tags = soup('span')
#print type(tags)

sums = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs
    sums = sums + int(tag.contents[0])
    count = count + 1

print count
print sums

#### Chuck Exercise -Following links in HTML Using BeautifulSoup

# The program will use urllib to read the HTML
# from the data files below, 
# extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position 
# from the top and follow that link, 
# repeat the process a number of times, 
# and report the last name you find.

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/known_by_Fox.html"

repeat = 0
while repeat < 7:
	print url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')
	list_urls = []
	for tag in tags:
		list_urls.append(tag.get('href', None))
	url = list_urls[17]
	repeat = repeat + 1

print "Last name in sequence:", re.findall("known_by_(.+).html",url)[0]




###############################################################################################
###############################################################################################
###############################################################################################


#### Chapter 13 : Using Web Services ####


# There are two common formats when exchanging data across the web.
	# XML     --“eXtensible Markup Language
					# for documents
	# JSON    -- JavaScript Object Notation
					# for data structures - lists, dicts,...


#### XML  - similar to HTML, but more structured.
	
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>
 
#Often it is helpful to think of an XML document as a tree structure 
# where there is a top tag person and other tags 
# such as phone are drawn as children of their parent nodes.


## Parsing XML

import xml.etree.ElementTree as ET
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')



# Calling fromstring converts the string representation 
	# of the XML into a “tree” of XML nodes. 
# When the XML is in a tree, we have a series of methods 
	# we can call to extract portions of data from the XML.
# The find function searches through the XML tree 
	# and retrieves a node that matches the specified tag. 
# Each node can have some text, some attributes (like hide), 
	# and some “child” nodes. 
# Each node can be the top of a tree of nodes.

## Looping through nodes

# Often the XML has multiple nodes and we need to write 
# a loop to process all of the nodes. 
# In the following program, we loop through all of the user nodes:


import xml.etree.ElementTree as ET

input = '''
<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x="7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')

print 'User count:', len(lst)

for item in lst:
	print 'Name', item.find('name').text
	print 'Id', item.find('id').text
	print 'Attribute', item.get('x')


# The findall method retrieves a Python list of subtrees 
# that represent the user structures in the XML tree. 
# Then we can write a for loop that looks at each of
# the user nodes, and prints the name and id text elements 
# as well as the x attribute from the user node



#### JSON -- JavaScript Object Notation

# The JSON format was inspired by the object and array format 
# used in the JavaScript language. 
# But since Python was invented before JavaScript, 
# Python’s syntax for dictionaries and lists 
# influenced the syntax of JSON. 
# So the format of JSON is nearly identical to 
# a combination of Python lists and dictionaries.

# Here is a JSON encoding that is roughly equivalent 
# to the sample XML from above:

{
	"name" : "Chuck",
	"phone" : {
		"type" : "intl",
		"number" : "+1 734 303 4456"
			},
	"email" : {
		"hide" : "yes"
	}
}

# You will notice some differences. 
# First, in XML, we can add attributes like “intl” to the “phone” tag. 
# In JSON, we simply have key-value pairs. 
# Also the XML “person” tag is gone, 
# replaced by a set of outer curly braces.

# In general, JSON structures are simpler than XML 
# because JSON has fewer capabilities than XML. 
# But JSON has the advantage that it maps directly to 
# some combination of dictionaries and lists. 
# And since nearly all programming languages have something 
# equivalent to Python’s dictionaries and lists, 
# JSON is a very natural format to have two cooperating programs exchange data.

# JSON is quickly becoming the format of choice for nearly 
# all data exchange between applications because of its 
# relative simplicity compared to XML.


## Parsing JSON

# We construct our JSON by nesting dictionaries (objects) and lists as needed. 
# In this example, we represent a list of users 
# where each user is a set of key-value pairs (i.e., a dictionary). 
# So we have a list of dictionaries.

# In the following program, we use the built-in json library to parse the JSON 
# and read through the data.
# Compare this closely to the equivalent XML data and code above. 
# The JSON has less detail, so we must know in advance 
# that we are getting a list and that the list is of users 
# and each user is a set of key-value pairs. 

# The JSON is more succinct (an advantage) 
# but also is less self-describing (a disadvantage).


import json
input = '''
[
	{ "id" : "001",
		"x" : "2",
		"name" : "Chuck"
	} ,
	{ "id" : "009",
		"x" : "7",
		"name" : "Brent"
	}
]'''

info = json.loads(input)
print 'User count:', len(info)
for item in info:
	print 'Name', item['name']
	print 'Id', item['id']
	print 'Attribute', item['x']

#### 13.6 Application Programming Interfaces (API)

# We now have the ability to exchange data between applications 
# using HyperText Transport Protocol (HTTP) 
# and a way to represent complex data that we are send- ing back and forth 
# between these applications using eXtensible Markup Language (XML) 
# or JavaScript Object Notation (JSON).

# The next step is to begin to define and document “contracts” 
# between applications using these techniques. 

# The general name for these application-to-application contracts is 
# Application Program Interfaces or APIs. 

# When we use an API, generally one program makes a set of services available 
# for use by other applications and publishes the APIs (i.e. the “rules”) 
# that must be followed to access the services provided by the program.


# When we begin to build our programs where the functionality of our program 
# includes access to services provided by other programs, 
# we call the approach a Service-Oriented Architecture or SOA. 

# A SOA approach is one where our overall application 
# makes use of the services of other applications. 
# A non-SOA approach is where the application is a single stand-alone application 
# which contains all of the code necessary to implement the application.

# We see many examples of SOA when we use the web. 
# We can go to a single web site and book air travel, hotels, 
# and automobiles all from a single site. 
# The data for hotels is not stored on the airline computers. 

# Instead, the airline computers contact the services on the hotel computers 
# and retrieve the hotel data and present it to the user. 
# When the user agrees to make a hotel reservation using the airline site, 
# the airline site uses another web service on the hotel systems to actually make the reservation. 
# And when it comes to charge your credit card for the whole transaction, 
# still other computers become involved in the process.

# A Service-Oriented Architecture has many advantages including: 
	# (1) we always maintain only one copy of data - 
		# this is particularly important for things like hotel reservations 
		# where we do not want to over-commit and 
	# (2) the owners of the data can set the rules about the use of their data. 

# With these advantages, a SOA system must be carefully designed to have good performance 
# and meet the user’s needs.

# When an application makes a set of services in its API available over the web, 
# we call these web services.


#### 13.7 Google geocoding web service

# Google has an excellent web service that allows us to make use 
# of their large database of geographic information. 
# We can submit a geographical search string like “Ann Arbor, MI” 
# to their geocoding API and have Google return its best guess 
# as to where on a map we might find our search string 
# and tells us about the landmarks nearby.

# The geocoding service is free but rate limited 
# so you cannot make unlimited use of the API in a commercial application. 
# But if you have some survey data where￼an end-user has entered a location 
# in a free-format input box, you can use this API to clean up your data quite nicely.

# When you are using a free API like Google’s geocoding API, 
# you need to be respectful in your use of these resources. 
# If too many people abuse the service, Google might drop or significantly curtail its free service.


# You can read the online documentation for this service, 
# but it is quite simple and you can even test it using a browser 
# by typing the following URL into your browser:

	# http://maps.googleapis.com/maps/api/geocode/json?sensor=false& address=Ann+Arbor%2C+MI

# Make sure to unwrap the URL and remove any spaces from the URL before pasting it into your browser.
# The following is a simple application to prompt the user for a search string 
# and call the Google geocoding API and extract information from the returned JSON.

import urllib 
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location: ') 
	if len(address) < 1 : break
	
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving', url

	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'

	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ====' 
		print data
		continue
	print json.dumps(js, indent=4)
	
	lat = js["results"][0]["geometry"]["location"]["lat"] 
	lng = js["results"][0]["geometry"]["location"]["lng"] 
	print 'lat',lat,'lng',lng
	location = js['results'][0]['formatted_address'] 
	print location


## Equivalent but using XML

import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location




# The program takes the search string and constructs a URL with the search string 
# as a properly encoded parameter and then uses urllib to retrieve the text 
# from the Google geocoding API. 
# Unlike a fixed web page, the data we get depends on the parameters we send 
# and the geographical data stored in Google’s servers.

# Once we retrieve the JSON data, we parse it with the json library 
# and do a few checks to make sure that we received good data 
# and then extract the information that we are looking for.


#### 13.8 Security and API usage

# It is quite common that you need some kind of “API key” 
# to make use of a vendor’s API. 
# The general idea is that they want to know who is using their services 
# and how much each user is using. 
# Perhaps they have free and pay tiers of their services 
# or have a policy that limits the number of requests that a single individual 
# can perform during a particular time period.

# Sometimes once you get your API key, you simply include the key as part of POST data 
# or perhaps as a parameter on the URL when calling the API.

# Other times, the vendor wants increased assurance of the source of the requests 
# and so they expect you to send cryptographically signed messages 
# using shared keys and secrets. 
# A very common technology that is used to sign requests over the Internet is called OAuth. 
# You can read more about the OAuth protocol at http://www.oauth.net.

# As the Twitter API became increasingly valuable, 
# Twitter went from an open and public API 
# to an API that required the use of OAuth signatures on each API request. 
# Thankfully there are a number of convenient and free OAuth libraries
# so you can avoid writing an OAuth implementation from scratch by reading the specification. 

# These libraries are of varying complexity and have varying richness. 
# The OAuth web site has information about various OAuth libraries.

# For this next sample program we will download these files: 
	# twurl.py, hidden.py, oauth.py, and twitter1.py 
	# from www.py4inf.com/code 
	# and put them all in a folder on your computer.

# To make use of these programs you will need to have a Twitter account, 
# and authorize your Python code as an application, 
# set up a key, secret, token and token secret. 

# You will edit the file hidden.py and put these 
# four strings into the appropriate variables in the file:

def auth() :
	return { "consumer_key" : "h7L...GNg",
			"consumer_secret" : "dNK...7Q",
			"token_key" : "101...GI", 
			"token_secret" : "H0yM...Bo" }

# The Twitter web service are accessed using a URL like this:
# https://api.twitter.com/1.1/statuses/user_timeline.json

# But once all of the security information has been added, the URL will look more like:

# https://api.twitter.com/1.1/statuses/user_timeline.json?count=2
	# &oauth_version=1.0&oauth_token=101...SGI&screen_name=drchuck 
	# &oauth_nonce=09239679&oauth_timestamp=1380395644
	# &oauth_signature=rLK...BoD&oauth_consumer_key=h7Lu...GNg 
	# &oauth_signature_method=HMAC-SHA1

# You can read the OAuth specification if you want to know more about the meaning 
# of the various parameters that are added to meet the security requirements of OAuth.
 
# For the programs we run with Twitter, 
# we hide all the complexity in the files oauth.py and twurl.py.
# We simply set the secrets in hidden.py and then send the desired URL to 
# the twurl.augment() function and the library code adds 
# all the necessary parameters to the URL for us.

# This program (twitter1.py) retrieves the timeline for 
# a particular Twitter user and returns it to us in JSON format in a string. 
# We simply print the first 250 characters of the string:

import urllib 
import twurl

TWITTER_URL='https://api.twitter.com/1.1/statuses/user_timeline.json'

while True: 
	print ''
	acct = raw_input('Enter Twitter Account:') 
	if(len(acct)<1):break
	url = twurl.augment(TWITTER_URL,
	{'screen_name': acct, 'count': '2'} ) 
	print 'Retrieving', url
	connection = urllib.urlopen(url)
	data = connection.read()
	print data[:250]
	headers = connection.info().dict
	# print headers
	print 'Remaining', headers['x-rate-limit-remaining']


# Along with the returned timeline data,
# Twitter also returns metadata about the request in the HTTP response headers. 
# One header in particular, x-rate-limit-remaining 
# informs us how many more requests we can make 
# before we will be shut off for a short time period. 
# You can see that our remaining retrievals drop by one 
# each time we make a request to the API.

# In the following example, we retrieve a user’s Twitter friends 
# and parse the returned JSON and extract some of the information 
# about the friends. 

# We also dump the JSON after parsing and “pretty-print” it 
# with an indent of four characters to allow us
# to pore through the data when we want to extract more fields.

import urllib 
import twurl 
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
while True: 
	print ''
	acct = raw_input('Enter Twitter Account:') 
	if(len(acct)<1):break
	url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'} ) 

	print 'Retrieving', url
	connection = urllib.urlopen(url)
	data = connection.read()
	headers = connection.info().dict
	print 'Remaining', headers['x-rate-limit-remaining'] 
	js = json.loads(data)
	print json.dumps(js, indent=4)
	for u in js['users'] : 
		print u['screen_name'] s = u['status']['text'] 
		print ' ',s[:50]

# Since the JSON becomes a set of nested Python lists and dictionaries, 
# we can use a combination of the index operation and for loops 
# to wander through the returned data structures with very little Python code.

# The last bit of the output is where we see the for loop reading 
# the five most recent “friends” of the drchuck Twitter account 
# and printing the most recent status for each friend. 

# There is a great deal more data available in the returned JSON. 
# Also if you look in the output of the program, 
# you can see that the “find the friends” of a particular account 
# has a different rate limitation than the number of timeline queries 
# we are allowed to run per time period.
# These secure API keys allow Twitter to have solid confidence 
# that they know who is using their API and data and at what level. 
# The rate limiting approach allows us to do simple, personal data retrievals 
# but does not allow us to build a product that pulls data 
# from their API millions of times per day.


## REST: REpresentational State Transfer - 
	# A style of Web Services that provide access to resources 
	# within an application using the HTTP protocol.


#### Exercise 13.1 

## Change either the www.py4inf.com/code/geojson.py 
## or www. py4inf.com/code/geoxml.py 
## to print out the two-character country code from the retrieved data. 
## Add error checking so your program does not traceback if the country code is not there. 
## Once you have it working, search for -- Atlantic Ocean 
## and make sure it can handle locations that are not in any country.

import urllib 
import json
import re

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location: ') 
	if len(address) < 1 : break
	
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving', url

	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'

	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ====' 
		print data
		continue
	#print json.dumps(js, indent=4)
	
	lat = js["results"][0]["geometry"]["location"]["lat"] 
	lng = js["results"][0]["geometry"]["location"]["lng"] 
	#print 'lat',lat,'lng',lng
	location = js['results'][0]['formatted_address'] 
	#print location

	print "new code"
	print data
	dicts = len(js["results"][0]["address_components"])
	country_code = js["results"][0]["address_components"][dicts-1]["short_name"]

	if len(re.findall('[A-Z][A-Z]',country_code))>0:
		print country_code
	else:
		print "Please enter location with valid country code."


#### Exercise Chuck -- Extracting Data from XML
	# From web services and XML

import urllib
import xml.etree.ElementTree as ET

#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_234596.xml'

url_open = urllib.urlopen(url)
data = url_open.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

#print data

#comments = tree.findall('comments')
#print comments[0].find('comment').find('count').text

##  you can use an XPath selector string to look 
## through the entire tree of XML for any tag named 'count'
counts = tree.findall('.//count')

#print type(counts) ## list
#print type(counts[0])

sums = 0
count = 0
for element in counts:
	count = count + 1
	sums = sums + int(element.text)

print count
print sums


#### Exercise Chuck -- Extracting data from JSON
	# from a url

# The program will prompt for a URL, read the JSON data from that URL using urllib 
# and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file.

import urllib
import json

url = raw_input("Enter url:")

#url = "http://python-data.dr-chuck.net/comments_42.json"
#url = "http://python-data.dr-chuck.net/comments_234600.json"


uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
	
js = json.loads(str(data))

#print json.dumps(js, indent=4)
#print type(js["comments"][0]["count"])

sums = int(0)
counts = int(0)
for comment in js["comments"]:
	sums = sums + int(comment["count"])
	counts = counts + 1

print counts
print sums


#### Exercise Chuck -- Using the GeoJSON API

# The program will prompt for a location, contact a web service 
# and retrieve JSON for the web service and parse that data, 
# and retrieve the first place_id from the JSON. 

# A place ID is a textual identifier that 
# uniquely identifies a place as within Google Maps.

import urllib 
import json
import re


#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input('Enter location: ') 
	if len(address) < 1 : break
	
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving', url

	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'

	try: js = json.loads(str(data))
	except: js = None

#	print js
	print json.dumps(js, indent=4)

	print js["results"][0]["place_id"]

print 'done'

# Simon Fraser University
# ChIJa8FTJPrzBFMR8dy-IfiXGMA


########################################################################################################
########################################################################################################
########################################################################################################
#############################       Using Databases with Python       ##################################
########################################################################################################
########################################################################################################
########################################################################################################



# This course will introduce students to the basics of the Structured Query Language (SQL) 
# as well as basic database design for storing data 
# as part of a multi-step data gathering, analysis, and processing effort.  
# The course will use SQLite3 as its database.  
# We will also build web crawlers and multi-step data gathering and visualization processes.  
# We will use the D3.js library to do basic data visualization

###############################################################################################
###############################################################################################
###############################################################################################


#### Chapter 14 : Using databases and Structured Query Language (SQL) ####


## 14.1 What is a database?

# A database is a file that is organized for storing data. Most databases are organized
# like a dictionary in the sense that they map from keys to values. The biggest
# difference is that the database is on disk (or other permanent storage), so it persists
# after the program ends. Because a database is stored on permanent storage, it can
# store far more data than a dictionary, which is limited to the size of the memory in
# the computer.

# Like a dictionary, database software is designed to keep the inserting and accessing
# of data very fast, even for large amounts of data. Database software maintains its
# performance by building indexes as data is added to the database to allow the
# computer to jump quickly to a particular entry.

# There are many different database systems which are used for a wide variety of
# purposes including: Oracle, MySQL, Microsoft SQL Server, PostgreSQL, and
# SQLite. We focus on SQLite in this book because it is a very common database
# and is already built into Python. SQLite is designed to be embedded into other
# applications to provide database support within the application. For example, the
# Firefox browser also uses the SQLite database internally as do many other products.

		# http://sqlite.org/

# SQLite is well suited to some of the data manipulation problems that we see in Informatics
# such as the Twitter spidering application that we describe in this chapter.


## 14.2 Database concepts

# When you first look at a database it looks like a spreadsheet with multiple sheets.
# The primary data structures in a database are: tables, rows, and columns.

# In technical descriptions of relational databases the concepts of table, row, and column
# are more formally referred to as relation, tuple, and attribute, respectively.
# We will use the less formal terms in this chapter.


## 14.3 SQLite manager Firefox add-on

# While this chapter will focus on using Python to work with data in SQLite database
# files, many operations can be done more conveniently using a Firefox add-on
# called the SQLite Database Manager which is freely available from:

		# https://addons.mozilla.org/en-us/firefox/addon/sqlite-manager/

# Using the browser you can easily create tables, insert data, edit data, or run simple
# SQL queries on the data in the database.
# In a sense, the database manager is similar to a text editor when working with text
# files. When you want to do one or very few operations on a text file, you can just
# open it in a text editor and make the changes you want. When you have many
# changes that you need to do to a text file, often you will write a simple Python
# program. You will find the same pattern when working with databases. You will
# do simple operations in the database manager and more complex operations will
# be most conveniently done in Python.


## 14.4 Creating a database table

# Databases require more defined structure than Python lists or dictionaries.
# When we create a database table we must tell the database in advance the names
# of each of the columns in the table and the type of data which we are planning to
# store in each column. When the database software knows the type of data in each
# column, it can choose the most efficient way to store and look up the data based
# on the type of data.

# You can look at the various data types supported by SQLite at the following url:
		
		# http://www.sqlite.org/datatypes.html

# Defining structure for your data up front may seem inconvenient at the beginning,
# but the payoff is fast access to your data even when the database contains a large
# amount of data

# The code to create a database file and a table named Tracks with two columns in
# the database is as follows:

import sqlite3
conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()

# The connect operation makes a “connection” to the database stored in the file
# music.sqlite3 in the current directory. If the file does not exist, it will be created.
# The reason this is called a “connection” is that sometimes the database is
# stored on a separate “database server” from the server on which we are running
# our application. In our simple examples the database will just be a local file in the
#  same directory as the Python code we are running.


# A cursor is like a file handle that we can use to perform operations on the data
# stored in the database. Calling cursor() is very similar conceptually to calling
# open() when dealing with text files.

# Once we have the cursor, we can begin to execute commands on the contents of
# the database using the execute() method.

# Database commands are expressed in a special language that has been standardized
# across many different database vendors to allow us to learn a single database
# language. The database language is called Structured Query Language or SQL
# for short.

# As a convention, 
# SQL keywords in uppercase 
# and the parts of the command that we are adding in lowercase
# (such as the table and column names)

# The commands: 
cur.execute('DROP TABLE IF EXISTS Tracks ')
	# means drop the table - Tracks (no undo button on drop table)

cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
	# means createthe table tracks with two columns, text and plays.

## INSERT
# The SQL INSERT command indicates which table we are using and then defines a
# new row by listing the fields we want to include (title, plays) followed by the
# VALUES we want placed in the new row. We specify the values as question marks
# (?, ?) to indicate that the actual values are passed in as a tuple ( ’My Way’,
# 15 ) as the second parameter to the execute() call.

import sqlite3
conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',( 'Thunderstruck', 20 ) )
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',( 'My Way', 15 ) )
conn.commit()

print 'Tracks:'
cur.execute('SELECT title, plays FROM Tracks')

for row in cur :
	print row

cur.execute('DELETE FROM Tracks WHERE plays < 100')

conn.commit()
cur.close()


# First we INSERT two rows into our table and use commit() to force the data to be
# written to the database file.


# Then we use the SELECT command to retrieve the rows we just inserted from
# the table. On the SELECT command, we indicate which columns we would like
# (title, plays) and indicate which table we want to retrieve the data from. After
# we execute the SELECT statement, the cursor is something we can loop through in
# a for statement. For efficiency, the cursor does not read all of the data from the
# database when we execute the SELECT statement. Instead, the data is read on
# demand as we loop through the rows in the for statement.


# The output of the program is as follows:
			Tracks:
			(u'Thunderstruck', 20)
			(u'My Way', 15)

# The u’ is an indication that the strings are Unicode strings 
# that are capable of storing non-Latin character sets

# At the very end of the program, we execute an SQL command to DELETE the
# rows we have just created so we can run the program over and over
# After the DELETE is performed, we also call commit() to force 
# the data to be removed from the database.


## 14.5 Structured Query Language summary

# So far, we have been using the Structured Query Language in our Python examples
# and have covered many of the basics of the SQL commands. In this section, we
# look at the SQL language in particular and give an overview of SQL syntax.
# Since there are so many different database vendors, the Structured Query Language
# (SQL) was standardized so we could communicate in a portable manner to
# database systems from multiple vendors.
# 174 Chapter 14. Using databases and Structured Query Language (SQL)
# A relational database is made up of tables, rows, and columns. The columns
# generally have a type such as text, numeric, or date data. When we create a table,
# we indicate the names and types of the columns:
# CREATE TABLE Tracks (title TEXT, plays INTEGER)
# To insert a row into a table, we use the SQL INSERT command:
# INSERT INTO Tracks (title, plays) VALUES ('My Way', 15)
# The INSERT statement specifies the table name, then a list of the fields/columns
# that you would like to set in the new row, and then the keyword VALUES and a list
# of corresponding values for each of the fields.
# The SQL SELECT command is used to retrieve rows and columns from a database.
# The SELECT statement lets you specify which columns you would like to retrieve
# as well as a WHERE clause to select which rows you would like to see. It also allows
# an optional ORDER BY clause to control the sorting of the returned rows.
# SELECT * FROM Tracks WHERE title = 'My Way'
# Using * indicates that you want the database to return all of the columns for each
# row that matches the WHERE clause.
# Note, unlike in Python, in a SQL WHERE clause we use a single equal sign to
# indicate a test for equality rather than a double equal sign. Other logical operations
# allowed in a WHERE clause include <, >, <=, >=, !=, as well as AND and OR and
# parentheses to build your logical expressions.
# You can request that the returned rows be sorted by one of the fields as follows:
# SELECT title,plays FROM Tracks ORDER BY title
# To remove a row, you need a WHERE clause on an SQL DELETE statement. The
# WHERE clause determines which rows are to be deleted:
# DELETE FROM Tracks WHERE title = 'My Way'
# It is possible to UPDATE a column or columns within one or more rows in a table
# using the SQL UPDATE statement as follows:
# UPDATE Tracks SET plays = 16 WHERE title = 'My Way'
# The UPDATE statement specifies a table and then a list of fields and values to change
# after the SET keyword and then an optional WHERE clause to select the rows that are
# to be updated. A single UPDATE statement will change all of the rows that match
# the WHERE clause. If a WHERE clause is not specified, it performs the UPDATE on all
# of the rows in the table.
# These four basic SQL commands (INSERT, SELECT, UPDATE, and DELETE)
# allow the four basic operations needed to create and maintain data.

CREATE TABLE Tracks (title TEXT, plays INTEGER)
INSERT INTO Tracks (title, plays) VALUES ('My Way', 15)
SELECT title,plays FROM Tracks ORDER BY title
DELETE FROM Tracks WHERE title = 'My Way'
UPDATE Tracks SET plays = 16 WHERE title = 'My Way'

###############################################################################################
###############################################################################################
###############################################################################################

## 14.6 Spidering Twitter using a database

# In this section, we will create a simple spidering program that will go through
# Twitter accounts and build a database of them. Note: Be very careful when running
# this program. You do not want to pull too much data or run the program for too
# long and end up having your Twitter access shut off.

# One of the problems of any kind of spidering program is that it needs to be able
# to be stopped and restarted many times and you do not want to lose the data that
# you have retrieved so far. You don’t want to always restart your data retrieval at
# the very beginning so we want to store data as we retrieve it so our program can
# start back up and pick up where it left off.

# We will start by retrieving one person’s Twitter friends and their statuses, looping
# through the list of friends, and adding each of the friends to a database to be
# retrieved in the future. After we process one person’s Twitter friends, we check
# in our database and retrieve one of the friends of the friend. We do this over and
# over, picking an “unvisited” person, retrieving their friend list, and adding friends
# we have not seen to our list for a future visit.

# We also track how many times we have seen a particular friend in the database to
# get some sense of their “popularity”.

# By storing our list of known accounts and whether we have retrieved the account
# or not, and how popular the account is in a database on the disk of the computer,
# we can stop and restart our program as many times as we like.

# This program is a bit complex. It is based on the code from the exercise earlier in
# the book that uses the Twitter API.

# Here is the source code for our Twitter spidering application:

import urllib
import twurl
import json
import sqlite3

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Twitter
(name TEXT, retrieved INTEGER, friends INTEGER)''')

while True:
	acct = raw_input('Enter a Twitter account, or quit: ')
	if ( acct == 'quit' ) : break
	if ( len(acct) < 1 ) :
		cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
		try:
			acct = cur.fetchone()[0]
		except:
			print 'No unretrieved Twitter accounts found'
			continue
	url = twurl.augment(TWITTER_URL,
			{'screen_name': acct, 'count': '20'} )

	print 'Retrieving', url
	connection = urllib.urlopen(url)
	data = connection.read()
	headers = connection.info().dict
	# print 'Remaining', headers['x-rate-limit-remaining']
	js = json.loads(data)
	# print json.dumps(js, indent=4)
	
	cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ) )
	
	countnew = 0
	countold = 0
	for u in js['users'] :
		friend = u['screen_name']
		print friend
	cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
		(friend, ) )
	try:
		count = cur.fetchone()[0]
		cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
			(count+1, friend) )
		countold = countold + 1
	except:
		cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
			VALUES ( ?, 0, 1 )''', ( friend, ) )
		countnew = countnew + 1
	print 'New accounts=',countnew,' revisited=',countold
	conn.commit()

cur.close()


# Our database is stored in the file spider.sqlite3 and it has one table named
# Twitter. Each row in the Twitter table has a column for the account name,
# whether we have retrieved the friends of this account, and how many times this
# account has been “friended”.

# In the main loop of the program, we prompt the user for a Twitter account name
# or “quit” to exit the program. If the user enters a Twitter account, we retrieve the
# list of friends and statuses for that user and add each friend to the database if not
# already in the database. If the friend is already in the list, we add 1 to the friends
# field in the row in the database.

# If the user presses enter, we look in the database for the next Twitter account that
# we have not yet retrieved, retrieve the friends and statuses for that account, add
# them to the database or update them, and increase their friends count.


# Once we retrieve the list of friends and statuses, we loop through all of the user
# items in the returned JSON and retrieve the screen_name for each user. Then
# we use the SELECT statement to see if we already have stored this particular
# screen_name in the database and retrieve the friend count (friends) if the record
# exists.

countnew = 0
countold = 0
	for u in js['users'] :
		friend = u['screen_name']
		print friend
	cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
		(friend, ) )
	try:
		count = cur.fetchone()[0]
		cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
			(count+1, friend) )
		countold = countold + 1
	except:
		cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
			VALUES ( ?, 0, 1 )''', ( friend, ) )
		countnew = countnew + 1
	print 'New accounts=',countnew,' revisited=',countold
	conn.commit()

# Once the cursor executes the SELECT statement, we must retrieve the rows. We
# could do this with a for statement, but since we are only retrieving one row (LIMIT
# 1), we can use the fetchone() method to fetch the first (and only) row that is the
# result of the SELECT operation. Since fetchone() returns the row as a tuple (even
# though there is only one field), we take the first value from the tuple using [0] to
# get the current friend count into the variable count.

# If this retrieval is successful, we use the SQL UPDATE statement with a WHERE
# clause to add 1 to the friends column for the row that matches the friend’s account.
# Notice that there are two placeholders (i.e., question marks) in the SQL,
# and the second parameter to the execute() is a two-element tuple that holds the
# values to be substituted into the SQL in place of the question marks.

# If the code in the try block fails, it is probably because no record matched the
# WHERE name = ? clause on the SELECT statement. So in the except block, we
# use the SQL INSERT statement to add the friend’s screen_name to the table with
# an indication that we have not yet retrieved the screen_name and set the friend
# count to zero.

# So the first time the program runs and we enter a Twitter account, the program
# runs as follows:
	Enter a Twitter account, or quit: drchuck
	Retrieving http://api.twitter.com/1.1/friends ...
	New accounts= 20 revisited= 0
	Enter a Twitter account, or quit: quit

# Since this is the first time we have run the program, the database is empty and we
# create the database in the file spider.sqlite3 and add a table named Twitter
# to the database. Then we retrieve some friends and add them all to the database
# since the database is empty.

# At this point, we might want to write a simple database dumper to take a look at
# what is in our spider.sqlite3 file:


import sqlite3
conn = sqlite3.connect('spider.sqlite3')
cur = conn.cursor()
cur.execute('SELECT * FROM Twitter')
count = 0
for row in cur :
	print row
	count = count + 1
print count, 'rows.'
cur.close()


# This program simply opens the database and selects all of the columns of all of the
# rows in the table Twitter, then loops through the rows and prints out each row.
# If we run this program after the first execution of our Twitter spider above, its
# output will be as follows:
	(u'opencontent', 0, 1)
	(u'lhawthorn', 0, 1)
	(u'steve_coppin', 0, 1)
	(u'davidkocher', 0, 1)
	(u'hrheingold', 0, 1)
	...
	20 rows.


# We see one row for each screen_name, that we have not retrieved the data for that
# screen_name, and everyone in the database has one friend.
# Now our database reflects the retrieval of the friends of our first Twitter account
# (drchuck). We can run the program again and tell it to retrieve the friends of the
# next “unprocessed” account by simply pressing enter instead of a Twitter account
# as follows:
	Enter a Twitter account, or quit:
	Retrieving http://api.twitter.com/1.1/friends ...
	New accounts= 18 revisited= 2
	Enter a Twitter account, or quit:
	Retrieving http://api.twitter.com/1.1/friends ...
	New accounts= 17 revisited= 3
	Enter a Twitter account, or quit: quit

# Since we pressed enter (i.e., we did not specify a Twitter account), the following
# code is executed:
if ( len(acct) < 1 ) :
	cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
	try:
		acct = cur.fetchone()[0]
	except:
		print 'No unretrieved twitter accounts found'
		continue


# We use the SQL SELECT statement to retrieve the name of the first (LIMIT 1) user
# who still has their “have we retrieved this user” value set to zero. We also use the
# fetchone()[0] pattern within a try/except block to either extract a screen_name
# from the retrieved data or put out an error message and loop back up.
# If we successfully retrieved an unprocessed screen_name, we retrieve their data
# as follows:

url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'} )
print 'Retrieving', url
connection = urllib.urlopen(url)
data = connection.read()
js = json.loads(data)
cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ) )

# Once we retrieve the data successfully, we use the UPDATE statement to set the
# retrieved column to 1 to indicate that we have completed the retrieval of the
# friends of this account. This keeps us from retrieving the same data over and over
# and keeps us progressing forward through the network of Twitter friends.
# If we run the friend program and press enter twice to retrieve the next unvisited
# friend’s friends, then run the dumping program, it will give us the following output:

	(u'opencontent', 1, 1)
	(u'lhawthorn', 1, 1)
	(u'steve_coppin', 0, 1)
	(u'davidkocher', 0, 1)
	(u'hrheingold', 0, 1)
	...
	(u'cnxorg', 0, 2)
	(u'knoop', 0, 1)
	(u'kthanos', 0, 2)
	(u'LectureTools', 0, 1)
	...
	55 rows.

# We can see that we have properly recorded that we have visited lhawthorn
# and opencontent. Also the accounts cnxorg and kthanos already have two
# followers. Since we now have retrieved the friends of three people (drchuck,
# opencontent, and lhawthorn) our table has 55 rows of friends to retrieve.

# Each time we run the program and press enter it will pick the next unvisited account
# (e.g., the next account will be steve_coppin), retrieve their friends, mark
# them as retrieved, and for each of the friends of steve_coppin either add them
# to the end of the database or update their friend count if they are already in the
# database.

# Since the program’s data is all stored on disk in a database, the spidering activity
# can be suspended and resumed as many times as you like with no loss of data.



###############################################################################################
###############################################################################################
###############################################################################################

## 14.7 Basic data modeling

# The real power of a relational database is when we create multiple tables and make
# links between those tables. The act of deciding how to break up your application
# data into multiple tables and establishing the relationships between the tables is
# called data modeling. The design document that shows the tables and their relationships
# is called a data model.

# Data modeling is a relatively sophisticated skill and we will only introduce the
# most basic concepts of relational data modeling in this section. For more detail on
# data modeling you can start with:

	# http://en.wikipedia.org/wiki/Relational_model

# Let’s say for our Twitter spider application, instead of just counting a person’s
# friends, we wanted to keep a list of all of the incoming relationships so we could
# find a list of everyone who is following a particular account.

# Since everyone will potentially have many accounts that follow them, we cannot
# simply add a single column to our Twitter table. So we create a new table that
# keeps track of pairs of friends. The following is a simple way of making such a
# table:

	# CREATE TABLE Pals (from_friend TEXT, to_friend TEXT)

# Each time we encounter a person who drchuck is following, we would insert a
# row of the form:

	# INSERT INTO Pals (from_friend,to_friend) VALUES ('drchuck', 'lhawthorn')

# As we are processing the 20 friends from the drchuck Twitter feed, we will insert
# 20 records with “drchuck” as the first parameter so we will end up duplicating the
# string many times in the database.

# This duplication of string data violates one of the best practices for database normalization
# which basically states that we should never put the same string data
# in the database more than once. If we need the data more than once, we create a
# numeric key for the data and reference the actual data using this key.

# In practical terms, a string takes up a lot more space than an integer on the disk
# and in the memory of our computer, and takes more processor time to compare
# and sort. If we only have a few hundred entries, the storage and processor time
# hardly matters. But if we have a million people in our database and a possibility
# of 100 million friend links, it is important to be able to scan data as quickly as
# possible.

# We will store our Twitter accounts in a table named People instead of the Twitter
# table used in the previous example. The People table has an additional column
# to store the numeric key associated with the row for this Twitter user. SQLite has
# a feature that automatically adds the key value for any row we insert into a table
# using a special type of data column (INTEGER PRIMARY KEY).

# We can create the People table with this additional id column as follows:

	# CREATE TABLE People(id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)

# Notice that we are no longer maintaining a friend count in each row of the People
# table. When we select INTEGER PRIMARY KEY as the type of our id column,
# we are indicating that we would like SQLite to manage this column and assign a
# unique numeric key to each row we insert automatically. We also add the keyword
# UNIQUE to indicate that we will not allow SQLite to insert two rows with the same
# value for name.

# Now instead of creating the table Pals above, we create a table called Follows
# with two integer columns from_id and to_id and a constraint on the table that the
# combination of from_id and to_id must be unique in this table (i.e., we cannot
# insert duplicate rows) in our database.

	# CREATE TABLE Follows(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id) )

# When we add UNIQUE clauses to our tables, we are communicating a set of rules
# that we are asking the database to enforce when we attempt to insert records. We
# are creating these rules as a convenience in our programs, as we will see in a
# moment. The rules both keep us from making mistakes and make it simpler to
# write some of our code.

# In essence, in creating this Follows table, we are modelling a “relationship” where
# one person “follows” someone else and representing it with a pair of numbers indicating
# that (a) the people are connected and (b) the direction of the relationship.



###############################################################################################
###############################################################################################
###############################################################################################

## 14.8 Programming with multiple tables

# We will now redo the Twitter spider program using two tables, the primary keys,
# and the key references as described above. Here is the code for the new version of
# the program:

import urllib
import twurl
import json
import sqlite3

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
conn = sqlite3.connect('friends.sqlitesqlite3')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS People
	(id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
	(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')
while True:
	acct = raw_input('Enter a Twitter account, or quit: ')
	if ( acct == 'quit' ) : break
	if ( len(acct) < 1 ) :
		cur.execute('''SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1''')
		try:
			(id, acct) = cur.fetchone()
			### cur.fetchone() is a tuple with two items
		except:
			print 'No unretrieved Twitter accounts found'
			continue
	else:
		cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',(acct, ) )
		try:
			id = cur.fetchone()[0]
			### cur.fetchone() is a tuple with one item
			### id here will be the id for the input acct
		except:
			cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
				VALUES ( ?, 0)''', ( acct, ) )
			### insert or ignore can be used because of the unique name constraint in the table.
			### but if the acct was already in there this code shouldn't run.
			conn.commit()
			if cur.rowcount != 1 :
				print 'Error inserting account:',acct
				continue
			id = cur.lastrowid
			print 'The new People id is:',id

	url = twurl.augment(TWITTER_URL,{'screen_name': acct, 'count': '20'} )
	print 'Retrieving account', acct
	connection = urllib.urlopen(url)
	data = connection.read() 
	headers = connection.info().dict
	print 'Remaining', headers['x-rate-limit-remaining']
	js = json.loads(data)
	# print json.dumps(js, indent=4)
	cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ) )
	countnew = 0
	countold = 0
	for u in js['users'] :
		friend = u['screen_name']
		print friend
		cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',(friend, ) )
		try:
			friend_id = cur.fetchone()[0]
			countold = countold + 1
		except:
			cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
				VALUES ( ?, 0)''', ( friend, ) )
			conn.commit()
			if cur.rowcount != 1 :
				print 'Error inserting account:',friend
				continue
			friend_id = cur.lastrowid
			countnew = countnew + 1
		cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
			VALUES (?, ?)''', (id, friend_id) )
		print 'New accounts=',countnew,' revisited=',countold
		conn.commit()
cur.close()

# This program is starting to get a bit complicated, but it illustrates the patterns that
# we need to use when we are using integer keys to link tables. The basic patterns
# are:
	# 1. Create tables with primary keys and constraints.

	# 2. When we have a logical key for a person (i.e., account name) and we need
		# the id value for the person, depending on whether or not the person is already
		# in the People table we either need to: (1) look up the person in the
		# People table and retrieve the id value for the person or (2) add the person
		# to the People table and get the id value for the newly added row.
	
	# 3. Insert the row that captures the “follows” relationship.
		
# We will cover each of these in turn.


#############################################################
#############################################################
#############################################################

## 14.8.1 Constraints in database tables

# As we design our table structures, we can tell the database system that we would
# like it to enforce a few rules on us. These rules help us from making mistakes and
# introducing incorrect data into out tables. When we create our tables:

cur.execute('''CREATE TABLE IF NOT EXISTS People
	(id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
	(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

# We indicate that the name column in the People table must be UNIQUE. We also
# indicate that the combination of the two numbers in each row of the Follows table
# must be unique. These constraints keep us from making mistakes such as adding
# the same relationship more than once.
# We can take advantage of these constraints in the following code:

cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
	VALUES ( ?, 0)''', ( friend, ) )

# We add the OR IGNORE clause to our INSERT statement to indicate that if this particular
# INSERT would cause a violation of the “name must be unique” rule, the
# database system is allowed to ignore the INSERT. We are using the database constraint
# as a safety net to make sure we don’t inadvertently do something incorrect.

# Similarly, the following code ensures that we don’t add the exact same Follows
# relationship twice.
cur.execute('''INSERT OR IGNORE INTO Follows
	(from_id, to_id) VALUES (?, ?)''', (id, friend_id) )

# Again, we simply tell the database to ignore our attempted INSERT if it would
# violate the uniqueness constraint that we specified for the Follows rows.


#############################################################
#############################################################
#############################################################

## 14.8.2 Retrieve and/or insert a record

# When we prompt the user for a Twitter account, if the account exists, we must
# look up its id value. If the account does not yet exist in the People table, we must
# insert the record and get the id value from the inserted row.

# This is a very common pattern and is done twice in the program above. This code
# shows how we look up the id for a friend’s account when we have extracted a
# screen_name from a user node in the retrieved Twitter JSON.

# Since over time it will be increasingly likely that the account will already be in
# the database, we first check to see if the People record exists using a SELECT
# statement.

# If all goes well (when we use 'if all goes well' that mean we should use a try/except)
# inside the try section, we retrieve the record using fetchone()
# and then retrieve the first (and only) element of the returned tuple and store it in
# friend_id.
# If the SELECT fails, the fetchone()[0] code will fail and control will transfer
# into the except section.

friend = u['screen_name']
		print friend
		cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',(friend, ) )
		try:
			friend_id = cur.fetchone()[0]
			countold = countold + 1
		except:
			cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
				VALUES ( ?, 0)''', ( friend, ) )
			conn.commit()
			if cur.rowcount != 1 :
				print 'Error inserting account:',friend
				continue
			friend_id = cur.lastrowid
			countnew = countnew + 1

# If we end up in the except code, it simply means that the row was not found, so
# we must insert the row. We use INSERT OR IGNORE just to avoid errors and then
# call commit() to force the database to really be updated. After the write is done,
# we can check the cur.rowcount to see how many rows were affected. Since we
# are attempting to insert a single row, if the number of affected rows is something
# other than 1, it is an error.

# If the INSERT is successful, we can look at cur.lastrowid to find out what value
# the database assigned to the id column in our newly created row.


#############################################################
#############################################################
#############################################################

## 14.8.3 Storing the friend relationship

# Once we know the key value for both the Twitter user and the friend in the JSON,
# it is a simple matter to insert the two numbers into the Follows table with the
# following code:
cur.execute('INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?, ?)',
	(id, friend_id) )

# Notice that we let the database take care of keeping us from “double-inserting” a
# relationship by creating the table with a uniqueness constraint and then adding OR
# IGNORE to our INSERT statement.
# Here is a sample execution of this program:

	# Enter a Twitter account, or quit:
	# No unretrieved Twitter accounts found
	# Enter a Twitter account, or quit: drchuck
	# Retrieving http://api.twitter.com/1.1/friends ...
	# New accounts= 20 revisited= 0
	# Enter a Twitter account, or quit:
	# Retrieving http://api.twitter.com/1.1/friends ...
	# New accounts= 17 revisited= 3
	# Enter a Twitter account, or quit:
	# Retrieving http://api.twitter.com/1.1/friends ...
	# New accounts= 17 revisited= 3
	# Enter a Twitter account, or quit: quit

# We started with the drchuck account and then let the program automatically pick
# the next two accounts to retrieve and add to our database.
# The following is the first few rows in the People and Follows tables after this run
# is completed:

print 'People:'
conn = sqlite3.connect('friends.sqlitesqlite3')
cur = conn.cursor()
cur.execute('''SELECT * FROM People''')
count = 0
for row in cur :
	print row
	count = count + 1
print count, 'rows.'

print 'Follows:'
cur.execute('''SELECT * FROM Follows''')
count = 0
for row in cur :
	print row
	count = count + 1
print count, 'rows.'

cur.close()

People:
(1, u'drchuck', 1)
(2, u'opencontent', 1)
(3, u'lhawthorn', 1)
(4, u'steve_coppin', 0)
(5, u'davidkocher', 0)
55 rows.
Follows:
(1, 2)
(1, 3)
(1, 4)
(1, 5)
(1, 6)
60 rows.

# You can see the id, name, and visited fields in the People table and you see
# the numbers of both ends of the relationship in the Follows table. In the People
# table, we can see that the first three people have been visited and their data has
# been retrieved. The data in the Follows table indicates that drchuck (user 1) is a
# friend to all of the people shown in the first five rows. This makes sense because
# the first data we retrieved and stored was the Twitter friends of drchuck. If you
# were to print more rows from the Follows table, you would see the friends of
# users 2 and 3 as well.


###############################################################################################
###############################################################################################
###############################################################################################

## 14.9 Three kinds of keys

# Now that we have started building a data model putting our data into multiple
# linked tables and linking the rows in those tables using keys, we need to look at
# some terminology around keys. There are generally three kinds of keys used in a
# database model.

	## Logical key
	
# • A logical key is a key that the “real world” might use to look up a row. In
# our example data model, the name field is a logical key. It is the screen name
# for the user and we indeed look up a user’s row several times in the program
# using the name field. You will often find that it makes sense to add a UNIQUE
# constraint to a logical key. Since the logical key is how we look up a row
# from the outside world, it makes little sense to allow multiple rows with the
# same value in the table.

	## Primary key

# • A primary key is usually a number that is assigned automatically by the
# database. It generally has no meaning outside the program and is only used
# to link rows from different tables together. When we want to look up a row
# in a table, usually searching for the row using the primary key is the fastest
# way to find the row. Since primary keys are integer numbers, they take up
# very little storage and can be compared or sorted very quickly. In our data
# model, the id field is an example of a primary key

	## Foreign key

# • A foreign key is usually a number that points to the primary key of an
# associated row in a different table. An example of a foreign key in our data
# model is the from_id.

# We are using a naming convention of always calling the primary key field name
# id and appending the suffix _id to any field name that is a foreign key.


###############################################################################################
###############################################################################################
###############################################################################################

## 14.10 Using JOIN to retrieve data

# Now that we have followed the rules of database normalization and have data
# separated into two tables, linked together using primary and foreign keys, we need
# to be able to build a SELECT that reassembles the data across the tables.

# SQL uses the JOIN clause to reconnect these tables. In the JOIN clause you specify
# the fields that are used to reconnect the rows between the tables.

# The following is an example of a SELECT with a JOIN clause:
	SELECT * FROM Follows JOIN People
		ON Follows.from_id = People.id 
			WHERE People.id = 1

# The JOIN clause indicates that the fields we are selecting cross both the Follows
# and People tables. The ON clause indicates how the two tables are to be joined:
# Take the rows from Follows and append the row from People where the field
# from_id in Follows is the same the id value in the People table.


# The result of the JOIN is to create extra-long “metarows” which have both the
# fields from People and the matching fields from Follows. Where there is more
# than one match between the id field from People and the from_id from People,
# then JOIN creates a metarow for each of the matching pairs of rows, duplicating
# data as needed.

# The following code demonstrates the data that we will have in the database after
# the multi-table Twitter spider program (above) has been run several times.


import sqlite3
conn = sqlite3.connect('spider.sqlite3')
cur = conn.cursor()

cur.execute('SELECT * FROM People')
count = 0
print 'People:'
for row in cur :
	if count < 5: print row
	count = count + 1
print count, 'rows.'

cur.execute('SELECT * FROM Follows')
count = 0
print 'Follows:'
for row in cur :
	if count < 5: print row
	count = count + 1
	print count, 'rows.'

cur.execute('''SELECT * FROM Follows JOIN People
ON Follows.to_id = People.id WHERE Follows.from_id = 2''')
count = 0
print 'Connections for id=2:'
for row in cur :
	if count < 5: print row
	count = count + 1
print count, 'rows.'
cur.close()

# In this program, we first dump out the People and Follows and then dump out a
# subset of the data in the tables joined together.

# Here is the output of the program:

python twjoin.py
People:
(1, u'drchuck', 1)
(2, u'opencontent', 1)
(3, u'lhawthorn', 1)
(4, u'steve_coppin', 0)
(5, u'davidkocher', 0)
55 rows.

Follows:
(1, 2)
(1, 3)
(1, 4)
(1, 5)
(1, 6)
60 rows.

Connections for id=2:
(2, 1, 1, u'drchuck', 1)
(2, 28, 28, u'cnxorg', 0)
(2, 30, 30, u'kthanos', 0)
(2, 102, 102, u'SomethingGirl', 0)
(2, 103, 103, u'ja_Pac', 0)
20 rows.

# You see the columns from the People and Follows tables and the last set of rows
# is the result of the SELECT with the JOIN clause.

# In the last select, we are looking for accounts that are friends of “opencontent”
# (i.e., People.id=2).
# In each of the “metarows” in the last select, the first two columns are from the
# Follows table followed by columns three through five from the People table. You
# can also see that the second column (Follows.to_id) matches the third column
# (People.id) in each of the joined-up “metarows”.


###############################################################################################
###############################################################################################
###############################################################################################

## 14.11 Summary

# This chapter has covered a lot of ground to give you an overview of the basics
# of using a database in Python. It is more complicated to write the code to use a
# database to store data than Python dictionaries or flat files so there is little reason
# to use a database unless your application truly needs the capabilities of a database.
# The situations where a database can be quite useful are: (1) when your application
# needs to make small many random updates within a large data set, (2) when your
# data is so large it cannot fit in a dictionary and you need to look up information
# repeatedly, or (3) when you have a long-running process that you want to be able
# to stop and restart and retain the data from one run to the next.

# You can build a simple database with a single table to suit many application needs,
# but most problems will require several tables and links/relationships between rows
# in different tables. When you start making links between tables, it is important to
# do some thoughtful design and follow the rules of database normalization to make
# the best use of the database’s capabilities. Since the primary motivation for using
# a database is that you have a large amount of data to deal with, it is important to
# model your data efficiently so your programs run as fast as possible.


###############################################################################################
###############################################################################################
###############################################################################################

## 14.12 Debugging

# One common pattern when you are developing a Python program to connect to an
# SQLite database will be to run a Python program and check the results using the
# SQLite Database Browser. The browser allows you to quickly check to see if your
# program is working properly.

# You must be careful because SQLite takes care to keep two programs from changing
# the same data at the same time. For example, if you open a database in the
# browser and make a change to the database and have not yet pressed the “save”
# button in the browser, the browser “locks” the database file and keeps any other
# program from accessing the file. In particular, your Python program will not be
# able to access the file if it is locked.

# So a solution is to make sure to either close the database browser or use the
# File menu to close the database in the browser before you attempt to access the
# database from Python to avoid the problem of your Python code failing because
# the database is locked.

#### Chuck Video Notes

# Start creating the tables from the leaves of the tree, making your way to the trunk 
# The trunk being the main use of the DB.

Create Table Artist(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
			,artist text)

Create Table Album(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
			,artist_id INTEGER 
			,album text)

Create Table Track(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
			,title text 
			,album_id INTEGER
			,artist_id INTEGER)

Insert into Artist (artist) values ('Led Zepplin')

Insert into Album (title, artist_id) values ('Stairway', 1)

select * from Track join Album on Track.album_id = Album.id

# Chuck says you can use the where clause like the on clause
# Also, if you join using:
	# 'on' (select on match only - quicker) 
	# 'where' (takes all and filters)
	# nothing it takes every row by every row. -- All Combinations

###############################################################################################
###############################################################################################
###############################################################################################

#### Exercise Chuck -- Our First Database

# Create a SQLITE database, then create a table in the database called "Ages"

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

# Then make sure the table is empty by deleting any rows that you previously inserted, 
# and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Sol', 29);
INSERT INTO Ages (name, age) VALUES ('Bayley', 35);
INSERT INTO Ages (name, age) VALUES ('Torran', 17);
INSERT INTO Ages (name, age) VALUES ('Shayla', 22);
INSERT INTO Ages (name, age) VALUES ('Shuni', 26);

# Once the inserts are done, run the following SQL command:

SELECT hex(name || age) AS X FROM Ages ORDER BY X

# Find the first row in the resulting record set 
# and enter the long string that looks like 53656C696E613333.

# This assignment must be done using SQLite - in particular, 
# the SELECT query above will not work in any other database. 
# So you cannot use MySQL or Oracle for this assignment.



#### Exercise Chuck -- Counting Email in a Database

## Counting Organizations

# This application will read the mailbox data (mbox.txt) count up the number email messages per organization 
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)

# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, 
# make sure to empty out the data before each run.

# You can use this code as a starting point for your application: 
	# http://www.pythonlearn.com/code/emaildb.py.

# The data file for this application is the same as in previous assignments: 
	# http://www.pythonlearn.com/code/mbox.txt.

# Because the sample code is using an UPDATE statement 
# and committing the results to the database as each record is read in the loop, 
# it might take as long as a few minutes to process all the data. 
# The commit insists on completely writing all the data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. 
# In any database program, there is a balance between the number of operations you execute between commits 
# and the importance of not losing the results of operations that have not yet been committed.





#### Original from http://www.pythonlearn.com/code/emaildb.py

## Open connection to a sqlite database
sqlite_conn = sqlite3.connect('emaildb.sqlite')
## Then create a cursor through which you can talk to the db
cur = sqlite_conn.cursor()

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
	sqlite_conn.commit()

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
	####conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
	print str(row[0]), row[1]

cur.close()


#### Exercise Chuck -- Counting Email in a Database
	
	#### 	MY WORKINGS		####

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


###############################################
###############################################
###############################################

#### Chuck tutorial example - take data from XML - convert into database.


import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);
''')

##	url = http://www.pythonlearn.com/code/tracks/Library.xml
##	fhand = urllib.urlopen(url)


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key : 
            found = True
    return None

#### Lookup function - my explanation ####
## The d attribute will be the list of dicts that contain the track info.
## The key attribute will be the 'key' of the tag.
	## the 'key' tag is <key>Name</key>, the key attibute is 'Name'.
	## he says it would have been better if they weren't named the same thing.

## When the function is used:
	## for child in dictionary -- ie any of the items (tags) in the dict
		## found is false, so skips 'if found : return child.text'
		## then asks if child tag is 'key'  and if child text is key.
			## eg. child tag = <key>Name</key>, and child text = Name. then found turns to true.
		## so the function is still on the same tag and runs through another iteration of the for loop.
		## but this time found = True.
			## this executes: if found : return child.text
	## rememer return exits the function (def lookup(d,key))
	## if not found then return None -- a very pythonic way of doing things.


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : 
        continue

    print name, artist, album, count, rating, length

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

## insert it if it isn't there alreadyor ignore it if it is already there.

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )

    conn.commit()


###############################################
###############################################
###############################################

#### Exercise Chuck -- Musical Track Database
	
	#### 	MY WORKINGS	 -- include Genre into the database	####

import xml.etree.ElementTree as ET
import sqlite3

import urllib


conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name    TEXT UNIQUE
);

CREATE TABLE Genre (
	id 	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name 	TEXT UNIQUE
);

CREATE TABLE Album (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id  INTEGER,
	title   TEXT UNIQUE
);

CREATE TABLE Track (
	id  INTEGER NOT NULL PRIMARY KEY 
		AUTOINCREMENT UNIQUE,
	title TEXT  UNIQUE,
	album_id  INTEGER,
	genre_id  INTEGER,
	len INTEGER, 
	rating INTEGER, 
	count INTEGER
);
''')

url = 'http://www.pythonlearn.com/code/tracks/Library.xml'
fhand = urllib.urlopen(url)


##fname = raw_input('Enter file name: ')
##if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
	found = False
	for child in d:
		if found : return child.text
		if child.tag == 'key' and child.text == key : 
			found = True
	return None

#### Lookup function - my explanation ####
## The d attribute will be the list of dicts that contain the track info.
## The key attribute will be the 'key' of the tag.
	## the 'key' tag is <key>Name</key>, the key attibute is 'Name'.
	## he says it would have been better if they weren't named the same thing.

## When the function is used:
	## for child in dictionary -- ie any of the items (tags) in the dict
		## found is false, so skips 'if found : return child.text'
		## then asks if child tag is 'key'  and if child text is key.
			## eg. child tag = <key>Name</key>, and child text = Name. then found turns to true.
		## so the function is still on the same tag and runs through another iteration of the for loop.
		## but this time found = True.
			## this executes: if found : return child.text
	## rememer return exits the function (def lookup(d,key))
	## if not found then return None -- a very pythonic way of doing things.


stuff = ET.parse(fhand)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entry in all:
	if ( lookup(entry, 'Track ID') is None ) : continue

	name = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')
	count = lookup(entry, 'Play Count')
	rating = lookup(entry, 'Rating')
	length = lookup(entry, 'Total Time')

	if name is None or artist is None or album is None or genre is None: 
		continue

	print name, artist, album, genre, count, rating, length

	cur.execute('''INSERT OR IGNORE INTO Artist (name) 
		VALUES ( ? )''', ( artist, ) )
	cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
	artist_id = cur.fetchone()[0]

## insert artist if it isn't there already or ignore artist if it is already there.

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
		VALUES ( ?, ? )''', ( album, artist_id ) )
	cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
	album_id = cur.fetchone()[0]

## Copy above but for Genre

	cur.execute('''INSERT OR IGNORE INTO Genre (name) 
		VALUES ( ? )''', ( genre, ) )
	cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
	genre_id = cur.fetchone()[0]

##add genre to the insert statement, Values ?, and tuple.

	cur.execute('''INSERT OR REPLACE INTO Track
		(title, album_id, genre_id, len, rating, count) 
		VALUES ( ?, ?, ?, ?, ?, ? )''', 
		( name, album_id, genre_id, length, rating, count ) )

	conn.commit()


###############################################
###############################################
###############################################


#### Chuck tutorial example - Roster data into many-to-many Tables

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup 
## executescript() returns None as it does not save any results in the cursor.
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

## fname = raw_input('Enter file name: ')
## if ( len(fname) < 1 ) : fname = 'roster_data.json'

url = 'http://www.pythonlearn.com/code/roster/roster_data.json'
fhand = urllib.urlopen(url)

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fhand).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];

    print name, title

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id) VALUES ( ?, ? )''', 
        ( user_id, course_id ) )

    conn.commit()


###############################################
###############################################
###############################################


#### Exercise Chuck -- Many Students in Many Courses into Database
	
# Not much change to the file:

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup 
## executescript() returns None as it does not save any results in the cursor.
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

#url = 'http://www.pythonlearn.com/code/roster/roster_data.json'
#fhand = urllib.urlopen(url)

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

	name = entry[0];
	title = entry[1]
	role = entry[2];

	print name, title, role

	cur.execute('''INSERT OR IGNORE INTO User (name) 
		VALUES ( ? )''', ( name, ) )
	cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
	user_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Course (title) 
		VALUES ( ? )''', ( title, ) )
	cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
	course_id = cur.fetchone()[0]

	cur.execute('''INSERT OR REPLACE INTO Member
		(user_id, course_id, role) VALUES ( ?, ?, ? )''', 
		( user_id, course_id, role ) )

	conn.commit()


cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
	User JOIN Member JOIN Course 
	ON User.id = Member.user_id AND Member.course_id = Course.id
	ORDER BY X''')

hex_id = cur.fetchone()[0]
print hex_id











########################################################################################################
########################################################################################################
########################################################################################################
#############################             ##################################
########################################################################################################
########################################################################################################
########################################################################################################

###############################################################################################
###############################################################################################
###############################################################################################

#### Chapter 15 : Visualizing data ####

# So far we have been learning the Python language and then learning how to use
# Python, the network, and databases to manipulate data.
# In this chapter, we take a look at three complete applications that bring all of these
# things together to manage and visualize data. You might use these applications as
# sample code to help get you started in solving a real-world problem.
# Each of the applications is a ZIP file that you can download and extract onto your
# computer and execute.

## 15.1 Building a Google map from geocoded data

# In this project, we are using the Google geocoding API to clean up some userentered
# geographic locations of university names and then placing the data on a
# Google map.

# To get started, download the application from:
# www.py4inf.com/code/geodata.zip

# The first problem to solve is that the free Google geocoding API is rate-limited to
# a certain number of requests per day. If you have a lot of data, you might need to
# stop and restart the lookup process several times. So we break the problem into
# two phases.

# In the first phase we take our input “survey” data in the file where.data and read
# it one line at a time, and retrieve the geocoded information from Google and store
# it in a database geodata.sqlite. Before we use the geocoding API for each userentered
# location, we simply check to see if we already have the data for that particular
# line of input. The database is functioning as a local “cache” of our geocoding
# data to make sure we never ask Google for the same data twice.

# You can restart the process at any time by removing the file geodata.sqlite.

# Run the geoload.py program. This program will read the input lines in
# where.data and for each line check to see if it is already in the database. If we
# don’t have the data for the location, it will call the geocoding API to retrieve the
# data and store it in the database.

# The first five locations are already in the database and so they are skipped. The
# program scans to the point where it finds new locations and starts retrieving them.

# The geoload.py program can be stopped at any time, and there is a counter that
# you can use to limit the number of calls to the geocoding API for each run. Given
# that the where.data only has a few hundred data items, you should not run into
# the daily rate limit, but if you had more data it might take several runs over several
# days to get your database to have all of the geocoded data for your input.

# Once you have some data loaded into geodata.sqlite, you can visualize the data
# using the geodump.py program. This program reads the database and writes the
# file where.js with the location, latitude, and longitude in the form of executable
# JavaScript code.


# The file where.html consists of HTML and JavaScript to visualize a Google map.
# It reads the most recent data in where.js to get the data to be visualized. Here is
# the format of the where.js file:

myData = [
[42.3396998,-71.08975, 'Northeastern Uni ... Boston, MA 02115'],
[40.6963857,-89.6160811, 'Bradley University, ... Peoria, IL 61625, USA'],
[32.7775,35.0216667, 'Technion, Viazman 87, Kesalsaba, 32000, Israel'],
...
];

# This is a JavaScript variable that contains a list of lists. The syntax for JavaScript
# list constants is very similar to Python, so the syntax should be familiar to you.
# Simply open where.html in a browser to see the locations. You can hover over
# each map pin to find the location that the geocoding API returned for the userentered
# input. If you cannot see any data when you open the where.html file, you
# might want to check the JavaScript or developer console for your browser.


###############################################################################################
###############################################################################################
###############################################################################################

## 15.2 Visualizing networks and interconnections

# In this application, we will perform some of the functions of a search engine.
# We will first spider a small subset of the web and run a simplified version of the
# Google page rank algorithm to determine which pages are most highly connected,
# and then visualize the page rank and connectivity of our small corner of the web.

# We will use the D3 JavaScript visualization library http://d3js.org/ to produce
# the visualization output.
# You can download and extract this application from:
# www.py4inf.com/code/pagerank.zip


# The first program (spider.py) program crawls a web site and pulls a series of
# pages into the database (spider.sqlite), recording the links between pages. You
# can restart the process at any time by removing the spider.sqlite file and rerunning
# spider.py.

	Enter web url or enter: http://www.dr-chuck.com/
	['http://www.dr-chuck.com']
	How many pages:2
	1 http://www.dr-chuck.com/ 12
	2 http://www.dr-chuck.com/csev-blog/ 57
	How many pages:

# In this sample run, we told it to crawl a website and retrieve two pages. If you
# restart the program and tell it to crawl more pages, it will not re-crawl any pages
# already in the database. Upon restart it goes to a random non-crawled page and
# starts there. So each successive run of spider.py is additive.

	Enter web url or enter: http://www.dr-chuck.com/
	['http://www.dr-chuck.com']
	How many pages:3
	3 http://www.dr-chuck.com/csev-blog 57
	4 http://www.dr-chuck.com/dr-chuck/resume/speaking.htm 1
	5 http://www.dr-chuck.com/dr-chuck/resume/index.htm 13
	How many pages:

# You can have multiple starting points in the same database—within the program,
# these are called “webs”. The spider chooses randomly amongst all non-visited
# links across all the webs as the next page to spider.
# If you want to dump the contents of the spider.sqlite file, you can run spdump.py
# as follows:
	(5, None, 1.0, 3, u'http://www.dr-chuck.com/csev-blog')
	(3, None, 1.0, 4, u'http://www.dr-chuck.com/dr-chuck/resume/speaking.htm')
	(1, None, 1.0, 2, u'http://www.dr-chuck.com/csev-blog/')
	(1, None, 1.0, 5, u'http://www.dr-chuck.com/dr-chuck/resume/index.htm')
	4 rows.

# This shows the number of incoming links, the old page rank, the new page rank,
# the id of the page, and the url of the page. The spdump.py program only shows
# pages that have at least one incoming link to them.
# Once you have a few pages in the database, you can run page rank on the pages
# using the sprank.py program. You simply tell it how many page rank iterations to
# run.
	How many iterations:2
	1 0.546848992536
	2 0.226714939664
	[(1, 0.559), (2, 0.659), (3, 0.985), (4, 2.135), (5, 0.659)]
	You can dump the database again to see that page rank has been updated:
	(5, 1.0, 0.985, 3, u'http://www.dr-chuck.com/csev-blog')
	(3, 1.0, 2.135, 4, u'http://www.dr-chuck.com/dr-chuck/resume/speaking.htm')
	(1, 1.0, 0.659, 2, u'http://www.dr-chuck.com/csev-blog/')
	(1, 1.0, 0.659, 5, u'http://www.dr-chuck.com/dr-chuck/resume/index.htm')
	4 rows.

# You can run sprank.py as many times as you like and it will simply refine the
# page rank each time you run it. You can even run sprank.py a few times and then
# go spider a few more pages sith spider.py and then run sprank.py to reconverge
# the page rank values. A search engine usually runs both the crawling and ranking
# programs all the time.
# If you want to restart the page rank calculations without respidering the web pages,
# you can use spreset.py and then restart sprank.py.

	How many iterations:50
	1 0.546848992536
	2 0.226714939664
	3 0.0659516187242
	4 0.0244199333
	5 0.0102096489546
	6 0.00610244329379
	...
	42 0.000109076928206
	43 9.91987599002e-05
	44 9.02151706798e-05
	45 8.20451504471e-05
	46 7.46150183837e-05
	47 6.7857770908e-05
	48 6.17124694224e-05
	49 5.61236959327e-05
	50 5.10410499467e-05
	[(512, 0.0296), (1, 12.79), (2, 28.93), (3, 6.808), (4, 13.46)]

# For each iteration of the page rank algorithm it prints the average change in page
# rank per page. The network initially is quite unbalanced and so the individual
# page rank values change wildly between iterations. But in a few short iterations,
# the page rank converges. You should run prank.py long enough that the page rank
# values converge.

# If you want to visualize the current top pages in terms of page rank, run spjson.py
# to read the database and write the data for the most highly linked pages in JSON
# format to be viewed in a web browser.

	Creating JSON output on spider.json...
	How many nodes? 30
	Open force.html in a browser to view the visualization

# You can view this data by opening the file force.html in your web browser. This
# shows an automatic layout of the nodes and links. You can click and drag any
# node and you can also double-click on a node to find the URL that is represented
# by the node.

# If you rerun the other utilities, rerun spjson.py and press refresh in the browser to
# get the new data from spider.json.

###############################################################################################
###############################################################################################
###############################################################################################

## 15.3 Visualizing mail data

# Up to this point in the book, you have become quite familiar with our mboxshort.txt
# and mbox.txt data files. Now it is time to take our analysis of email data
# to the next level.

# In the real world, sometimes you have to pull down mail data from servers. That
# might take quite some time and the data might be inconsistent, error-filled, and
# need a lot of cleanup or adjustment. In this section, we work with an application
# that is the most complex so far and pull down nearly a gigabyte of data and
# visualize it.

# You can download this application from:
	# www.py4inf.com/code/gmane.zip

# We will be using data from a free email list archiving service called www.gmane.
# org. This service is very popular with open source projects because it provides a
# nice searchable archive of their email activity. They also have a very liberal policy
# regarding accessing their data through their API. They have no rate limits, but ask
# that you don’t overload their service and take only the data you need. You can
# read gmane’s terms and conditions at this page:
	# http://gmane.org/export.php

	# It is very important that you make use of the gmane.org data responsibly by adding
	# delays to your access of their services and spreading long-running jobs over a
	# longer period of time. Do not abuse this free service and ruin it for the rest of us.

# When the Sakai email data was spidered using this software, it produced nearly
# a Gigabyte of data and took a number of runs on several days. The file
# README.txt in the above ZIP may have instructions as to how you can download
# a pre-spidered copy of the content.sqlite file for a majority of the Sakai email
# corpus so you don’t have to spider for five days just to run the programs. If you
# download the pre-spidered content, you should still run the spidering process to
# catch up with more recent messages.

# The first step is to spider the gmane repository. The base URL is hard-coded in the
# gmane.py and is hard-coded to the Sakai developer list. You can spider another
# repository by changing that base url. Make sure to delete the content.sqlite file if
# you switch the base url.

# The gmane.py file operates as a responsible caching spider in that it runs slowly
# and retrieves one mail message per second so as to avoid getting throttled by
# gmane. It stores all of its data in a database and can be interrupted and restarted
# as often as needed. It may take many hours to pull all the data down. So you may
# need to restart several times.

# Here is a run of gmane.py retrieving the last five messages of the Sakai developer
# list:

	How many messages:10
	http://download.gmane.org/gmane.comp.cms.sakai.devel/51410/51411 9460
	nealcaidin@sakaifoundation.org 2013-04-05 re: [building ...
	http://download.gmane.org/gmane.comp.cms.sakai.devel/51411/51412 3379
	samuelgutierrezjimenez@gmail.com 2013-04-06 re: [building ...
	http://download.gmane.org/gmane.comp.cms.sakai.devel/51412/51413 9903
	da1@vt.edu 2013-04-05 [building sakai] melete 2.9 oracle ...
	http://download.gmane.org/gmane.comp.cms.sakai.devel/51413/51414 349265
	m.shedid@elraed-it.com 2013-04-07 [building sakai] ...
	http://download.gmane.org/gmane.comp.cms.sakai.devel/51414/51415 3481
	samuelgutierrezjimenez@gmail.com 2013-04-07 re: ...
	http://download.gmane.org/gmane.comp.cms.sakai.devel/51415/51416 0
	Does not start with From

# The program scans content.sqlite from one up to the first message number not
# already spidered and starts spidering at that message. It continues spidering until
# it has spidered the desired number of messages or it reaches a page that does not
# appear to be a properly formatted message.

# Sometimes gmane.org is missing a message. Perhaps administrators can delete
# messages or perhaps they get lost. If your spider stops, and it seems it has hit
# a missing message, go into the SQLite Manager and add a row with the missing
# id leaving all the other fields blank and restart gmane.py. This will unstick the
# spidering process and allow it to continue. These empty messages will be ignored
# in the next phase of the process.

# One nice thing is that once you have spidered all of the messages and have them
# in content.sqlite, you can run gmane.py again to get new messages as they are
# sent to the list.

# The content.sqlite data is pretty raw, with an inefficient data model, and not compressed.
# This is intentional as it allows you to look at content.sqlite in the SQLite
# Manager to debug problems with the spidering process. It would be a bad idea to
# run any queries against this database, as they would be quite slow.
 
# The second process is to run the program gmodel.py. This program reads the raw
# data from content.sqlite and produces a cleaned-up and well-modeled version of
# the data in the file index.sqlite. This file will be much smaller (often 10X smaller)
# than content.sqlite because it also compresses the header and body text.

# Each time gmodel.py runs it deletes and rebuilds index.sqlite, allowing you to
# adjust its parameters and edit the mapping tables in content.sqlite to tweak the
# data cleaning process. This is a sample run of gmodel.py. It prints a line out each
# time 250 mail messages are processed so you can see some progress happening,
# as this program may run for a while processing nearly a Gigabyte of mail data.

	Loaded allsenders 1588 and mapping 28 dns mapping 1
	1 2005-12-08T23:34:30-06:00 ggolden22@mac.com
	251 2005-12-22T10:03:20-08:00 tpamsler@ucdavis.edu
	501 2006-01-12T11:17:34-05:00 lance@indiana.edu
	751 2006-01-24T11:13:28-08:00 vrajgopalan@ucmerced.edu
	...

# The gmodel.py program handles a number of data cleaning tasks.

# Domain names are truncated to two levels for .com, .org, .edu, and .net. Other
# domain names are truncated to three levels. So si.umich.edu becomes umich.edu
# and caret.cam.ac.uk becomes cam.ac.uk. Email addresses are also forced to lower
# case, and some of the @gmane.org address like the following

arwhyte-63aXycvo3TyHXe+LvDLADg@public.gmane.org

# are converted to the real address whenever there is a matching real email address
# elsewhere in the message corpus.

# In the content.sqlite database there are two tables that allow you to map both
# domain names and individual email addresses that change over the lifetime of the
# email list. For example, Steve Githens used the following email addresses as he
# changed jobs over the life of the Sakai developer list:

	s-githens@northwestern.edu
	sgithens@cam.ac.uk
	swgithen@mtu.edu

# We can add two entries to the Mapping table in content.sqlite so gmodel.py will
# map all three to one address:

	s-githens@northwestern.edu -> swgithen@mtu.edu
	sgithens@cam.ac.uk -> swgithen@mtu.edu

# You can also make similar entries in the DNSMapping table if there are multiple
# DNS names you want mapped to a single DNS. The following mapping was added
# to the Sakai data:

	iupui.edu -> indiana.edu
	
# so all the accounts from the various Indiana University campuses are tracked together.
# You can rerun the gmodel.py over and over as you look at the data, and add mappings
# to make the data cleaner and cleaner. When you are done, you will have a
# nicely indexed version of the email in index.sqlite. This is the file to use to do
# data analysis. With this file, data analysis will be really quick.
# The first, simplest data analysis is to determine ”who sent the most mail?” and
# ”which organization sent the most mail”? This is done using gbasic.py:

	How many to dump? 5
	Loaded messages= 51330 subjects= 25033 senders= 1584
	Top 5 Email list participants
	steve.swinsburg@gmail.com 2657
	azeckoski@unicon.net 1742
	ieb@tfd.co.uk 1591
	csev@umich.edu 1304
	david.horwitz@uct.ac.za 1184
	Top 5 Email list organizations
	gmail.com 7339
	umich.edu 6243
	uct.ac.za 2451
	indiana.edu 2258
	unicon.net 2055
 	
# Note how much more quickly gbasic.py runs compared to gmane.py or even
# gmodel.py. They are all working on the same data, but gbasic.py is using the
# compressed and normalized data in index.sqlite. If you have a lot of data to manage,
# a multistep process like the one in this application may take a little longer
# to develop, but will save you a lot of time when you really start to explore and
# visualize your data.

# You can produce a simple visualization of the word frequency in the subject lines
# in the file gword.py:

	Range of counts: 33229 129
	Output written to gword.js

# This produces the file gword.js which you can visualize using gword.htm to produce
# a word cloud similar to the one at the beginning of this section.
# A second visualization is produced by gline.py. It computes email participation
# by organizations over time.

	Loaded messages= 51330 subjects= 25033 senders= 1584
	Top 10 Oranizations
	['gmail.com', 'umich.edu', 'uct.ac.za', 'indiana.edu',
	'unicon.net', 'tfd.co.uk', 'berkeley.edu', 'longsight.com',
	'stanford.edu', 'ox.ac.uk']
	Output written to gline.js

# Its output is written to gline.js which is visualized using gline.htm.

## there is a cool graph with date by email domain.

# This is a relatively complex and sophisticated application and has features to do
# some real data retrieval, cleaning, and visualization.



########################################################################################################
########################################################################################################
########################################################################################################
################### Capstone: Retrieving, Processing and visualizing Data       ########################
########################################################################################################
########################################################################################################
########################################################################################################


###############################################################################################
###############################################################################################
###############################################################################################



# This week we will download and run a simple version of the Google PageRank Algorithm. 
# Here is an early paper by Larry Page and Sergy Brin, the founders of Google, 
# that describes their early thoughts about the algorithm:

	# http://infolab.stanford.edu/~backrub/google.html

# We will provide you with sample code and lectures that walk through the sample code:

	# http://www.dr-chuck.net/pythonlearn/code/pagerank.zip

# There is not a lot of new code to write - it is mostly looking at the code and making the code work. 
# You will be able to spider some simple content that we provide and then play with the program 
# to spider some other content. 
# Part of the fun of this assignment is when things go wrong and 
# you figure out how to solve a problem when the program wanders 
# into some data that breaks its retrieval and parsing. 
# So you will get used to starting over with a fresh database and running your web crawl.


###############################################
###############################################
###############################################


#### Exercise Chuck -- Peer Grade: Page Rank

# First you will spider 100 pages from http://python-data.dr-chuck.net/ run the page rank algorithm 
# and take some screen shots. 

# Then you will reset the spider process and spider 100 pages from any other site on the Internet, 
# run the page rank algorithm, and take some screen shots.

# This course uses a third-party tool, Peer Grade: Page Rank, to enhance your learning experience. 
# The tool will reference basic information like your name, email, and Coursera ID.

# Don't take off points for little mistakes. 
# If they seem to have done the assignment give them full credit. 
# Feel free to make suggestions if there are small mistakes. 
# Please keep your comments positive and useful. 

# Sample solution: http://www.dr-chuck.net/pythonlearn/code/pagerank.zip

############

# Steps to run the pagerank project

# Start with spider.py -- it spiders pages. goes to the page and takes all the url links.

# Then use sprank.py -- it ranks the spidered pages. only ranks those which have links. 

# Then use spdump.py -- it prints out the joined data of Pages and Lins.

# Then run spjson.py -- it puts the data into spider.js ready for d3 visualisation.

<<<<<<< Updated upstream
###############################################
###############################################
###############################################


#### Exercise Chuck -- Retrieving GEOData

# Download the code from http://www.pythonlearn.com/code/geodata.zip - 
# then unzip the file and edit where.data to add an address nearby where you live - 
# don't reveal your actual location. Then run the geoload.py to lookup 
# all of the entries in where.data (including the new one) and produce the geodata.sqlite. 
# Then run geodump.py to read the database and produce where.js. 
# Then open where.html to visualize the map. 
# Take screen shots as described below.

# This is a relatively simple assignment. 
# Don't take off points for little mistakes. 
# If they seem to have done the assignment give them full credit. 
# Feel free to make suggestions if there are small mistakes. 
# Please keep your comments positive and useful. 
# If you do not take grading seriously, 
# the instructors may delete your response and you will lose points.


# Screen shot (JPG or PNG - Maximum 1MB) of the geoload.py program running
# Screen shot (JPG or PNG - Maximum 1MB) of the geodump.py program running
# Screen shot (JPG or PNG - Maximum 1MB) of the map zoomed into the location that you added.) of your home page.


## First step run geoload.py

## Second step run geodump.py

## Third step open the where.html file.






########################################################################################################
########################################################################################################
########################################################################################################
#############################       Python for Everybody Capstone      #################################
########################################################################################################
########################################################################################################
########################################################################################################




###############################################################################################
###############################################################################################
###############################################################################################



# Welcome to the Python for Everybody Capstone. 
# We want the capstone to be a different experience than the rest of the courses. 
# Since we are a much smaller course I want to make sure that there is lots of 
# opportunity for student-to-student interactions. 
# We understand that some of you will be in a hurry to finish and that 
# others will want to spend time interacting with the instructional staff and other students. 
# So we have designed the course with only three required peer-graded assignments 
# (Weeks 2, 4, and 6) and three optional presentation-oriented assignments (Weeks 3, 5, and 7).

# A goal of the Capstone is to set up structures to let you learn from each other 
# instead of just making more lectures and assignments. We have done several things to make that work:

# In this course you can paste any code into the forums that you want to discuss with other 
# students about problems you are having. By now we assume you know how to code.
# We have used a Wiki system provided by Coursera to allow you to edit pages 
# and upload your information and share your information with other students. 
# These Wiki pages are visible to other Coursera students, so do not post any personal information here.

# We have built a private presentation system using a technology called WarpWire that allows you 
# to upload presentation videos in a way that is 100% private - 
# the videos can only be seen by those in the class.

# All presentations are optional but everyone is welcome to review, rate, 
# and interact with the presentations and add value to the class.

# In the project/presentation side of the class it is perfectly fine for students 
# to approach a problem as a team and use other technologies like Slack or Github to coordinate their work.

# You can see that a big theme of this Capstone is to get you to contribute to the course. 
# And of course since this is the first time we are using some of this technology and pedagogy, 
# there will be plenty of room for improvement. We will be watching the forums closely and 
# may adjust the course as it progresses based on your comments, issues, and suggestions.

###############################################################################################
###############################################################################################
###############################################################################################

# You won't be surprised to know that I have built new software for this course. 
# We have a partnership with WarpWire that allows us to use their video for education platform. 
# We have built a way for you to record and share presentations with your other students that are 
# 100% private and can only be seen by your fellow students in this class. 
# We think that this a great technology and will have lots of applications 
# in other Coursera courses once we figure things out.

# Since this is the first time we are using this software at scale, 
# we have invited some of the technical support team at WarpWire to join the class 
# so they can monitor the forums and work through any problems that we identify. 
# Of course the errors might be in my gallery software - so we will just figure out 
# which part is broken and get things fixed.

# I made sure that the required parts of the class were using simple, well-proven technology 
# and we will be using the advanced cool technology only in the optional parts of the class.

# So if you have a problem - don't be shy - let us know in the forums.








=======
# Then open force.html from a brownser -- it will use d3 to open the visualisation.
>>>>>>> Stashed changes

############

## Excersise

# A screen shot of the spdump.py running after you have crawled 100 pages from python-data.dr-chuck.net

# A screen shot of the top 25 pages according to page rank that you crawled from python-data.dr-chuck.net visualized using force.html

# A screen shot of the spdump.py running after you have crawled 100 pages from another web site

# A screen shot of the top 25 pages according to page rank that you crawled from the other web site visualized using force.html





























#### 20160512: Readings -> 15   http://do1.dr-chuck.com/py4inf/EN-us/book.pdf

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




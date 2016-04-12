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


 #################################################################
 #################################################################
 ########        Using Python to Access Web Data       ###########
 #################################################################
 #################################################################

## Scrape, Parse and Read Web Data as well as access data using web APIs.
	# Work with HTML, XML, JSON data formats in python.


#### Regluar Expressions ####

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

################################################################

#### 12 Networked Programs ####

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






















































#### 20160407: Readings -> 12   http://do1.dr-chuck.com/py4inf/EN-us/book.pdf

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




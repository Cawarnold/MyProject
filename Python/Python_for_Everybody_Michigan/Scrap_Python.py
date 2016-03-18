#!/usr/bin/env Env3_Python276_Django171_djangoextensions


## Just Scrap stuff

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
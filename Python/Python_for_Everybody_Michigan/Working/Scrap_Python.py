#!/usr/bin/env Env3_Python276_Django171_djangoextensions

## http://www.pythonlearn.com/book_009.pdf

import urllib

# url = 'http://www.pythonlearn.com/code/mbox.txt'
url = 'http://www.pythonlearn.com/code/mbox-short.txt'

fhand = urllib.urlopen(url)

dom_list = list()
domain_dict = dict()

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From': continue
	domain = words[1].split('@')[1]
	print domain
	dom_list.append(words[1].split('@')[1])
	for item in dom_list:
		if item not in domain_dict:
			domain_dict[item] = 1
		else:
			domain_dict[item] = domain_dict[item] + 1

print(domain_dict)



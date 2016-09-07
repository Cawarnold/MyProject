#!/usr/bin/env 



####### Connect to SQL Server #########

payload = {
	'v': '1'		# Version
	, 'format': 'json'
	, 'useragent': 'Mozilla'
	, 'action': 'employers'
	, 'q': 'pharmaceutical'		# Query phrase
	, 'l': 'london'				# Location,  city, state, or country
	, 'country': 'UK'			# Country
}


print(payload['q'])
print(payload['l'])
print(payload['country'])

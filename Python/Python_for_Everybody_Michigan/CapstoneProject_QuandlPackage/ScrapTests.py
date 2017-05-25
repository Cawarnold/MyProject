#!/usr/bin/env Env_Python34_Quandl289



####### Connect to SQL Server #########

import pyodbc
import codecs

cnxn = pyodbc.connect('')

cursor = cnxn.cursor()



#### Query the DB ####

cursor.execute("")
row = cursor.fetchone()
while row is not None:
	if row > 0 : print('CONNECTION WORKS')
	row = cursor.fetchone()


#### Append each row of data to a line in a file ####

# Opens file, truncates file (with 'w+').

filepath = ""
fhand = codecs.open(filepath, "w+", "utf-8")

cursor.execute("select distinct rn.RN_ID,rn.OrgType,rn.JobClass,rn.JobType,rn.JobLevel,rn.JobFunction,rn.JobTitle from [vMDB_Test].dbo.[RN_NormalisedRoles_ID]")

count = 0
row = cursor.fetchone()
while row is not None:
	count = count + 1

print(count)



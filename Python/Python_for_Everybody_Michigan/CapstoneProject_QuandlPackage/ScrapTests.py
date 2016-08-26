#!/usr/bin/env Env_Python34_Quandl289



####### Connect to SQL Server #########

import pyodbc
import codecs

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LDNSQLDEV03.PRACTICALLAW.COM;DATABASE=vMDB;UID=TEN\U6030064;Trusted_connection=yes')

cursor = cnxn.cursor()



#### Query the DB ####

cursor.execute("select top 1 * from [vMDB_Test].dbo.[RN_NormalisedRoles_ID]")
row = cursor.fetchone()
while row is not None:
	if row > 0 : print('CONNECTION WORKS')
	row = cursor.fetchone()


#### Append each row of data to a line in a file ####

# Opens file, truncates file (with 'w+').

filepath = "C:/Users/U6030064/Documents/MyThomsonReuters_20150601/Christian_MarketingProjects/CRS_ContractReportingSystem_CDB_20150827/WebsubsMigration/Websubs_20160804/WRPWebsubs_JF05_AddressBack_20160816/JF_Websubs_Data_ContactDetails_TextFile_CA01.txt"
fhand = codecs.open(filepath, "w+", "utf-8")

cursor.execute("select distinct rn.RN_ID,rn.OrgType,rn.JobClass,rn.JobType,rn.JobLevel,rn.JobFunction,rn.JobTitle from [vMDB_Test].dbo.[RN_NormalisedRoles_ID]")

count = 0
row = cursor.fetchone()
while row is not None:
	count = count + 1

print(count)



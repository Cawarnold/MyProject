#!/usr/bin/env 
# -*- coding: utf-8 -*-


import sys			# sys.exit()
import os

import csv

import numpy as np
import pandas as pd
import sqlite3
import re
import datetime


#### Calculate market rate

## sql version

## Python 2.7.11 |Anaconda 4.0.0 (x86_64)|

#### Questions ####
# Do i need to consider a market.csv file where a name appears twice?
# Do i need to validate the market.csv file, eg. negative rate, zero amount available?
# Do I need to store all the Borrowers in a database of their own, with the quote / outcome?


## open file
if len(sys.argv) > 1:
	market_file = sys.argv[1]
	#print(market_file)
else:
	market_file = os.path.expanduser("~/Desktop/Zopa_Test/market.csv")

if len(sys.argv) > 2:
	total_to_borrow = int(sys.argv[2])
	#print(total_to_borrow)
else:
	total_to_borrow = 1000
#print(total_to_borrow)

#### Validate the arguements
# borrowing amount must be a multiple of 100
if not (total_to_borrow % 100)==0:
	print('Please enter a borrowing amount in multipes of 100.')
	sys.exit()

# borrowing amount must be between 1000 and 150000.
if not (total_to_borrow >= 1000 and total_to_borrow <= 150000):
	print("Please enter a borrowing amount the is between £1000 and £150000.")
	sys.exit()



#### Connect to (or Create) Database for the job postings from Indeed ####

conn = sqlite3.connect('p2p_database.sqlite')
#conn.text_factory = str
cur = conn.cursor()


#### Create Tables ####

## Drop tables if need to restart
cur.execute('''DROP TABLE IF EXISTS Lenders_RateAmount''')
cur.execute('''DROP TABLE IF EXISTS Borrower_Rates''')


## Create tables Lenders_RateAmount 
try:
	cur.execute('''CREATE TABLE IF NOT EXISTS Lenders_RateAmount
		(name TEXT UNIQUE
		, rate DECIMAL(10,2) 
		, amount_available INTEGER
		, total_owed DECIMAL(10,2)
		, month_owed DECIMAL(10,2)
		)''')
except:
	print('Lenders_RateAmount not created')

## Create tables Borrower_Rates
try:
	cur.execute('''CREATE TABLE IF NOT EXISTS Borrower_Rates
		(option_number INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
		, lend_amount INTEGER
		, borrow_subsetsum TEXT
		, rate DECIMAL(10,1) 
		, total_repayment DECIMAL(10,2) 
		)''')
except:
	print('Borrower_Rates not created')

## test Lenders_RateAmount
try:
	cur.execute('''INSERT INTO Lenders_RateAmount (name, rate, amount_available) VALUES ('Example', '6.4', '140')''')
	conn.commit()
	cur.execute('''SELECT name FROM Lenders_RateAmount''')
	if cur.fetchone()[0] == 'Example':
		 a = 'passed'
except:
	print('test insert failed')

try:
	cur.execute('''DELETE FROM Lenders_RateAmount''')
	cur.execute('''DELETE FROM SQLITE_SEQUENCE WHERE name="Lenders_RateAmount"''')
except:
	print('truncation failed')

## test Borrower_Rates
try:
	cur.execute('''INSERT INTO Borrower_Rates (lend_amount, borrow_subsetsum, rate) VALUES ('1000', '[540,460]', '7.0')''')
	conn.commit()
	cur.execute('''SELECT lend_amount FROM Borrower_Rates''')
	if cur.fetchone()[0] == '1000':
		 a = 'passed'
except:
	print('test insert failed')

try:
	cur.execute('''DELETE FROM Borrower_Rates''')
	cur.execute('''DELETE FROM SQLITE_SEQUENCE WHERE name="Borrower_Rates"''')
except:
	print('truncation failed')

#DECIMAL(10,2)


#### Import Lenders data ####

with open(market_file) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=",")
	next(readCSV, None)
	for row in readCSV:
		try:
			cur.execute('''INSERT INTO Lenders_RateAmount (name, rate, amount_available) VALUES (?, ?, ?)''',(str(row[0]),float(row[1]),int(row[2])))
			#print('inserting details into table.')
			conn.commit()
		except:
			#print('Lender already in database')
			continue

	conn.commit()


#for row in cur.execute('''SELECT * FROM Lenders_RateAmount'''):
#	print(cur.fetchall())


#### Compound Interest ####

# A = P(1+r/n)^(nt)

# A = the future value of the investment/loan, including interest
# P = the principal investment amount (the initial deposit or loan amount)
# r = the period interest rate (decimal)
# n = the number of times that interest is compounded per time period
# t = the number of time periods the money is invested or borrowed for

months_of_loan = 36
n = 12
t = months_of_loan / n

def calc_total_owed(principal,rate,n,t):
	return principal*(1+(rate/n))**(n*t)

def calc_month_owed(total_owed,months):
	return total_owed/months

def calc_rate_borrow(total_repayment,total_to_borrow,n,months_of_loan):
	#return (((total_repayment / total_to_borrow) ** (1/(n*t)) -1)* n)*100
	return (((total_repayment/total_to_borrow)**(float(n)/months_of_loan))-1)*100



cur.execute('''SELECT * FROM Lenders_RateAmount''')
lenders = cur.fetchall()

for i in lenders:
	name = i[0]
	rate = i[1]
	principle = float(i[2])
	total_owed = calc_total_owed(principle,rate,n,t)
	total_owed = ("%.2f" % total_owed)
	month_owed = calc_month_owed(float(total_owed),months_of_loan)
	month_owed = ("%.2f" % month_owed)
	cur.execute('''UPDATE Lenders_RateAmount SET total_owed = ?, month_owed = ? WHERE name = ? ''', (total_owed,month_owed,name))
	conn.commit()

cur.execute('''SELECT * FROM Lenders_RateAmount''')
#print(cur.fetchall())


#### Subset Sum ####

options = []

def subset_sum(numbers, target, partial=[]):
	s = sum(partial)

	# check if the partial sum is equals to target
	if s == target:
		options.append(partial)
	if s >= target:
		return  # if we reach the number why bother to continue

	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers[i+1:]
		subset_sum(remaining, target, partial + [n]) 


cur.execute('''SELECT amount_available FROM Lenders_RateAmount''')
numbers = []
for i in cur.fetchall():
	numbers.append(i[:][0])
#print(numbers)

subset_sum(numbers,total_to_borrow)
if len(options) < 1:
	print("Unfortunately it is not possible to provide you with a quote at this time.")
	sys.exit()
#print(options)


for subsets in options:
	borrow_subsetsum = subsets
	try:
		cur.execute('''INSERT INTO Borrower_Rates (lend_amount, borrow_subsetsum) VALUES (?,?)''',(total_to_borrow,str(borrow_subsetsum)))
		#print('inserting details into table.')
		conn.commit()
	except:
		print('insert failed')

cur.execute('''SELECT * FROM Borrower_Rates''')
#print(cur.fetchall())


## Calculate rate from lender options
# Borrower_Rates (lend_amount, borrow_subsetsum, rate)
# Lenders_RateAmount total_owed

counter = 1
for subsets in options:
	#print(subsets)
	#print(counter)

	total_repayment = 0.0
	for i in subsets:
		#print(i)
		cur.execute('''SELECT total_owed FROM Lenders_RateAmount WHERE amount_available = ?''',(str(i), ))
		repayment = cur.fetchone()[:][0]
		total_repayment = total_repayment + repayment
		#print(total_repayment)
		try:
			cur.execute('''UPDATE Borrower_Rates SET total_repayment = ? WHERE option_number = ?''', (total_repayment, counter, ))
			conn.commit()
		except:
			print('update failed')
	rate = calc_rate_borrow(total_repayment,total_to_borrow,n,months_of_loan)
	rate = ("%.1f" % rate)
	#print(rate)
	try:
		cur.execute('''UPDATE Borrower_Rates SET rate = ? WHERE option_number = ?''', (rate, counter, ))
		conn.commit()
	except:
		print('update failed')	
	#rate = (((1233.08/1000)**(1.0/3.0))-1)*100
	#print(rate)

	counter = counter + 1

## Choose option with lowest rate / lowest repayment

cur.execute('''SELECT min(rate) FROM Borrower_Rates''')
lowest_rate = cur.fetchone()[0]
cur.execute('''SELECT option_number, lend_amount, rate, total_repayment FROM Borrower_Rates WHERE rate = ?''',(lowest_rate, ))

for item in cur.fetchall():
	lowest_option = item[0]
	lowest_rate = item[2]
	lowest_total_repayment = item[3]

lowest_monthly_repayment = ("%.2f" % (lowest_total_repayment / months_of_loan))

#print "sum(%s)=%s" % (partial, target)
print('Requested amount: £%s') % (total_to_borrow)
print('Rate: %s%%') % (lowest_rate)
print('Monthly Repayment: £%s') % (lowest_monthly_repayment)
print('Total repayment: £%s') % (lowest_total_repayment)


cur.close()

		





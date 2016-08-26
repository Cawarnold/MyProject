#!/usr/bin/env Env_Python34_Quandl289

import numpy as np
import pandas as pd
import sqlite3
import Quandl
from hidden import quandl_ticker_get_df 
import datetime
import sys

# activate Env_Python34_Quandl289


#### Connect to (or Create) Database for stocks ####

conn = sqlite3.connect('my_lse_database.sqlite')
conn.text_factory = str
cur = conn.cursor()
####


#### Create Stock Price Table ####

## Drop tables if need to restart
#cur.execute('DROP TABLE IF EXISTS Stock_EOD_Prices ')
cur.execute('DROP TABLE IF EXISTS My_Current_Stocks ')

## Create tables
cur.execute('''CREATE TABLE IF NOT EXISTS Stock_EOD_Prices
	(Date DATE, Stock_Symbol TEXT, Price_EOD TEXT
	, UNIQUE(Date, Stock_Symbol) ON CONFLICT REPLACE)''')

cur.execute('''CREATE TABLE IF NOT EXISTS My_Current_Stocks
	(Stock_Symbol TEXT, Number_of_Shares INT)''')
####


#### Import list of my current Stocks and Shares ####

Example_Stocks_and_Shares = [
	# in the format: ['Stocks', 'Shares'],
['AGM'	,'314'],
['SEPU'	,'1184'],
['TED'	,'40'],
['LLOY'	,'1500'],
['BARC'	,'372'],
['ABC'	,'81'],
['AGM'	,'416'],
['BARC'	,'987'],
['EMIS'	,'49'],
['GLEN'	,'278'],
['MONY'	,'400'],
['MONI'	,'38655'],
['RMV'	,'27'],
['TRIG'	,'498'],
['WPG'	,'387'],
]

for item in Example_Stocks_and_Shares:
	# extract the stock and the number of shares
	stock = item[0]
	share = item[1]

	# insert symbol and number of shares into My_Current_Stocks database
	cur.execute('''INSERT OR IGNORE INTO My_Current_Stocks (Stock_Symbol, Number_of_Shares) 
		VALUES ( ?, ? )''', ( stock, share, ) )
	conn.commit()
####




#### Check if Stock Price table is up to date, if so exit program ####
cur.execute('''select distinct Date from Stock_EOD_Prices''')
dates = cur.fetchall()


## Issue: need to account for Stock Exchange working days, mon to fri. not sat or sun.
if len(dates) > 0:
	latest_stockprice_date = dates[-1][0] # Need last element dates[-1]
	yesterdays_date = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(1),'%Y-%m-%d')
	
	if latest_stockprice_date == yesterdays_date:
		print("Yesterday's,",latest_stockprice_date,", data already in table.")
		print("Exiting before sending request to Quandl.")
		sys.exit() 
####


# select distinct stock symbols from My_Current_Stocks database
cur.execute('''select distinct Stock_Symbol from My_Current_Stocks''')
list_stocks = cur.fetchall()

for item in list_stocks:
	stock_df = pd.DataFrame()
	# get ticker for quandl input
	quandl_ticker = "LSE/"+str(item[0])
	print(quandl_ticker)

	# get pandas dataframe of stock
	stock_df = quandl_ticker_get_df(quandl_ticker)

	#if stock_df.empty:
	#	print('Quandl DataFrame is empty!')
	#else:
	#	print('Quandl DataFrame is not empty.')

	# get yesterday's date and stock price for each current stock
	yesterday_date = stock_df.tail(1).index[0].date() 	## Gives the date of the price -- yesterdays date.
	yesterday_price = stock_df.tail(1).iloc[0,0] 	## Gives the yesterdays price

	# insert date, stock symbol and price into Stock_EOD_Prices database
	cur.execute('''INSERT OR IGNORE INTO Stock_EOD_Prices (Date, Stock_Symbol, Price_EOD) 
		VALUES ( ?, ?, ? )''', ( yesterday_date, item[0], yesterday_price, ) )
	conn.commit()


cur.close()


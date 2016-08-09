#!/usr/bin/env Env_Python34_Quandl289

import numpy as np
import pandas as pd
import sqlite3
import Quandl

# activate Env_Python34_Quandl289


#### Create Database for stocks ####

conn = sqlite3.connect('my_lse_database.sqlite')
conn.text_factory = str
cur = conn.cursor()

## Create Stock Price Table

cur.execute('DROP TABLE IF EXISTS Stock_EOD_Prices ')

cur.execute('''CREATE TABLE IF NOT EXISTS Stock_EOD_Prices
	(Date date unique, Stock_Symbol TEXT UNIQUE, Price_EOD TEXT)''')


cur.execute('DROP TABLE IF EXISTS My_Current_Stocks ')

cur.execute('''CREATE TABLE IF NOT EXISTS My_Current_Stocks
	(Stock_Symbol TEXT UNIQUE, Number_of_Shares int)''')


## List of my current Stocks and Shares

Example_Stocks_and_Shares = [
['Stocks', 'Shares'],
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


# select distinct stock symbols from My_Current_Stocks database
cur.execute('''select distinct Stock_Symbol from My_Current_Stocks''')
list_stocks = cur.fetchall()

for item in list_stocks:
	# get ticker for quandl input
	quandl_ticker = "LSE/"+str(item[0])

	# get pandas dataframe of stock
	stock_df = Quandl.get(quandl_ticker)

	# get yesterday's date and stock price for each current stock
	yesterday_date = stock_df.tail(1).index[0].date() 	## Gives the date of the price -- yesterdays date.
	yesterday_price = stock_df.tail(1).iloc[0,0] 	## Gives the yesterdays price

	# insert date, stock symbol and price into Stock_EOD_Prices database
	cur.execute('''INSERT OR IGNORE INTO Stock_EOD_Prices (Date, Stock_Symbol, Price_EOD) 
		VALUES ( ?, ?, ? )''', ( yesterday_date, item[0], yesterday_price, ) )
	conn.commit()

cur.close()




'''

# Create function that gets data from Quandl

My_Current_Stock_Symbols = [
	'BARC' #Barclays
	,'LLOY' #Lloyds
	,'MONI' #Monitise
	,'MONY' #Moneysupermarket
	,'WPG' #World Pay Group
	,'TED' #Ted Baker
	,'TCM' #Telit Communications
	,'RMV' #Rightmove
	,'GLEN' #Glencore
	,'TRIG' #Renewables Infrastructure Group
	,'EMIS' #EMIS 	#Electronic Patient Record System
	,'ABC' #Abcam 	#Anitbodies research and kits
	,'SEPU' #Sepura 	#Critical radio communications
	]

# print(type(My_Current_Stock_Symbols))

lloyd_stock = My_Current_Stock_Symbols[1]
quandl_ticker = "LSE/"+str(lloyd_stock)
lloyd_df = Quandl.get(quandl_ticker)


#### Get last days Stock value and date

	## print(lloyd_df.iloc[0,0]) #iloc[rows,cols]


#print(lloyd_df['Price'])

yesterday_date = lloyd_df.tail(1).index[0].date() 	## Gives the date of the price -- yesterdays date.
yesterday_price = lloyd_df.tail(1).iloc[0,0] 	## Gives the yesterdays price
'''
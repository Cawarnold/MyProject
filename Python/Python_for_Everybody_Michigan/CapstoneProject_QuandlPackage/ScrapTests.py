#!/usr/bin/env Env_Python34_Quandl289

import numpy as np
import pandas as pd
import sqlite3
import Quandl

# activate Env_Python34_Quandl289


conn = sqlite3.connect('my_lse_database.sqlite')
conn.text_factory = str
cur = conn.cursor()

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
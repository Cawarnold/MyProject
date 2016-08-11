#!/usr/bin/env Env_Python34_Quandl289

#### Quandl 2.8.9

import numpy as np
import pandas as pd
import sqlite3
import Quandl
from hidden import quandl_ticker_get_df 
import datetime
import sys

# activate Env_Python34_Quandl289

conn = sqlite3.connect('my_lse_database.sqlite')
conn.text_factory = str
cur = conn.cursor()

# Check if Stock Price table is up to date
cur.execute('''select distinct Date from Stock_EOD_Prices''')
dates = cur.fetchall()

latest_stockprice_date = dates[0][0]
yesterdays_date = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(1),'%Y-%m-%d')

if latest_stockprice_date == yesterdays_date:
	print("Yesterday's data already in table")
	sys.exit()

print("Stuff")


cur.close()
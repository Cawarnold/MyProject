#### Where I'll put my keys which will not be uploaded to Github (Hopefully) ####

## my key
import numpy as np
import pandas as pd
import sqlite3
import Quandl

def quandl_ticker_get_df(quandl_ticker):
	return Quandl.get(quandl_ticker, authtoken='1bXF4N7MdecopWUkMvzn')
	

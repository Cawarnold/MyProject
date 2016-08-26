#!/usr/bin/env Env_Python34_Quandl289

#### Setting the python Environment ####
# python 3.4
# quandl 2.8.9

# conda create --name Env_Python34_Quandl289 python=3.4 quandl=2.8.9
# activate Env_Python34_Quandl289
# deactivate 
# conda remove --name Env_Python34_Quandl289 --all

# or conda install -c anaconda quandl=2.8.9


#### Testing the Quandl Python Library Environment ####

import numpy as np
import pandas as pd
import Quandl

#import hidden.py


mydata = Quandl.get("LSE/BARC")


if len(mydata.head(1))>0:
	print("Imported Python 3.4")
	print("Imported Quandl 2.8.9")
	print("Quandl API data not empty")

#print(type(mydata))


'''
#Calls the daily changes in facebooks closing price for 2016 untiil aug.
data = Quandl.get("WIKI/FB.11", start_date="2016-01-01", end_date="2016-08-01", collapse="daily", transformation="diff")

print(data.head(100))
'''

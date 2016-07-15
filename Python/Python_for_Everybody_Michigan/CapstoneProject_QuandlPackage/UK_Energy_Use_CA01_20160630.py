#!/usr/bin/env Env_Python2711_Quandl289

# python 2.7.6
# quandl 2.8.9

# conda create --name Env_Python2711_Quandl289 python=2.7.11 quandl=2.8.9
# source activate Env_Python2711_Quandl289
# source deactivate 
# conda remove --name Env_Python2711_Quandl289 --all

# or conda install -c anaconda quandl=2.8.9

import numpy as np
import pandas as pd
import Quandl

#import hidden.py

mydata = Quandl.get("EIA/IES_2_2_12_GBR")

print type(mydata)


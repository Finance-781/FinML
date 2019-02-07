# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:17:38 2017

@author: Christopher
"""
#Preamp
#%%
import numpy as np

import pandas as pd
pd.options.display.float_format = '{:,.5f}'.format

import matplotlib.pyplot as plt
plt.clf
plt.cla
plt.close('all')

from matplotlib import style
style.use('seaborn-whitegrid')
#print(plt.style.available)
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import matplotlib.mlab as mlab

import statsmodels.api as sm
from matplotlib.ticker import FuncFormatter
import datetime as dt
import statsmodels.tools

from scipy import stats
import time
#%%
def valuecalculator (inputlist):
    "You'll need a Dataframe and the values to be in relative form \n Insert initial portfolio value"
    a = 10000
    print("'The portfolio's initial value: ", a)
    Value = [int(a)]
    for i in range (0, len(inputlist)):
        Value.append(Value[i]*inputlist[i])
    return Value

def division(inputlist):
    reindex = inputlist.index
    reindex = reindex[1:]
    Copyportfolio = inputlist.copy (deep = True)
    
    Copyportfolio = Copyportfolio.shift(-1) / Copyportfolio
    Copyportfolio.reset_index(drop = True, inplace = True)
    Copyportfolio = Copyportfolio [:-1]
    Copyportfolio.set_index(reindex, inplace = True)
    
    return Copyportfolio

# In[160]:

def LPM(inputlist, limit, q):
    "Only using this as a downside measurement of risk \n Insert initial portfolio value"
    n = len(inputlist)-1
    mean = sum(inputlist)/len(inputlist)
    sv = []
    for i in inputlist:
        if i < float(limit):
            sv.append((i - mean)**q)
        else:
            sv.append(0)

    return (sum(sv) / n)  

#%%
def DD_measure(Prices):
    DD = [0]
    for i in range (1, len(Prices)):
        DD.append(Prices.iloc[i]/Prices.iloc[0:i+1].max()-1)
    DD = min(DD) * 100

    return DD    

#%%
def DD_measure2(Prices):
    DD = [0]
    for i in range (1, len(Prices)):
        DD.append(np.log(Prices.iloc[i]/Prices.iloc[0:i+1].max()))
    DD = min(DD) * 100

    return DD    

#%%
def VaR (inputlist):
    weights = []
    for i in range (0 , len(inputlist)):
        weights.append(1/(len(inputlist)))
    VaR = pd.DataFrame(inputlist.sort_values())
    VaR ['Weights'] = weights
    VaR ['Cumulative Weight'] = VaR.loc[:,'Weights'].cumsum()
    return VaR
#%%

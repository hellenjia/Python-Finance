#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import pandas as pd


# In[2]:


ser = pd.Series(np.random.random(5),name = "Column 01")


# In[3]:


ser


# In[6]:


ser[2]


# In[47]:


from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
yf.pdr_override()


# In[55]:


y_symbols = ['PG','AAPL']
from datetime import datetime
startdate = datetime(2002,1,1)
enddate= datetime(2009,1,1)
dados = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)['Adj Close']


# In[56]:


dados


# In[59]:


pg= pdr.get_data_yahoo('PG',start='1995-1-1')


# In[60]:


pg


# In[61]:


pg.info()


# In[62]:


pg.head(10)


# In[63]:


pg.tail(10)


# In[64]:


tickers = ['PG','MSFT','T','GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = pdr.get_data_yahoo(t,start='1995-1-1')['Adj Close']


# In[65]:


new_data.tail(10)


# In[69]:


tickers = ['AAPL','GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = pdr.get_data_yahoo(t,start='1995-1-1')['Close']


# In[71]:


new_data.tail()


# In[ ]:





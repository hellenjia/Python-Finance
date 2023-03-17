#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


# In[2]:


PG= pdr.get_data_yahoo('PG',start='1995-1-1')


# In[3]:


PG.head()


# In[4]:


PG.tail()


# # SIMPLE RATE OF RETURN

# In[5]:


PG['simple_return']=(PG['Adj Close']/PG['Adj Close'].shift(1)) - 1
print (PG['simple_return'])


# In[6]:


PG['simple_return'].plot(figsize=(8, 5))


# In[7]:


avg_returns_d = PG['simple_return'].mean()
avg_returns_d


# In[8]:


avg_returns_a = PG['simple_return'].mean() * 250
avg_returns_a


# # Log Return
# 
#                     ln (P1/P(t-1)

# In[9]:


PG.head()


# In[12]:


PG['log_return']=np.log(PG['Adj Close']/PG['Adj Close'].shift(1))
print (PG['log_return'])


# In[13]:


PG['log_return'].plot(figsize=(8, 5))


# In[14]:


log_returns_d = PG['log_return'].mean()
log_returns_d


# In[15]:


log_returns_a = PG['log_return'].mean()*250
log_returns_a


# In[47]:


a =print (round(log_returns_a*100,5))


# In[49]:





# In[46]:





# In[ ]:





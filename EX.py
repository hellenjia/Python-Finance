#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
yf.pdr_override()


# In[4]:


tickers = ['MSFT','AAPL']
ind_data = pd.DataFrame()
for t in tickers:
    ind_data[t]=pdr.get_data_yahoo(t,start='2002-1-1')['Adj Close']


# In[5]:


ind_data.info()


# In[6]:


ind_data.head()


# In[7]:


(ind_data/ind_data.iloc[0]*100).plot(figsize= (15,6));
plt.show()


# In[8]:


retorno_ind = (ind_data/ind_data.shift(1))-1

retorno_ind.tail()


# In[9]:


retorno_anual = retorno_ind.mean()*250
retorno_anual


# In[10]:


sec_retorno = np.log(ind_data/ind_data.shift(1))


# In[11]:


sec_retorno


# # MSFT

# In[16]:


sec_data = pd.read_csv(r'C:\Users\BD931KB\Downloads\MSFT_AAPL_2000_2017.csv', index_col='Date')


# In[17]:


sec_data.tail()


# In[18]:


sec_returns = np.log(sec_data/ sec_data.shift(1))


# In[19]:


sec_returns


# In[20]:


sec_returns['MSFT'].mean()


# In[21]:


sec_returns['MSFT'].mean()*250


# In[23]:


sec_returns['MSFT'].std()*250**0.5


# # APPLE

# In[24]:


sec_returns['AAPL'].mean()


# In[25]:


sec_returns['AAPL'].mean() * 250


# In[26]:


sec_returns['AAPL'].std()


# In[27]:


sec_returns['AAPL'].std() * 250 ** 0.5


# --------------------------------------------------------------------------

# In[28]:


sec_returns[['MSFT', 'AAPL']].mean() * 250


# In[29]:


sec_returns[['MSFT', 'AAPL']].std() * 250 ** 0.5


# # Covariance and Correlation

# In[30]:


cov_matrix = sec_returns.cov()
cov_matrix


# In[31]:


cov_matrix_a = sec_returns.cov() * 250
cov_matrix_a


# In[32]:


corr_matrix = sec_returns.corr()
corr_matrix


# ## Calculating Portfolio Risk

# In[33]:


weights = np.array([0.5, 0.5])


# In[34]:


pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
pfolio_var


# In[35]:


pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
pfolio_vol


# In[36]:


print (str(round(pfolio_vol, 5) * 100) + ' %')


# In[ ]:





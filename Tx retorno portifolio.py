#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
yf.pdr_override()


# In[2]:


tickers = ['AAPL','MSFT','AMZN','TSM','NVDA']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t]= pdr.get_data_yahoo(t,start = '2002-1-1')['Adj Close']


# In[3]:


new_data.info()


# In[4]:


new_data.head()


# In[5]:


new_data.tail()


# ## Normatization to 100:
# 
#             (Pt/Po = 100) * 100

# In[6]:


new_data.iloc[0]


# In[7]:


(new_data/new_data.iloc[0]*100).plot(figsize= (15,6));
plt.show()


# In[11]:


tickers = ['PG','MSFT','F','GE']
my_data = pd.DataFrame()
for t in tickers:
    my_data[t]= pdr.get_data_yahoo(t,start = '1995-1-1',end ='2017-4-1')['Adj Close']


# In[12]:


(my_data/my_data.iloc[0]*100).plot(figsize= (15,6));
plt.show()


# In[13]:


my_data.iloc[0]


# In[14]:


my_data.plot(figsize= (15,6));
plt.show()


# 
# # Calcular o retorno do portifolio

# Usando taxa de retorno simples calcular o retorno das ações do portifolio

# In[15]:


retorno = (my_data/my_data.shift(1)) -1 
retorno.head()


# In[16]:


peso = np.array([0.25,0.25,0.25,0.25])


# np.dot() -    Calcula o vetor ou matrix do produtos

# In[18]:


np.dot(retorno,peso)


# In[19]:


retorno_anual = retorno.mean()*250
retorno_anual


# In[20]:


np.dot(retorno_anual,peso)


# In[22]:


portilio1 = str(round(np.dot(retorno_anual,peso),5)*100) + "%"
print (portilio1)


# In[23]:


peso_2 = np.array([0.4,0.4,0.15,0.05])


# In[31]:


portifolio2= str(round(np.dot(retorno_anual,peso_2),5)*100) + "%"
print ("O portifolio 1 = "+ portilio1)
print ("O portifolio 2 = " + portifolio2)


# In[ ]:





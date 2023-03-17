#!/usr/bin/env python
# coding: utf-8

# # Calcular a taxa de retorno de um portifolio

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt 
import yfinance as yf
yf.pdr_override()


# In[2]:


tickers =['^GSPC','^IXIC','^GDAXI','^FTSE']

ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] =pdr.get_data_yahoo(t,start='1995-1-1')['Adj Close']


# In[3]:


ind_data.info()


# In[4]:


ind_data.tail()


# In[5]:


ind_data.head()


# In[6]:


(ind_data/ind_data.iloc[0]*100).plot(figsize= (15,6));
plt.show()


# In[7]:


retorno_ind = (ind_data/ind_data.shift(1))-1

retorno_ind.tail()


# In[8]:


retorno_anual = retorno_ind.mean()*250
retorno_anual


# In[9]:


tickers1 = ['PG','^GSPC','^DJI'] 

dados_1 = pd.DataFrame()

for t in tickers1:
    dados_1[t]= pdr.get_data_yahoo(t,start ="2007-1-1")['Adj Close']


# In[10]:


dados_1.tail()


# In[11]:


(dados_1/dados_1.iloc[0]*100).plot(figsize=(16,6));
plt.show()


# # Security's risk

# In[12]:


tickers2 = ['PG','BEI.DE']

sec_data = pd.DataFrame()

for t in tickers2:
    sec_data[t] = pdr.get_data_yahoo(t,start='2007-1-1')['Adj Close']


# In[13]:


sec_data.tail()


# In[14]:


sec_data.head()


# In[15]:


#Log returns
sec_retorno = np.log(sec_data/sec_data.shift(1))


# In[16]:


sec_retorno


# # PG

# In[17]:


#Dayly average return
day_pg =sec_retorno['PG'].mean()


# In[18]:


#Year average return
sec_retorno['PG'].mean()*250


# In[19]:


#Volatilidade da ação
sec_retorno['PG'].std()


# In[20]:


#Anualizar a volatilidade e preciso de multiplicar por quantos dias o mercado fica aberto e elevar a 0.5 
sec_retorno['PG'].std()*250 **0.5


# # Beiersdorf

# In[21]:


day_bei = sec_retorno['BEI.DE'].mean()


# In[22]:


sec_retorno['BEI.DE'].mean()*250


# In[23]:


sec_retorno['BEI.DE'].std()


# In[24]:


sec_retorno['BEI.DE'].std()*250**0.5


# In[25]:


print(day_bei)
print(day_pg)


# In[26]:


print (sec_retorno['BEI.DE'].mean()*250)
print(sec_retorno['PG'].mean()*250)


# Briefly, each pair of brackets we surround our column names with will increase the number of dimensions of the newly created numpy object by one.
# 
# Hence we can correct our code by using double instead of single brackets.

# In[27]:


sec_retorno[['PG','BEI.DE']].mean()*250


# In[28]:


sec_retorno[['PG','BEI.DE']].std()*250**0.5


# # Covariancia e Correlação

# In[29]:


PG_var = sec_retorno['PG'].var()
PG_var


# In[30]:


BEI_var = sec_retorno['BEI.DE'].var()
BEI_var


# In[31]:


PG_var_a = sec_retorno['PG'].var()*250
PG_var_a


# In[32]:


BEI_var_a = sec_retorno['BEI.DE'].var()*250
BEI_var_a


# In[33]:


cov_matrix =sec_retorno.cov()
cov_matrix


# In[34]:


cov_matrix_a =sec_retorno.cov()*250
cov_matrix_a


# In[35]:


corr_matriz = sec_retorno.corr()
corr_matriz


# # Calcular risco do Portifolio

# Equal weigthing scheme:

# In[36]:


weigths = np.array ([0.05,0.5])


# Variancia do portifolio:

# In[37]:


pfolio_vol = np.dot(weigths.T, np.dot(sec_retorno.cov()*250,weigths))
pfolio_vol


# Volatilidade do portifolio:

# In[39]:


pfolio_vol = (np.dot(weigths.T,np.dot(sec_retorno.cov()*250,weigths)))**0.5
pfolio_vol


# In[53]:


print (str(round(pfolio_vol, 5)* 100 )+ '%')


# In[ ]:


Calcular diversificavel e não diversificado 


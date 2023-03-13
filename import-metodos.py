#!/usr/bin/env python
# coding: utf-8

# #### Numpy nos permite a trabalhar com orgaziações multidimencionais

# In[1]:


import numpy as np


# #### Pandas nós permite a organizar dados através de tabelas e anexar tabelas descritivas nas linhas e colunas de uma tabela. 

# In[2]:


import pandas as pd


# In[4]:


import matplotlib as mtp


# In[5]:


import math as mt


# In[6]:


import random as rand


# In[7]:


import statsmodels as stmd


# In[9]:


import pandas_datareader as pd_reader


# In[11]:


a = np.array([[0,1,2,3],[4,5,6,7]])
a


# In[12]:


a.shape


# In[13]:


a[1,3]


# In[14]:


a[0,3]=10


# In[15]:


a


# # Random

# In[18]:


prob= rand.random()
print(prob)


# In[19]:


number= rand.randint(1,6)
print(number)


# In[27]:


np.random.randint(1,9,(4,6))


# In[ ]:





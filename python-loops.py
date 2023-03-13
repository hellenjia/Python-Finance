#!/usr/bin/env python
# coding: utf-8

# In[1]:


even = [0,2,4,6,8,10,12,14,16,18,20]


# In[2]:


for n in even:
    print(n)


# In[3]:


for n in even:
    print(n, end = " ")


# In[5]:


x = 0 
while x <= 20:
    print(x,end = " ")
    x = x+2


# In[8]:


list(range(0,22,2))


# In[13]:


for n in range(10):
    print(2**n,end = " ")


# In[15]:


for x in range(20):
    if x % 2 == 0:
        print (x,end = " ")
    else:
        print("Odd",end = " ")


# In[16]:


x=[0,1,2]


# In[17]:


for item in x:
    print(item, end=" ")


# In[18]:


for item in range(len(x)):
    print(x[item],end=" ")


# In[19]:


x = list(range(0,22,2))


# In[20]:


for item in range(len(x)):
    print(x[item],end=" ")


# In[30]:


for y in list(range(1,11,2)):
    print(y, end=" ")
    


# In[32]:


for n in range(1,11):
    print (n * 2, end=" ")


# In[34]:


for a in range(1,30):
    if a % 2 == 1:
        print (a,end = " ")
    else:
        print("Even",end = " ")


# In[35]:


n = [1,2,3,4,5,6]


# In[36]:


for item in n:
    print(item*10, end=" ")


# In[38]:


for item in range(len(n)):
    print (n[item]*10, end =" ")


# In[39]:


def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
    return total


# In[41]:


list_1 =[1,3,9,7,15,30,23,90]


# In[42]:


count(list_1)


# In[ ]:





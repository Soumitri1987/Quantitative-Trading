
# coding: utf-8

# In[1]:


# Calculating return of a portfolio


# In[4]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[14]:





# In[19]:


tickers = ['PG','MSFT','F','GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]= wb. DataReader( t, data_source= 'yahoo', start= '1995-1-1')['Adj Close']


# In[21]:


mydata.info()


# In[18]:


mydata.to_csv('E:/data.csv')


# In[22]:


mydata.head()


# In[23]:


mydata.tail()


# In[24]:


mydata.info()


# In[25]:


mydata.iloc[0]


# In[27]:


(mydata/mydata.iloc[0]*100).plot(figsize=(15,6));
plt.show()


# In[28]:


mydata.plot(figsize= (15,6))
plt.show()


# In[29]:


returns= (mydata/ mydata.shift(1))-1
returns.head()


# In[30]:


weights= np.array([0.25,0.25,0.25,0.25])


# In[33]:


np.dot(returns,weights)


# In[34]:


annual_returns= returns.mean()*250
annual_returns


# In[35]:


np.dot(annual_returns,weights)


# In[42]:


portfolio_1= round(np.dot(annual_returns,weights)*100,3)
portfolio_1


# In[44]:


weights1= np.array([0.4,0.4,0.15,0.05])


# In[45]:


np.dot(annual_returns,weights1)


# In[47]:


portfolio_2= round(np.dot(annual_returns,weights1)*100,2)
portfolio_2


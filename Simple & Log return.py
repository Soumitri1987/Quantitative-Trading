
# coding: utf-8

# participants=['rohan','roshan','mihir']
# participants

# In[5]:


participants[1:2]


# In[2]:


x=5


# In[4]:


print (x)


# In[5]:


x= 5+4


# In[6]:


print (x)


# In[7]:


x=5**2


# In[8]:


print(x)


# In[9]:


x=5/2


# In[10]:


print(x)


# In[11]:


x=50*2


# In[12]:


print(x)


# In[84]:


type(x)


# In[14]:


type(x)


# In[15]:


type(10.2)


# In[16]:


type(False)


# In[17]:


type(True)


# In[18]:


type(-5.5)


# In[19]:


type("bapu")


# In[22]:


x= 'bapu you come here'


# In[23]:


x


# In[24]:


print(x)


# In[26]:


print('love')


# In[30]:


x="I'm fine"


# In[31]:


print(x)


# In[32]:


x= 'I\'M fine'


# In[33]:


print(x)


# In[34]:


x= 3 % 2


# In[35]:


print(x)


# In[36]:


5**2==25


# In[37]:


# read carefully
x= 5/2


# In[38]:


print(x)


# In[39]:


"Soumitri"[3]


# In[42]:


"Binay Bhusan Nanda"[7]


# In[45]:


def five(x):
    X= 7
    return X


# In[46]:


five(9)


# In[48]:


def f (x):
    x=a+3
    return x


# In[51]:


f(9)


# In[52]:


True and False


# In[53]:


True and True


# In[54]:


False and True


# In[55]:


False and False


# In[56]:


True or True


# In[57]:


False or True


# In[58]:


True or False


# In[59]:


False or False


# In[60]:


not True


# In[62]:


not False


# In[64]:


not True and False or False


# In[65]:


not False or False


# In[79]:


if 5 == 15/3:
    print("perfect!")


# In[80]:


if 5==5:
    print("bapu")


# In[78]:


if 5==5:
    print("Bapu")


# In[82]:


x=5
if x>3:
    print('case1')
else:
    print('case2')


# In[90]:


def compare_to_ five(y):
    if y> 5:
        return "Greater"
    elif y <5:
        return "Less"
    else :
        return "Equal"


# In[2]:


def plus_ten(a):
    return a+ 10


# In[3]:


plus_ten(5)


# In[4]:


print(5)


# In[12]:


def length(x):
    return x
def breadth(y):
    return y
def area_rectangle(z):
    return length*breadth
    
    


# In[17]:


def area_rectangle(x,y):
    return x*y


# In[18]:


area_rectangle(7,8)


# In[19]:


def area_triangle(b,h):
    return 0.5*b*h


# In[20]:


area_triangle(3,4)


# In[22]:


def square(a,b):
    return a**2+b**2+2*a*b


# In[23]:


square (2,0)


# In[24]:


square(2,1)


# In[25]:


int(25.02566)
str(25.365)
max(125,256,369)


# In[26]:


str(25.365)


# In[27]:


int(25.02566)


# In[28]:


abs(-.56)


# In[34]:


list= [9,0.6]


# In[35]:


sum(list)


# In[36]:


round(9.06,1)


# In[37]:


len('soumitribhusannanda')


# In[1]:


pip3 install numpy


# In[2]:


import numpy as np


# In[3]:


height = [1.65,1.56,1.69,1.52,1.51]


# In[4]:


weight = [62.5,63.2,56.2,55.5,70.7]


# In[5]:


np_height = np.array (height)


# In[6]:


np_height


# In[7]:


np_weight = np. array(weight)


# In[8]:


np_weight


# In[9]:


bmi = np_weight/np_height**2


# In[10]:


bmi


# In[11]:


type(np_height)


# In[12]:


np.mean(np_height)


# In[13]:


help(round)


# In[2]:


import quandl



# In[4]:


mydata_01= quandl.get("FRED/GDP")


# In[10]:


import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[11]:


PG = wb.DataReader("PG",data_source= "yahoo", start= "1995-1-1")


# In[12]:


PG.head()


# In[13]:


PG.tail()


# In[46]:


simple_return= PG['Adj Close'] / PG['Adj Close'].shift(1)-1
print(simple_return)



# In[56]:


plt.plot(simple_return)
plt.show()


# In[62]:


average_return= simple_return.mean()
print(average_return)


# In[66]:


avarage_return_a =  simple_return.mean()*250
print(avarage_return_a)


# In[76]:


round((avarage_return_a*100),2)


# In[77]:


log_return= np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print(log_return)


# In[78]:


plt.plot(log_return)
plt.show()


# In[80]:


average_log_return= log_return.mean()
average_log_return


# In[84]:


average_log_return_a= average_log_return*250*100
round(average_log_return_a,3)


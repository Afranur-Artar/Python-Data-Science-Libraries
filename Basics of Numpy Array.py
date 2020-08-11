#!/usr/bin/env python
# coding: utf-8

# # Soru 1:
# Create three lists representing house features, each list containing ten values. The first one for the house's size in square meters, the second one for rooms and last for price. Then, create an array combining these lists.

# In[16]:


size=[80,76,110,50,100,102,130,120,122,144]
rooms=[2,1,3,1,3,3,2,3,4,2]
price=[1100,2000,3000,4000,5000,3030,4040,2020,1010,2040]

import numpy as np

array_=np.array([size,rooms,price])
print(array_)


# # Soru 2:
# Transpose the array you have created, so that every line can represent features of one house.

# In[18]:


trans=np.transpose(array_)
print(trans)


# # Soru 3:
# Display the shape of the array and explain what it means.

# In[20]:


print(np.shape(array_))

# "array_"   adlı array' in içerisinde 3 liste ve her listenin içeriisnde 10 tane eleman var demektir.


# # Soru 4:
# Write a function that returns an array of ones with zeros where both row and column numbers are even. The sample array is below. The number of rows and columns will be parameters.
# 
# Hem satır hem de sütunu çift olan yere 0; diğer türlü 1 getir!
# 
# shape(6 x 5) --> [[1   1   1   1   1]
#                   [1   0   1   0   1]
#                   [1   1   1   1   1]
#                   [1   0   1   0   1]
#                   [1   1   1   1   1]
#                   [1   0   1   0   1]]

# In[56]:


def arr(row,column):
    
    array_=np.ones((row,column))
    i=0
    j=0
    
    for i in range(row):
        for j in range(column):
            if i%2==0 and j%2==0:
                array_[i,j]=0
    return(array_)

arr(6,5)


# In[ ]:





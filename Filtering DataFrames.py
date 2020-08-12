#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # Soru 1:
# For Pandas assignments, you are going to use Titanic (train.csv) dataset. Download the dataset and load to a DataFrame.
# 
# By using conditional selection methods, calculate the survival rate for all passengers under 30 years old.

# In[44]:


train=pd.read_csv("train.csv",index_col=0)

len(train[(train['Age']<30) & (train['Survived']==1)])/len(train[(train['Age']<30)])


# # Soru 2:
# Calculate the survival rate by gender.

# In[60]:


print("Survival rate of male: ",len(train[(train['Sex']=="male") & (train['Survived']==1)])/len(train[(train['Sex']=='male')]))

print("Survival rate of female: ",len(train[(train['Sex']=="female") & (train['Survived']==1)])/len(train[(train['Sex']=='female')]))


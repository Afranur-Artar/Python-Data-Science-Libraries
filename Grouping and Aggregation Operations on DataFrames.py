#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# # Soru 1:
# For Pandas assignments, you are going to use Titanic (train.csv) dataset. Download the dataset and load to a data frame.
# 
# * Calculate the average age of the passengers for each gender and passenger class by using groupby() method.

# In[8]:


train=pd.read_csv("train.csv",index_col=0)
train

train.groupby(by=["Sex","Pclass"])['Age'].mean()


# # Soru 2:
# Group by embarkation port and print values. (Notice that you get unique values with this.)

# In[11]:


train=pd.read_csv("train.csv",index_col=0)


train.groupby(by='Embarked').agg({"Embarked": "nunique"})
train


# "Embarked"  kolonuna göre gruplama yapıldıktan sonra hangi değerin unique olması istenmetedir?


# In[ ]:


count(['PassengerId']).nunique().to_frame()


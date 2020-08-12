#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# # Soru 1:
# Create a DataFrame whose index is the first 10 letters of the alphabet and contains two more columns with first 10 prime numbers and the first 10 fibonacci numbers.

# In[4]:


# Asal sayıların data frame i
asal=[]
for i in range(3,36):

    bolundu = False
    for j in range(2,i):
            if i % j == 0:
                bolundu=True
                # break yok...
    if bolundu == False:
        asal.append(i)
print ("Prime numbers's lists: ",asal,"\n")
asal_np=np.array(asal)
asal_df=pd.DataFrame(asal_np,columns=['Prime numbers'])
print("Data frame: ","\n",asal_df,"\n")


# Fibonacci sayıları
dizi = []
a = 1
b = 1
c = 1
while c<100: 
    c = a+b
    a = b
    b = c
    dizi.append(b) 
print(dizi)
dizi_np=np.array(dizi)
dizi_df=pd.DataFrame(dizi_np,columns=['Fibonacci numbers'])
print("Data frame: ","\n",dizi_df,"\n")


# Ffirst 10 alphabet
alphabet=["a","b","c","d","e","f","g","h","i","j"]
alphabet_np=np.array(["a","b","c","d","e","f","g","h","i","j"])
alphabet_df=pd.DataFrame(alphabet_np,columns=['Alphabets'])

print("Data frame: ","\n",alphabet_df,"\n")


df_dict=pd.DataFrame({'Prime numbers':asal_np,'Fibonacci':dizi_np,'Alphabet':alphabet_np})

print("Data Frame: ","\n",df_dict)


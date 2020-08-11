#!/usr/bin/env python
# coding: utf-8

# # Soru 1:
# Load the array you saved in the previous lesson from the disk.

# In[ ]:


import numpy as np

with open("Earthquakes.csv","r",encoding='utf-8') as f:
    earthquake=f.read()
    print(earthquake)
np.save("Earthquakes.npy",earthquake)

earthquake_array=np.array([earthquake])
earthquake=np.load("Earthquakes.npy")

print([earthquake_array])

# Earthquake csv dosyasını array formatında import edemediğim için 
# array formatına nasıl dönüştürüleceği sorulacak!!!


# # Soru 2:
# Display the mean and the standard deviation for each column.

# In[ ]:


for j in range(len(earthquake_array)):
    for i in range(len(earthquake_array)):
        print("Standart deviation of column: ", np.std(earthquake_array[:,j])
        print("Standart deviation of column: ", np.mean(earthquake_array[:,j])


# # Soru 3:
# Subtract 1, 25, 25, 10, 4 from columns in order. (Remember it can be dobe in one line of code.)

# In[ ]:


print(np.delete(earthquake_array,(1,25,25,10,4)))


# # Soru 4:
# Multiply each element by 2. (Remember it can be done in one line of code.)
# 
# 
# 

# In[ ]:


print(earthquake_array*2)


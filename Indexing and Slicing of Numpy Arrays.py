#!/usr/bin/env python
# coding: utf-8

# # Soru 1:
# Load the Earthquakes dataset. Export the dataset to an array as you covered in the previous lesson.

# In[7]:


import numpy as np


# In[19]:


with open("Earthquakes.csv","r",encoding='utf-8') as f:
    earthquake=f.read()
    print(earthquake)


# In[20]:


np.save("Earthquakes.npy",earthquake)

earthquake_array=np.array([earthquake])
earthquake=np.load("Earthquakes.npy")

print([earthquake_array])


# # Soru 2:
# Slice first 20 rows and column numbers 3, 5, 6, 7, 12. Then, assign the array you sliced to a variable.

# In[10]:


earthquake_new=earthquake_array[0:20,(3,5,6,7,12)]
print(earthquake_new)


# # Soru 3:
# Display the row numbers where last values are equal to 4.5 or higher.

# In[22]:


print(earthquake_array[earthquake_array>=4.5])


# # Soru 4:
# Assign 1 to first row.

# In[21]:


earthquake_array[0:,]=1
print(earthquake_array)


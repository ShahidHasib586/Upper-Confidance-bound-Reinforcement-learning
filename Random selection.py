#!/usr/bin/env python
# coding: utf-8

# # Random selection
# 

# ## importing the libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


# In[3]:


dataset


# ## Implementing the random selection

# In[4]:


import random
N = 1000
d = 10
ads_selected = []
total_reward = 0
for n in range (0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward


# ## visualizing the result

# In[10]:


plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of time each ad was selected')
plt.show()


# In[ ]:





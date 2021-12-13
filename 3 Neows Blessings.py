#!/usr/bin/env python
# coding: utf-8

# # Load Data

# In[1]:


# load libraries
import glob
import os
import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#import statsmodels.api as sm


# In[2]:


#%matplotlib inline


# In[3]:


# display all columns
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None


# In[4]:


prep_data = pd.read_json("data/A20runs.json")
#prep_data = pd.read_csv("data/A20runs.csv")
prep_data.head()


# In[5]:


prep_data.shape


# # Group Character Chosen Count

# In[6]:


char_cnt = prep_data.groupby('character_chosen').size()
char_cnt =char_cnt.reindex(["IRONCLAD", "THE_SILENT", "DEFECT", "WATCHER"])
char_cnt


# In[7]:


my_colors = ['tab:red','tab:green','tab:blue','tab:purple']  #red, green, blue, black, etc.

plt.style.use('default')

fig, ax = plt.subplots()
ax.bar(char_cnt.index, char_cnt, color = my_colors)
for i in range(len(char_cnt)):
    ax.annotate(str(char_cnt[i]), xy=(char_cnt.index[i], char_cnt[i]), ha='center', va='bottom')
ax.set_ylim([0,3000])
ax.set_ylabel("Count")
ax.set_title("Ascension 20 Victorious Runs")

plt.tight_layout()

plt.show()


# In[8]:


#fig.savefig("img/A20runs.png")


# # Neow Bonus Count

# In[9]:


neow_cnt = prep_data.groupby('neow_bonus').size().sort_values(ascending = True)
neow_cnt


# In[18]:


#my_colors = ['tab:red','tab:green','tab:blue','tab:purple']  #red, green, blue, black, etc.

#plt.style.use('default')

fig, ax = plt.subplots()
ax.barh(neow_cnt.index, neow_cnt, color = 'grey')
ax.set_title("Neow's Blessings | Top Picked", loc = 'left', fontdict = {'family': 'sans-serif',
                                                                        'color':  'black',
                                                                        'weight': 'bold',
                                                                        'size': 18
                                                                        })
ax.set_xlabel('count')

plt.tight_layout()

plt.show()


# In[18]:


fig.set_size_inches([7,7])
fig.savefig("img/neow_cnt.png")


# **Ironclad**

# In[19]:


neow_cnt_red = prep_data[prep_data['character_chosen'] == 'IRONCLAD'].groupby('neow_bonus').size().sort_values(ascending = True)


# In[20]:


fig, ax = plt.subplots()
ax.barh(neow_cnt_red.index, neow_cnt_red, color = 'tab:red')
ax.set_title("Neow's Blessings | Ironclad", loc = 'left', fontdict = {'family': 'sans-serif',
                                                                        'color':  'darkred',
                                                                        'weight': 'bold',
                                                                        'size': 18
                                                                        })
ax.set_xlabel('count')

plt.tight_layout()

plt.show()


# In[21]:


fig.set_size_inches([7,7])
fig.savefig("img/neow_cnt_ironclad.png")


# **Silent**

# In[22]:


neow_cnt_green = prep_data[prep_data['character_chosen'] == 'THE_SILENT'].groupby('neow_bonus').size().sort_values(ascending = True)


# In[23]:


fig, ax = plt.subplots()
ax.barh(neow_cnt_green.index, neow_cnt_green, color = 'tab:green')
ax.set_title("Neow's Blessings | Silent", loc = 'left', fontdict = {'family': 'sans-serif',
                                                                        'color':  'darkgreen',
                                                                        'weight': 'bold',
                                                                        'size': 18
                                                                        })
ax.set_xlabel('count')

plt.tight_layout()

plt.show()


# In[24]:


fig.set_size_inches([7,7])
fig.savefig("img/neow_cnt_silent.png")


# **Defect**

# In[25]:


neow_cnt_blue = prep_data[prep_data['character_chosen'] == 'DEFECT'].groupby('neow_bonus').size().sort_values(ascending = True)


# In[26]:


fig, ax = plt.subplots()
ax.barh(neow_cnt_blue.index, neow_cnt_blue, color = 'tab:blue')
ax.set_title("Neow's Blessings | Defect", loc = 'left', fontdict = {'family': 'sans-serif',
                                                                        'color':  'darkblue',
                                                                        'weight': 'bold',
                                                                        'size': 18
                                                                        })
ax.set_xlabel('count')

plt.tight_layout()

plt.show()


# In[27]:


fig.set_size_inches([7,7])
fig.savefig("img/neow_cnt_defect.png")


# **Watcher**

# In[28]:


neow_cnt_purple = prep_data[prep_data['character_chosen'] == 'WATCHER'].groupby('neow_bonus').size().sort_values(ascending = True)


# In[29]:


fig, ax = plt.subplots()
ax.barh(neow_cnt_purple.index, neow_cnt_purple, color = 'tab:purple')
ax.set_title("Neow's Blessings | Watcher", loc = 'left', fontdict = {'family': 'sans-serif',
                                                                        'color':  'darkmagenta',
                                                                        'weight': 'bold',
                                                                        'size': 18
                                                                        })
ax.set_xlabel('count')

plt.tight_layout()

plt.show()


# In[30]:


fig.set_size_inches([7,7])
fig.savefig("img/neow_cnt_watcher.png")


# In[ ]:





# In[ ]:





# In[ ]:





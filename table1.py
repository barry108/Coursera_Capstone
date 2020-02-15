#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")[0]


# In[51]:


df.head()


# In[52]:


Bo_drop = df[df['Borough'] == "Not assigned"].index
df.drop(Bo_drop, inplace = True)


# In[53]:


df.head()


# In[54]:


df = df.groupby(['Postcode'])['Neighbourhood'].apply(','.join).reset_index()


# In[56]:


df.head(20)


# In[57]:


df['Neighbourhood'].loc[df['Neighbourhood'] == 'Not assigned'] = df['Borough']


# In[60]:


df.shape


# In[ ]:





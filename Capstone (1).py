#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
import pandas as pd
import json
import glob


# In[34]:


response= requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=c680984d1f261c766c61129ac1b932fa')
resdict=response.json


# In[35]:


print(response.status_code)


# In[36]:


response.json()


# In[37]:


df2=pd.read_json('https://api.themoviedb.org/3/genre/movie/list?api_key=c680984d1f261c766c61129ac1b932fa')
df2


# In[ ]:





# In[28]:


r1= requests.get('https://api.themoviedb.org/3/movie/popular?api_key=c680984d1f261c766c61129ac1b932fa')


# In[29]:


print(r1.status_code)


# In[30]:


x=r1.json()
x


# In[4]:


import requests
from bs4 import BeautifulSoup


# In[8]:


r=requests.get('https://www.boxofficemojo.com/weekly/2023W02/?ref_=bo_wly_table_1')
print(r)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


# In[22]:



soup = BeautifulSoup(r.content, 'html.parser')
for movie in soup.find_all('td'):
    print(movie.string) # Movie name


# In[25]:


from glob import glob
x['page'].apply(lambda row: glob(row, 'results.title'))


# In[33]:


FIELDS = ["key", "results.title","results.popularity"]
df = pd.json_normalize(x["page"])
df[FIELDS]


# In[31]:


df=pd.json_normalize(x['page'])


# In[10]:


df


# In[12]:


df.info()


# In[53]:


import pandas as pd
import json

with open(x,'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(data)


# In[ ]:





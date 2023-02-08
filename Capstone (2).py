#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import json
import glob


# In[2]:


response= requests.get('https://api.themoviedb.org/3/movie/315162?api_key=c680984d1f261c766c61129ac1b932fa')
resdict=response.json


# In[3]:


print(response.status_code)


# In[4]:


response.json()


# In[5]:


df2=pd.read_json('https://api.themoviedb.org/3/genre/movie/list?api_key=c680984d1f261c766c61129ac1b932fa')
df2


# In[6]:


r1= requests.get('https://api.themoviedb.org/3/movie/popular?api_key=c680984d1f261c766c61129ac1b932fa')


# In[7]:


print(r1.status_code)


# In[8]:


x=r1.json()
x


# In[9]:


import requests
from bs4 import BeautifulSoup


# In[10]:


import requests
import pandas as pd

#Gets the data and puts it into a dictionary.
url = 'https://api.themoviedb.org/3/movie/popular?api_key=c680984d1f261c766c61129ac1b932fa'
response = requests.get(url)
json_data = response.json()

#The problem with json_data is it is a dictionary with one row - the value for that row is another
#dictionary. So we have to put that into separate dictionary of its own.
sub_dict = json_data["results"]

#Now we have the dictionary we want. We can convert into a dataframe.
df = pd.DataFrame.from_dict(sub_dict)


# In[11]:


newdf=df[['id','popularity','title','vote_average','vote_count','genre_ids']]
newdf=newdf.rename(columns={'id':'ID'})


# In[12]:


newdf


# In[17]:


for ID in newdf:
    print(ID)
    url = 'https://api.themoviedb.org/3/movie/'+ID+'?api_key=c680984d1f261c766c61129ac1b932fa'
    response = requests.get(url)
    json_data = response.json()
    subdict=json_data['budget']
print(json_data)


# In[18]:


newdf.to_csv('capdata', index=False)


# In[19]:


df2=pd.read_csv('capdata')
df2


# In[22]:



soup = BeautifulSoup(r.content, 'html.parser')
for movie in soup.find_all('td'):
    print(movie.string) # Movie name


# In[12]:


df.info()


# In[ ]:





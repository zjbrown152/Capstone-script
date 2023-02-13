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


# In[166]:


r1= requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=c680984d1f261c766c61129ac1b932fa')


# In[167]:


print(r1.status_code)


# In[168]:


x=r1.json()
x


# In[9]:


import requests
from bs4 import BeautifulSoup


# In[186]:


import requests
import pandas as pd

#Gets the data and puts it into a dictionary.
url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=c680984d1f261c766c61129ac1b932fa'
response = requests.get(url)
json_data = response.json()

#The problem with json_data is it is a dictionary with one row - the value for that row is another
#dictionary. So we have to put that into separate dictionary of its own.
sub_dict = json_data["results"]

#Now we have the dictionary we want. We can convert into a dataframe.
df = pd.DataFrame.from_dict(sub_dict)


# In[187]:


newdf=df[['id','release_date','popularity','title','vote_average','vote_count','genre_ids']]
newdf=newdf.rename(columns={'id':'ID','genre_ids':'Genre'})


# In[188]:


newdf #if statement to check for existing


# In[196]:


import requests
import pandas as pd

#Gets the data and puts it into a dictionary.
url2 = 'https://api.themoviedb.org/3/movie/popular?api_key=c680984d1f261c766c61129ac1b932fa'
response1 = requests.get(url2)
json_data = response1.json()

#The problem with json_data is it is a dictionary with one row - the value for that row is another
#dictionary. So we have to put that into separate dictionary of its own.
sub_dict1 = json_data["results"]

#Now we have the dictionary we want. We can convert into a dataframe.
df4 = pd.DataFrame.from_dict(sub_dict1)


# In[198]:


newdf1=df4[['id','release_date','popularity','title','vote_average','vote_count','genre_ids']]
newdf1=newdf1.rename(columns={'id':'ID','genre_ids':'Genre'})
newdf1


# In[205]:


if newdf1['ID'] in newdf['ID']:
    print(ID)
    print("Already there")
else:
    print(i)


# In[189]:


newdf.info()


# In[190]:


newdf.to_csv('capdata', index=False)
df2=pd.read_csv('capdata')
df2


# In[191]:


import pandas as pd
import numpy as np
df3 = pd.DataFrame({'Budget': [],
                   'Revenue': [],})
for ID in newdf['ID']:  ##<-- you didn't have the ['ID] part.
    print(ID)
    url1 = 'https://api.themoviedb.org/3/movie/'+str(ID)+'?api_key=c680984d1f261c766c61129ac1b932fa'
    response = requests.get(url1)
    json_data = response.json()
    list1=json_data['budget']
    list2=json_data['revenue']
    print('Budget '+str(list1)+'\nRevenue '+str(list2))
    df3.loc[len(df3)] = list1, list2


# In[192]:


df3


# In[194]:





# In[195]:


final1=pd.concat([df2, df3], axis=1, join='inner')
final1


# In[183]:


final1.to_csv('finaldata', index=False)
final2=pd.read_csv('finaldata')
final2


# In[12]:


df.info()


# In[ ]:





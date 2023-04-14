#!/usr/bin/env python
# coding: utf-8

# In[15]:


print("Name : ")
print("Will plot graphs to show which countries has the higher expenditure on health and higher life expectancy, Developed or Developing countries")


# # Task 1 - Show which countries has the higher expenditure on health, Developed or Developing countries

# In[4]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='map.png') 
#predefine code end


# Developed Countries refers to the sovereign (independent) nation/state whose economy has highly progressed and possesses great technological infrastructure, as compared to other nations. The countries with low industrialization and low human development index are termed as developing countries.

# In[1]:


#import libraries and csv
import pandas as pd
import matplotlib.pyplot as plt 

pd.set_option('display.max_columns', None)

df = pd.read_csv('Life_Expectancy_Data.csv')
df


# In[3]:


#Create a new dataframe only for country Australia which is a developed country
Australia = df.loc[df['Country']== 'Australia']
Australia


# In[4]:


#Create a new dataframe only for country Italy which is a developed country
Italy = df.loc[df['Country']== 'Italy']
Italy


# In[6]:


#Create a new dataframe only for country Brazil which is a developing country
Brazil = df.loc[df['Country']== 'Brazil']
Brazil


# In[7]:


#Create a new dataframe only for country Colombia which is a developing country
Columbia = df.loc[df['Country']== 'Columbia']
Columbia


# In[11]:


#Plot a line graph showing the Total expenditure on health of developed and developing countries
fig = plt.subplots(figsize=(10,6))
label = Australia['Year']
value = Australia['Total expenditure']

plt.plot(label, value, label = "Australia" , linewidth=3.0)

label = Italy['Year']
value = Italy['Total expenditure']
plt.plot(label, value, label = "Italy" , linewidth=3.0)

label = Brazil['Year']
value = Brazil['Total expenditure']
plt.plot(label, value, label = "Brazil" , linewidth=3.0)

label = Columbia['Year']
value = Columbia['Total expenditure']
plt.plot(label, value, label = "Columbia" , linewidth=3.0)

plt.xlabel('Year')

plt.ylabel('Total expenditure')

plt.title('Total Expenditure on health of developind and developed city', fontsize=20)

plt.legend()

plt.show()


# Conclusion - 

# # Task 2 Show which countries has the higher Life expectancy, Developed OR Developing countries

# In[16]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='map2.png') 
#predefine code end


# The term “life expectancy” refers to the number of years a person can expect to live. By definition, life expectancy is based on an estimate of the average age that members of a particular population group will be when they die
# 

# In[7]:


#Plot a line graph showing the correlation between the Coal Consumption and Coal Price 


# Conclusion - 

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Python Data Analysis\Udemy Courses Analysis\Udemy Courses.csv")
df


# In[3]:


df.dtypes


# In[4]:


df.isnull().sum()


# In[5]:


# What are all different subjects for which Udemy is offering courses?

df.subject.unique()


# In[6]:


# Which subjects has the maximum number of subjects ?

course_count = df.subject.value_counts()
course_count


# In[10]:


course_count.plot(kind = 'bar', title = 'Maximum Number Of Courses', xlabel= 'Subject', ylabel= 'Number of Courses')


# In[11]:


# Show all the courses which are Free of cost.

df[df.is_paid == False]


# In[12]:


##Either
df[df.price == 'Free']


# In[13]:


# Show all the courses which are paid.
df[df.is_paid== True]


# In[14]:


##Either
df[df.price!='Free']


# In[18]:


# Arraning course in term of price.

df.sort_values(by='price', ascending= False)



# In[21]:


#Top Selling Courses

top_10_courses = df.sort_values(by='num_subscribers',ascending = False).head(10)
top_10_courses


# In[22]:


#Least Selling Courses

df.sort_values(by='num_subscribers', ascending = True).head(10)


# In[25]:


#Show all courses of Graphics Design

df[df.subject=='Graphic Design']


# In[27]:


df[(df['subject']== 'Graphic Design')& (df['num_subscribers']==0)]


# In[31]:


#List out all the courses related to 'Python'

df[df.course_title.str.contains('Python')]


# In[37]:


#Maximum number of subscriber for each level of courses.

total_subscriber_per_level= df.groupby('level')['num_subscribers'].sum()
total_subscriber_per_level


# In[43]:


total_subscriber_per_level.plot(kind='bar')


# In[44]:


max_subscriber_per_level=df.groupby('level')['num_subscribers'].max()
max_subscriber_per_level


# In[45]:


max_subscriber_per_level.plot(kind= 'pie')


# In[ ]:


plt.style.available
['Solarize_Light2',
 '_classic_test_patch',
 '_mpl-gallery',
 '_mpl-gallery-nogrid',
 'bmh',
 'classic',
 'dark_background',
 'fast',
 'fivethirtyeight',
 'ggplot',
 'grayscale',
 'seaborn-v0_8',
 'seaborn-v0_8-bright',
 'seaborn-v0_8-colorblind',
 'seaborn-v0_8-dark',
 'seaborn-v0_8-dark-palette',
 'seaborn-v0_8-darkgrid',
 'seaborn-v0_8-deep',
 'seaborn-v0_8-muted',
 'seaborn-v0_8-notebook',
 'seaborn-v0_8-paper',
 'seaborn-v0_8-pastel',
 'seaborn-v0_8-poster',
 'seaborn-v0_8-talk',
 'seaborn-v0_8-ticks',
 'seaborn-v0_8-white',
 'seaborn-v0_8-whitegrid',
 'tableau-colorblind10']


# In[46]:


plt.style.use('ggplot')
max_subscriber_per_level.plot.pie()


# In[57]:


# What are the courses that were published in the year 2017?

d1=df[df.year==2017]
d1


# In[58]:


d2= df.is_paid.value_counts()
d2


# In[59]:


d2.plot(kind='pie')


# In[ ]:





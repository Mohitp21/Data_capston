#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import numpy and pandas
import numpy as np
import pandas as pd


# In[2]:


#Import visualization libraries and set %matplotlib inline.import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


# read the csv file
df = pd.read_csv('911.csv')


# In[31]:


df


# In[5]:


#top 5 zipcalls of 911 calls
df['zip'].value_counts().head(5)


# In[6]:


# top 5 townships of 911 calls
df['twp'].value_counts().head(5)


# In[7]:


#Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[8]:


#most common Reason for a 911 call based off of this new column
df['Reason'].value_counts()


# In[9]:


# seaborn to create a countplot of 911 calls by Reason
sns.countplot(x='Reason',data=df,palette='viridis')


# In[ ]:


#data type of the objects in the timeStamp column


# In[10]:


type(df['timeStamp'].iloc[0])


# In[11]:


# use pd.to_datetime to convert the column from strings to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[ ]:


#.apply() to create 3 new columns called Hour, Month, and Day of Week


# In[12]:


df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[13]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[14]:


df['Day of Week'] = df['Day of Week'].map(dmap)


# In[15]:


sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[16]:


sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:


# use gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation


# In[17]:


byMonth = df.groupby('Month').count()
byMonth.head()


# In[18]:


#creating a simple plot off of the dataframe indicating the count of calls per month
# Could be any column
byMonth['twp'].plot()


# In[19]:


#using seaborn's lmplot() to create a linear fit on the number of calls per month
sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[20]:


#Creating a new column called 'Date' that contains the date from the timeStamp column
df['Date']=df['timeStamp'].apply(lambda t: t.date())


# In[21]:


df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


# In[22]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[23]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


# In[24]:


# creating heatmaps with seaborn and our data
dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()


# In[25]:


plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')


# In[26]:


# creating a clustermap using this DataFrame
sns.clustermap(dayHour,cmap='viridis')


# In[27]:


dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()


# In[28]:


plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[29]:


sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)


# In[2]:


#Reading File
df = pd.read_csv(r'/Users/luciac/Desktop/Portfolio/Python Projects/coaster_db.csv')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.columns


# In[6]:


df.dtypes


# In[7]:


df.describe()


# In[8]:


df.head()


# In[ ]:





# # Data Preparation

# In[9]:


df = df[['coaster_name', 
    #'Length', 'Speed', 
    'Location', 'Status', 
    #'Opening date',
     # 'Type', 
    'Manufacturer', 
    #'Height restriction', 'Model', 'Height',
      # 'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 'Opened', 'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean', 
    #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
    #'height_value', 'height_unit', 
    'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()


# In[10]:


#Changind Colum Data Type
df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])


# In[ ]:





# In[11]:


#Renaming Columns
df = df.rename(columns = {'coaster_name':'Coaster_Name',
                    'year_introduced':'Year_Introduced',
                    'latitude':'Latitude',
                    'longitude':'Longitude',
                    'opening_date_clean':'Opening_Date',
                    'speed_mph':'Speed_Mph',
                    'height_ft':'Height_Ft',
                    'Inversions_clean':'Inversions',
                    'Gforce_clean':'Gforce'})


# In[12]:


#Checking for Null Values
df.isna().sum()



# In[13]:


#Checking for Duplicates
df.loc[df.duplicated()]


# In[14]:


df.loc[df.duplicated(subset=['Coaster_Name'])]


# In[15]:


#Checking a duplicate example
df.query('Coaster_Name == "Crystal Beach Cyclone"')


# In[16]:


df = df.loc[~df.duplicated(subset=['Coaster_Name', 'Location', 'Opening_Date' ])] \
.reset_index(drop=True).copy()


# In[17]:


df.shape


# # Feature Exploration - Univariate Analysis

# In[18]:


#Feature Exploration (Univariate Analysis)

df['Year_Introduced'].value_counts()


# In[19]:


ax = df['Year_Introduced'].value_counts() \
    .head(10)\
    .plot(kind='bar', title = 'Top 10 Years Coasters Introdced')

ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')


# In[20]:


ax = df['Speed_Mph'].plot(kind='hist', 
                      bins=20,
                      title='Coaster Speed (mph)')

ax.set_xlabel('Speed (mph)')


# In[21]:


ax = df['Type_Main'].value_counts() \
    .plot(kind='barh', 
         title='Materials Distribution')

ax.set_ylabel('Material')


# In[ ]:





# # Feature Relationships

# In[22]:


#Exploring Feature Relationships

df.plot(kind='scatter',
        x='Speed_Mph',
        y='Height_Ft',
        title='Coaster Speed vs. Height')
plt.show()


# In[23]:


#Comparing two features (Seaborn)
sns.scatterplot(x='Speed_Mph',
                y='Height_Ft',
                hue='Year_Introduced',
                data=df)
plt.show()


# In[24]:


df


# In[ ]:


#Comparing Multiple Features
sns.pairplot(df, 
             vars=['Year_Introduced', 'Speed_Mph', 
                   'Height_Ft', 'Inversions', 'Gforce'],
            hue='Type_Main')

plt.show()


# In[30]:


df_corr = df[['Year_Introduced', 'Speed_Mph', 
    'Height_Ft', 'Inversions', 'Gforce']].dropna().corr()

df_corr


# In[33]:


sns.heatmap(df_corr, annot=True)
plt.show()


# In[ ]:





# In[35]:


#Asking Question About Data - What are the locations with the fastest roller coasters? [Minimum of 10 coasters at loc]

df['Location'].value_counts()


# In[41]:


ax = df.query('Location != "Other"')\
    .groupby('Location')['Speed_Mph']\
    .agg(['mean', 'count']) \
    .query('count >= 10')\
    .sort_values('mean')['mean']\
    .plot(kind='barh', figsize=(12, 5), title='Average Coast Speed by Location')

ax.set_xlabel('Average Coaster Speed')

plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure
from scipy.stats import f_oneway
from scipy.stats import pearsonr
from scipy.stats import kruskal
import scikit_posthocs as sp


get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

#Reading File
df = pd.read_csv(r'/Users/luciac/Desktop/Portfolio/Python Projects/movies.csv')


# # Data Exploration & Finding Missing Values

# In[2]:


# Glipse data
df.head()
pd.set_option('display.max_rows', None)


# In[3]:


# Finding any missing data

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
    


# In[5]:


# Dropping rows with missing info on budget and gross
df.dropna(subset=['budget', 'gross', 'company'], inplace=True)


# In[ ]:





# In[6]:


#Changing data type of columns
df['budget']= df['budget'].astype('int64')
df['gross']= df['gross'].astype('int64')


# In[19]:


df.head()


# In[ ]:





# In[7]:


# Extracting year from 'released' column to check consistency
df['correctyear'] = df['released'].str.extract(r'(\d{4})').astype(int)


# In[20]:


df.head()


# In[ ]:





# In[9]:


df.sort_values(by=['gross'], inplace = False, ascending = False)


# In[8]:





# In[ ]:





# In[9]:


# Droping duplicates (if any)
df.drop_duplicates()


# # Exploring Correlations & Visualisation

# In[12]:


# Identifying correlations within this dataset
# One possibility is that the budget and gross will be highly correlated
# Companies might also influence total gross


# In[13]:


# Scatter plot with budget v gross

plt.scatter(x=df['budget'], y=df['gross'])

plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget')
plt.ylabel('Gross Earnings')
plt.show()


# In[ ]:





# In[14]:


# Plotting budget v gross using seaborn
sns.regplot(x='budget', y='gross', data = df, scatter_kws ={"color": "purple"}, line_kws ={"color": "black"})


# In[ ]:





# In[15]:


# First look at correclation

df.corr(method='pearson') #Pearson

#High correlation between budget and groos


# In[16]:


correlation_matrix = df.corr(method='pearson')

sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()


# In[18]:


# Next Steps - investigating correlation with categorical variables (company, director, actor)
# However, my hypothesis is that it will be difficult to draw conclusions due to the high volume of levels 
# in the categorical variables. 


# In[ ]:





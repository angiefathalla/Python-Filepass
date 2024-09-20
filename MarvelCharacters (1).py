#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Import required libraries
#2. Read csv
import pandas as pd
marvel = pd.read_csv('charcters_stats.csv')


# In[4]:


#3. Show first records from csv
print(marvel.head(1))


# In[5]:


#4. Show number of rows and columns
print("Rows and Columns: ")
print(marvel.shape)


# In[9]:


#5. You need to find the values of alignment ,can use value_counts()
print(marvel.value_counts(subset ='Alignment'))


# In[11]:


#6. Find out only good alignment holders superheroes
print(marvel.loc[marvel['Alignment'] == 'good'])


# In[12]:


#7. Show first five records which you found in point 6
print(marvel.loc[marvel['Alignment'] == 'good'].head(5))


# In[13]:


#8. Show top five records having top speed of heroes of good alignment
print(marvel.loc[marvel['Alignment'] == 'good'].nlargest(5, ['Speed']))


# In[14]:


#9. Show 5 records of super heroes who have maximum power of good alignment
print(marvel.loc[marvel['Alignment'] == 'good'].nlargest(5, ['Power']))


# In[21]:


#10. Find out how many super heroes are there with power 100 of good alignment
print(marvel.loc[marvel['Alignment'] == 'good'].loc[marvel['Power'] == 100].count())


# In[14]:


#11. Shape them what you got in point 10
print(marvel.loc[marvel['Alignment'] == 'good'].loc[marvel['Power'] == 100])


# In[13]:


#12. Show all records from point 10
print(marvel.loc[marvel['Alignment'] == 'good'].loc[marvel['Power'] == 100])


# In[30]:


#13. Retrieve total of first five records of max power of good alignment super heroes
max_power_heroes = marvel.loc[:,['Alignment','Power']].loc[marvel['Alignment'] == 'good'].nlargest(5, ['Power']).head(5)
print(max_power_heroes)


# In[31]:


#14. Draw a bar plot of all super heroes who are having good alignment and max power of
#top five only , take same object of point 13 , show name and total in plot with green 
#bars
print(max_power_heroes.plot.bar(color = {"green"}))


# In[11]:


#15. Extract villains having bad alignment
print(marvel.loc[marvel['Alignment'] == 'bad'])


# In[12]:


#16. Show first five records of point 15
print(marvel.loc[marvel['Alignment'] == 'bad'].head(5))


# In[24]:


#17. Show top five fastest super villains in terms of super speed
print(marvel.loc[marvel['Alignment'] == 'bad'].nlargest(5, ['Speed']))


# In[25]:


#18. Top five super villains in terms of intelligence
print(marvel.loc[marvel['Alignment'] == 'bad'].nlargest(5, ['Intelligence']))


# In[27]:


#19. Show who is most dangerous super villain after calculating their total (top 5 only)
print(marvel.loc[marvel['Alignment'] == 'bad'].nlargest(5, ['Total']))


# In[9]:


#20. Draw a histogram for speed of super heroes having fig size 10,5 , provide speed in 
#histogram for only good alignment super heroes ,title should be "distribution of 
#speed" , xlabel should be "speed"
marvel.hist(column='Speed',bins=5,rwidth=10)


# In[10]:


#21. Draw a histogram for combat of super villains having fig size 10,5 , provide combat in 
#histogram for only bad alignment super heroes ,title should be "distribution of 
#combat" , xlabel should be "combat"
marvel.hist(column='Combat',bins=5,rwidth=10)


# In[ ]:





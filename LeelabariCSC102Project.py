#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
 
lyst = {'Student Name':['Oluchi Mordi', 'Adams Aliyu', 'Shania Bolade', 'Adekunle Gold', 'Blanca Edemoh'],
        'Matric Number':['ACC10211111', 'ECO10110101', 'CSC10328828', 'EEE11020202', 'MEE10202001'],
        'Department':['Accounting', 'Economics', 'Computer', 'Electrical', 'Mechanical'],
        'Level':[300, 100, 200, 200, 100]}
 
df = pd.DataFrame(lyst)

df.to_excel('leela_record.xlsx')

df


# In[6]:


import pandas as pd
   
record = {'Company':['Enron', 'Anderson', 'GK Jones', 'Mica', 'Dune'],
        'Date Founded': [1987, 1936, 2001, 1996, 2008],
        'Company Shares':[1000000, 1500000, 3000000, 250000, 800000],
          'Company Liability': [200000, 500000, 1500000, 50000, 300000],
         'Percentage Leverage': [20, 33.3, 50, 20, 37.5]}
  
df = pd.DataFrame(record)

df.to_excel('Leela_records_2.xlsx')


# In[ ]:





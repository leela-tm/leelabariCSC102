#!/usr/bin/env python
# coding: utf-8

# # Python | Pandas DataFrame

# ### What is Pandas?

# <b>pandas</b> is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. 

# ### What is a Pandas DataFrame?

# <b>Pandas DataFrame</b> is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). 
# 
# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. 
# 
# Pandas DataFrame consists of three principal components, the data, rows, and columns.

# <img src="images/pandas.jpg">

# A Pandas DataFrame will be created by loading the datasets from existing storage. Storage can be SQL Database, CSV file, and Excel file. 
# Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc.
# 
# Dataframe can be created in different ways here are some ways by which we create a dataframe:
# 

# ### Creating a dataframe using List:

# In[3]:


# import pandas as pd
import pandas as pd
 
# list of strings
lyst = ['CSC', '102', 'is', 'the', 'best', 'course', 'ever']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lyst)

# Print the output.
df


# ### Creating a dataframe using dict of narray/lists:

# In[5]:


import pandas as pd
 
# intialise data of lists.
data = {'Name':['Angela', 'Precious', 'Luis', 'Ade'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
df


# ### Column Selection:

# In[6]:


# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Clem', 'Prince', 'Edward', 'Adele'],
        'Age':[27, 24, 22, 32],
        'Address':['Abuja', 'Kano', 'Minna', 'Lagos'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
df[['Name', 'Qualification']]


# ### Row Selection:
# Pandas provide a unique method to retrieve rows from a Data frame.<br>
# <i><font color="green">DataFrame.iloc[]</font></i> method is used to retrieve rows from Pandas DataFrame.<br>

# In[7]:


import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Oyin', 'Mary', 'David', 'Bola'],
        'Age':[27, 24, 22, 32],
        'Address':['Asaba', 'Maiduguri', 'Onitsha', 'Kwara'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select first row
df.iloc[0]


# ### Read from a file:

# In[3]:


# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("employee_records.csv")

# print excel
print(data)


# ### Select first row from file

# In[6]:


# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("employee_records.csv")

df=data.iloc[0]

# print excel
df


# ### Selecting Row with Title Header

# In[10]:


# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("employee_records.csv")

df=data.head(1)

# print excel
df


# ### Looping over rows and columns
# A loop is a general term for taking each item of something, one after another.<br> Pandas DataFrame consists of rows and columns so, in order to loop over dataframe, we have to iterate a dataframe like a dictionary.<br><br>
# In order to iterate over rows, we can use two functions <i><font color="green">iteritems(), iterrows() </font></i>. These two functions will help in iteration over rows.

# In[12]:


# importing pandas as pd
import pandas as pd
  
# dictionary of lists
dict = {'name':["Abdul", "Chukwuemeka", "Seyi", "Matt"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)

# iterating over rows using iterrows() function 
for i, j in df.iterrows():
    print(i, j)
    print()


# ### Looping over Columns :
# In order to loop over columns, we need to create a list of dataframe columns and then iterating through that list to pull out the dataframe columns.

# In[15]:


# importing pandas as pd
import pandas as pd
   
# dictionary of lists
dict = {'name':["Bello", "Kamara", "Ugochi", "David"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
  
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)

# creating a list of dataframe columns
columns = list(df)
 
for i in columns:
 
    # printing the third element of the column
    print (df[i][2])


# ### Saving a DataFrame as CSV file

# In[18]:


# importing pandas as pd
import pandas as pd
   
# dictionary of lists
records = {'name':["Abel", "Kamsi", "Oyode", "Chinelo"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
  
# creating a dataframe from a dictionary 
df = pd.DataFrame(records)

# saving the dataframe
df.to_csv('record.csv')


# ## Class Project I
# 

# ####  Go to www.kaggle.com
# 
# Kaggle allows users to find and publish data sets, explore and build models in a web-based data-science environment, work with other data scientists and machine learning engineers, and enter competitions to solve data science challenges.
# 
# #### Download the following dataset:
# 1. Top Apps in Google Play
# 2. Cryptocurrency Predict Artificial Intelligence V3
# 3. Programming Laungages and File Format Detection
# 
# #### Clue
# You can signin with either Google, facebook or Linkedin account
# 
# #### Task
# Display the first 7 rows of each dataset<br>
# Select the first 3 colums of each dataset<br>
# Display only one row and header of each dataset
# 

# In[19]:


import pandas as pd

data = pd.read_csv("Top-Apps-in-Google-Play.csv")

df=data.head(7)

df


# In[20]:


import pandas as pd

data = pd.read_csv("Top-Apps-in-Google-Play.csv")

df[['App Name', 'App Id', 'Category']]


# In[21]:


import pandas as pd

data = pd.read_csv("Top-Apps-in-Google-Play.csv")

df = data.head(1)

df


# In[22]:


import pandas as pd

data = pd.read_csv("BTC_DATA_V3.0.csv")

df=data.head(7)

df


# In[23]:


import pandas as pd

data = pd.read_csv("BTC_DATA_V3.0.csv")

df[['Date', 'Price', 'Open']]


# In[24]:


import pandas as pd

data = pd.read_csv("BTC_DATA_V3.0.csv")

df = data.head(1)

df


# In[27]:


import pandas as pd

data = pd.read_csv("dataset.csv")

df=data.head(7)

df


# In[28]:


import pandas as pd

data = pd.read_csv("dataset.csv")

df[['id', 'file_path', 'file_size']]


# In[29]:


import pandas as pd

data = pd.read_csv("dataset.csv")

df=data.head(1)

df


# ## Class Project II

# In[ ]:





# <b>Cadbury Nigeria Plc</b> manufactures and sells branded fast moving consumer goods to the Nigerian market and exports in West Africa. The Company produces intermediate products, such as cocoa butter, liquor, cake and powder. It exports cocoa butter, cake and liquor to international customers, and cocoa powder locally. It operates through three segments: Refreshment Beverages, Confectionery and Intermediate Cocoa Products. The Refreshment Beverages segment includes the manufacture and sale of Bournvita and Hot Chocolate. The Confectionery segment includes the manufacture and sale of Tom Tom and Buttermint. The Intermediate Cocoa Products segment includes the manufacture and sale of cocoa powder, cocoa butter, cocoa liquor and cocoa cake. The Refreshment Beverages' brands include CADBURY BOURNVITA and CADBURY 3-in-1 HOT CHOCOLATE. The Confectionery's brands include TOMTOM CLASSIC, TOMTOM STRAWBERRY and BUTTERMINT. The Intermediate Cocoa Products' brands include COCOA POWDER and COCOA BUTTER.
# 
# You have been employed as an expert python developer to create a program to document the consumption categories of their products and brands. Using your knowledge of Pandas DataFrames develop the program that saves the list of products (export, segments and brands) in a .csv excel file.<br><br>
# Hint: save the filename as <font color="green"><i>cadbury_market.csv</i></font>.

# In[39]:


import pandas as pd
 

data = {'Refreshment Beverages':['Cadbury Bournvita', 'Cadbury 3-in-1 Hot Chocolate'],
        'Confectionary':['TomTom Classic', 'TomTom Strawberyy'],
        'Intermediate Cocoa Brands':['Cocoa Powder', 'Cocoa Butter']}
 

df = pd.DataFrame(data)
 

df.to_csv('cadbury_market.csv')


# In[ ]:





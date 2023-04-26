#!/usr/bin/env python
# coding: utf-8

# ## What is NumPy?
# 
# <ul><li>NumPy is a Python library used for working with arrays.</li>
# 
# <li>It has functions for working in domain of linear algebra, fourier transform, and matrices.</li>
# 
# <li>NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.</li></ul>

# ## Why Use NumPy?
# 
# <ul><li>In Python we have lists that serve the purpose of arrays, but they are slow to process.</li>
# 
# <li>NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.</li>
# 
# <li>The array object in NumPy is called <b>ndarray</b>, it provides a lot of supporting functions that make working with <b>ndarray</b> very easy.</li></ul>

# ## Import NumPy
# 
# Once NumPy is installed, import it in your applications by adding the <b>import</b> keyword:

# In[ ]:


import numpy


# ## NumPy as np
# 
# <ul><li>NumPy is usually imported under the np alias.</li>
# <li>Create an alias with the as keyword while importing:</li></ul>

# In[2]:


import numpy as np


# ## Checking NumPy Version
# 
# The version string is stored under __ __version__ __ attribute.

# In[4]:


import numpy as nk

print(nk.__version__)


# ## Create a NumPy ndarray Object
# <ul><li>NumPy is used to work with arrays.</li>
#     <li>The array object in NumPy is called <b>ndarray</b>.</li>
#     <li>We can create a NumPy <b>ndarray</b> object by using the <b>array()</b> function.</li>

# In[5]:


import numpy as np

arr_ = np.array([101, 201, 301, 401, 501])

print(arr_)

print(type(arr_))


# To create an <b>ndarray</b>, we can pass a list, tuple or any array-like object into the <b>array()</b> method, and it will be converted into an <b>ndarray</b>:

# In[8]:


import numpy as np

nameList = ['Angel', "Shemi", "Marvel", "Linda"]

ageTuple = (41, 32, 21, 19)

gradeDict = {"CSC102": 89, "MTH 102": 77, "CHM 102": 69, "GST 102": 99}

arr_nameList = np.array(nameList)

arr_ageTuple = np.array(ageTuple)

arr_gradeDict = np.array(gradeDict)

print(arr_nameList)
print(arr_ageTuple)
print(arr_gradeDict)


# ## Dimensions in Array
# A dimension in arrays is one level of array depth (nested arrays).

# ### 0-Dimension
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

# In[11]:


import numpy as np

classNum = int(input("How many students are in the CSC 102 class?"))

class_arr = np.array(classNum)

if (class_arr == 1):
    print("There is only ", class_arr, "student in CSC 102 class" )
else:
    print("There are", class_arr, "students in CSC 102 class" )


# ### 1-D Arrays
# <ul><li>An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.</li>
#     <li>These are the most common and basic arrays.</li>
# </ul>

# In[12]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# ### 2-D Arrays
# <ul><li>An array that has 1-D arrays as its elements is called a 2-D array.</li>
#     <li>These are often used to represent matrix or 2nd order tensors.</li></ul>

# In[14]:


import numpy as np

arr = np.array([[1, 2, 3], 4, 5, 6])

print(arr_)


# ### 3-D arrays
# <ul><li>An array that has 2-D arrays (matrices) as its elements is called 3-D array.</li>
#     <li>These are often used to represent a 3rd order tensor.</li></ul>

# In[17]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], 
               [[1, 2, 3], [4, 5, 6]], 
               [[1, 2, 3], [4, 5, 6]]])

print(arr)


# ## Check Number of Dimensions?
# NumPy Arrays provides the <b>ndim</b> attribute that returns an integer that tells us how many dimensions the array have

# In[21]:


import numpy as np

a = np.array(42)
b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([1, 2, 3, 4, 5])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# ## Higher Dimensional Arrays
# <ul><li>An array can have any number of dimensions.</li>
#     <li>When the array is created, you can define the number of dimensions by using the ndmin argument.</li>
# <li>In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.</li></ul>

# In[22]:


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=8)

print(arr)
print('number of dimensions :', arr.ndim)


# ## Access Array Elements

# In[23]:


import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])


# ## Access 2-D Arrays

# In[24]:


import numpy as np

arr = np.array([[1,2,3,4,5], 
                [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])


# ## Access 3-D Arrays

# In[25]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


# ## Negative Indexing
# Use negative indexing to access an array from the end.

# In[26]:


import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, 1])


# ## Slicing arrays
# <ul><li>Slicing in python means taking elements from one given index to another given index.</li>
#     <li>We pass slice instead of index like this: <b>[start:end]</b>.</li>
#     <li>We can also define the step, like this: <b>[start:end:step]</b>.</li>
#     <li>If we don't pass start its considered 0</li>
#     <li>If we don't pass end its considered length of array in that dimension</li>
#     <li>If we don't pass step its considered 1</li></ul>

# In[27]:


# Slice elements from index 1 to index 5 from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])


# In[29]:


# Slice elements from index 4 to the end of the array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4])


# In[31]:


# Slice elements from the beginning to index 4 (not included):

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4])


# ## Checking the Data Type of an Array

# In[32]:


import numpy as np

int_arr = np.array([1, 2, 3, 4])

str_arr = np.array(['apple', 'banana', 'cherry'])

print(int_arr.dtype)

print(str_arr.dtype)


# ## Iterating Arrays

# In[33]:


#Iterate on each scalar element of the 2-D array:
    
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y,x)


# In[36]:


# Iterate on the elements of the following 3-D array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x[0][1])
    print(x[1][0])


# ## Joining NumPy Arrays
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

# In[38]:


# Join two arrays

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


# ## Splitting NumPy Arrays
# <ul><li>Splitting is reverse operation of Joining.</li>
#     <li>Joining merges multiple arrays into one and Splitting breaks one array into multiple.</li>
#     <li>We use <b>array_split()</b> for splitting arrays, we pass it the array we want to split and the number of splits.</li></ul>

# In[42]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


# In[44]:


# Access splitted arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# ## Splitting 2-D Arrays

# In[45]:


import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], {9, 10}, [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


# In[ ]:





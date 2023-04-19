#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Print the given sequence of numbers using for loop
count = [10,20,30,40,50]
for num in count :
    print(num)


# In[2]:


#Print multiples of 10 for numbers in a given range
for num in range(5):
    if num > 0:
        print(num * 10)


# In[3]:


#Print first 5 natural number using while loop
count = 1
while count <= 5:
    print(count)
    count += 1


# In[5]:


entry = 0
sum1 = 0
print("enter numbers to find their sum, negative number ends the loop:")
while True:
    #int() typecats string to integer
    entry = int(input())
    if (entry < 0):
        break
    sum1 += entry
print("Sum =", sum1)


# In[7]:


num = 0
for num in range(6):
    num = num +1
    if num == 3:
        continue
    print('Num has value ' + str(num))
print('End of loop')


# In[8]:


for var1 in range(3):
    print( "Iteration " + str(var1 + 1) + " of outer loop")
    for var2 in range(2): #nested loop
        print(var2 + 1)
    print("Out of inner loop")
print("Out of outer loop")


# In[9]:


#Python program to swap two cities

#To take inputs from the user
city_1 = input('Enter name of City 1: ')
city_2 = input('Enter name of City 2: ')

# create a temporary variable and swap the cities
temp = city_1
city_1 = city_2
city_2 = temp

print(f"The name of City 1 after swapping is {city_1}")
print(f"The name of City 2 after swapping is {city_2}")


# In[10]:


#Program to check if a Number is Positive, Negative or 0

num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[11]:


# COUPE DE ESCRIVA 2023: FOOTBALL PICKS

print("Welcome to the COUPE DE ESCRIVA 2023: FOOTBALL PICKS \n")

captain = {'Madiba: ': 'Chubby Obiora-Okafor: ', 'Blue-Jays: ': 'Christopher Uweh', 'Cirok: ': 'Alexander', 'TSG Walkers: ': 'Ikechukwu'}

goalkeepers = {'Madiba: ': 'Chubby Obiora-Okafor', 'Blue-Jays: ': 'Oladimeji Abaniwondea/Jeffery Awagu', 'Cirok: ': 'Timileyin Pearse/Izuako Jeremy', 'TSG Walkers: ': 'Ayomide Ojituku'}

for pick in captain:
    print(pick, captain[pick])
    
print("\n")

for pick in goalkeepers:
    print(pick, goalkeepers[pick])


# In[ ]:





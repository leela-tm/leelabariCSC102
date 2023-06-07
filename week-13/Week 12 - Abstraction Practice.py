#!/usr/bin/env python
# coding: utf-8

# # What is Abstraction in OOP

# <ul><li>Abstraction is the concept of object-oriented programming that “shows” only essential attributes and “hides” unnecessary information.</li><li>The main purpose of abstraction is hiding the unnecessary details from the users. </li><li> Abstraction is selecting data from a larger pool to show only relevant details of the object to the user. </li><li> It helps in reducing programming complexity and efforts. </li><li>It is one of the most important concepts of OOPs.</li></ul> 

# # Abstraction in Python

# <ul><li>Abstraction in python is defined as hiding the implementation of logic from the client and using the particular application. </li><li>It hides the irrelevant data specified in the project, reducing complexity and giving value to the efficiency.</li><li> Abstraction is made in Python using <b>Abstract classes</b> and their methods in the code.</li></ul>

# ## What is an Abstract Class?

# <ul><li>Abstract Class is a type of class in OOPs, that declare one or more abstract methods. </li><li>These classes can have abstract methods as well as concrete methods. </li><li>A normal class cannot have abstract methods.</li><li>An abstract class is a class that contains at least one abstract method.</li></ul>

# ## What are Abstract Methods?
# <ul><li>Abstract Method is a method that has just the method definition but does not contain implementation.</li><li>A method without a body is known as an Abstract Method.</li><li>It must be declared in an abstract class.</li><li>The abstract method will never be final because the abstract class must implement all the abstract methods.</li></ul>

# ## When to use Abstract Methods & Abstract Class?
# <ul><li>Abstract methods are mostly declared where two or more subclasses are also doing the same thing in different ways through different implementations.</li><li>It also extends the same Abstract class and offers different implementations of the abstract methods.</li><li>Abstract classes help to describe generic types of behaviors and object-oriented programming class hierarchy. </li><li>It also describes subclasses to offer implementation details of the abstract class.</li></ul>

# ## Difference between Abstraction and Encapsulation

# <table style="background-color:#ffe6e6">
#     <tr><th><b>Abstraction</b></th><th><b>Encapsulation</b></th></tr>
#     <tr><td>Abstraction in Object Oriented Programming solves the issues at the design level.</td><td>Encapsulation solves it implementation level.</td></tr>
#     <tr><td>Abstraction in Programming is about hiding unwanted details while showing most essential information.</td><td>Encapsulation means binding the code and data into a single unit.</td></tr>
#     <tr><td>Data Abstraction in Java allows focussing on what the information object must contain</td><td>Encapsulation means hiding the internal details or mechanics of how an object does something for security reasons.</td></tr>
# </table>

# ## Advantages of Abstraction
# <ol><li>The main benefit of using an Abstraction in Programming is that it allows you to group several related classes as siblings.</li><li>
# Abstraction in Object Oriented Programming helps to reduce the complexity of the design and implementation process of software.</li></ol>

# ## How Abstract Base classes work : 
# <ul><li>By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. </li><li>ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. </li><li>A method becomes abstract when decorated with the keyword @abstractmethod.</li></ul>

# #### Syntax
# 
# Abstract class Syntax is declared as:

# In[1]:


from abc import ABC

# declaration
class classname(ABC):
    pass
        


# Abstract method Syntax is declared as

# In[5]:


def abstractmethod_name(self):
    pass


# ### Few things to be noted in Python:
# 
# <ul><li>In python, an abstract class can hold both an abstract method and a normal method.</li><li>
# The second point is an abstract class is not initiated (no objects are created).</li><li>
# The derived class implementation methods are defined in abstract base classes.</li></ul>

# In[6]:


from abc import ABC

# here abc and ABC are case-sensitive. When we swap it creates


# ### Code I:

# In[8]:


from abc import ABC, abstractmethod

# Abstract Class
class product(ABC):                    
    
    # Normal Method
    def item_list(self, rate):
        print("amount submitted : ",rate)
    
    # Abstract Method
    @abstractmethod
    def product(self,rate):                      
        pass


# ### Code II:
# A program to generate the volume of geometric shapes

# In[13]:


from abc import ABC

class geometric(ABC):
    
    def volume(self):
        #abstract method
        pass
    
class Rect(geometric):
    length = 4
    width = 6
    height = 6
    
    def volume(self):
        return self.length * self.width *self.height
    
class Sphere(geometric):
    radius = 8
    def volume(self):
        return 1.3 * 3.14 * self.radius * self.radius *self.radius
    
class Cube(geometric):
    Edge = 5
    def volume(self):
        return self.Edge * self.Edge *self.Edge
    
class Triangle_3D:
    length = 5
    width = 4
    def volume(self):
        return 0.5 * self.length * self.width
    
rr = Rect()
ss = Sphere()
cc = Cube()
tt = Triangle_3D()
print("Volume of a rectangle:", rr.volume())
print("Volume of a circle:", ss.volume())
print("Volume of a square:", cc.volume())
print("Volume of a triangle:", tt.volume())


# ### Code III
# A program to generate different invoices

# In[20]:


from abc import ABC, abstractmethod

class Bill(ABC):
    def final_bill(self, pay):
        print('Purchase of the product: ', pay)
        
    @abstractmethod
    def Invoice(self, pay):
        pass
    
class paycheque(Bill):
    def Invoice(self, pay):
        print('paycheque of: ', pay)
        
class CardPayment(Bill):
    def Invoice(self, pay):
        print('pay through card of: ', pay)
        
aa = paycheque()
aa.Invoice(6500)
aa.final_bill(6500)
print(isinstance(aa,paycheque))

aa = CardPayment()
aa.Invoice(2600)
aa.final_bill(2600)
print(isinstance(aa,CardPayment))


# ### Code IV:
#  Python program showing abstract base class work

# In[23]:


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    
    def move(self,Animal):
        print(f"\n You are {animal}. You can walk and run")

class Snake(Animal):
    
    def move(self,animal):
        print(f"\n You are a {animal}. You can crawl")

class Dog(Animal):

    def move(self,animal):
        print(f"\n You are a {animal}. You can bark")

class Lion(Animal):
    
    def move(self,animal):
        print(f"\n You are a {animal}. You can roar")

# Object Instantiation
animal = input("What animal specie are you?: ")

if animal == "Human":
    H = Human()
    H.move(animal)
elif animal == "Snake":
    S = Snake()
    S.move(animal)
elif animal == "Dog":
    D = Dog()
    D.move(animal)
elif animal == "Lion":
    L = Lion()
    L.move(animal)
else:
    print("Invalid animal specie")


# ### Concrete Methods in Abstract Base Classes : 
# <ul><li>Concrete (normal) classes contain only concrete (normal) methods whereas abstract classes may contain both concrete methods and abstract methods.</li><li> The concrete class provides an implementation of abstract methods, the abstract base class can also provide an implementation by invoking the methods via super().</li></ul>

# ### Code V:
# Python program invoking a method using super()

# In[33]:


from abc import ABC, abstractmethod

class R(ABC):
    
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass")

# Object instantiation
r = K()
r.rk()


# ### Code VI:

# In[32]:


from abc import ABC, abstractmethod

class Bank(ABC):
    def branch(self, Naira):
        print("Fees submitted : ",Naira)
   
    @abstractmethod
    def Bank(Naira):
        pass
        
    
class private(Bank):
    
    def Bank(Naira):
        print("Total Naira Value here: ",Naira)
        
class public(Bank):
    
    def Bank(Naira):
        print("Total Naira Value here:",Naira)

private.Bank(5000)
public.Bank(2000)

a = public()
#a.branch(3500)


# ## Class Project I

# Develop a python OOP program that creates an abstract base class called coup_de_ecriva.  The base class will have one abstract method called <b>Fan_Page</b> and four subclassses namely; <b>FC_Cirok, Madiba_FC, Blue_Jay_FC and TSG_Walker</b>. The program will receive as input the name of the club the user supports and instantiate an object that will invoke the <b>Fan_Page</b> method in the subclass that prints Welcome to <b>"club name"</b>.
# 
# <p><b>Hint:</b></p>
# The subclasses will use <b>Single Inheritance</b> to inherit the abstract base class.
#  

# In[ ]:


from abc import ABC

class coup_de_escriva(ABC):
    
    @abstractmethod
    def Fanpage(self):
        pass


class FC_Cirok(coup_de_escriva):
    
    def Fanpage(self, club):
        print('Welcome to ', club)
        
class Madiba_FC(coup_de_escriva):
    def Fanpage(self, club):
        print('Welcome to ', club)

class Blue_Jay_FC(coup_de_escriva):
    def Fanpage(self, club):
        print('Welcome to ', club)
        
class TSG_Walker(coup_de_escriva):
    def Fanpage(self, club):
        print('Welcome to ', club)
        
club = input('What club do you support?')

if club == "FC_Cirok":
    F = FC_Cirok()
    F.Fanpage(club)
    
elif club == "TSG_Walker":
    T = TSG_Walker()
    T.Fanpage(club)
    
elif club == "Madiba_FC":
    M = Madiba_FC()
    M.Fanpage(club)
    
elif club == "Blue_Jay_FC":
    B = Blue_Jay_Fc()
    B.Fanpage(club)
    
else:
    print('Your club is not available')
    


# ## Class Project II

# The Service Unit of PAU has contacted you to develop a program to manage some of the External Food Vendors. With your knowledge in python OOP develop a program to manage the PAU External Food Vendors. The program receives as input the vendor of interest and display the menu of the interested vendor. The External vendors are Faith hostel, Cooperative Hostel, and Student Center. Find below the menus:
# 
# <table><tr><td>
# <table style="background-color:#47b5ff">
#     <tr><th colspan='2'>Cooperative Cafeteria</th></tr>
#     <tr><th>Main Meal</th><th>Price (N)</th></tr>
#     <tr><td>Jollof Rice and Stew</td><td>200</td></tr>
#     <tr><td>White Rice and Stew</td><td>200</td></tr>
#     <tr><td>Fried Rice</td><td>200</td></tr>
#     <tr><td>Salad</td><td>100</td></tr>
#     <tr><td>Platain</td><td>100</td></tr>
# </table>
#     </td><td>
# <table style="background-color:pink">
#     <tr><th colspan='2'>Faith Hostel Cafeteria</th></tr>
#     <tr><th>Main Meal</th><th>Price (N)</th></tr>
#     <tr><td>Fried Rice</td><td>400</td></tr>
#     <tr><td>White Rice and Stew</td><td>400</td></tr>
#     <tr><td>Jollof Rice</td><td>400</td></tr>
#     <tr><td>Beans</td><td>200</td></tr>
#     <tr><td>Chicken</td><td>1000</td></tr>
# </table>
#     </td><td>
#     <table style="background-color:#fcf96c">
#     <tr><th colspan='2'>Student Centre Cafeteria</th></tr>
#     <tr><th>Main Meal</th><th>Price (N)</th></tr>
#     <tr><td>Chicken Fried Rice</td><td>800</td></tr>
#     <tr><td>Pomo Sauce</td><td>300</td></tr>
#     <tr><td>Spaghetti Jollof</td><td>500</td></tr>
#     <tr><td>Amala/Ewedu</td><td>500</td></tr>
#     <tr><td>Semo with Eforiro Soup</td><td>500</td></tr>
# </table>
#     </td></tr>
# <table>
#     
# <p><b>Hints:</b></p>
#     <ul><li>The abstract base class is called <b>External_Vendors()</b>.</li><li>
#         The abstract method is called <b>menu()</b>.</li><li>
# The subclasses (the different vendors) will inherit the abstract base class.</li><li>
#         Each subclass will have a normal method called <b>menu()</b>.</li></ul>
#     
#        

# In[ ]:


from abc import ABC, abstractmethod

class External_Vendors(ABC):
    @abstractmethod
    def menu(self):
        pass

class CooperativeCafeteria(External_Vendors):
    def menu(self, vendor):
        print("Cooperative Cafeteria Menu")
        print("Main Meal\tPrice (N)")
        print("Jollof Rice and Stew\t200")
        print("White Rice and Stew\t200")
        print("Fried Rice\t200")
        print("Salad\t100")
        print("Platain\t100")

class FaithHostelCafeteria(External_Vendors):
    def menu(self, vendor):
        print("Faith Hostel Cafeteria Menu")
        print("Main Meal\tPrice (N)")
        print("Fried Rice\t400")
        print("White Rice and Stew\t400")
        print("Jollof Rice\t400")
        print("Beans\t200")
        print("Chicken\t1000")

class StudentCentreCafeteria(External_Vendors):
    def menu(self, vendor):
        print("Student Centre Cafeteria Menu")
        print("Main Meal\tPrice (N)")
        print("Chicken Fried Rice\t800")
        print("Pomo Sauce\t300")
        print("Spaghetti Jollof\t500")
        print("Amala/Ewedu\t500")
        print("Semo with Eforiro Soup\t500")



vendor = input("Enter the name of the vendor (Cooperative Hostel, Faith Hostel, or Student Center) ")

if vendor() == "Cooperative hostel":
        cafeteria = CooperativeCafeteria()
        
elif vendor() == "Faith hostel":
        cafeteria = FaithHostelCafeteria()
        
elif vendor() == "Student center":
        cafeteria = StudentCentreCafeteria()
        
else:
        print("Invalid vendor name.")
       



    


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Inheritance in Python

# Inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are: 
#  
# <ol><li>
# It represents real-world relationships well.</li><li>
# It provides reusability of a code, so that you don’t have to write the same code again and again. </li><li>It allows for adding more features to a class without modifying it.</li><li>
# It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.</li><ol>

# ### A Python program to demonstrate inheritance

# In[7]:


class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name method
    def getname(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False
    

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here employee method returns true
    def isEmployee(self):
        return True

# Object Instantiation
emp = Person("April Apakama") # An Object of Person
print(emp.getname(), emp.isEmployee())

emp = Employee("Chidum Umeh") # An Object of Employee
print(emp.getname(), emp.isEmployee())


# ### What is object class? 
# In Python (from version 3.x), object is root of all classes. 
# In Python 3.x, <b>“class Test(object)”</b> and <b>“class Test”</b> are same. 
# 
# ### Subclassing (Calling constructor of parent class) 
# <ul><li>A child class needs to identify which class is its parent class.</li><li> This can be done by mentioning the parent class name in the definition of the child class. 
# Eg: class subclass_name (superclass_name): </li></ul>

# In[8]:


# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

        # __init__ is known as the constructor
        def __init__(self, name, idnumber):
            self.name = name
            self.idnumber = idnumber
            
        def display(self):
            print("Name:", self.name)
            print("ID No.:", self.idnumber)
            print("Salary:", self.salary)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post, age):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self)

                
# creation of an object variable or an instance
a = Employee('Basit Inaolaji', 886012, 200000, "Intern", 32)

# calling a function of the class Person using its instance
a.display()


# ### Note that:
# <ul><li>In Python, every class inherits from a built-in basic class called ‘object’. The constructor i.e. the ‘__init__’ function of a class is invoked when we create an object variable or an instance of the class.</li><li>
# The variables defined within __init__() are called as the instance variables or objects. Hence, ‘name’ and ‘idnumber’ are the objects of the class Person. Similarly, ‘salary’ and ‘post’ are the objects of the class Employee.</li><li> Since the class Employee inherits from class Person, ‘name’ and ‘idnumber’ are also the objects of class Employee.</li><li>
# If you forget to invoke the __init__() of the parent class then its instance variables would not be available to the child class. </li></ul>

# In[10]:


# Python program to demonstrate error if we
# forget to invoke __init__() of the parent.

class A:
    def __init__(self, n = 'Ehi Elijah'):
        self.name = n
        
class B(A):
    def __init__(self, roll):
        self.roll = roll

# Object Instance
object = B(23)
print (object)


# ## Types of Inheritance in Python
# There are four types of inheritance in Python. The type of Inheritance depends upon the number of child and parent classes involved. : 
# 
# #### Single Inheritance:
# <ul><li> Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.</li></ul>

# In[14]:


# Python program to demonstrate
# single inheritance


# Base class
class parents: 
    def func1(self):
        print("This function is in parent class.")

# Derived class
class Child(parents):
    def func2(self):
        print("This function is in child class.")

# Object Instance
object = Child()
object.func1()
object.func2()


# #### Multiple Inheritance:
# <ul><li>When a class can be derived from more than one base class this type of inheritance is called multiple inheritance. </li><li>In multiple inheritance, all the features of the base classes are inherited into the derived class. </li></ul>
#  

# In[19]:


# Python program to demonstrate
# multiple inheritance


# Base class1
class Mother: 
    motherName = "Caroline Aina"
    def mother(self):
        print(self.mothername)

# Base class2
class Father:
    fathername = "Paul Abiodun"
    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.motherName)

# Object Instance
s1 = Son()
s1.parents()


# #### Multilevel Inheritance
# <ul><li>In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.</li><li> This is similar to a relationship representing a child and grandfather.</li></ul> 

# In[27]:


# Python program to demonstrate
# multilevel inheritance

# Base class
class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname

        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

# Object Instance
s1 = Son('Gbenga', 'Abiodun', 'Oluwafemi')
print(s1.grandfathername)
s1.print_name()


# #### Hierarchical Inheritance:
# <ul><li>When more than one derived classes are created from a single base this type of inheritance is called hierarchical inheritance.</li><li> In this program, we have a parent (base) class and two child (derived) classes.</li></ul>

# In[32]:


# Python program to demonstrate
# Hierarchical inheritance


# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derivied class2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Object Instantiation
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# #### Hybrid Inheritance:
# <ul><li>Inheritance consisting of multiple types of inheritance is called hybrid inheritance.</li></ul>

# In[35]:


# Python program to demonstrate
# hybrid inheritance


class School():
    def func1(self):
        print("This function is in school.")

class Student1(School):
    def func2(self):
        print("This function is in student 1. ")

class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Object Instantiation
object = Student3()
object.func1()
object.func2()


# # Polymorphism in Python

# <ul><li>In programming, Polymorphism is a concept of OOP.</li><li>The word polymorphism means having many forms.</li><li>
#     It enables using a single interface with the input of different data types, different classes or maybe for a different number of inputs.</li><li>Polymorphism means the same function name (but different signatures) being used for different types.</li></ul>

# ### Inbuilt polymorphic functions

# In[37]:


# Python program to demonstrate in-built polymorphic functions

# len() being used for a string
print(len("Department of Computer Science"))

# len() being used for a list
print(len([10, 20, 30, 40, 50, 60, 70]))


# ### User-defined polymorphic functions : 

# In[39]:


# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z = 0, w = 4): 
    return x + y + z 

# Driver code
print(add(2, 3))
print(add(2, 3, 4))
print(add(2, 3, 5, 6))


# ### Polymorphism with class methods: 
# <ul><li>The code below shows how Python can use two different class types, in the same way.</li><li> We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class.</li></ul> 

# In[43]:


class Nigeria():
    def capital(self):
        print("Lagos is the capital of Nigeria.")

    def language(self):
        print("English is the official language of Nigeria.")

    def type(self):
        print("Nigeria is the giant of Africa.")

class Togo():
    def capital(self):
        print("Lome is the capital of Togo.")

    def language(self):
        print("French is the primary language of Togo.")

    def type(self):
        print("Togo is known for its palm-lined beaches and hilltop villages.")

obj_naija = Nigeria()
obj_togo = Togo()
for country in (obj_naija, obj_togo):
    country.capital()
    country.language()
    country.type()


# ### Polymorphism with Inheritance:
# <ul><li>In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class.</li><li> However, it is possible to modify a method in a child class that it has inherited from the parent class.</li><li> This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method in the child class.</li><li> This process of re-implementing a method in the child class is known as <b>Method Overriding. </b> </li></ul>

# In[4]:


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):
    def flight(selfie):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


# # Class Project I

# Mary, Agatha and Noel work with Zenith Bank Nigeria. Mary works in the Retail Banking Division, Agatha works in the Global Banking Division and Noel works in the Commercial Banking Division. The three divisions have some unique services and some mutual services as indicated:
# 
# #### Retail Banking:
# <ul><li>Lines of credit</li><li>
# Investment management and accounts</li><li>
# Insurance</li><li>
# Retirement and education accounts</li><li>
#     loans and mortgagges</li><li>
#     Checking and saving</li></ul>
# 
# #### Global Banking:
# <ul><li>Multi-currency management services and products</li><li>
# Foreign currency accounts</li><li>
# Foreign currency credit cards</li><li>
# Transborder advisory services</li><li>
# Liquidity management</li></ul>
# 
# #### Commercial Banking:
# <ul><li>Lines of credit</li><li>
# Investment management and accounts</li><li>
# Insurance</li><li>
# Advisory services</li></ul>
# 
# With your knowledge in OOP develop a python program that will take as input an employee name and division, and then displays the service rendered in the division. The program should highlght key concepts of OOP; class objects inheritance and polymorphism.
# 
# #### Hints:
# <ul><li>Create parent class <b>zenith()</b> with two methods <b>unique_services()</b> and <b>mutual_services()</b></li><li>
#     The different divisions can be subclasses of the parent class, inheriting the parent methods.</li><li>
#     Ploymorphism can be used to overide exclusive services.</li><ul>

# In[7]:


class Zenith:
    def unique_services(self):
        pass
    
    def mutual_services(self):
        pass


class RetailBanking(Zenith):
    def unique_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance",
            "Retirement and education accounts",
            "Loans and mortgages",
            "Checking and saving"
        ]
    
    def mutual_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance"
        ]


class GlobalBanking(Zenith):
    def unique_services(self):
        return [
            "Multi-currency management services and products",
            "Foreign currency accounts",
            "Foreign currency credit cards",
            "Transborder advisory services",
            "Liquidity management"
        ]
    
    def mutual_services(self):
        return []


class CommercialBanking(Zenith):
    def unique_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance",
            "Advisory services"
        ]
    
    def mutual_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance"
        ]


def display_services(employee_name, division):
    if division == "Retail Banking":
        employee_division = RetailBanking()
    elif division == "Global Banking":
        employee_division = GlobalBanking()
    elif division == "Commercial Banking":
        employee_division = CommercialBanking()
    else:
        print("Invalid division!")
        return
    
    unique_services = employee_division.unique_services()
    mutual_services = employee_division.mutual_services()
    
    print(f"Services for {employee_name} in {division}:")
    print("Unique Services:")
    for service in unique_services:
        print("- " + service)
    
    print("\nMutual Services:")
    for service in mutual_services:
        print("- " + service)


# Test the program
employee_name = input("Enter employee name: ")
division = input("Enter division: ")

display_services(employee_name, division)


# In[ ]:





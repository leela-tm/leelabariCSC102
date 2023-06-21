#!/usr/bin/env python
# coding: utf-8

# # CONNECTING PYTHON WITH POSTGRES DATABASE 

# ### 1. CREATE A DATABSE student_profile

# In[2]:


import psycopg2

# Establish a connection to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="menegbo5"
)

# Create a new database
new_db_name = "student_profile"
conn.autocommit = True
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE {new_db_name};")

cursor.close()


# Close the connection
conn.close()


# ### 2. CREATE A TABLE student_info

# In[ ]:


# Establish a connection to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="student_profile",
    user="postgres",
    password="csc101"
)
# Create a cursor object
cursor = conn.cursor()

# Define the CREATE TABLE statement
create_table_query = '''
    CREATE TABLE student_info (
        name varchar,
        email varchar,
        mat_no varchar  )
'''

# Execute the CREATE TABLE statement
cursor.execute(create_table_query)


# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


# ### 3. INSERT INTO TABLE student_info

# In[80]:


import psycopg2

# Establish a connection to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="student_profile",
    user="postgres",
    password="csc101"
)

# Create a cursor object
cursor = conn.cursor()

# Define the INSERT statement
insert_query = '''
    INSERT INTO student_info (name, email, mat_no)
    VALUES (%s, %s, %s)
'''

# Define the values to be inserted
values = ('Ade Jones', 'ajones@pau.edu.ng', '121234222')

# Execute the INSERT statement
cursor.execute(insert_query, values)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


# ### 4. SELECT ALL FROM student_info

# In[81]:


import psycopg2

# Establish a connection to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="student_profile",
    user="postgres",
    password="csc101"
)

# Create a cursor object
cursor = conn.cursor()

# Define the SELECT statement
select_query = "SELECT * FROM student_info;"

# Execute the SELECT statement
cursor.execute(select_query)

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Process the fetched rows
for row in rows:
    # Access individual columns using index or column names
    column1_value = row[0]
    column2_value = row[1]
    column3_value = row[2]
    
    print(f"{column1_value} | {column2_value} | {column3_value}")

# Close the cursor and connection
cursor.close()
conn.close()


# ### 5. DELETE FROM student_info

# In[82]:


import psycopg2

# Establish a connection to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="student_profile",
    user="postgres",
    password="csc101"
)

# Create a cursor object
cursor = conn.cursor()

# Define the DELETE statement
delete_query = "DELETE FROM student_info;"

# Execute the DELETE statement
cursor.execute(delete_query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


# # CLASS PROJECT I
# 
# 
# 

# <ul>
#     <li>Create a database called <b><i>mtn_nigeria</i></b></li>
# <li>Create a table called <b><i>customer_info</i></b></li>
# <li>Insert the following customer information into the database</li>
# </ul>
# 

# In[73]:


import pandas as pd

customer_info = {"Name": ["Favor Okpara-Ngbo", "Joshua Asekhauno", "Collins Odoh-Ifeanyi", "Chibundum Umeh", "Clinto Okpara"], 
  "Email": ["fokpara-ngbo@mtn.com", "jasekhauno@mtn.com", "codoh-ifeanyi@mtn.com", "cumeh@mtn.com", "cokpara@mtn.com"], 
  "State of Residence": ["Lagos", "Portharcourt", "Abuja", "Owerri", "Kaduna"],
   "Mobile": ["08038212938", "080374930210", "08067392029","0803493712348", "08068381138"]}
info = pd.DataFrame(customer_info)
info


# In[4]:


import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="student_profile",
    user="postgres",
    password="menegbo5"
)

new_db_name = "mtn_nigeria"
conn.autocommit = True
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE {new_db_name};")

cursor.close()


conn.close()


# In[13]:


import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mtn_nigeria",
    user="postgres",
    password="menegbo5"
)

cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE customer_info (
        name varchar,
        email varchar,
        state_of_residence varchar,
        mobile varchar  );
'''

cursor.execute(create_table_query)


conn.commit()

cursor.close()
conn.close()


# In[20]:


import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mtn_nigeria",
    user="postgres",
    password="menegbo5"
)

cursor = conn.cursor()

insert_query = '''
    INSERT INTO customer_info (name, email, state_of_residence, mobile)
    VALUES (%s, %s, %s, %s)
'''

values = [('Favor Okpara-Ngbo', 'fokpara@mtn.com', 'Lagos', '08038212938'),
('Joshua Asekhauno', 'jasekhauno@mtn.com', 'Portharcourt', '080374930210'),
('Collins Odoh-Ifeanyi', 'codoh-ifeanyi@mtn.com', 'Abuja', '08067392029'),
('Chibundum Umeh', 'cumeh@tn.com', 'Owerri', '0803493712348'),
('Clinto Okpara', 'cokpara@mtn.com', 'Kaduna', '08068381138')
]

cursor.executemany(insert_query, values)

conn.commit()

cursor.close()
conn.close()


# # Class Project II

# <ul>
#     <li>Create a database called <b><i>comp_sci_dpt</i></b></li>
# <li>Create a table called <b><i>csc102_class_list</i></b></li>
# <li>Download the class list .csv file from e-learning</li>
# <li>Insert the the class list into the database</li>
# <li>Dump the database and class list table</li>
# <li>Commit the python code and dumped database to your GitHub (Week 14)</li>
# </ul>
# 

# In[15]:


import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="menegbo5"
)

new_db_name = "comp_sci_dpt"
conn.autocommit = True
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE {new_db_name};")

cursor.close()


conn.close()


# In[16]:


import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="comp_sci_dpt",
    user="postgres",
    password="menegbo5"
)

cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE csc102_class_list (
        first_name varchar,
        middle_name varchar,
        surname varchar)
'''

cursor.execute(create_table_query)


conn.commit()

cursor.close()
conn.close()


# In[36]:


import pandas as pd
import psycopg2

data = pd.read_csv("csc102_class_list_II.csv")
df = pd.DataFrame(data)


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="menegbo5"
)

cursor = conn.cursor()

for row in df.itertuples():
    cursor.execute(
        'INSERT INTO csc102_class (first_name, middle_name, surname) VALUES (%s,%s,%s)',
                '(row.FIRST NAME, row.MIDDLE NAME, row.SURNAME)'
                )
conn.commit()

cursor.close()
conn.close()


# In[26]:


import pandas as pd 

data = pd.read_csv("csc102_class_list_II.csv")
df = pd.DataFrame(data)

print(df)


# In[ ]:





# we need a module named : mysql-connector-python

import mysql.connector as msl

conn = msl.connect(
    host="localhost",
    user="root",
    password="pradipto1",
    database="student"
)

print("Connected to mysql server successfully and database connection successful")

cursor = conn.cursor()
cursor.execute("SELECT * FROM marksdetails")

for i in cursor:
    print(i)
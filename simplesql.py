#!C:\Users\Astitva Rastogi\AppData\Local\Programs\Python\Python39\python.exe

print ("Content-type:text/html\r\n\r\n")
import cgitb
import mysql.connector
# Open database connection

db= mysql.connector.connect(user='root',
        password="", host='localhost', port=3306, database="TESTDB")
# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("%s " % data)

# disconnect from server

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
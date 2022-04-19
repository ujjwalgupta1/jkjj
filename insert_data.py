#!C:\Users\Astitva Rastogi\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-type:text/html\r\n\r\n")
import cgitb
import mysql.connector
# Open database connection

db= mysql.connector.connect(user='root', password="", host='localhost', port=3306,database="TESTDB")
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('suchita', 'arora',35,'F', 32000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnet
db.close()
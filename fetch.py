#!C:\Users\Suchi\AppData\Local\Programs\Python\Python37-32\python.exe
print ("Content-type:text/html\r\n\r\n")
import cgitb
import mysql.connector
# Open database connection

db= mysql.connector.connect(user='root',
        password="", host='localhost', port=3306,database="TESTDB")
# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()
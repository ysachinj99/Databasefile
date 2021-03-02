import mysql.connector
mydb=mysql.connector.connect(
     host='localhost',
     user='root',
     password='sachin',
     database='fy2'
     )
cur=mydb.cursor()

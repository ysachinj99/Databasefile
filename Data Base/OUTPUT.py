import mysql.connector
conn= mysql.connector.connect(user="root",password="sachin",host="127.0.0.1",database="fy2")
cursor= conn.cursor()
#preperaing Sql Query to INSERT a record into the Database.
sql ='''SELECT * FROM STUDENT'''
cursor.execute(sql)
result= cursor.fetchone();
print(result)
result= cursor.fetchall();
print(result)
conn.close()

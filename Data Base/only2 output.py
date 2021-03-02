import mysql.connector
conn= mysql.connector.connect(user="root",password="sachin",host="127.0.0.1",database="fy2")
cursor= conn.cursor()
sql= '''SELECT * FROM STUDENT'''
cursor.execute(sql)
result= cursor.fetchmany(size=2);
print(result)
conn.close()

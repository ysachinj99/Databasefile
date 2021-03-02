import mysql.connector
conn = mysql.connector.connect(user="root",password="sachin",host="127.0.0.1",database="fy2")
cursor= conn.cursor()
sql=''' CREATE TABLE STUDENT(NAME varchar(50),Roll_no int,Stream varchar(50),Year varchar(50),Result varchar(50))'''
cursor.execute(sql)
print("Table Created Sucessfully")
conn.close()

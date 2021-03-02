import mysql.connector
conn=mysql.connector.connect(user="root",password="sachin",host="127.0.0.1")
print("Connection Sucessful")
cursor=conn.cursor()
sql="CREATE database fy2";
cursor.execute(sql)
print("List Of Data Base")
cursor.execute("SHOW DATABASES");
print(cursor.fetchall())
conn.close()

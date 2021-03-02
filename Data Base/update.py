import mysql.connector
conn= mysql.connector.connect(user="root",password="sachin",host="127.0.0.1",database="fy2")
cursor= conn.cursor()
sql ='''UPDATE STUDENT SET Stream = %s WHERE Result = %s '''
value= ("Bsc-cs","Fail")
try:
      cursor.execute(sql,value)
      conn.commit()
      
except:
      conn.rollback()
sql= '''SELECT * FROM STUDENT '''
cursor.execute(sql)
print("Updated Sucessfully")
print(cursor.fetchall())
conn.close()

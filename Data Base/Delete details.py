import mysql.connector
conn= mysql.connector.connect(user="root",password="sachin",host="127.0.0.1",database="fy2")
cursor= conn.cursor()
print("Content of Table:")
cursor.execute("SELECT * FROM STUDENT")
print(cursor.fetchall())
Query = ''' DELETE FROM STUDENT WHERE Result = 'Fail' '''
#value = "Fail"
cursor.execute (Query)
try:
      cursor.execute(Query)
      conn.commit()
except:
      conn.rollback()
      print("Content of all table after Delete operation")
      cursor.execute("SELECT * FROM STUDENT")
      print(cursor.fetchall())
      conn.commit()    
conn.close()
  

import mysql.connector
conn= mysql.connector.connect(user="root",password="sachin",host="127.0.0.1",database="fy2")
cursor= conn.cursor()
#preperaing Sql Query to INSERT a record into the Database.
insert_stmt = "INSERT INTO STUDENT (NAME,Roll_no,Stream,Year,Result)VALUES(%s,%s,%s,%s,%s)"
data = [("Krishna",19,"BSC-CS","F_year","Pass"),("Ramya",25,"BSC-CHEM","S_year","Pass"),("Ram",42,"B-COM","S_year","Fail")]
try:
      cursor.executemany(insert_stmt,data)
      conn.commit()
      print("Data insert Sucessfully")
except:
      conn.rollback()
conn.close()

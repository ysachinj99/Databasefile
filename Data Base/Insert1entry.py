import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='sachin', host='127.0.0.1', database='fy2')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO STUDENT(NAME,Roll_no,Stream,Year,Result)VALUES(%s,%s,%s,%s,%s)"""
v = ('SACHIN',76,'BSC-CS','1st','Pass')
#try:
   # Executing the SQL command
cursor.execute(sql,v)

   # Commit your changes in the database
conn.commit()
print("Data Inserted Sucessfully")
#except:
   # Rolling back in case of error
#conn.rollback()

# Closing the connection
#conn.close()

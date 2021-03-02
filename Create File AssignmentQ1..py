file = open ("D://Python//Bsc.txt","w")
file.write("76-Yadav Sachin")
file.close
file = open ("D://Python//Bsc.txt","r")
a = file.read()
print(a)
file.close
file = open ("D://Python//Bsc.txt","a")
file.write("\n Welcome To Python World!!")
file = open ("D://Python//Bsc.txt","r")
a = file.read()
print(a)
file.close
import os
os.remove("D://Python//Bsc.txt")
print("File Removed Sucessfully")


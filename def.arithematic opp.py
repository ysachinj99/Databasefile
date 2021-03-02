def add(x,y):
     return(x+y)
def sub(x,y):
     return(x-y)
def mul(x,y):
     return(x*y)
def div(x,y):
     return(x/y)
a= int(input("Enter the NO."))
b= int (input("Enter a No:"))
c=add(a,b)
d=sub(a,b)
e=mul(a,b)
f=div(a,b)
print("Addition of NO",(a,b),"is",c)
print("Subtraction of NO",(a,b),"is",d)
print("Multiplication of NO",(a,b),"is",e)
print("Division of NO",(a,b),"is",f)

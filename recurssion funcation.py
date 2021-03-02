def factorial(x):
      if x==1:
            return 1
      else:
            return(x*factorial(x-1))
num = int(input("Enter a no")) 
print("The factorial of ",factorial(num))
      

def sum(n):
      sum = 0
      while (n>0):
            sum=sum+(n%10)
            n=n/10
      return sum
n=int(input("Enter a No:"))
print(sum(n))

#Reverse
def Reverse(n):
      q=0
      while (n>0):
            r = n%10
            q=q*10+r
            n=n/10
      print("Reverse of no is",q)
n=int(input("Enter a NO:"))
Reverse(n)

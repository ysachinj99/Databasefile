t=0
l=[12,13,14,15,16,17,18,19]
for i in range(len(l)-1):
     if (l[i]<l[i+1]):
          t=l[i]
          break
print("The smallest no:",t)

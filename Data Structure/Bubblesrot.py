def bubblesort(nlist):
      for passnum in range(len(nlist)-1,0,-1):
            for j in range(passnum):
                  if nlist[j] > nlist[j+1]:
                        tmp= nlist[j]
                        nlist[j]= nlist[j+1]
                        nlist[j+1]=tmp
nlist=[14,98,46,43,27,5765,100,41,45,21,70]
bubblesort(nlist)
print(nlist)

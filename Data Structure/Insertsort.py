def insertsort(nlist):
    for i in range(1,len(nlist)):
        currentvalue=nlist[i]
        position=i
        while position>0 and nlist[position-1]>currentvalue:
            nlist[position]=nlist[position-1]
            position=position-1
        nlist[position]=currentvalue
nlist=[12,23,34,56,67,78,45,22,10,100,99]
insertsort(nlist)
print(nlist)

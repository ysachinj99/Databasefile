#Aim: Implement use of sets and Variable
#create a new enpty set
x= set()
print(x)
#create a non empty set
n= set([0,1,2,3,4])
print("The list is",n)
#create a set
seta=set([5,10,3,15,2,20])
#find the length use len()
print("Length of the set is:",len(seta))
#A new empty set
color_set= set()
color_set.add("Red")
print(color_set)
#Add Multiple items
color_set.update(["Blue","Green"])
print("Updated List is:")
print(color_set)
#removing a Item
num_set= set([0,1,3,4,5])
num_set.pop()
print(num_set)
num_set.pop()
print("changed list is:",num_set)
#create a New set
numset=set([0,1,2,4,5])
#Discard Number 4
num_set.discard(4)
print("Changed List after items is Discared is:",num_set)
#Intersection
setx= set(["Blue","Green"])
sety= set(["Blue","Yellow"])
setz= setx&sety
print("Intersecting item is:",setz)
#Union
setx=set(["Green","Blue"])
sety=set(["Blue","Yellow"])
seta=setx|sety
print("Union set is:",seta)
#Set Difference
setx= set(["Apple","Mango"])
sety= set(["Mango","Orange"])
setz= setx & sety
setb= setx - setz
print("Difference item is:",setb)
setx= set(["Apple","Mango"])
sety= set(["Mango","Orange"])
#Symmeteric Difference
setc= setx^sety
print("Symmetric Difference item is:",setc)
setx=set(["Apple","Mango"])
sety=set(["Mango","Orange"])
setz=set(["Mango"])
issubset=setx <= sety
print(issubset)
issubset= setx >= sety
print(issubset)
#Create a Set
seta= set([5,10,3,15,2,20])
#Find Maximum Value
print("Maximum value is",max(seta))
#Find Minimum Value
print("Minimum value is",min(seta))
#Clear a set
setp= set(["Red","Green"])
setq= setp.copy()
print(setq)
setq.clear()
print(setq)                                                     

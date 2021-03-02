import dbm
db=dbm.open("websites","c")
#add a n item
db["www.python.org"]="Python Home Page"
print(db["www.python.org"])
#Close and Save Disk
db.close()

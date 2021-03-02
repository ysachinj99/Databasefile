import re
count=0
p=re.compile("Sac")
m=p.finditer("SacabbaaSacababb")
for match in m:
      count+=1
      print(match.start(),"...",match.end(),"...",match.group())
      print("The Number of Occrance",count)

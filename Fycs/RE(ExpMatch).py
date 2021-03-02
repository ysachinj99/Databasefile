# to Retrive all word Starting with "an" or "ak"
import re
str = "Sachin, Avinash, Anil, Anant, Arun, Anirudh, Abhijit, Ankur"
result = re.findall(r"a[nk][\w]*",str)
print(result)

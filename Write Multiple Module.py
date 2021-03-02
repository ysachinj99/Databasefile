file = open ("C://Python//CsDept.txt","w")
file.write("76- Yadav Sachin"
           "\n Welcome TO Python World!!\n"
           "1.Designed by - Guido van Rossum \n"
           "2.Developer:Python Software Foundation \n"
                       "First appeared 1991;30 years ago \n"
           "3.OS: Linux, macOS, Windows \n"
           "4.License:Python Software Foundation License \n"
                    "---*12 Real-world Applications of Python*--- \n"
           "5.Web Development.\n"
           "6.Game Development.\n"
           "7.Scientific and Numeric Applications.\n"
           "8.Artificial Intelligence and Machine Learning.\n"
           "9.Software Development.\n"
           "10.Enterprise-level/Business Applications.\n"
           "11.Education programs and training courses.\n"
           "12.Language Development.")
file = open ("C://Python//CsDept.txt","r")
b = file.read()
print(b)
file.close

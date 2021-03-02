Filename = input("Enter the Filename (with Extension) To Read")
if Filename == "x":
      exit();
else:
      f = open(Filename,"r")
      print("\n The File",Filename,"Opened SuccessFully!")
      print("The File",Filename,"Contains:\n")
      print(f.read())
      f.close()
      

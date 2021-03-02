Filename = input("Enter File Name to Cerate and Write Content:");
if Filename == "x":
      exit();
else:
      f = open(Filename,"w");
      print("\n The File,",Filename,"Created SucecssFul")
      print("Enter 3 Sentence to Write on the files:")
      sent1 = input();
      sent2 = input();
      sent3 = input();
      f.write(sent1);
      f.write("\n");
      f.Write(sent2);
      f.write("\n");
      f.write(sent3);
      f.close();
      print("\n Content Sucessfully placed inside the File,!!");

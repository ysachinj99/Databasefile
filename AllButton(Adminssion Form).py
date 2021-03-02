from tkinter import *
root= Tk()
root.geometry("400x300+10+10")
root.title("Admission Form")
var= IntVar()

l=Label(root,text="Admission Form",width=15,font=("Bold",20))
l.place(x=90,y=53)

l1=Label(root,text="Enter First Name",width=15,font=("Bold",10))
l1.place(x=80,y=130)

e1=Entry(root)
e1.place(x=240,y=130)

l2=Label(root,text="Enter Last Name",width=15,font=("Bold",10))
l2.place(x=68,y=180)

e2=Entry(root)
e2.place(x=240,y=180)

l3=Label(root,text="Gender",width=15,font=("Bold",10))
l3.place(x=58,y=230)
Radiobutton(root,text= "Male",variable= var,value=1,padx=15).place(x=235,y=230)
Radiobutton(root,text= "Female",variable= var,value=2,padx=20).place(x=300,y=230)

l4=Label(root,text="Subject",width=15,font=("Bold",10))
l4.place(x=55,y=300)

#var1 = IntVar()
Checkbutton(root,text="python",variable=var).place(x=235,y=300)
#var2 = IntVar()
Checkbutton(root,text="java",variable=var).place(x=315,y=300)
#var3=IntVar()
Checkbutton(root,text="C++",variable=var).place(x=235,y=325)
#var4=IntVar()
Checkbutton(root,text="Linux",variable=var).place(x=315,y=330)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=230,y=400)

root.mainloop()



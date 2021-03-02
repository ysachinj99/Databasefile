from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="First Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Last Name",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=80,y=300)
var1 = IntVar()
Checkbutton(root,text="python",variable=var1).place(x=235,y=300)
var2 = IntVar()
Checkbutton(root,text="java",variable=var2).place(x=315,y=300)
var3=IntVar()
Checkbutton(root,text="C++",variable=3).place(x=235,y=325)
var4=IntVar()
Checkbutton(root,text="Linux",variable=4).place(x=315,y=330)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=230,y=400)

root.mainloop()

#1st program
from tkinter import *
root = Tk()
root.title("Login validator") 
def login():
    global username
    global password
    username = StringVar()
    password = StringVar()
    if(username=="" and password==""):
        messagebox.show("","Blank is not allowed")
    elif(username=="Avinash" and password=="123"):
        messagebox.show("","Login success")
    else:
        messagebox.show("","Login id and password is incorrect")
l1=Label(root,text="Username",font=('arial',10,'bold'),padx=35).grid(row=0)
l2=Label(root,text="Password",font=('arial',10,'bold'),padx=35).grid(row=1)
l1=Entry(root,textvariable=username)
l2=Entry(root,textvariable=password)
l1.grid(row=0,column=1)
l2.grid(row=1,column=1)

Button(root,text="Login",command=login,font=('arial',10,'bold'),padx=40).grid(row=3,column=1)

root.mainloop()

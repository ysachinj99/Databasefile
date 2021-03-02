from tkinter import *
root=Tk()
var=StringVar()
label=Message(root,textvariable=var,relief=RAISED)
var.set("Hey!!")
label.pack()
root.mainloop()

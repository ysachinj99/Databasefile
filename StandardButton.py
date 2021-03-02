from tkinter import*
bt=Tk()
def display():
    print("Welcome to GUI program")
b=Button(bt,text="Click here",command=display)
b.pack()
mainloop()

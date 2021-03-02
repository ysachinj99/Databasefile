from tkinter import*
rb=Tk()
r=IntVar()
Radiobutton(rb,text="Python",variable=r,value=1,padx=40).pack(anchor=W)
Radiobutton(rb,text="Linux",variable=r,value=2,padx=40).pack(anchor=W)
mainloop()

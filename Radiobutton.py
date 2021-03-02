from tkinter import*
rb=Tk()
r=IntVar()
Radiobutton(rb,text="Python",variable=r,value=1,padx=40).pack(anchor=W)
Radiobutton(rb,text="Linux",variable=r,value=2,padx=40).pack(anchor=W)
Radiobutton(rb,text="Data Structure",variable=r,value=3,padx=40).pack(anchor=W)
Radiobutton(rb,text="Calculus",variable=r,value=4,padx=40).pack(anchor=W)
Radiobutton(rb,text="Programing c",variable=r,value=5,padx=40).pack(anchor=W)
mainloop()

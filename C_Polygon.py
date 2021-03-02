import tkinter
t=tkinter.Tk()
C=tkinter.Canvas(t,bg="blue",height=400,width=400)
coord=150,
a=C.create_polygon(coord,fill="black")
C.pack()
t.mainloop()

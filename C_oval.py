import tkinter
t=tkinter.Tk()
C=tkinter.Canvas(t,bg="green",height=300,width=275)
coord=10,90,240,250
a=C.create_line(coord,fill="black")
C.pack()
t.mainloop()

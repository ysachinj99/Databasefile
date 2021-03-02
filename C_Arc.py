import tkinter 
t=tkinter.Tk()
C=tkinter.Canvas(t,bg="Indigo",height=205,width=350)
coord = 10,50,150,250
a=C.create_arc(coord,start=0,extent=180,fill="Yellow")
C.pack()
t.mainloop()

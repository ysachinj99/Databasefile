import tkinter
t=tkinter.Tk()
C=tkinter.Canvas(t,bg='red',height=200,width=400)
a=C.create_line(10,90,240,250,fill='black')
a=C.create_rectangle(10,10,100,100,fill='yellow')
a=C.create_polygon(150,75,225,0,300,75,225,350,150,200,fill='green')
C.pack()
C.mainloop()

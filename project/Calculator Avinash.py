from tkinter import*
cal=Tk()
cal.title("calculator")
operator=" "
text_Input=StringVar()
txtdisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=40,insertwidth=4,bg='White',justify='right').grid(columnspan=4)

#############Button click
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
    
##########Equalbutton
def Equalsbtn():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=" "
    

##############Clear button
def Clearbtn():
    global operator
    operator=" "
    text_Input.set(" ")
    
#########################Row 1 button
btn7=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(7),text=7).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(8),text=8).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(9),text=9).grid(row=1,column=2)
Addittion=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick('+'),text='+').grid(row=1,column=3)

#########################Row 2 button
btn4=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(4),text=4).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(5),text=5).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(6),text=6).grid(row=2,column=2)
Subtraction=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick('-'),text='-').grid(row=2,column=3)


######################Row 3 button
btn1=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(1),text=1).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(2),text=2).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick(3),text=3).grid(row=3,column=2)
Multiplication=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick('*'),text='*').grid(row=3,column=3)

#########################Row 4 button
btn0=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),text=0).grid(row=4,column=0)
btnclear=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=Clearbtn,text='C').grid(row=4,column=1)
btnequals=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=Equalsbtn,text='=').grid(row=4,column=2)
Division=Button(cal,padx=16,bd=6,fg='black',font=('arial',20,'bold'),command=lambda:btnClick('/'),text='/').grid(row=4,column=3)
cal.mainloop()

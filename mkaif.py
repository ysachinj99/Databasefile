from tkinter import * expression = "" def press(num): global expression expression = expression + str(num) equation.set(expression) def equalpress():
try:

	global expression 
	total = str(eval(expression)) 

	equation.set(total) 

	expression = ""  
except: 

	equation.set("ohh shitt...error ") 
	expression = "" 
def clear(): global expression expression = "" equation.set("")
if name == "main": gui = Tk() gui.configure(background="dark blue") gui.title("kaif's Calculator") gui.geometry("310x230") equation = StringVar() expression_field = Entry(gui,textvariable=equation)

expression_field.grid(columnspan=4, ipadx=40) 

equation.set('')  
button1 = Button(gui, text=' 1 ', fg='black', bg='white', 
				command=lambda: press(1), height=2, width=9) 
button1.grid(row=2, column=0) 

button2 = Button(gui, text=' 2 ', fg='black', bg='white', 
				command=lambda: press(2), height=2, width=9) 
button2.grid(row=2, column=1) 

button3 = Button(gui, text=' 3 ', fg='black', bg='white', 
				command=lambda: press(3), height=2, width=9) 
button3.grid(row=2, column=2) 

button4 = Button(gui, text=' 4 ', fg='black', bg='white', 
				command=lambda: press(4), height=2, width=9) 
button4.grid(row=3, column=0) 

button5 = Button(gui, text=' 5 ', fg='black', bg='white', 
				command=lambda: press(5), height=2, width=9) 
button5.grid(row=3, column=1) 

button6 = Button(gui, text=' 6 ', fg='black', bg='white', 
				command=lambda: press(6), height=2, width=9) 
button6.grid(row=3, column=2) 

button7 = Button(gui, text=' 7 ', fg='black', bg='white', 
				command=lambda: press(7), height=2, width=9) 
button7.grid(row=4, column=0) 

button8 = Button(gui, text=' 8 ', fg='black', bg='white', 
				command=lambda: press(8), height=2, width=9) 
button8.grid(row=4, column=1) 

button9 = Button(gui, text=' 9 ', fg='black', bg='white', 
				command=lambda: press(9), height=2, width=9) 
button9.grid(row=4, column=2) 

button0 = Button(gui, text=' 0 ', fg='black', bg='white', 
				command=lambda: press(0), height=2, width=9) 
button0.grid(row=5, column=0) 

plus = Button(gui, text=' + ', fg='black', bg='white', 
			command=lambda: press("+"), height=2, width=9) 
plus.grid(row=2, column=3) 

minus = Button(gui, text=' - ', fg='black', bg='white', 
			command=lambda: press("-"), height=2, width=9) 
minus.grid(row=3, column=3) 

multiply = Button(gui, text=' * ', fg='black', bg='white', 
				command=lambda: press("*"), height=2, width=9) 
multiply.grid(row=4, column=3) 

divide = Button(gui, text=' / ', fg='black', bg='white', 
				command=lambda: press("/"), height=2, width=9) 
divide.grid(row=5, column=3) 

equal = Button(gui, text=' = ', fg='black', bg='white', 
			command=equalpress, height=2, width=9) 
equal.grid(row=5, column=2) 

clear = Button(gui, text='Clear', fg='black', bg='white', 
			command=clear, height=2, width=9) 
clear.grid(row=5, column='1') 

Decimal= Button(gui, text='.', fg='black', bg='white', 
				command=lambda: press('.'), height=2, width=9) 
Decimal.grid(row=6, column=0) 
gui.mainloop()

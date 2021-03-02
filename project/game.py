from tkinter import *
import tkinter.messagebox
board = Tk()
board.title("tic-tac-toe game")
p1_score='stringvar()'
p2_score='stringvar()'
ptr1 = 0
ptr2 = 0
flag = True
ctr=1

def play(btn):
    global flag,ctr
    if btn["text"]==" " and flag==True:
        flag=False
        btn["text"]="X"
        ctr+=1
        check()
    elif btn["text"]==" " and flag==False:
        flag=True
        btn["text"]="O"
        ctr+=1
        check()
    else:
        tkinter.messagebox.showinfo("learn TechTotech","Not allowed")
        
def ClearButton():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    
def check():
    global ptr1,ptr2,p1_score,p2_score,ctr
    if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
       button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
       button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
       button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
       button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
       button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
       button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
       button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        ClearButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player 1 win")
        ptr1+=1
        ctr=0
        p1_score.set(ptr1)
    elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
         button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
         button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
         button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
         button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
         button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
         button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
         button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
         button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        ClearButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player 2 win")
        ptr2+=1
        ctr=0
        p2_score.set(ptr2)
    elif(ctr==9):
         tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
    
button1 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button1))
button1.grid(row=1 , column=0)
button2 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button2))
button2.grid(row=1 , column=1)
button3 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button3))
button3.grid(row=1 , column=2)
button4 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button4))
button4.grid(row=2 , column=0)
button5 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button5))
button5.grid(row=2 , column=1)
button6 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button6))
button6.grid(row=2 , column=2)
button7 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button7))
button7.grid(row=3 , column=0)
button8 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button8))
button8.grid(row=3 , column=1)
button9 = Button(board, text=" ", font='Times 15 bold', bg='Black', fg='white',
                 bd=5, height=3, width=5, command=lambda: play(button9))
button9.grid(row=3 , column=2)
board.mainloop()

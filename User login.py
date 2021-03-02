from tkinter import *
Login = Tk()
Login.title("User Login")
Login.geometry("312x324+45+30")


#username_entry = Login("Ysachinj99")
#password_entry = psswrd("1234")
#lable(Login_b,text="").pack()
#Button(Register,text="Register",width=10,height=1,command = Login).grid(row=3)

def Login_b():
      print("Enter Your Login I'd -")
      Login_b.title("Login")
      Login_b.geometry("152*250")
      Label(Login,text="Login I'd -").pack()
      Label(Login,text="").pack()
      e1=Entry(Login)
      e1.grid(row=0,column=1)
      Label(Login,text="").pack()
      Label(Login,text="Psswrd - ").pack()
      e2=Entry(Login)
      e2.grid(row=1,column=1)
     

Login.mainloop()


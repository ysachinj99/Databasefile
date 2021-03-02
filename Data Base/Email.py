import smtplib
  
#Establish SMTP Connection
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
#Start TLS based SMTP Session
s.starttls() 

#Login Using Your Email ID & Password
s.login("ysachinj99@gmail.com", "39013942")

#Email Body Content
message = """
Hello, this is a test message!
Illustrated for WTMatter Python Send Email Tutorial
<h1>How are you?</h1>
"""

#To Send the Email
s.sendmail("ysachinj99@gmail.com", "profrajesh28@gmail.com",message)
print("Massage Send Sucessfully") 
#Terminating the SMTP Session
s.quit()

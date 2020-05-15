# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("anant.flekdeno@gmail.com", "*****") 

# message to be sent 
message = "BUILD/TEST FAILED"

# sending the mail 
s.sendmail("anant.flekdeno@gmail.com", "anantjakhmola9@gmail.com", message) 

# terminating the session 
s.quit() 


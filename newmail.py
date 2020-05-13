import smtplib

send = "anant.flekdeno@gmail.com"
rece = "anantjakhmola9@gmail.com"
passw = "anant1234"
message = "BUILD/TEST FAILED"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login = (send,passw)
server.sendmail = (send,rece,message)
server.quit()

#!/usr/bin/python

import smtplib

sender = 'anant.flekdeno@gmail.com'
receivers = ['anantjakhmola9@gmail.com']

message = """From: From Person <anant.flekdeno@gmail.com>
To: To Person <anantjakhmola9@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('192.168.0.110')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"

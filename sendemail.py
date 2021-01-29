"""
Desc:
    This program implements sending email
Author:
    Jyotsna Sagiraju
    29-01-2021
"""
import smtplib
import ssl
import getpass

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "jyotsna.alcove@gmail.com"
password = getpass.getpass(prompt="Type your password for jyotsna.alcove@gmail.com and press enter: ")
receiver_email = "jyotsna.kalidindi@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""
# Create a secure SSL context
context = ssl.create_default_context()
# Try to log in to server and send mail
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email,message)
except Exception as e:
    print(e)
finally:
    server.quit()

import time 
import smtplib
import ssl
from email.message import EmailMessage
from config import *

class SendAlert():
    def __init__(self, body):
        self.body = body
    def send_alert(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = f'WebEx Network Test - Failed'
        msg['From'] = sender
        msg['To'] = receiver
        try:
            s = smtplib.SMTP(mailserver, port)
            s.login(mailuser, mailpassword)
            s.send_message(msg)
            s.quit()
        except:
            context = ssl.create_default_context()
            s = smtplib.SMTP_SSL(mailserver, port, context=context)
            s.login(mailuser, mailpassword)
            s.send_message(msg)

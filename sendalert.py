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
        msg['Subject'] = f'WebEx Network Test Results'
        msg['From'] = SENDING_EMAIL
        msg['To'] = RECEIVING_EMAIL
        try:
            s = smtplib.SMTP(MAILSERVER, PORT)
            s.login(MAILSERVER_USERNAME, MAILSERVER_PASSWORD)
            s.send_message(msg)
            s.quit()
        except:
            context = ssl.create_default_context()
            s = smtplib.SMTP_SSL(MAILSERVER, PORT, context=context)
            s.login(MAILSERVER_USERNAME, MAILSERVER_PASSWORD)
            s.send_message(msg)

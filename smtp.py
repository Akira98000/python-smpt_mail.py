# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'sender@example.com'
sender_password = 'password'
recipient_email = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email sent using Python.'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject

message.attach(MIMEText(body, 'plain'))

smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
smtp_session.starttls()
smtp_session.login(sender_email, sender_password)

smtp_session.sendmail(sender_email, recipient_email, message.as_string())
print('Email sent successfully')

smtp_session.quit()

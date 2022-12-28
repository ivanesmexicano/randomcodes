# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:01:36 2022

@author: Ivan Tonatiuh
"""

from email.message import EmailMessage
import ssl
import smtplib

email_sender= "gfmega.inteligencia.comercial@gmail.com"
email_password="gtsocvkrsgpwooul"
email_receiver="ivanesmexicano@gmail.com"

subject="Check my new video"

body="""
Ive publsihed a new video

"""

em=EmailMessage()

em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    

'''
Challenge: If you want to make this project more
 challenging, try to attach images to your emails.
 To do so, you need to use the imghdr library.
'''
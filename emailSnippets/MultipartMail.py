#!/usr/bin/python

import smtplib

##Multipurpose Internet Mail Extensions (MIME) is an Internet standard that extends the format of email to support:
##
##Text in character sets other than ASCII
##Non-text attachments: audio, video, images, application programs etc.
##Message bodies with multiple parts
##Header information in non-ASCII character sets


from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

us = [100, 105, 115, 116, 114, 111, 98, 121, 116, 101]
ps = [100, 105, 115, 116, 114, 111, 66, 121, 116, 101, 50, 54, 56]

def cd_us(l):
    x = ''
    for i in l:
        x=x+chr(i)
    return(x)


uss =  cd_us(us).strip()
pss = cd_us(ps).strip()

fromaddr = "hacked@gmail.com"
toaddr = 'dejanualex@yahoo.com'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TEST"

body = "YOUR MESSAGE HERE"

msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(uss,pss)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

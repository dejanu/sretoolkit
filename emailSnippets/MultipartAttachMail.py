import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
us = [100, 105, 115, 116, 114, 111, 98, 121, 116, 101]
ps = ['1100100', '1101001', '1110011', '1110100', '1110010', '1101111', '1000010', '1111001', '1110100', '1100101', '110010', '110110', '111000']


def cd_us(l):
    x = ''
    for i in l:
        x=x+chr(i)
    return(x)

def cd_uss(l):
    x=''
    for i in l:
        x=x+chr((int(i,2)))
    return x
        

uss =  cd_us(us).strip()
pss = cd_uss(ps).strip()

fromaddr = "HACKATHON@gmail"
toaddr = 'dejanualex@yahoo.com'
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "EMAIL CU ATASAMENT"
 
body = "VEZI ATASAMENTUL"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = 'aaa.html'
attachment = open(filename, "rb")
    
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(uss,pss)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

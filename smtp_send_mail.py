import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


#content="ALEX"

#server and port
mail=smtplib.SMTP('smtp.gmail.com',587)

#identify to the server ESMTP
mail.ehlo()

#start TLS mode = encrypt smtp for login
mail.starttls()
mail.login('distrobyte','distroByte268')

#attachment
msg = MIMEMultipart()
part = MIMEBase('application', "octet-stream")
#part.set_payload(open("text.txt", "rb").read())
part.set_payload("aaa")
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="text.txt"')

msg.attach(part)

#spoof mail #content
mail.sendmail('Vladimir_Serghei@luxoft.com','dejanualex@yahoo.com',msg.as_string())




mail.close()



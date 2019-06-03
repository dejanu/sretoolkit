import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

username = 'distrobyte'
parola = 'pass'
server.login(username,parola)


msg ="test message"
server.sendmail('jenkins@tvaas.com','dejanualex@yahoo.com',msg)

server.quit()

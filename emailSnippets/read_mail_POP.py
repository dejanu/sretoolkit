#!usr/bin/python
import poplib,imaplib
#import email
from email import parser

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('distrobyte@gmail.com')
pop_conn.pass_('distroByte268')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    print message['subject']
    if message['subject'].lower() == "start test":
        print("wowo")
    else:
        pass
pop_conn.quit()
##
##
###email server = imap.gmail.com (read) or smtp.gmail.com (send)
##
##ORG_EMAIL   = "@gmail.com"
##FROM_EMAIL  = "distrobyte" + ORG_EMAIL
##FROM_PWD    = "distroByte268"
##SMTP_SERVER = "imap.gmail.com"
##SMTP_PORT   = 993
###connect to the SMTP server over SSL
##mail = imaplib.IMAP4_SSL(SMTP_SERVER)
##mail.login(FROM_EMAIL,FROM_PWD)
##
##mail.select('inbox')
##type, data = mail.search(None, 'ALL')
##mail_ids = data[0]
##id_list = mail_ids.split()
##
##type, data = mail.search(None, 'ALL')
##mail_ids = data[0]
##
##first_email_id = int(id_list[0])
##latest_email_id = int(id_list[-1])
##
##
##for i in range(latest_email_id,first_email_id, -1):
##    typ, data = mail.fetch(i, '(RFC822)' )
##    for response_part in data:
##        if isinstance(response_part, tuple):
##            msg = email.message_from_string(response_part[1])
##            email_subject = msg['subject']
##            email_from = msg['from']
##            #print 'From : ' + email_from + '\n'
##            print 'Subject : ' + email_subject + '\n'
##            


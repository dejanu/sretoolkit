import imaplib,email


imap_host = 'imap.gmail.com'
imap_user = 'distrobyte@gmail.com'
imap_pass = 'distroByte268'

#open a connection - standard IMAP4 port (143) is used
imap = imaplib.IMAP4_SSL(imap_host)

#login
imap.login(imap_user, imap_pass)

#get status fot the mailbox(folder) INBOX - Request named status conditions for mailbox
folderStatus,unseenInfo = imap.status('INBOX',"(UNSEEN)")

# no of unseen mails
print (unseenInfo[0])

#select INBOX
status,data=imap.select('INBOX')

###############################################search in INBOX
#retcode,messages=imap.search(None,'ALL')
#retcode,messages = imap.search(None, '(SUBJECT "test")')
retcode,messages=imap.search(None, '(UNSEEN)')

#messages = list of messages from the first view (1,2,3..28) = no of message on a page
id_list=messages[0].split() #['1','2'...]
latest_email_id = id_list[-1] # SELECT the latest email

# fetch the email body (RFC822) for the given ID
result, data = imap.fetch(latest_email_id, "(RFC822)")

# here's the body, which is raw text of the whole email
# including headers and alternate payloads
raw_email = data[0][1]

#print raw_email[0]


b = email.message_from_string(raw_email)

#Print FROM and SUBJECT
print (b['From'])
print (b['Subject'])
if b.is_multipart():
    for part in b.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        # skip any text/plain (txt) attachments
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            print body
            break
# not multipart - i.e. plain text, no attachments, keeping fingers crossed
else:
    body = b.get_payload(decode=True)
    print body
            
   
        


#message_set, message_parts)
#Fetch (parts of) messages. message_parts should be a string of message part names enclosed within parentheses, eg: "(UID BODY[TEXT])".
#Returned data are tuples of message part envelope and data.



    
## List mailbox names in directory matching pattern.
#directory defaults to the top-level mail folder
#e.g  "INBOX" , [Gmail]/Trash, [Gmail]/Draft
#status, folder_list = imap.list()
#print (folder_list)



#select a specific folder - Select a mailbox. Returned data is the count of messages in mailbox (EXISTS response).
#The default mailbox is 'INBOX'.
#If the readonly flag is set, modifications to the mailbox are not allowed.
#status,data=imap.select('[Gmail]/Trash')
#print (data)

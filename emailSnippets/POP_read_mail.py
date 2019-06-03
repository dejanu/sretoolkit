import poplib
'''
POP3, which encapsulates a connection to a POP3 server and implements the protocol as defined in RFC 1725.
The POP3 class supports both the minimal and optional command sets. Additionally, this module provides a class POP3_SSL,
which provides support for connecting to POP3 servers that use SSL as an underlying protocol layer.
'''
mailServer = 'pop.gmail.com'

emailID = 'distrobyte@gmail.com'
emailPwd = 'pass'


#open secured connection (using SSL) to mail server
#poplib.POP3(host[, port[, timeout]]) -  default port 110
emailConn = poplib.POP3_SSL(mailServer)

#print the response message from server
#Returns the greeting string sent by the POP3 server
print (emailConn.getwelcome())

#set email address
emailConn.user(emailID)

#set password
emailConn.pass_(emailPwd)


#get information about email address
#Get mailbox status. The result is a tuple of 2 integers: (message count, mailbox size).
EmailInfo =  emailConn.stat()

print (EmailInfo)
print("No of emails : %s (%s bytes)") %EmailInfo


##read all emails
no_of_emails=EmailInfo[0]
print (no_of_emails)
for i in range(no_of_emails):
    for email in emailConn.retr(i+1)[1]: #Retrieve whole message number which, and set its seen flag. Result is in form (response, ['line', ...], octets)
        print (email)

emailConn.quit()

# – date object: stores the date
# – time object: stores the time
# – datetime object: stores both the date and the time

## https://www.python-course.eu/python3_time_and_date.php

import datetime
import os, sys
import time,re


# datetime.datetime object aka. datetime.datetime(2018, 12, 11, 11, 47, 7, 870350)
datetime_object = datetime.datetime.now()

epoch = datetime.datetime(1970,1,1)
i = datetime.datetime.now()

delta_time_object = (i - epoch).total_seconds()

a = datetime.datetime(2009,3,12,3,11,11) #year month day hour[0..23] min sec
b = datetime.datetime(2009,3,12,1,10,11)
c = a - b # obtain a datetime.timedelta object
 
  
# datetime.time object is a point in a day
time_object = datetime.datetime.now().time()



# time obj do not support __sub__ of 2 time objects 
your_time = datetime.time(hour=12, minute=15, second= 15)
your_time.replace(hour=10)



import time 

# return a str with  12H/12h format
T=time.strftime("%I:%M:%S")
t=time.strftime("%H:%M:%S")


#Tue Dec 11 11:47:29 2018  C-style like string

time.ctime(time.time())

#epoch time
time.time()
    
def timeConversion(s):
    #
    # Write your code here.
    slist = s.split(":")
    am_pm = re.findall("\D{1,2}", slist[-1])

    #remove AM or PM from last element
    slist[-1] = str(re.findall("\d{1,2}", slist[-1])[0])

    if am_pm[0].lower() == "am":
        if int(slist[0]) == 12:
            slist[0] = "00"
        else:
            pass
        return ":".join(slist)
    elif am_pm[0].lower() == "pm":
        #convert to 24h format
        if int(slist[0]) < 12:
            slist[0] = str(12 + int(slist[0]))
        else:
            pass
        return ":".join(slist)
    else:
        print("Not am or pm")    
#--------------------------------------------------------------------------#
##use a NTP server to sync the time with the server
## we asked the time from that server
import ntplib,time

#create a NTP object
obj=ntplib.NTPClient()
#(server-host,versiune,port,timeout)
rasp=obj.request("2.ro.pool.ntp.org",2,123,5)
x=time.ctime(rasp.tx_time)
#print rasp.tx_time
#print (x)

#-------------------------------------------------------------------------#

hour = re.findall(r'\d\d:\d\d',time.ctime())[0]
print (hour)

#---------------------------------------------------------------------------#

    

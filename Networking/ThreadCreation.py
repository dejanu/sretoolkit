## THREAD creation



## Basic method

from threading import *



def mt():
    """Create child thread"""
    for i in range(6):
        print("Child thread  {}".format(current_thread().getName()))

# print main thread
print(current_thread().getName())

# Constructor for creating a thread where target is callable object aka function
child = Thread(target=mt)
child.start()

#Wait until the child thread terminates and then print
child.join()
print("Bye {}".format(current_thread().getName()))


###################################################
print("------------------------------------------")

## Extending Thread class

## the only 2 function that can be override are run() and __init__()

import time

print("Control under {}".format(current_thread().getName()))

class mythread(Thread):
    """ mythread extends Thread class """

    #override run
    def run(self):
        for _ in range(6):
            print(" Child thread {}".format(current_thread().getName()))

obj=mythread()
obj.start()
obj.join()

print("Control returned to {}".format(current_thread().getName()))



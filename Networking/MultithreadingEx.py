## Thread exercise


## run the following functions on different threads


import time
from threading import *



def foo():
    for _ in range(5):
        print("I am foo \n")

def bar():
    for _ in range(5):
        print("I am bar \n")


if __name__ == "__main__":

    # without multithreading (sequential execution)
    print("Guess I am {}".format(current_thread().getName()))
    s = time.time()
    foo()
    bar()
    e = time.time()
    print("time {}".format(e-s))
    print("Guess I am {}".format(current_thread().getName()))

##    ######################
    # with multithreading
    a = Thread(target=foo)
    b = Thread(target=bar)
    
    print("Guess I am {}".format(current_thread().getName()))
    s = time.time()
    a.start()
    b.start()
    a.join()
    b.join()
    e =  time.time()
    print("time {}".format(e-s))
    print("Guess I am {}".format(current_thread().getName()))


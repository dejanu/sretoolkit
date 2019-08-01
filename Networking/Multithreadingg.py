### Multi-processing vs Multi-threading

## Thread = lightweight process, memory is shared between all threads of the same process


## Multi-threading when program is network bound
##(threads are uused in cases where the execution of a task involves some WAITING)

## Multi-processing when program is CPU bound
## (processes are used for parallel CPU computation)

from threading import *
from time import *


class Hello(Thread):

    # override run method from Thread
    def run(self):
        for _ in range(5):
            print("Hello\n")
            sleep(1)


class Hi(Thread):

    def run(self):
        for _ in range(5):
            print("Hi\n")
            sleep(1)


if __name__ == "__main__":

    # Creating objects of type thread
    t1 = Hello()
    t2 = Hi()

    # sincer Hello and Hi inherit Thread t1 and t2 become 2 separe threads
    # start will call run internal
    t1.start()
    t2.start()



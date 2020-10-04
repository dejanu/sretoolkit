#!/usr/bin/python


## context manager protocol == class with __enter__() and __exit__() method
## $ulimit -n = no of leak-ed file descriptors supported by OS
## context managers work on sockets, db_connections, file_descriptors
## subprocess.Popen

with open("clasic_file.txt",'r') as my_resource:
    for line in my_resource:
        print("> {}".format(line))

## contextlib class for creating context_managers
class myManager():
    """ sort of interface """
    def __init__ (self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """ create attr open_file which can be used on exit"""
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

## as KEYWORD does biding 
with myManager("clasic_file.txt","r") as my_file:
    for i in my_file:
        print(i)

        

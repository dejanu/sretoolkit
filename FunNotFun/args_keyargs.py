## ARGS and KWARGS - pass a variable number of args/keyword args to a function

#############   UNPACKING args #############  

# ARGS = (tuple)
def sum_nums(*args):
    """return sum of args"""
    s=0
    for i in args:
        s+=i 
    return s

#KWARGS={dict}
def foofoo(required,*args,**kwargs):
    """ order of args """
    print("required args")
    if args:
        #tuple
        print(args)
    if kwargs:
        #dict
        print(kwargs)
        for i in kwargs.keys():
            print(kwargs[i])


if __name__ == "__main__":

    # unpacking using * operator
    print("Unpack list [1,2,3] and call sum_nums {}".format(sum_nums(*[1,2,3,4])))






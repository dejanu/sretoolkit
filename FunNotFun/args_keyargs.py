#############   UNPACKING args #############  

def sum_nums(a,b,c):
    return a+b+c

l=[1,2,3]
sum_nums(*l)






#ARGS and KWARGS pass a variable no of non keyword/keyword arguments to a function


def enumerate_arg(*args):
    """ args is a TUPLE """
    for i in args:
        print (i)


#pass a list and iterate through each element of list
l=[1,2,3,4]

def square_elem(*args):
    """call the function (*l) to UNPACK a list"""
    x=[]
    for i in args:
        x.append(i**2)
    return x
            

##interview and shit 

def trick(*args,l=[]):
    for i in args:
        l.append(i**i)
    print(l)

trick(1,2,3) # [2,4,9]
trick(5,6) #[2,4,9,25,36]


#KWARGS={dict}
def foofoo(required,*args,**kwargs):
    print("required args")
    if args:
        #tuple
        print(args)
    if kwargs:
        #dict
        print(kwargs)
        for i in kwargs.keys():
            print(kwargs[i])

        


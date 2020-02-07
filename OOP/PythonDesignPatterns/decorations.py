#!/usr/bin/python


##Decorators : Function decorators and Class decorators (Structural Pattern)


## FUNCTION ARE OBJECTS:  function names are references to function objects

def g():
    print("Hi i am G thanks for calling me")

def f(func):
    g()
    print("Hi i am F thanks for calling me")
    print("func's real name is " + func.__name__) 

#passing to a variable a function reference
i=g #can call i() now

##pass as a parameter to a function a reference to a function aka a function object
f(i)



#-----------------FuckedUp-decorators--------------------------

def call_counter(func):
    """ create calls attribute 
	usage func.calls"""

    def helper(*args):
        """increment attribute for the called function"""
        helper.calls+=1
        return func(*args)
    #somehow contraintuitive, create attribute for the called function
    helper.calls=0
    return helper

@call_counter
def succ(x):
    return x+1

succ(1)
succ(2)
print(succ.calls)#2


def delay_execution(x):
    """delay code execution by x ammount of seconds"""
    def deco(f):
        def wrapper(*args):
            import time
            time.sleep(x)
            return f(*args)
        return wrapper
    return deco

def exec_time(f):
    """ return elapsed time for function execution """
    def wrapper(*args):
        import time
        #return epoch as float
        start = time.time()
        #call decorated function
        f(*args)
        end = time.time() - start
        print(end)
        print(time.ctime(end))
    return wrapper

@delay_execution(4)
def test():
    print("dasdas")

@exec_time    
def tests():
    import os
    print(os.listdir(os.getcwd()))


def get_args_kwargs(function):
        """ return args and kwargs of called function """
        def deco(*args, **kwargs):
              print (f"Function {function.__name__} called with args {args} and kwargs {kwargs}")
              return function(*args, **kwargs)
          return deco

def whois_calling():
	""get the name of the caller function"""
	import inspect
	print (inspect.stack()[1][3])


#------------basic-decorators------------------------

def deco_p(functie):
    def wrapper(*args,**kwargs):
        return "<p>"+str(functie(*args,**kwargs))+"</p>"
    return wrapper

def deco_b(functie):
    def wrapper(*args,**kwargs):
        return "<b>"+str(functie(*args,**kwargs))+"</b>"
    return wrapper

def deco_deco(tag):
    def deco(functie):
        def wrapper(*args,**kwargs):
            return str(tag)+str(functie(*args,**kwargs))+str(tag)
        return wrapper
    return deco

@deco_b
@deco_p
def text(s):
    return s.upper()

@deco_deco("<strong>")
def texttwo(s):
    return s.capitalize()

print(text("alex"))
print(texttwo("xela"))


#--------~WRAPS for decoratos------------
from functools import wraps

def make_blink(function):
    """define decorator"""

    #this makes the decorator transparent in terms of
    # its __name__ and docstring
    @wraps(function)

    #define inner function
    def decorator():
        # grab the return value of the function being decorated
        r = function()

        # add new functionality to the function being decorated
        return "woow new functionality" + str(r)

    return decorator

if __name__ == "__main__":

    @make_blink
    def hello_world():
        return "hello"


    print(hello_world())

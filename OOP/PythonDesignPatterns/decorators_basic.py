# DECORATOR (Structural Pattern)


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



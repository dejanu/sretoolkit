
def outer():
	"""enclosing function"""
	x=3
	def inner():
		""" nested function """
		return x+3
	return inner

a = outer()

## CLOSURE = executing a function object outisde his scope
## inner() cannot be called outside outer's scope
## so it will be called using a 
print(a.__name__) # it is inner
print(a())

######################################################

## CLOSURE = anonymous function

## ANONYMOUS function = function literal without a name
## CLOSURE = instance of a function ....


def f(x):
	def g(y):
		return x+y
	return g # Return a closure


def h(x):
	return lambda y:x+y #Return a closure

##assigning specific closures to variables

closurevar = f(2)

##using closures stored in variables (closurevar)
closurevar(3) ## 5


### using closure without binding them to variables

assert f(2)(3) = 5 # f(2) is the closure


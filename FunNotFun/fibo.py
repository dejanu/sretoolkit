
############################## Fibonnaci ###############
#### fib_seq = [1,1,2,3,5,8,13,21,34,55] ###############


def fib_recursive(x):
    ''' Fibbonaci series for a given number - RECURSIVE'''
    if (x==1) or (x==2):
        return 1
    else:
        return fib(x-1)+fib(x-2)

def fib(n):
    '''Fibonnaci series for a given number'''
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a

def fib_two (n):
    ''' Return n-th number from fibonnaci sequence'''
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a    

##############################

#fibonaci with cached values
fib_cached = {}

def _fib(n):
	if n not in fib_cached:
		fib_cached[n]=fibo(n)
	return fib_cached[n]

def fibo(n):
	if n<2:
		return n
	else:
		return fibo(n-2)+fibo(n-1)

##############################


def fibo_generator(a=1, b=1):
	"""fibonnaci as generator"""
        while True:
		yield a
		a, b = b, a+b
		


############################## Factorial ###############

## compute the number of permutations (combinations)
##of arranging a set of n numbers
def factorial(n):
    """n!= n * (n-1) * (n-2)
       0! ==1  """
    if (n == 1) or (n==0):
        return 1
    else:
        return n * factorial(n-1)


def factorial_new(x):
	""" non recursive"""
	r,i=1,2
	while i<=n:
		r*=i
		i+=1
	return r


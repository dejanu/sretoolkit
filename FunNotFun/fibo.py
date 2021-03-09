
############################## Fibonnaci sequence [1,1,2,3,5,8,13,21,34,55] ###############



def fibo(n):
	""" revursive """"
	if n<2:
		return n
	else:
		return fibo(n-1)+fibo(n-2)

# oneliner	
fib = lambda n: n if n < 2 else (fib(n - 1) + fib(n - 2))
	

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

#fibonacci dict with cached values
fib_cached = {}

def _fib(n):

    # check if fibo number is already cached
    if n in fib_cached:
        return fib_cached[n]

    if n<=2:
        value=1
    else:
        value = _fib(n-1) + _fib(n-2)

    # save the fibo number to dict
    fib_cached[n]=value
    return value


##############################

#fibonacci as generator


def fibo_generator(a=0, b=1):
	"""fibonnaci as generator"""
        while True:
		yield a
		a, b = b, a+b
		
## for i in fibo_generator():
##	print(i)

## f = fibo_generator()
## fibs = [next(f) for i in range(10)]

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



def create_multipliers():
	# return list of functions
	return [lambda x: i * x for i in range(5)]

def some_f():
	
	l = []
	return [lambda x:x*i for i in range(3)]
	return l


def fix_create_multipliers():
	return [ lambda x, i=i: i*x for i in range(5)]

if __name__ == "__main__":
	
	## iterate through list of functions returned by create_multipliers()
	for m in create_multipliers():
		print (id(m))
		print(m(2))
	
	## python closures are late binding 
	## which means that the values of variables used in closures
	## are looked up at the time the inner function it is called
	ll = [m(2) for m in fix_create_multipliers()]
	print(ll)

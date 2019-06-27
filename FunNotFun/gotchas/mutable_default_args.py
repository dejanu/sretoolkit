# mutable default args (list,dict) in function definitions

# DEFAULT VALUES ARE EVALUATED ONCE AT FUNCTION DEFINITION TIME

def append_to (element,x=[]):
	x.append(element)
    	return x


def fix_append_to(element, x=None):
    	""" fix: Create a new object each time the function is called
	so if you do not pass any list as argument you will have None as default arg for list"""
	if x is None:
        	x = list()
    	x.append(element)
    	return x

if __name__ == "__main__":
		

	#create a list x and append an element
	x = append_to("one")

	#create another list x and append an element
	y = append_to("something")

	## a new list is created ONCE when the function append_to it is defined
	## and the same list is used in each succesive call
	
	print("ID of list x:{0} and ID of list y: {1}".format(id(x),id(y)))
	print(x)
	print(y)
	
	## Pythons default args are evaluated once at function definition
	## not each time the functions is called
	## This means that if you use a mutable default argument and mutate it,
	##  you will and have mutated that object for all future calls to the function as well.i
	## Intentend behaviour when  we want maintain state 
	##between calls of a function. This is often done when writing a caching function

	a = fix_append_to(1)
	b = fix_append_to(22)
		
	print(a)
	print(b)


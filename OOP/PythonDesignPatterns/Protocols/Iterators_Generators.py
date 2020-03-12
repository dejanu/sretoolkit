## ITERATORS

# Def: objects that support __iter__ and __next__ dunder methods
# if you can run a for-in over an object, this means that the object is an interator
# Iterators are objects that allow you to traverse/process through all the elements of a CONTAINER, regardless of its specific implementation

## CONTAINERS = iterable object (list,dict,tuple,string,open files, open sockets) which support membership test e.g (if 'apple' in 'pineapple')

class Repeater:
    """Iterator implementation"""
    
    def __init__ (self,name,no_of_iterations):
        self.name = name
        self.noi = no_of_iterations
        self.counter = 0
        
    def __iter__(self):
        """ returns an iterator object"""
        return self

    def __next__(self):
        """ fetch new values from the iterator
            and knowing about the current state of the of the iterable"""

        self.counter+=1
        if self.counter < self.noi:
            return self.name
        else:
            raise StopIteration
        
#---------------------------------------------------------------------------------------------------------------------
## GENERATOR == resumable function

# functions that implement iterators (function doesn't hold the enitre result in memory instead it yields one result at a time)
# every generator is a iterator (issubclass(types.GeneratorType, collection.Iterator)

def fibo_generator():
    """ fibonacci generator """
    a,b=0,1
    while True:
        yield(a)
        a,b=b,a+b
        

def fibogenerator(a=1, b=1):
	"""fibonnacci as generator with default args"""
        while True:
		yield a
		a, b = b, a+b

#usage for first 10 no from fibo sequence
g = fibo_generator()
fibs = [next(a) for _ in range(10)]


if __name__ == "__main__":

    # user the iterator
    r = Repeater("alex",5)
    for i in r:
        # actually calls __next__
        print(i)

    # cast a list to iterator
    l = [1,2,3,5]
    list_iterator = iter(l)

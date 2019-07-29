### Abstract class = CANNOT be instantiated
## Subclasses of an abstract class in Python are not required to implement abstract methods from parent class


##Python3 compliant where you must inherit ABC
from abc import ABC, abstractmethod

# Python 2 compliant
from abc import ABCMeta, abstractmethod

class AbstractOld:
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass
    
# Abstract method implementation    
class Animal(object):
    
    def __init__(self, name):    
        self.name = name
        
    def talk(self):
        """abstract method is declared but does not have any IMPLEMENTATION"""
        
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal): pass

      
class Cat(Animal):

    def talk(self):
        print("Meeow")




    
class AbstractClassExample(ABC):
    """inherit the ABC class from abc module"""
    
    def __init__(self,value):
        self.value=value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class ChildAbstract(AbstractClassExample):
    
    def __init__(self):
        pass
    
    def do_something(self):
        print("abstract method from abstract class")

if __name__ == "__main__":
    
    c = ChildAbstract()
    c.do_something()

    # will raise NotImplementedError
    Dog("Alex").talk()

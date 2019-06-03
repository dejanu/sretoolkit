class Animal(object):
    def __init__(self, name):    
        self.name = name
    def talk(self):
        """abstract method is declared but does not have any IMPLEMENTATION"""
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def talk(self):
        print("Ham Ham")
class Cat(Animal):
    def talk(self):
        print("Meeow")

##abstract classes CAN NOT BE instantiated
##Subclasses of an abstract class in
##Python are not required to implement abstract methods of the parent class.


##Python3 compliant
from abc import ABC, abstractmethod
    
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

c = ChildAbstract()
c.do_something()

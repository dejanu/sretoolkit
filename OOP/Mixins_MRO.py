## Mix-in = a class not meant for direct instantiation

## Use multiple-inheritance to combine the mix-ins in the concrete class

## MRO = Memory Resolution Order
## hierarchy in which base classes are searched when looking for a method in the parent class


class Door:
    """ base class"""
    pass


class LockedDoor(Door):
    pass

class ShortDoor(Door):
    pass


class MagicDoor(Door):
    pass


class LockedShortMagicDoor(LockedDoor, ShortDoor, MagicDoor):
    pass


#-------------------

class Parent2(object):
    def f00(self):
        print('foo from PARENT2')
    def bar(self):
        print('bar from PARENT2')

class Child1(Parent1,Parent2):
    pass

class Child2(Parent1,Parent2):
    #overide the bar method from parent
    def bar(self):
        print('bar from CHILD2')

class GrandChild(Child1,Child2):
    pass

obj1=GrandChild()

#new type classes
'''
class GrandChild(Child1, Child2)
 |  Method resolution order:
 |      GrandChild
 |      Child1
 |      Child2
 |      Parent1
 |      Parent2
 |      __builtin__.object
 |  
 |  Methods inherited from Child2:
 |  
 |  bar(self)
 '''

#old type classes
'''
class GrandChild(Child1, Child2)
 |  Method resolution order:
 |      GrandChild
 |      Child1
 |      Parent1
 |      Parent2
 |      Child2
 |  
 |  Methods inherited from Parent2:
 |  
 |  bar(self)
 |  
 |  f00(self)
 '''

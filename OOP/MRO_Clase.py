#MRO mostenire multipla

class Parent1(object):
    pass

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

class Animal(object):
    def __init__(self,name):
        self.name = name
        print('constructor')

    def whoAmI(self):
        print('animal')

    def eat(self):
        print('eating')

    def __str__(self):
        """string repr of the object"""
        return self.name

    def __len__(self):
        return len(self.name)


class Dog(Animal):
    def __init__(self):
        print('Dog construnctor')

    #overwrite
    def eat(self):
        print("Dog eating")


#################### Super

class X(object):
    def __init__(self):
        print("X")
        self.a = 'X parent'

class Y(object):
    def __init__(self,name):
        print("Y")
        self.name=name
        self.b='Y parent'

class C(X,Y):
    def __init__(self):
        #first class MRO
       # super(C,self).__init__()
        #if I want the attr from Y baseclass
        #super(X,self).__init__()
        super(Y,self).__init__()
        print("C sublass")
            

###when we create a C() object the only contructor that is called is the one from C - WITHOUT SUPER
###super refers to the base class, but not explicitly



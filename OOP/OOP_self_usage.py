
# self = binds the attributes with name arguments

class Spam:
    """ self is used to represent the instance of the class """
    
    x = 1
    y = 1

    def __init__(self,value_x, value_y):
        
        # value_x will not be binded to a Spam object
        x = value_x

        # value_y will be binded to a Spam object 
        self.y = value_y

################################ Namespaces
# global var declaration
a,b = 0,0
class MyClass():

    a,b= 1,1
    def __init__(self):
        self.a = 2 
        self.b = 2
    
    def __str__(self):
        
        # for a,b == 2
        # return str(self.a + self.b)

        # for a,b == 1
        # return str(type(self).a + Myclass.b)
        return str(a+b)


if __name__ == "__main__":

    # object instantiation
    s = Spam(5,6)

    # True
    s.x == Spam.x

    # False
    s.y == Spam.y

    ################################ Namespaces

    m = MyClass()

    # 0 
    print(m)

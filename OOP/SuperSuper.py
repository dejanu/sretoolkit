##super() = built in function only for NewType classes , return a proxy object to delegate method calls
##to a class aka GAIN ACCESS TO INHERITED METHODS FROM PARENT OR SIBLING CLASS


class BaseClass(object):
    def __init__(self,name="Base Class ID"):
        self.name = name
        self.hard_code = "HardCoded atr"


class ChildClass(BaseClass):
    def __init__(self,name,surname):
        ## avoid writing self.name = name like in BaseClass just use super
        ##super(subClass, instance).method(args), in orderd to access Baseclass attr
        ##super(ChildClass,self).__init__(*args)
        super().__init__(name)
        self.surname =  surname
    
        

c = ChildClass("alex","dej")
print(c.surname)
print(c.hard_code)

class Car:
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

class AlwaysBlue(Car):
    """extend class"""
    def __init__(self,*args,**kwargs):
        """fking bad signature"""
        super().__init__(*args,**kwargs)
        self.color = blue

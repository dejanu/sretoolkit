## a method is a function that is stored as a class attribute
## classes are objects too

##STATIC METHODS staticmethod decorator allows us to call the method object
## Bound methods are objects too, and creating them has a cost, having a static method avoids that

from itertools import count

class MyClass(object):

    #static var for counting instances
    no_instances = 0

    #another approach for static var using itertools.count
    _ids = count(0)
    
    
    def __init__(self,name):

        #use class var 
        #type(self).no_instances+=1
        MyClass.no_instances+=1
        
        self.id = next(self._ids)

        
        self.name=name
    
    @staticmethod
    def the_static_method(x):
        """method that is not bound to a class or instance"""
        
        print("I can be called on a instance or on a class")
        return x+1
        
    @classmethod
    def uppersize(cls,name):
        """method that is bound to a class and not bound to a instance"""
        """see DATEIME"""
        return cls(name.upper())

    @classmethod
    def another_constructor(cls,name,surname):
        """ factory """
        
        ##create instance based on init
        new_instance = cls(name)
        new_instance.surname = surname
        return new_instance


if __name__ == "__main__":
    

    # classmethod usage
    obj=MyClass.uppersize("alex")   
    print(obj.name)

    
    ##call method from class object and also from instance object
    print(MyClass.the_static_method == MyClass("test").the_static_method) #TRUE

    ##it is the same for 2 instance objects
    print(MyClass("ale").the_static_method == MyClass("ionut").the_static_method) #TRUE



    ##CLASSMETHODS used as FACTORY methods, to create an instance with a pre-processing a priori
    print(MyClass.uppersize("test") == MyClass("test").uppersize("aha")) #TRUE







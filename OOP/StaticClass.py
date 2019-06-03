## A method is a function that is stored as a class attribute

## classes are objects too

class MyClass(object):

    class_attr = 314
    
    def __init__(self,name):
        self.name=name

    @staticmethod
    def the_static_method(x):
        """method that is not bound to a class or instance"""
        print("I can be called on a instance or on a class")
        return x+1
        
    @classmethod
    def the_class_method(cls,name):
        """method that is bound to a class and not bound to a instance"""
        """see DATEIME"""
        #Create an object
        parsed_name = name.lower()
        ###CALL THE INIT must have the same number of parameters
        return cls(parsed_name)

    @classmethod
    def another_constructor(cls,name,surname):
        ##create instance based on init
        new_instance = cls(name)
        new_instance.surname = surname
        return new_instance


#-------------------------------------------------

class Myclass:
	def __init__(self,a=0,b=0):
		self.a=a
		self.b=b
	@classmethod
	def value_ax10(cls,value):
		return cls(value*10)

##new objects creation
##  obj=Myclass(1,2).value_ax10(3)   => obj.a=30 obj.b=0
 

##STATIC METHODS staticmethod decorator allows us to call the method object
##Bound methods are objects too, and creating them has a cost.
##Having a static method avoids that
    
##call method from class object and also from instance object
print(MyClass.the_static_method == MyClass("test").the_static_method) #TRUE

##it is the same for 2 instance objects
print(MyClass("ale").the_static_method == MyClass("ionut").the_static_method) #TRUE

#-------------------------------------------------

##CLASSMETHODS used as FACTORY methods, to create an instance with a pre-processing a priori
print(MyClass("alexs").the_class_method == MyClass.the_class_method) #TRUE

#basic constructor
a = MyClass("alex")
print(a.name)

#classmethod constructor
b = MyClass.the_class_method("ALEX")
print(b.name)

#classmethod another constructor
c = MyClass.another_constructor("dejanu","alex")
print(c.name)
print(c.surname)


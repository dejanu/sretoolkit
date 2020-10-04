### Objects

# global var declaration
x = 100
y = 200

# blank class
class Test():pass


class Car():

    # class variables
    x = 1
    y = 2
    
    def __init__ (self,brand,age):
        """
        self is used to represent the instance of a class
        """

        # self = binds the attributes with name arguments
        print(f"SELF is: {type(self)}")
        
        self.b = brand
        self.a = age

        self.x = 2
        self.y = 2
        
        # mock_value will not be binded to Car object
        mock_values = 111

    def __str__(self):
        """ string representation"""

        #return str(self.x + self.y)
        return str (Car.x + Car.y)
        #return str(x+y)

    @classmethod
    def with_plates(cls, brand, age, country):
        """ helper method for initialization"""
        c = cls(brand,age)
        c.country = country
        return c

    @staticmethod
    def upper_brand(name):
        """ utility function"""
        return name.upper()
    


if __name__ == "__main__":

    obj = Test()

    c1 = Car("bmw",23)
    c2 = Car("audi",245)

    # string representation 300 3 or 4
    print(c1)

    # helper method
    c3 = Car.with_plates("bwm",234,"DT")

    # static method usage
    c1.b = Car.upper_brand(c1.b)

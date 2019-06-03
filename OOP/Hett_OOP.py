import math

class Circle(object):
    """Object enables MRO, super and descriptors"""
    #class variable
    version = '0.5b'

    def __init__(self,radius):
        """initializer for populating a new instances"""
        self.radius=radius #exposed instance variable

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self,radius):
        self.diameter = radius * 2.0
    @classmethod
    def from_bbd(cls,bbd):
        """alternative constructor"""
        radius = bbd/2.0/math.sqrt(2.0)
        return cls(radius)

    @staticmethod
    def angle_to_grade(angle):
        """static methods attach functions to classes"""
        return math.tan(math.radians(angle))*100.0

    def area(self):
        """perform quadrature ona  shape of a uniform radius"""
        #piR^2
        #get the self.radius by calling perimeter instance method
        p = self._perimeter()
        r = p/2.0/math.pi
        return math.pi * r ** 2.0

    def perimeter(self):
        #2piR
        return 2.0 * math.pi * self.radius

    #copy of perimeter class local reference
    __perimeter = perimeter

class Tire(Circle):
    """subclass of Circle methods that arent overriten are called from parent """

    def perimeter(self):
        """overwrite the base class perimeter"""
        return Circle.perimeter(self) * 1.25

##class is a namespace ,
##what it is inside the class is efectively a module


if __name__ == "__main__":
    print("Current version: ", Circle.version)
    c = Circle(10)
    print("A circle radius",c.radius)
    print("it has an area of",c.area())

    #call alternative constructor from subclass
    t=Tire.from_bbd(10)
    print(t.radius)

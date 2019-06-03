### FACTORY Method (Creational Pattern)

# another type of contructor (e.g time module)
# encapsulates object creation (object specialized in creation of other objects)


# Problem: class allowed only dogs initially, now cats too
# Decision: what type of class to user at runtime for object initalization
# You must still create an object of your new type, and at the point of creation you must specify the exact constructor to use

class Dog:

    def __init__ (self, name):
        self.name = name

    def speak(self):
        #return "Woof!"
        if self.race == "cat":
            return "meow"
        else:
            return "wof"

    @classmethod
    def cat(cls,name,race):
        c = cls(name)
        c.race = race
        return c



if __name__ == "__main__":

        a = Dog.cat("alex","cat")
        a.speak()
    
    

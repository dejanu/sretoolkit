## SINGLETON (Creational pattern)

# providing global variables (cached values) for multiple instances

# provide one and only one object of a particular type

# MODULES IN PYTHON act as SINGLETONS


class Borg:
    """ make class attrib globals"""
    _shared_state = {}

    def __init__ (self):
        # Make it an attribute dict of instance
        self.__dict__ = self._shared_state




class Singleton(Borg):

    def __init__(self, **kwargs):

        # create borg instance
        Borg.__init__(self)
        self._shared_state.update(kwargs)
            

if __name__ == "__main__":

    a = Singleton(HTTP = "Hyper Transfer Protocol")
    b = Singleton(SSH = "Secure SHell")

    # share attrs between instances
    print(b.HTTP)

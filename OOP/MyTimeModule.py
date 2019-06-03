class MyTime(object):
    #create static list of objects
    list_of_objects = list()

    
    def __init__(self,h=0  ,m=0  ,s=0):
        """ create MyTime object h=hour, m=minutes, s=seconds"""
        self.h = h
        self.m = m
        self.s = s

        #add the object to staic list
        MyTime.append(self)
        

    @classmethod
    def from_array(cls,info_array = None):
        try:
            # list unpacking and type casting to int
            h,m,s = list(map (lambda x: int(x),info_array))
            new_obj = cls(h,m,s)
            return new_obj
        except TypeError:
            print ("Pass info_array as list")
            return None
        
        
    def __add__(self,other):
        """ overload built-in + operator """
        hh = self.h + other.h
        mm = self.m + other.m
        ss = self.s + other.s

        s_add = ss // 60
        ss = ss % 60

        mm = mm + s_add
        mm_add = mm // 60
        mm = mm % 60

        hh = hh + mm_add
        # return a new instance of the class
        # instead of modifying the calling instance itself
        return MyTime (hh,mm,ss)

    def __sub__(self,other):
        """ overload built-in - operator"""
        if self.s < other.s:
            # take from minutes
            ss = self.s + 60
            self.m = self.m - 1

            new_s = ss - other.s
        elif self.s >= other.s:
            new_s = self.s - other.s

        if self.m < other.m:
            # take from hours
            mm = self.m + 60
            self.h = self.h - 1

            new_m = mm - other.m

        elif self.m >= other.m:
            new_m = self.m - other.m

        new_h = self.h - other.h
        return MyTime(new_h, new_m, new_s)

    def __str__(self):
        """string representation of MyTime object"""
        return "Hour:{0} Minutes:{1} Seconds:{2}".format(self.h, self.m, self.s)

    


if __name__ == "__main__":

    #create MyTime objects
    a = MyTime(2,17,17)
    b = MyTime(1,15,59)
    c = MyTime(["12","3","5"])




####class ABC(object):
####    x = "some attribute"
####    def say(self,n):
####        """this is a method"""
####        self.name = n
####        
####getatt(obj,"name_of_attr") function return the value of the attr
####if the attr exists
####getattr(ABC(),'x')
####
####more precisely you can get a reference to a function without knowing
####its name until run time
####l= [1,2,3,]
####
####l.pop(index) is equivalent
####getattr(l,"pop")(0)
####
####filtering list
####atributes = [ e for e in dir(ABC()) if callable(getattr(ABC(),e))]    
####
####    
    
            

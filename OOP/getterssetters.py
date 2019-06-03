class Employee(object):

    #static class variable
    counter = 0

    def __init__(self,first,last):
        __class__.counter+=1
        self.first = first
        self.last = last
        #create instance variable
        self.nick = 'aka'+first+last

    @property
    def email(self):
        """define email as an attribute"""
        return'{}.{}@email.com'.format(self.first,self.last)

    @email.setter
    def email(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last =last


    def __str__(self):
        return str(self.first)

    def fullname(self):
        return '{}{}'.format(self.first,self.last)

    @classmethod
    def all_names(cls,x):
        first,last = x.split('-')
        new_instance = cls(first,last)
        return new_instance

if __name__ == '__main__':
    #create instances
    c = Employee("alex","dejanu")
    e = Employee.all_names("ionut-mocanu")
    print(Employee.counter)
    print(c)
    print(c.email)
    c.email = 'mocanu neamu'
    print(c.email)

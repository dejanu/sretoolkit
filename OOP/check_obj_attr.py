
 ### library.py - provides classes for business

class Base:

	# abstract method:	
	def implement_me(self):
		raise NotImplementedError("To be implemented")

	def foo(self):
		return 'foo'
############################################################################### diffrent files

# user.py - uses functionality provided by library.py

from library import Base

## verify if methods exists in the module which was imported
assert hasattr(Base, 'foo'), "there is no foo method in Base class"

class Derived(Base):
	def bar(self):
		return self.foo


derived_object = Derived()
derived_object.implement_me()

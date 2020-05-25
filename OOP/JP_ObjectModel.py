class Resistor:

	def __init__ (self, number, manufacturer, resistance):
		self.number = number
		self.manufacturer = manufacturer
		self.resitance = resistance
		


if __name__ == "__main__":

	r = Resistor('10-232-1412', 'honhai', 10)
	
	$ __dict__ - stores instace state aka stores an object's (writable) attributes.
	print(f'{r.__dict__ }') 

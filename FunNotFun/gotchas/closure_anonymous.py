## CLOSURE = executing a function object outside his scopee
## CLOSURE = anonymous function
## ANONYMOUS function = function literal without a name
## CLOSURE = instance of a function ....

def outer_function(text):
	text = text

	def inner_function():
		print(text)

	# RETURNING A CLOSURE (function object without parenthisis)
	return inner_function

if __name__ == "__main__":
	
	my_f = outer_function("much wooow")
	
	#call my_f and access inner_function outside her scope
	my_f()

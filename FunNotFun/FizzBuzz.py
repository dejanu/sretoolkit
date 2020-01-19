# Generate list of numbers from 1 to 100 
# foreach multiple of 3 print Fizz instead of number
# foreach multiple of 5 print Buzz insteam of number
# for numbers multiple of both 3 and 5 print FizzBuzz

def fizz_buzz(l):
	""" fizz%3 buzz%5"""
	fb = []
	for i in l:
		if i%3 == 0:
			if i%5 ==0:
				fb.append("fizzbuzz")
			else:
				fb.append("fizz")
		elif i%5 == 0:
			fb.append("buzz")
		else:
			fb.append(i)
	return fb


# using comprehension
fbb = ["fizzbuzz" if n%3 == 0 and n%5==0 else "fizz" if n%3==0 else "buzz" if n%5==0 else n for n in range(1,45)]
print(fbb)

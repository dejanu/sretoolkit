# uses indexes to remove elements from array
arr = [1,2,3,9,10,12]
for i in arr:
  arr.remove(i)

print(arr) # arr = [2,9,12]

# doesn't use indexes because array does not resize during removing
arr = [1,2,3,9,10,12]
for i in list(arr):
  arr.remove(i)
print(arr) # arr = []


####################################

# for loop takes longer OUTSIDE of function

import timeit

start = timeit.timeit()
for i in range(100):
	print(i)
end = timeit.timeit()
finish = end - start
 
def for_loop():
	for i in range(100):
		print(i)


s = timeit.timeit()
for_loop()
e = timeit.timeit()
f = e - s
print("for outside took {}".format(finish))
print("for inside function took {}".format(f))
	
####################################
# for with else
for i in [4,2,6]:
	if i%2 == 1:
		print(i)
else:
	print("endfor")

####################################
# for vs while speed - which one is fastest (FOR is faster due to range C implementation)

def while_loop(n=1000):
	""" sum no until n"""
	s=0
	i=0
	while i<n:
		s+=i
		i+=1
	return s

def foor_loop(n=1000):
	"""sum no until n"""
	s=0
	for i in range(n):
		s+=i
	return s

print("WHILE loop tool: ", timeit.timeit(while_loop,number=1)) # 7.240000013553072e-05
print("FOR loop tool: ", timeit.timeit(for_loop,number=1)) # 4.8099999730766285e-05

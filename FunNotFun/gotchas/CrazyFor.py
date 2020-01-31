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

for i in [4,2,6]:
	if i%2 == 1:
		print(i)
else:
	print("endfor")

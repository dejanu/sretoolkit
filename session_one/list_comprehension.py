#/usr/bin/python

#######################
# List comprehension  #
#######################


"""
for item in iterable:
	if condition:
		expression

list_comprehension = [ expression for item in iterable if condition ]

"""

# ex1: create a new list which contains the acronym for the words given in list_str
list_str = ["Light","Amplification","Stimulated","Emission","Radiation"]

# ex2. create a new list with all the even number give in the list_no
list_no = [1,2,3,4,5,6,7,8,9,10]

# ex3. create a new list which contains the names of the persons with age == 20
person_list = [{"name":"Alex","age":20}, {"name":"Guido","age":48}, {"name":"Dirk", "age":20}]

# ex4. create a new list which contains the names of the persons from the nested_list
nested_list = [
	[ 
	{"name":"alex",
	"age":"28"
	},
	{"name":"damian",
	"age":"88"
	},	
	],

	[
	{"name":"guido",
	"age":"54"
	},
	{"name":"dan",
	"age":"10"
	},	
	],
]

# ex5. generate a 3x3 matrix using list comprehension
# matrix = [[0,1,2], [0,1,2] ,[0,1,2]]


# ex6. fizzbuzz

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




if __name__ == "__main__":


	# simple iteration
	l = [1, 2, 3, 4, 5]
	double_l = []

	for i in l:
		double_l.append(i*2)

	print("first list : {} second list {}".format(l,double_l))

	# simple iteration with list comprehension

	double_l2 = [i*2 for i in [1,2,3,4,5] ]
	print("first list : {} second list {}".format(l,double_l2))

	# ex1 solution:
	#acronym = [i[0] for i in list_str]
	#print(acronym)

	# ex2 solution:
	even_no = [ i for i in list_no if i%2 == 0]
	print(even_no)

	# ex3 solution:
	names_list = [i.get("name") for i in person_list if i.get("age") == 20]
	print(names_list)


	# ex4 solution:
	print(nested_list)
	names_nested_list = [person.get("name") for group  in nested_list  for person  in group]
	print(names_nested_list)

	# ex5 solution:
	matrix = [ [i for i in range(5)] for j in range(3)]
	print(matrix)
	
	# ex6 solution:
	print(fizz_buzz(range(1,45)))
	fbb = ["fizzbuzz" if n%3 == 0 and n%5==0 else "fizz" if n%3==0 else "buzz" if n%5==0 else n for n in range(1,45)]
	print(fbb)


##FILTER = constructs an iterator for those elements from iterable for which the function returs TRUE  (item for item in iterable if function(item))
##MAP = return an iterator that applies the function to every item of iterable  [cube(1), cube(2), ..., cube(10)]

def par(x):
    """return boolean"""
    pass
    return x%2==0

#MAP returns function return [par(1),par(2)]
map_list = list(map(par,range(1,11)))
print(map_list) #True False

#FILTER returns a filter object, predicate
# is eq with [item for item in iterable if function(item)]
filter_list = list(filter(par,range(1,11)))
print(filter_list)

import math

my_func = lambda x : x+2
#lambda function for max of two elements
y = lambda x,y : x if x > y else y

l=[1,4,6,7,3]

##list of squares from l
s=list(map(lambda x :x**2,l))

even_no = list(filter(lambda x: x%2==0,l))
odd_no = list(filter(lambda x:x%2==1,l))


#########################################
def quadtratic_function(a,b,c):
    """return the quadratic function f(x)=ax^2 + bx + c"""
    return lambda x : a*x**2 + b*x + c

f = quadtratic_function(2,3,-5)
##print(f(1))
##print(f(2))


g = quadtratic_function(2,3,-5)(0)
print(g)
#########################################

def circle_area(r):
    """returns the area of a circle"""
    return math.pi * (r**2)


#list of radius
areas = list(map(circle_area,[2,3,4]))

#############################################EXERCICES##################

# Count the number of letter for each word in the sentence
sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split(" ")
apparitions = list(map(lambda x : len(x),sentence.split(" ")))


#Return all the nubers divisible with 3 in the interval 0:30

numbs = range(0,31)
divthree = list(map(lambda x : x if x%3 == 0 else 0, numbs))
divthree_2 = list(x for x in numbs if x%3 == 0)


###################################
## LIST COMPREHENSION [ expression for item in list if conditional ]
'''
for item in list:
    if conditional:
        expression
'''

#squares
s=[x**2 for x in range(0,10)]


#divizibile cu 3
t=[i for i in range(20) if i%3 == 0]



#take the first letter from every word in a list
m=["Light","Amplification","Stimulated","Emission","Radiation"]
##LASER
acronim=[i[0] for i in m]

########
##Filtering lists
####Return words longer then 6 characters
longest=[i for i in m if len(i)>5]

################################################################
#####PRIME

def isPrime(x):
    """check if a number is prime"""
    for i in range(2,x):
        if x%i == 0:
            return False
    return True


for i in range(1,33):
    print(i,isPrime(i))

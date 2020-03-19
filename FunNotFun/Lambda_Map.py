## FILTER = constructs an iterator for those elements from iterable for which the function returs TRUE  
## (item for item in iterable if function(item)), FILTER returns a filter object aka predicate

## MAP = return an iterator that applies the function to every item of iterable  [cube(1), cube(2), ..., cube(10)]

## REDUCE = is a function that turns an iterable into one thing


import math

# anonymous functions
y = lambda x,y : x if x > y else y


s=list(map(lambda x :x**2,[1,4,6,7,3]))

even_no = list(filter(lambda x: x%2==0,range(100)))
odd_no = list(filter(lambda x:x%2==1,range(100)))


#########################################
def quadtratic_function(a,b,c):
    """return the quadratic function f(x)=ax^2 + bx + c as closure"""
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

##########Filtering lists

####Return words longer then 6 characters
longest=[i for i in m if len(i)>5]

#####Extract the names from the following structure for persons with age ==20

person_list = [{"name":"Alex","age":28}, {"name":"Guido","age":48}, {"name":"Dirk", "age":20}]

names_list = [i.get("name") for i in person_list if i.get("age") == 20]
print(f"{names_list}")

    
 #####################################################

def classic():
    """my_list=[]
       for i in range(10):
            my_list.append(i)"""
    return [i for i in range(10)]


def generate_matrix(columns = 4 , rows = 5):
    """ generate nested arrays aka MATRIX"""
    return [[ j for j in range(columns)] for i in range(rows)]

def flatten_matrix( arr ):
    """ arr: list of lists
    flatten the nested list structure"""
    # [value for inner_list in outer_list for value in inner_list]
    return [e for sub_arr in arr for e in sub_arr]


###### List comphrehension

# [ Ret-Value Outer-loop Inner-loop ]

# e.g Uppercase all letters from string  ['T', 'E', 'S', 'T', ' ', 'S', 'T', 'R', 'I', 'N', 'G']
s = "test string"
upper_s = [ letter.upper() for word in s for letter in word]


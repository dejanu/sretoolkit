

# ternary operator for eval

a,b = 10, 5

min = a if a<b else b

# using tuple

# (if_test_false, if_test_true) [ test ]

print( (b, a) [a < b] ) 

# using lambda we assure that only one expression will be evaluated unlike in tuple
print((lambda: b, lambda: a)[a < b]())



# case when a==b , put all 3 conditions in a list and index will return the one which is True

print(( "a is less than b", "a is equal to b", "a is greater than b")[ [a<b,a==b,a>b].index(True)])


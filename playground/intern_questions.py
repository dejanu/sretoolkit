# question for inters

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1

#different id, nu mutability shit
fruit_list3 = fruit_list1[:]

print(fruit_list1,fruit_list2,fruit_list3)

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'


print(fruit_list1,fruit_list2,fruit_list3)


##########################################

# tuple declaration

t = 'a','b'
tt = ('a','b')

print( t is tt) #False
print(t == tt) #True

##################################

# Dict key assigment {1: 2, '1': 2}
arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1


##################################
# copy return a SHALLOW copy , meanind different id's
rec = {"Name":"Python", "Age":"w0"}




##################################
# Different behaviour interpreter, REPL vs IDLE
# how unique are id's()


d = {1:"one" , 2:"two"}
id1 = id(d)

del(d)

d = {1:"one" , 2:"two"}
id2 = id(d)

# True but in IDLE is False
print(id1==id2)



r = rec.copy()

print(id(r)==id(rec))

############################

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)




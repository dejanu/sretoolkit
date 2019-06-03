#/!usr/bin/python

## Associative arrays (hashes)

## KEYS must be unique and immutable; VALUES can be anything: int, string, list , dict
## Dictionary has O(1) search time complexity whereas List has O(n) time complexity. 

my_dict = {'key1':'value','key2':23,'key3':[1,2,3],'key3':123,'key3':'ooo'}

#create a dict from with given keys and 1 as values
dict.fromkeys(["KeyOne","KeyTwo"],1)

#create dict from zip object (merge two lists)
le_dict = dict(zip([1,2,3],['one','two','three']))

#create dict for alphabet representation
d=dict(zip(map(chr, range(97,123)),range(1,26)))

def return_value_from_key(v,my_dict):
    """ return value if key exist in dict"""
    #print(my_dict.get('key1','key not present in dict'))
    
    if v in my_dict:
        return my_dict[v]
    else:
        return "Key not present in dict"

#return True if the key, available only 2.x
# my_dict.has_key('key5')

# returns an iterator, available only in 2.x
# my_dict.d.iteritems()

#returna list of kvp tuples - [(kvp),(kvp)]
print(my_dict.items())

#return a list of dict KEYS
print(my_dict.keys())

#return a list of dict VALUES
print(my_dict.values())


#update dict - prost style, it appends the key:value at the beggining of the dict
my_dict['key3'] = 'updated'

def Update_DICT():
    '''add a key value pair in dictonary'''
    key=raw_input("Please giva a value: ")
    val=int(input("Please give a key: "))
    try:
        d.update({key:val})
    except:
        print ("Could not add")

def Delete():
    key=raw_input("please give the key to be deleted: ")
    try:
        d.pop(key)
    except:
        print ("key not present")


def sort_d(d):
    '''sort a dictonary by KEYS'''
    new_d = {}
    sorted_k = d.keys().sort()
    for i in sorted_k:
        val=d.get(i)
        dd.update({i:val})
    return new_d

def sort_dd(d):
    """sort dict d by keys"""
    intermediary_dict = dict()
    for i in sorted(d.keys()):
        intermediary_dict[i] = d[i]
    return intermediary_dict
        
#generate a dict mapping no of appearances
s = "Sphinx of black quart judge my voow"
dict_appear = dict()
for i in s:
    if i in dict_appear:
        dict_appear[i]+=1
    else:
        dict_appear[i] = 0
        
# return key if value is found
want_key  = [key for key,value in dict_appear.items() if value == x]
print(dict_appear)
print(want_key)

def recurse_dict(d):
	""" iterative function for nested dict """
	for k,v in d.items():
		if isinstance(v, dict):
			recurse_dict(v)
		else:
			print(k,":",v)


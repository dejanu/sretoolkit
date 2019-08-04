#/!usr/bin/python
import string
## Associative arrays (HASH MAPS) - by default unordered data type
## KEYS must be unique and immutable; VALUES can be anything: int, string, list , dict
## Dictionary has O(1) search time complexity whereas List has O(n) time complexity. 

# dictionary mix
my_dict = {'key1':'value', ('key2','key22'):23, 'key3':[1,2,3], 'key3':123, 3:'ooo'}

#create a dict from with given keys and 1 as values TBD
dict.fromkeys(["KeyOne","KeyTwo"],1)

#creating dict with zip 
le_alphabet = dict(zip(range(len(string.ascii_letters)),string.ascii_letters))

#bench-mark
d = {"Pierre": 42, "Anne": 33, "Zoe": 24}

def dict_info(d):
    """print keys and values and their type"""
    if isinstance(d,dict):
        for k,v in d.items():
            print(f" Key {k} of type{type(k)} and value {v} of type{type(k)}")

# dict look-up is based on keys (e.g search for key k: k in my_dict)
# my_dict.get('key1','key not present in dict')

# if you want look-up by value (e.g search for value v)
# wanted_key  = [key for key,value in dict_appear.items() if value == v]

# not the purpose of dict
def sort_keys(d):
    '''sort a dictonary by KEYS '''
    new_d = {}
    sorted_k = d.keys().sort()
    for i in sorted_k:
        new_dd[i] = d.get(i) 
    return new_d

def sort_values(d): 
    """ sort a dictionary by VALUES """
    dd = dict()
    # list of tuples (k,v) sorted by v
    # where x in lambda is a (k,v) tuple == (d.items(), key=lambda (k,v): v)
    sorted_d = sorted(d, key = lambda x : x[1])
    for i in sorted_d:
        dd[i[0]]=i[1]
    return dd


def unqiue_values_dict(d):
    """create a new dict with only unqiue values
        d = {"f1":312,"f2":432,"f3":312, "f4":432}
        dd = {"f1":312,"f2":432}
    """
    dd = {}
	for k,v in d.items():
		if v not in dd.values():
			dd[k]=v
    return dd


def string_mapping(s="Sphinx of black quart judge my voow"):
        """return a dict mapping no of appearances"""
        dict_appear = dict()
        for i in s:
        if i in dict_appear:
            dict_appear[i]+=1
        else:
            dict_appear[i] = 0
        return dict_appear
        


def recurse_dict(d):
	""" iterative function for nested dict """
	for k,v in d.items():
		if isinstance(v, dict):
			recurse_dict(v)
		else:
			print(k,":",v)


sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]


# sort team by number of wins team(W,L)
d_wins = sorted(sportTeams, key = lambda x: x[1][0], reverse = True)

if __name__ == "__main__":

    #return True if the key, available only 2.x
    # my_dict.has_key('key5')

    # returns an iterator, available only in 2.x
    # my_dict.d.iteritems()

    #returns a list of kvp tuples - [(kvp),(kvp)]
    # my_dict.items()

    #update dict - prost style, it appends the key:value at the beggining of the dict
    # my_dict['key3'] = 'updated'

    #update dict - not prost style, if key update value else add key:value
    # my_dict.update({"key":5})

    


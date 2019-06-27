# given dict

d = {"f1":312,"f2":432,"f3":312, "f4":432}

# return dict

dd = {"f1":312,"f2":432}

def unqiue_values_dict(d):
    """create a new dict with only unqiue values"""
    dd = {}
	for k,v in d.items():
		if v not in dd.values():
			dd[k]=v
    return dd

def sort_keys(d):
    """sorting by key"""
    dd = dict()
    key_sort = sorted(d.keys())
    for i in key_sort:
        dd[i] = d[i]
    return dd

def sort_values(d): 

##    get_val(d):
##        return d[1]
    
    sorted_d = sorted(d.items(), key = get_val)
      return sorted_d

if __name__ == "__main__":

    test_dict = {'c': 3, 'b':45, 'd':32, 'a': 1}

    #sortare directa
    #print({i:test_dict[i] for i in sorted(test_dict.keys())})
    
    #print(sort_dict(d))
    #print(sort_values(test_dict))

    def dict_val(test_dict):
        return test_dict[1]
   
    sorted_x = sorted(test_dict.items(), key=dict_val)
    print(sorted_x)

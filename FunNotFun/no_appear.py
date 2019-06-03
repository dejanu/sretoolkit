#Count the number of appereances of an item in a list

def count_appeareances(l):
    """ take a list arg and count how many times the elements appear in the list"""
    d= {}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print ('the maximum no of apeareances is', max(d.values()))
    return d

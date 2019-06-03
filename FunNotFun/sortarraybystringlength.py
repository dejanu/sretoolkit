"""

Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:

["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:

["Eyes", "Glasses", "Monocles", "Telescopes"]

"""

def get_small(l):
    """ get the smallest element from a list"""
    s=l[0]
    for i in l:
        if len(i)<len(s):
            s=i
        else:
            pass
    return s
    
def sort_by_length(arr):
    #list are mutable do not fuck around
    new_arr = list()
    cp = list(set(arr))
    for i in range(len(cp)):
        small = get_small(cp)
        new_arr.append(small)
        cp.remove(small)
    return new_arr

def one_liner(l):
    return sorted(arr, key=len)

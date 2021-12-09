#!/usr/bin/env python


# choose pivot - best, worst, random
# Partitioning - should be done in linear time
# store elements <= pivot in left sublist
# store elements > pivot in right sublist
# call quick_sort on left sublist
# call quick_sort on right sublist

def quick_sort_one(l):
    """ quick sort first iteration """
    lenght = len(l)
    if lenght <= 1:
        return l
    else:
        #define the pivot as the last element
        pivot=l.pop()
    # define the left and right sublists
    items_greater = []
    items_lower = []
    for item in l:
        if item > pivot:
            items_greater.append(item)
        else:        
            items_lower.append(item)

    # recursively sort the sublists
    return quick_sort_one(items_lower) + [pivot] + quick_sort_one(items_greater)

def quick_sort_two(l):
    """quick sort second iteration"""
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]
    return quick_sort_two(less) + [pivot] + quick_sort_two(greater)

if __name__ == "__main__":
    from rando_generator import gen_random_list

    a=gen_random_list(8,10)
    print(a)
    print(quick_sort_one(a))
    print("------------")
    b=gen_random_list(8, 10)
    print(b)
    print(quick_sort_two(b))
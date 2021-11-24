#!/usr/bin/env python

import random

def gen_random_list(size, max_value):
    """generate a random list of numbers"""
    return [random.randint(0, max_value) for _ in range(size)]

###################################
def bubble_sort(l):
    """bubble sort"""
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                 l[i],l[j+1]=l[j+1],l[i]
    return l
###################################
# def quick_sort(l):
#     """ quick sort first iteration"""
#     lenght = len(l)
#     if lenght <= 1:
#         return l
#     else:
#         #define the pivot as the last element
#         pivot=l.pop()

#     # define the left and right sublists
#     items_greater = []
#     items_lower = []

#     for item in l:
#         if item > pivot:
#             items_greater.append(item)
#         else:        
#             items_lower.append(item)

#     # recursively sort the sublists
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def quick_sort(l):
    """quick sort second iteration"""
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

###################################
def insertion_sort(l):
    """ insertion sort"""
    for i in range(1, len(l)):
        value_to_sort = l[i]

        while l[i-1] > value_to_sort and i > 0:
            # swap elements
            l[i],l[i-1] = l[i-1],l[i]
            i -= 1
    return l

if __name__ == "__main__":
  
    # generate a list of 100 random numbers
    l = gen_random_list(5, 10)
  
    print(l)

    # quick sort
    print("Quick sorted list:     {}".format(quick_sort(l)))
    # insertion sort
    print("Insertion sorted list: {}".format(insertion_sort(l)))
    # bubble sort
    print("Bubble sorted list:    {}".format(bubble_sort(l)))
    
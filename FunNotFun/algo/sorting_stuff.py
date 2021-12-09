#!/usr/bin/env python

def bubble_sort(l):
    """bubble sort"""
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                 l[i],l[j+1]=l[j+1],l[i]
    return l

def bubble(l):
    """bubble sort second approach"""
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                sorted_flag = False
    return l
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

    # # quick sort
    # print("Quick sorted list:     {}".format(quick_sort(l)))
    # # insertion sort
    # print("Insertion sorted list: {}".format(insertion_sort(l)))
    # # bubble sort
    print("Bubble sorted list:    {}".format(bubble(l)))
    
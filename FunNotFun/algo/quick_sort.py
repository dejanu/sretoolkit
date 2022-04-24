#!/usr/bin/env python


# choose pivot - best, worst, random
# Partitioning - should be done in linear time
# store elements <= pivot in left sublist
# store elements > pivot in right sublist
# recursion call quick_sort on left sublist + call quick_sort on right sublist

def quick_sort_one(l):
    """ quick sort first iteration """
    lenght = len(l)
    if lenght <= 1:
        return l
    else:
        # define the pivot as the last element (fucks up the list due to pop)
        pivot = l.pop()
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
        # define the pivot as first element
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]
    return quick_sort_two(less) + [pivot] + quick_sort_two(greater)

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right of pivot
 
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low, high):
        # If current element <= pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
def quick_sort_3(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        # Separately sort elements before partition and after partition
        quick_sort_3(arr, low, pi-1)
        quick_sort_3(arr, pi+1, high)

if __name__ == "__main__":
    from rando_generator import gen_random_list

    # a=gen_random_list(8,10)
    # print(a)
    # print(quick_sort_one(a))
    # print("------------")
    # b=gen_random_list(8, 10)
    # print(b)
    # print(quick_sort_two(b))

    # generate random list if legnth 10 and values between 0 and 100
    array=gen_random_list(10,100)
    print(array)
    # in place sorting
    quick_sort_3(array,0,len(array)-1)
    print(array)
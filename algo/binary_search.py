## algos

def bubble_sort(l):
    """bubble sort in descending order"""
    for i in range(0,len(l)):
        for j in range(0,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l


def binary_search(element,lista):
    """return the position of an element
        using binary search on a sorted list"""
    low = 0
    high = len(lista)-1
    while low<=high:
        mid = (low+high)
        quess=lista[mid]
        if quess == element:
            return mid
        if quess > element:
            high = mid -1
        else:
            low = mid + 1
    return None
        
    
l=[5,6,1,4,12,0]
ll=[1,3,5,7,9]


if __name__ == "__main__":
    print(bubble_sort(l))
    print(binary_search(1,ll))

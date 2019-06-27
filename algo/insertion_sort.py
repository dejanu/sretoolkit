


def insertion_sort(a):
    """ insertion sort"""
    for i in range(1,len(a)):
        print("i : {}".format(i))
        for j in range(i-1, -1, -1):
            print("j : {}".format(j))
            if a[j] > a[j+1]:
                a[j], a[j+1] =  a[j+1], a[j]

            else:
                break
    return a



def insertion_sort2(arr):
    """ another insertion sort"""

    for i in range(1, len(arr)):
        
        j = i -1
        #print("i: {} and j: {}".format(i,j)) 
        while arr[j] > arr[j+1] and j>= 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
            print(arr)
    return arr

if __name__ == "__main__":

    import random

    l = [random.randint(1,100) for i in range(4)]
    print(l)

    print(insertion_sort2(l))

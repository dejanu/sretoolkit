#link: https://www.hackerrank.com/challenges/pairs/problem

## Given an array of integers and a target value, 
## determine the number of pairs of array elements that have a difference equal to the target value.

def pairs(k, arr):
    pairSet = set()
    arr.sort()
    counter = 0
    for val in arr:
        if val - k in pairSet:
            counter += 1
        pairSet.add(val)
    return counter

# in O(n)

def pairs(k, arr):
    # Write your code here
    result = 0
    
    hashPair = {}
    
    # abs(x - element) = k, then x = element +- k
    for element in arr:
        if element + k  in hashPair:
            result += 1
        
        if element -k in hashPair:
            result += 1
        hashPair[element] = True
    return result
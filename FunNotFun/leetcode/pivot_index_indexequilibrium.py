#!/usr/bin/env python3

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# https://leetcode.com/problems/find-pivot-index/

def testequilibrium(arr):
    """ Equilibrium index of an array is an index such that the sum of elements at 
    lower indexes is equal to the sum of elements at higher    """
    
    n = len(arr) 

    # Check for indexes one by one  until an equilibrium index is found 
    for i in range(n): 
        leftsum = 0
        rightsum = 0
      
        # get left sum 
        for j in range(i): 
            leftsum += arr[j] 
          
        # get right sum 
        for j in range(i + 1, n): 
            rightsum += arr[j] 
          
        # if leftsum and rightsum are same, 
        # then we are done 
        if leftsum == rightsum: 
            return i 
      
    # return -1 if no equilibrium index is found 
    return -1



if __name__ == "__main__":

    a = myequi([-7, 1, -3, 7, -4, -7, 0])
    b = myequi([-7, 1, 5, 2, -4, 3, 0])
    print(a)
    print(b)
    

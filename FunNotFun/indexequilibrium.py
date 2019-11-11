def testequilibrium(arr):
    """ Equilibrium index of an array is an index such that the sum of elements at 
    lower indexes is equal to the sum of elements at higher    """
    
    n = len(arr) 
  
    # Check for indexes one by one  
    # until an equilibrium index is found 
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


def myequi(l):
    for i in range(len(l)):
        ss = 0
        sd = 0
        for j in range(i):
            ss+=l[j]
        for j in range(i+1,len(l)):
            sd+=l[j]
        if ss == sd:
            return i
    return -1

if __name__ == "__main__":

    a = myequi([-7, 1, -3, 7, -4, -7, 0])
    b = myequi([-7, 1, 5, 2, -4, 3, 0])
    print(a)
    print(b)
    

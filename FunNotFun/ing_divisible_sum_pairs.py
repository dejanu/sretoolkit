# given an array of integers arr = [a, b, c, d, e] and a positive integer K find the NUMBER OF PAIRS (i,j) 
# where indices i,j are i<j and  arr[i] + arr[j] divisible by k



def divisibleSumPairs(n, k, ar):
   """ nice nested iteration """ 
    c = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if ((ar[i] + ar[j])%k == 0):
                c+=1
            else:
                pass
    return c


#--------------------------------------------------------------------------------------------------------
## Find the maximum difference between two elements such
## that the larger element appears before the smaller one

# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

def generate_list(ll):
    import random
    x = list()
    for i in len(1,ll):
        x.append(random.randint(1,100))
    return x



ll = [98, 88, 34, 88, 12, 14, 56]

def maxDiff(arr):
    #suppose the first two elements are good
    max_diff = arr[1] -arr[0]
    for i in range (0,len(arr)):
        for j in range(i+1, len(arr)):
            print((arr[i],arr[j]))
            if (arr[j] - arr[i] > max_diff):
                maxx_diff = arr[j] -arr[i]
    return maxx_diff



 

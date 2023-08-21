#link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Given an array ar of integers and a positive integer k, 
# determine the number of pairs where ar[i]+ar[j] are divisible by k

def divisibleSumPairs(n, k, ar):
    # return the no of pairs in ar that are divisible with k
    pairs = 0
    # greedy iteration through the array
    for i in range(0,len(ar)-1):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j])%k==0:
                pairs+=1
            else:
                pass
    return pairs
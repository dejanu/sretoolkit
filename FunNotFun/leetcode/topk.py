#!/usr/bin/env python3
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # sort by values
        d_sort = {k:v for k,v in sorted(d.items(),key=lambda i: i[1])}
        print(d_sort)
        return list(d_sort.keys())[:k]


if __name__ == "__main__":


    # Input: nums = [1,1,1,2,2,3], k = 2
    # Output: [1,2]

    print(topKFrequent([1,1,1,2,2,3],2))
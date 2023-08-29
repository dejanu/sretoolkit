#!/usr/bin/env python3

# Given a set of time intervals in any order, our task is to merge all overlapping intervals into one 
# and output the result which should have only mutually exclusive intervals.

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
# https://leetcode.com/problems/merge-intervals/submissions/

def merge(intervals):
    """
    intervals: List[List[int]]
    returns List[List[int]]
    """
    # sort the interval
    intervals.sort()
    # create new list with the first elem from sorted intervals
    new_l = [intervals[0]]

    for i in intervals[1:]:
        # check overlapping
        if new_l[-1][0] <= i[0] <= new_l[-1][1]:
            new_l[-1][-1] = max(new_l[-1][-1],i[-1])
        else:
            new_l.append(i)
    return new_l

if __name__ == "__main__":
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # expected output: [[1,6],[8,10],[15,18]]

    print(intervals)
    print(merge(intervals))



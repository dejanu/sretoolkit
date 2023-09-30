#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Complete the 'droppedRequests' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.

# Given the times at which requests arrive, determine the number of requests that will be dropped.
# Any requests that exceeds the following limits will be dropped:
# the number of requests in any 3-second period cannot exceed 3
# the number of requests in any 10-second period cannot exceed 20
# the number of requests in any 60-second period cannot exceed 60

# The function should return an integer representing the number of requests that will be dropped.

requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
n = len(requestTime)
def droppedRequests(requestTime):
    # Write your code here
    # 3 second period
    count = 0
    for i in range(n):
        if i < 3:
            continue
        if requestTime[i] == requestTime[i-3]:
            count += 1
    # 10 second period
    for i in range(n):
        if i < 10:
            continue
        if requestTime[i] == requestTime[i-10]:
            count += 1
    # 60 second period
    for i in range(n):
        if i < 60:
            continue
        if requestTime[i] == requestTime[i-60]:
            count += 1
    return count

print(droppedRequests(requestTime))
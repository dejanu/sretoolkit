#!/usr/bin/env python3

def ThrottlingGateway(n, requestTime):
    cnt = 0
    for i in range(n):
        if i > 2 and requestTime[i] == requestTime[i - 3]:
            cnt += 1
        elif i > 19 and requestTime[i] - requestTime[i - 20] < 10:
            cnt += 1
        elif i > 59 and requestTime[i] - requestTime[i - 60] < 60:
            cnt += 1
    return cnt

# Example usage
n = 27
requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
print(ThrottlingGateway(n, requestTime)) 

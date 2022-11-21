

# link: https://www.hackerrank.com/challenges/truck-tour/problem

def truckTour(petrolpumps):
    # Calculate the first point from where the truck will be able to complete the circle
    # [[petrol,distance]]: [[1, 5], [10, 3], [3, 4]] - petrolpumps
    fuel=0
    l=0
    i=l
    while i<len(petrolpumps):
        fuel=fuel+petrolpumps[i][0]-petrolpumps[i][1]
        if fuel<0:
            l=l+1
            i=l
            fuel=0
        else:
            i+=1
    return l

def truckTour2(petrolpumps):
    """ same as above but with a for loop """
    total_gas = sum([i[0] for i in petrolpumps])
    total_distance = sum([i[1] for i in petrolpumps])
    if total_gas<total_distance:
        return -1
    fuel = 0
    starting = 0
    diff = 0
    for i in range(len(petrolpumps)):
        fuel = fuel+petrolpumps[i][0]-petrolpumps[i][1]
        if fuel<0:
            starting =i+1
            diff = diff+fuel
            fuel = 0
    if fuel+diff > 0:
        return starting
    else:
        return -1

def GasStation(A, B):
    """ 
    Gast station: A[i] - fuel , B[i] - distance to next station
    A = list with fuel
    B = list with distance
    """
    if sum(A) < sum(B):
        return -1
    res = 0
    cur_gas = 0
    for i in range(len(A)):
        cur_gas += A[i] - B[i]
        if cur_gas < 0:
            cur_gas = 0
            res = i + 1
    return res
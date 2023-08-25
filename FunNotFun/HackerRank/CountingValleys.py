#!/us/bin/env python3

# countingValleys has the following parameter(s): int steps: the number of steps on the hike string path: a string describing the path
# Return: int: the number of valleys traversed

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    seaLevel = 0
    for i in range(steps):
        if path[i] == 'U':
            seaLevel += 1
            # if he climbs up to sea level, he just came out of a valley
            if seaLevel == 0:
                valley += 1
        else:
            seaLevel -= 1
    return valley
l=[1005,1,2,234,12,4,6,3,543,9,27,4,6,1000,1002]


def maxprod(list):
    max_m3 = 0
    max_abs = 0
    max_abs_m3 = 0
    for i in list:
        if i%3 == 0:
            if i>max_abs:
                if max_abs * i > max_m3 * i:
                    max_m3 = i
                elif max_abs * i <= max_m3 * i:
                    max_abs = i
                    max_abs_m3 = i
            elif i>max_m3:
                max_m3  = i
        elif i>max_abs:
            max_abs = i
            if max_abs_m3 > max_m3:  #uitasem verificarea asta
                max_m3 = max_abs_m3
    print(max_m3)
    print(max_abs)
    print(max_m3 * max_abs)

maxprod(l)

## tema2.3
## dict sorting based- on int keys

d = {"alex":8, "mimi":3, "titi":2}

def sort_dict(d):
    """ sorting dict based on values"""
    lv = sorted(d.values())
    dd = {}
    for i in lv:
        for j in d:
            if d[j] == i:
                dd[j]=i
    return dd


def sort_dict2(d):
    """ sorting dict based on values"""
 #  dd = {k:v for k,v in d.items() for i in sorted(d.values()) if v==i}
    return  {k:v for v in sorted(d.values()) for k in d.keys() if d[k]==v}



# calendar_sync


def compare_strings(a,b):
    """ a,b: strings military time representation
        return int: 1,0,2
    """
    a_time = a.split(":")
    b_time = b.split(":")
    if int(a_time[0])>int(b_time[0]):
        return 1
    elif int(a_time[0])== int(b_time[0]):
        # check minutes
        if int(a_time[1])> int(b_time[1]):
            return 1
        elif  int(a_time[1])<int(b_time[1]):
            return 2
        else:
            # equal min
            return 0
    else:
        return 2


def merge_calendars(p1_schedule,p2_schedule):
    """ merge 2 SORTED list of listst"""
    merged_schedules=[]
    p1_l = len(p1_schedule)
    p2_l = len(p2_schedule)
    for i in range(min(p1_l,p2_l)):
        merged_schedules.append(p1_schedule[i])
        merged_schedules.append(p2_schedule[i])
    # place the remaining elements from the longer list
    if p1_l > p2_l:
        merged_schedules.extend(p1_schedule[p2_l:])
    elif p2_l > p1_l:
        merged_schedules.extend(p2_schedule[p1_l:])

    # full merged callendars
    print(merged_schedules)
    clean=[]

    # clean calendar aka merge overlapping stuff
    for i in range(len(merged_schedules)-1):
        if merged_schedules[i][1]>=merged_schedules[i+1][0]:
            if merged_schedules[i][1] >= merged_schedules[i+1][1]:
                clean.append([merged_schedules[i][0],merged_schedules[i][1]])
            else:
                clean.append([merged_schedules[i][0],merged_schedules[i+1][1]])
    print(clean)
            
            

if __name__ == "__main__":

    
    a=[['9:00','10:30'], ['12:00','13:00'], ['16:00','18:00']]
    b=[['10:00','11:30'], ['12:30','14:30'], ['16:00','17:00']]
    # test comparator function
    compare_strings('9:00', '10:30')
    
    print("Person one:{}".format(a))
    print("Person two:{}".format(b))
    merge_calendars(a,b)

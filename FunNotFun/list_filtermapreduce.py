def classic():
    """my_list=[]
       for i in range(10):
            my_list.append(i)"""
    return [i for i in range(10)]


def generate_matrix(columns = 4 , rows = 5):
    """ generate nested arrays aka MATRIX"""
    return [[ j for j in range(columns)] for i in range(rows)]

def flatten_matrix( arr ):
    """ arr: list of lists
    flatten the nested list structure"""i
    # [value for inner_list in outer_list for value in inner_list]
    return [e for sub_arr in arr for e in sub_arr]

if __name__ == "__main__":
    print(classic())
    
    print(flatten_matrix( [[-1, 1, 2, -2, 6], [3, 4, -5] ]))



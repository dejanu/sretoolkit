#!/usr/bin/env python

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def gen_random_matrix(cols,rows):
    """ Generate a random matrix of size cols x rows """
    import numpy as np
    # Generate a random matrix of floats
    # return np.random.rand(cols,rows)
    return np.random.randint(1, 10, size=(cols,rows))

def generate_matrix(cols,rows):
    import random
    #print( [[ j for j in range(cols)] for i in range(rows)] )
    # empty_matrix = [[] for _ in range(3)]
    l=[[random.randint(1, 10)]*cols for i in range(rows)]
    return(l)


if __name__ == '__main__':
    test = gen_random_matrix(3,3)
    print(test)

    # flatten the matrix
    max_col = len(test[0])
    max_row = len(test)
    for x in range(max_col):
        for y in range(max_row):
            print(test[x][y])

    # sum the diagonals
    dp = [test[i][i] for i in range(0, len(test))]
    dc = [test[i][~i] for i in range(0, len(test))]
    print(dp)
    print(dc)

    # get columns
    cols = list(zip(*test))
    print(cols)
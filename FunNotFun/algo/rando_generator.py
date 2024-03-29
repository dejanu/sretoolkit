#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def gen_random_list(size, max_value):
    """
    size: int size of list
    max_value: int max value of elements in list
    return random generate list of size size
    """
    return [random.randint(0, max_value) for _ in range(size)]

# # shuffle list
# sample_list = [1, 2, 3, 4, 5]
# # shuffle inplace using Fisher–Yates shuffle Algorithm
# random.shuffle(sample_list)

# # create a new shuffled list and retain the original sample_list
# res = random.sample(test_list, len(sample_list))

import random


# shuffle list
sample_list = [1, 2, 3, 4, 5]

# shuffle inplace using Fisher–Yates shuffle Algorithm
random.shuffle(sample_list)

# create a new shuffled list and retain the original sample_list
res = random.sample(test_list, len(sample_list))


# manipulating list while iterating

# remove no bigger than five

nums = [1, 2, 3, 5, 6, 7, 0, 1]
for ind, n in enumerate(nums):
    if n < 5:
        del(nums[ind])# expected: nums = [5, 6, 7]
#result [2, 5, 6, 7, 1]

# list comprehension
nums = [n for n in nums if n >= 5]
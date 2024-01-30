# Write a function, maxValue, that takes in list of numbers as an
# argument. The function should return the largest number in the list.

# Solve this without using any built-in list methods.

# You can assume that the list is non-empty.

# max_value([4, 7, 2, 8, 10, 9]) # -> 10
# max_value([10, 5, 40, 40.3]) # -> 40.3
# max_value([-5, -2, -1, -11]) # -> -1
# max_value([42]) # -> 42
# max_value([1000, 8]) # -> 1000
# max_value([1000, 8, 9000]) # -> 9000
# max_value([2, 5, 1, 1, 4]) # -> 5

# method 1 - non-built in methods
def max_value(nums):
    maximum = float('-inf')

    for num in nums:
        if num > maximum:
            maximum = num 

    return maximum

print(max_value([-5, -2, -1, -11])) # -> -1

# method 2 - built-in method: max()
def max_value_2(nums_2):
    return max(nums_2)

print(max_value_2([-5, -2, -1, -11]))


# n = len of nums input
# time: O(n)
# space: O(1) - the function only uses a constant amount of additional space, regardless of the size of the input list
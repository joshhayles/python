# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

# pair_sum([3, 2, 5, 4, 1], 8)  # -> (0, 2)
# pair_sum([4, 7, 9, 2, 5, 1], 5)  # -> (0, 5)
# pair_sum([4, 7, 9, 2, 5, 1], 3)  # -> (3, 5)
# pair_sum([1, 6, 7, 2], 13)  # -> (1, 2)
# pair_sum([9, 9], 18)  # -> (0, 1)
# pair_sum([6, 4, 2, 8], 12)  # -> (1, 3)

# Option 1: Brute force
def pair_sum(nums, target_sum):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                return (i, j)
            
print(pair_sum([3, 2, 5, 4, 1], 8))  # -> (0, 2)

# Option 2: Hash
def pair_sum_2(nums_2, target_sum_2):
    seen = {}

    for index, num in enumerate(nums_2):
        complement = target_sum_2 - num 

        if complement in seen:
            return (index, seen[complement])

        seen[num] = index

print(pair_sum_2([4, 7, 9, 2, 5, 1], 5))  # -> (5, 0)
print(pair_sum_2([3, 2, 5, 4, 1], 8))  # -> (2, 0)
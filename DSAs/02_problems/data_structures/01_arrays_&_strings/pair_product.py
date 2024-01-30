# same as pair_sum, but with multiplication:
def pair_product(nums, target_product):
    seen = {}

    for index, num in enumerate(nums):
        complement = target_product / num 

        if complement in seen:
            return (index, seen[complement])

        seen[num] = index

print(pair_product([3, 2, 5, 4, 1], 8))  # -> (3, 1)
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
# intersection([2,4,6], [4,2]) # -> [2,4]
# intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
# intersection([0,1,2], [10,11]) # -> []
# a = [ i for i in range(0, 50000) ]
# b = [ i for i in range(0, 50000) ]
# intersection(a, b) # -> [0,1,2,3,..., 49999]

# Option 1: Loop through both sets and compare:
def intersection(a, b):
    matching_set = set()
    result = []

    for item in a:
        matching_set.add(item)

    for item in b:
        if item in matching_set:
            result.append(item)

    return result

# print(intersection([4,2,1,6], [3,6,9,2,10]))  # -> [6, 2]

# Option 2: Loop through only one set, pass the other to set() function:
def intersection_2(a, b):
    matching_set_2 = set(a)
    result_2 = []

    for item in b:
        if item in matching_set_2:
            result_2.append(item)

    return result_2

# print(intersection([4,2,1,6], [3,6,9,2,10]))  # -> [6, 2]

# Option 3: One-line
def intersection_3(a, b):
    matching_set_3 = set(a)
    return [item for item in b if item in matching_set_3]

print(intersection([4,2,1,6], [3,6,9,2,10]))  # -> [6, 2]

# n = len of a
# m = len of b
# time: 
# space: 
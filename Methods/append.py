# add an item to the end of the list using slicing method. 
# Equivalent to a[len(a):] = [x]
numbers = [1, 2, 3]

numbers[len(numbers):] = [21]

print(numbers)  # -> [1, 2, 3, 21]

# numbers[len(numbers):] = [21] this is a slicing operation that takes the space after the last item in numbers using the expression [len(numbers):]. Then, you assign the iterable to that slice ( = [21] )

# using this kind of assignment allows you to add several items to the end of your list at once (something you can't do with .append because that adds a single item:
numbers_2 = [1, 2, 3, 4]

numbers_2[len(numbers_2):] = [22, 23, 24]

print(numbers_2)  # -> [1, 2, 3, 4, 22, 23, 24]

# using.append() you can add a number, list, tuple, dictionary, user-defined object, or any object to an existing list, but it only adds a single item, or object at a time:
x = [1, 2, 3, 4]

y = (5, 6)

x.append(y)

print(x)  # -> [1, 2, 3, 4, (5, 6)]

# if you want to add each individual item to the end, you can use .extend():
a = [1, 2, 3, 4]

b = (5, 6, 7)

a.extend(b)

print(a)  # -> [1, 2, 3, 4, 5, 6, 7]
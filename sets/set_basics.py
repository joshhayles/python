
# a set is a collection which is unordered (don't have a defined order), unchangeable (except for removing and/or adding items) and duplicates are not allowed

# a set is a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table.

myset = {"apple", "banana", "cherry"}
print(myset) # set(['cherry', 'apple', 'banana'])

# get the number of items in a set
myset = {"apple", "banana", "cherry"}
print(len(myset)) # => 3

# a set can contain different data types:
set1 = {"abc", 34, True}

# you can also use the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))
print(thisset) # => set(['cherry', 'apple', 'banana'])

# {} does not represent an empty set. It represents an empty dictionary. To create an empty set: set() syntax is used

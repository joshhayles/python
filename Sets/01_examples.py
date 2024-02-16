# Python's built-in set type is:
    # unordered
    # set elements are unique (duplicates are not allowed)
    # a set itself can be modified, but the elements contained in the set must be of an immutable type (values can't be changed after they are created)

# Define a set using built-in set() function:
# x = set(<iterable>)

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)  # -> {'baz', 'qux', 'bar', 'foo'} ... returns unique elements

# passing a string, since strings are also iterable
a = set("joshua")
print(a)  # -> {'h', 'a', 'o', 'u', 'j', 's'} ... unpredictable return order

# Define a set using curly braces:
# x = {<obj>, <obj>, ...}

# Example 1: each obj becomes a distinct element of the set (similar to the .append() method)
b = {'foo'}
print(b) # -> {'foo'} ... returns the obj

# Example 2: this will accomplish the same as set([]):
c = {'foo', 'bar', 'baz', 'foo', 'qux'}
print(c)  # -> {'baz', 'qux', 'foo', 'bar'}

# Example 3: including a tuple, and a mixture of types in a set:
d = {43, 'Josh', 5.44, (1,3,5)}
print(d)  # -> {'Josh', 43, 5.44, (1, 3, 5)}  Note: the order of the tuple elements stay in tact
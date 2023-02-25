
# this is great for "doing something" for each element in a list, tuple, set, etc.

# loop through index numbers using range() and len()
thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
    print(thislist[i]) # => apple banana cherry (listed vertically)

# print a list of your friends:
friends = ["Tom", "Jerry", "Josh"]

for friend in friends:
    print(f"{friend} is my friend.")
# => Tom is my friend. Jerry is my friend.Josh is my friend.


# list comprehension offers the shortest syntax for looping through lists

# short hand for loop:
# syntax: 1. The first variable is what you want to add to the list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # apple banana cherry

# another example:
friends = ["Tom", "Bob", "Sam"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s) # => ['Sam']
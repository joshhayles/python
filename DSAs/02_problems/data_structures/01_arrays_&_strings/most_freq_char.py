# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

# most_frequent_char('bookeeper')  # -> 'e'
# most_frequent_char('david')  # -> 'd'
# most_frequent_char('abby')  # -> 'b'
# most_frequent_char('mississippi')  # -> 'i'
# most_frequent_char('potato')  # -> 'o'
# most_frequent_char('eleventennine')  # -> 'e'
# most_frequent_char('riverbed')  # -> 'r'

def most_frequent_char(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    best = None # use a variable for any tie breakers

    for ele in s:
        if best is None or count[ele] > count[best]:
            best = ele

    return best 

print(most_frequent_char("bookeeper"))  # -> e
print(most_frequent_char("eleventennine"))  # -> e
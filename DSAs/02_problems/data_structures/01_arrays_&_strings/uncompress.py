# Write a function, uncompress, that takes in a string as an argument. The
# input string will be formatted into multiple groups according to the
# following pattern:

# <number><char>

# for example, '2c' or '3a'.

# The function should return an uncompressed version of the string where
# each 'char' of a group is repeated 'number' times consecutively. You may
# assume that the input string is well-formed according to the previously
# mentioned pattern.

# uncompress("2c3a1t") # -> 'ccaaat'
# uncompress("4s2b") # -> 'ssssbb'
# uncompress("2p1o5p") # -> 'ppoppppp'
# uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
# uncompress("127y") # ->
# 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

def uncompress(s):
    i = 0
    j = 0
    numbers = "0123456789"
    result = []

    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            number_parse = int(s[i:j])
            result.append(number_parse * s[j])
            j += 1
            i = j

    return "".join(result)

print(uncompress("2p1o5p")) # -> ppoppppp

# n = number of groups
# m = max_number found in any group
# time: O(n*m)
# space: O(n*m)

# note: without casting number_parse as an integer (line 31, performing the string slice), the string slice is already a string, and concatenation would have to be performed ( + ) instead of multiplication. You can't multiply two strings together, you'll get a TypeError.

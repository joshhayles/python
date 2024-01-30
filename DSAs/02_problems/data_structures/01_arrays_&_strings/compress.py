# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

# compress('ccaaatsss')  # -> '2c3at3s'
# compress('ssssbbz')  # -> '4s2bz'
# compress('ppoppppp')  # -> '2po5p'
# compress('nnneeeeeeeeeeeezz')  # -> '3n12e2z'
# compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
# // -> '127y'

def compress(s):
    s += "!"
    i = 0
    j = 0
    result = []

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            number = j - i 
            if number == 1:
                result.append(s[i]) # append only the char at index i to the result
            else:
                result.append(str(number) + s[i])

            i = j # "i" is set to the value of "j" because it's the start of a new sequence. "i" belongs nested under the first else block so that it's not updating on every iteration of the loop vs just when a new char sequence starts

    return "".join(result)

print(compress("ccaaatsss")) # -> 2c3at3s


# n = len of string
# time: O(n)
# space: O(n)
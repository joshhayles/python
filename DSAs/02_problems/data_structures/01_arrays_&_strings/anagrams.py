# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

# anagrams('restful', 'fluster')  # -> True
# anagrams('cats', 'tocs')  # -> False
# anagrams('monkeyswrite', 'newyorktimes')  # -> True
# anagrams('paper', 'reapa')  # -> False
# anagrams('elbow', 'below')  # -> True
# anagrams('tax', 'taxi')  # -> False
# anagrams('taxi', 'tax')  # -> False
# anagrams('night', 'thing')  # -> True
# anagrams('abbc', 'aabc')  # -> False
# anagrams('po', 'popp')  # -> false
# anagrams('pp', 'oo')  # -> false

from collections import Counter

# Method 1: using a helper function and dictionary
def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0

        count[char] += 1

    return count 

# print(char_count("catss")) # -> {'c': 1, 'a': 1, 't': 1, 's': 2}
print(anagrams('restful', 'fluster')) # -> True

# Method 2: Built-in Counter method
def anagrams_2(s1, s2):
    return Counter(s1) == Counter(s2)

print(anagrams_2('restful', 'fluster')) # -> True


# n = length string 1
# m = length string 2
# time: O(n + m)
# space: O(n + m)
# Using Hashmap
# It uses a hashmap (dictionary) to count the frequency
# of each character in both strings and compares the two
# frequency maps. If both strings have identical character
# frequencies, they are anagrams.

from collections import Counter  # for character frequency counting

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):  # check length
    print("No")
else:
    if Counter(s1) == Counter(s2):  # compare character counts
        print("Yes")
    else:
        print("No")
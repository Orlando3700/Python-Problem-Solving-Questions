# Write a Python program to find the longest word in a sentence

# This defines a function called longest_word that takes
# a single parameter sentence.
# sentence is expected to be a string
def longest_word(sentence):
    # This splits the sentence into individual words using
    # the default separator, which is whitespace.
    words = sentence.split()
    # This uses Python’s built-in max() function to find
    # the longest word in the list.
    # The key=len argument tells max() to compare the
    # words by their length (i.e., len(word))
    return max(words, key=len)

print(longest_word("The fox jumps over the lazy dog"))  # jumps
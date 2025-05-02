# Write a Python code to check if a string is a palindrome

# This defines a function named is_palindrome that takes
# one parameter called s.
# s is expected to be a string
def is_palindrome(s):
    # This is the body of the function, and it returns a Boolean (True or False).
    # s[::-1] is a slicing operation that reverses the string s.
    # s == s[::-1] checks if the original string is equal to its reversed version.
    # If they are equal, the string is a palindrome, so the function returns True; otherwise, False.
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
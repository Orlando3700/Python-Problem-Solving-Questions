# Removing All Whitespace in a String

import re

string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)

# Using replace() method
# To remove all spaces from a string, we can use replace()
# method.

s = "Python is fun"
s = s.replace(" ", "")
print(s)

# Removing Leading and Trailing Spaces
 
s = "   Hello World   "
s = s.strip()
print(s)

# s.strip() removes spaces from the start and end of s.

# If we only want to remove spaces from the beginning of
# the string, we can use lstrip().

s = "   Hello World"
s = s.lstrip()
print(s)

# s.lstrip() removes spaces from the left side of s only.

# Removing Trailing Spaces Only
# To remove spaces from the end of a string, we can use
# rstrip().

s = "Hello World   "
s = s.rstrip()
print(s)

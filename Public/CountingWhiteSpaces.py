# Counting the White Spaces in a String

# Option 1

string = "O rl and o "
print(string.count(' '))

# Option 2

# Using split()
# split() method in Python splits a string into a list of
# substrings based on a specified delimiter, which can be
# used to count spaces by calculating the difference
# between the total number of words and one.

s = "Count the spaces in this string."

# Split the string by spaces and count the spaces
space_count = len(s.split()) - 1

print(space_count)

# Option 3

# Using count() Method
# count() method in Python is used to return the number
# of occurrences of a specified element in a list or
# string

s = "Count the spaces in this string."

# Count spaces using the count() method
space_count = s.count(" ")

print(space_count)

# Option 4

# Using for Loop
# Using a for loop with a conditional check allows us to
# iterate through a string or list and perform an action
# based on a specific condition, such as counting
# occurrences of a particular character

s = "Count the spaces in this string."

# Initialize space counter
space_count = 0

# Loop through each character in the string
for char in s:
    # Check if the character is a space
    if char == " ":
        # Increment space count
        space_count += 1

print(space_count)

# Option 5

# Using re.findall()
# re.findall() function with regular expressions allows
# us to find all occurrences of a specific pattern, such
# as spaces, and count them by measuring the length of
# the resulting list.

# Import the regular expression module
import re

# Input string
s = "Count the spaces in this string."

# Use re.findall() to find all spaces
space_count = len(re.findall(" ", s))

# Print the number of spaces
print(space_count)


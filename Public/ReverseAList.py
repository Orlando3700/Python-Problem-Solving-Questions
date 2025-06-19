# Reverse a list

# Example 1

# The reverse() method reverses the elements of the list
# in-place and it modify the original list without creating
# a new list. This method is efficient because it doesn't
# create a new list.

a = [1, 2, 3, 4, 5]
# Reverse the list in-place
a.reverse()
print(a)

# Example 2

# Using List Slicing
# Another efficient way to reverse a list is by using
# list slicing. This method creates a new list that
# contains the elements of the original list in reverse
# order.
 
a = [1, 2, 3, 4, 5]

# Create a new list that is a reversed list
# of 'a' using slicing
rev = a[::-1]

print(rev)

#Example 3

# Using the reversed()
# Python’s built-in reversed() function is another way
# to reverse the list. However, reversed() returns an
# iterator, so it needs to be converted back into a list.

a = [1, 2, 3, 4, 5]

# Use reversed() to create an iterator
# and convert it back to a list
rev = list(reversed(a))
print(rev)

# Example 4

# Using a Loop (creating new reversed list)
# If we want to reverse a list manually, we can use a
# loop (for loop) to build a new reversed list. This
# method is less efficient due to repeated insertions
# and extra space required to store the reversed list.

a = [1, 2, 3, 4, 5]

# Initialize an empty list to store reversed element
res = []

# Loop through each item and insert
# it at the beginning of new list
for val in a:
    res.insert(0, val)
print(res)

# Example 5

# Using a Loop (In-place reverse)
# We can use this method if we want to reverse the list
# in-place (without creating new list) using for loop.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define the start and end indices
start, end = 2, 6

# Reverse the elements from index 2 to 6
while start < end:
  
    # Swap elements at start and end
    a[start], a[end] = a[end], a[start]
    
    # Move the start index forward
    start += 1
    
    # Move the end index backward
    end -= 1

print(a)

# Example 6

# Using List Comprehension
# We can also use list comprehension to reverse the
# list, although this is less common than the other
# methods mentioned.

a = [1, 2, 3, 4, 5]

# Use list comprehension to create
# a reversed version of the list
rev = [a[i] for i in range(len(a) - 1, -1, -1)]
print(rev)


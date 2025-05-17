# Adding Two List Elements Together

# Option 1
lst1 = [1, 2, 3]
lst2 = [4, 5, 6] 

res_lst = [] 
for i in range(0, len(lst1)):
    res_lst.append(lst1[i] + lst2[i]) 
print(res_lst)

# Option 2

# Another approach 

# Using zip() Function
# zip() function zip() combines two or more iterables
# element by element that makes it easy to iterate over
# corresponding elements. It returns a tuple, which we can
# sum.

a = [1, 2, 3]
b = [4, 5, 6]

c = [x + y for x, y in zip(a, b)]
print(c)

# Option 3

# Input lists
a = [1, 3, 4, 6, 8]
b = [4, 5, 6, 2, 10]

# Add corresponding elements using list comprehension
c = [a[i] + b[i] for i in range(len(a))]

# Print the result
print(c)

# Option 4

# Using map() Function
# map() function applies a given function to each item of
# an iterable (like a list) and returns a map object. We
# can use this to add corresponding elements of two lists.

# Input lists
a = [1, 3, 4, 6, 8]
b = [4, 5, 6, 2, 10]

# Use map to add corresponding elements of both lists
c = list(map(lambda x, y: x + y, a, b))

# Print the result
print(c)

# Option 5

# Using a Simple for Loop
# The most basic way to add corresponding elements is by
# using a simple for loop.

# Input lists
a = [1, 3, 4, 6, 8]
b = [4, 5, 6, 2, 10]

# Create an empty list to store the result
c = []

# Loop through both lists and add corresponding elements
for i in range(len(a)):
    c.append(a[i] + b[i])

# Print the result
print(c)
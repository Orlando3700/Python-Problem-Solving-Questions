# Write a Python program to find common elements in two lists

# Using Set Intersection (Most Efficient)
# The & operator or intersection() method is the most
# efficient way to find common elements between two lists.
# Here it converts both lists to sets to eliminate
# duplicates and perform a set intersection and the result
# contains all elements common to both sets which are
# converted back to a list for further use

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common) #[3, 4]

# Using List Comprehension
# This method filters elements from one list that also
# exist in the other list. Here it Iterates through the
# first list and checks if each element exists in the
# second list. It works well for medium sized lists.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Find common elements using list comprehension
common = [x for x in a if x in b]

print(common)

# Using filter() and lambda
# The filter() function can be combined with a lambda
# expression to find common elements. It applies a
# condition to each element of the first list and retains
# those present in the second list.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Find common elements using filter and lambda
common = list(filter(lambda x: x in b, a))

print(common)

# Using Nested Loops
# This method compares each element of the first list
# with every element of the second list. Here it Iterates
# through both lists to check for common elements, it is
# simple but inefficient for large lists due to nested lists.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Find common elements using nested loops
common = []
for x in a:
    if x in b:
        common.append(x)

print(common)



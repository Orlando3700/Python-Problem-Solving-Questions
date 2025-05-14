# Python Set intersection() Method

# The intersection() method returns a set that
# contains the similarity between two or more sets.

# Meaning: The returned set contains only items
# that exist in both sets, or in all sets if the
# comparison is done with more than two sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)


# Use & as a shortcut instead of intersection():

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x & y

print(z)


# Join 3 sets, and return a set with items that
# is present in all 3 sets:

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)


# Join 3 sets with the & operator:

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x & y & z

print(result)



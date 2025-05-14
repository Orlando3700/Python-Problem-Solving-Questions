# Python Set intersection() Method Example:
s1 = {1, 2, 3}
s2 = {2, 3}
print(s1.intersection(s2))
# Output: {2, 3}


# Example 1: Working of set intersection()

# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4, 6, 8}
 
# intersection of two sets
print("set1 intersection set2 : ",
      set1.intersection(set2))
 
# intersection of three sets
print("set1 intersection set2 intersection set3 :",
      set1.intersection(set2, set3))

# Output: 
# set1 intersection set2 :  {4, 6}
# set1 intersection set2 intersection set3 : {4, 6}


# Example 2: Python set intersection operator(&)

# We can also get intersections using ‘&’ operator.

# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {1, 0, 12}
 
print(set1 & set2)
print(set1 & set3)
 
print(set1 & set2 & set3)

# Output:
# {4, 6}
# set()
# set()


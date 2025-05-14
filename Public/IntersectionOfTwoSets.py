# Write a Python program to find the intersection of two sets

def intersection(set1, set2):
    return set1 & set2

print(intersection({1, 2, 3}, {2, 3, 4}))  # {2, 3}
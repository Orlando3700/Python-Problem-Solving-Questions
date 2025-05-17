# Finding the Minimum Number in a List

# Option 1

numberList = [15, 85, 35, 89, 125, 2]

minNum = numberList[0]
for num in numberList:
    if minNum > num:
        minNum = num
print(minNum)

# Option 2

# Using min()
# The min() function takes an iterable and returns the smallest value.

a = [8, 3, 5, 1, 9, 12]

# Find the smallest number
smallest = min(a)
print(smallest)

# Option 3

# Using Sorting
# Another way to find the smallest number in a list is by
# sorting it. Once sorted in ascending order, the smallest
# number will be at the beginning of the list.

a = [8, 3, 5, 1, 9, 12]
a.sort()
smallest = a[0]
print(smallest)
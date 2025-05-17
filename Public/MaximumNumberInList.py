# Finding the Maximum Number in a List

# Option 1

numberList = [15, 85, 35, 89, 125]

maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)

# Option 2

# Using max()
# Python provides a built-in max() function that returns
# the largest item in a list or any iterable. The time
# complexity of this approach is O(n) as it traverses
# through all elements of an iterable.

a = [10, 24, 76, 23, 12]

# Max() will return the largest in 'a'
largest = max(a)
print(largest)

# Option 3

# Using reduce() function from functools
# Another method to find the largest number in a list is
# by using the reduce() function along with a lambda
# expression.

from functools import reduce

a = [10, 24, 76, 23, 12]

# Find the largest number using reduce
largest = reduce(lambda x, y: x if x > y else y, a)

print(largest)
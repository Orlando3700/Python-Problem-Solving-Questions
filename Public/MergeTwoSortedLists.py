# Merge Two Sorted Lists

# Example 1

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

# Example 2

# Using heapq.merge()
# heapq.merge() function efficiently merges two sorted
# iterables.

import heapq
a = [1, 3, 5]
b = [2, 4, 6]
c = list(heapq.merge(a, b))
print(c)

# Example 3

# Using sorted() with Concatenation
# We can simply concatenate the lists and then sort them
# using sorted().

a = [1, 3, 5]
b = [2, 4, 6]
c = sorted(a + b)
print(c)

# Example 4

# Using Two Pointers (Manual Merge)
# This method manually merges two sorted lists without
# using extra sorting.

a = [1, 3, 5]
b = [2, 4, 6]
i, j, c = 0, 0, []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
c.extend(a[i:])
c.extend(b[j:])
print(c)

# Example 5

# Using itertools.chain()
# This method flattens both lists and sorts the result
# using itertools.chain() and sorted().

from itertools import chain
a = [1, 3, 5]
b = [2, 4, 6]
c = sorted(chain(a, b))
print(c)


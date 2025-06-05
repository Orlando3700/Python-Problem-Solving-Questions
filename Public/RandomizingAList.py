# Randomizing the Items of a List in Python

# Example 1
from random import shuffle

lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)

# Example 2

# Using random.shuffle()
# random.shuffle() function is simplest way to shuffle a
# list in-place. It directly modifies the list and doesn't
# return a new list.

import random
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)

# Example 3

# Using random.sample()
# If we don't want to modify the original list then use
# random.sample() to generate a shuffled copy. This method
# returns a new list with shuffled elements.

import random
a = [1, 2, 3, 4, 5]
b = random.sample(a, len(a))
print(b)

# Example 4

# Using sorted() with random Keys
# We can also use sorted() with a random key to get a new
# shuffled list but this method is not commonly used to
# shuffle a list.

import random
a = [1, 2, 3, 4, 5]
b = sorted(a, key=lambda x: random.random())
print(b)


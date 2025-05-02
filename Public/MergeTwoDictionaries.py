# Write a Python code to merge two dictionaries

# Option 1
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged) #{'a': 1, 'b': 3, 'c': 4}

# Option 2

# Using update()
# update() method can be used to merge dictionaries.
# It modifies one dictionary by adding or updating
# key-value pairs from another.

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d1.update(d2)
print(d1)

# Option 3

# Using | Operator (Python 3.9+)
# | operator introduced in Python 3.9 can be used to merge
# dictionaries. It creates a new dictionary without
# modifying the original dictionary.


d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1 | d2
print(d3)

# Option 4

# Using Dictionary Unpacking (**)
# Dictionary unpacking allows us to merge dictionaries
# into a new one.

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = {**d1, **d2}
print(d3)

# Option 5

# Using Loop
# We can use a loop (for loop) to merge dictionaries.

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value

print(d3)




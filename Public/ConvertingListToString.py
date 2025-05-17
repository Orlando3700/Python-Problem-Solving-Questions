# Converting a List into a String

# Option 1

lst = ["P", "Y", "T", "H", "O", "N"]
string = ''.join(lst)

print(string)
print(type(string))

# Option 2

# Using the join() Method

a = ['Orlando', 'and', 'Amanda']
res = ' '.join(a)
print(res)

# Option 3

# Using a Loop
# Another approach is to use a loop (for loop) to iterate
# through the list and concatenate each element to a
# result string. This method provides more control if we
# need to manipulate each element before adding it to the
# string.

a = ['Orlando', 'and', 'Amanda']

# Convert list to string using a loop
res = ''
for s in a:
    res += s + ' '

# Remove trailing space
res = res.strip()  
print(res)

# Option 4

# Using List Comprehension with join()
# List comprehension provides a concise way to convert
# each element in the list a to a string.

a = [1, 'apple', 3.14, 'banana']
res = ' '.join([str(s) for s in a])
print(res)

# Option 5

# Using the map()
# The map() function can also be used to convert each
# element in a list to a string. This is similar to list
# comprehension but it can be more readable in certain cases.

a = [1, 'apple', 3.14, 'banana']

# Converting list to string using map() function
res = ' '.join(map(str, a))

print(res)
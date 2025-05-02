# Write a Python code to remove duplicates from a list

# Using set() method is most efficient for unordered lists.
# Converting the list to a set removes all duplicates since
# sets only store unique elements.

list1 = [1, 2, 2, 3, 4, 4]
unique_list1 = list(set(list1))
print(unique_list1) #[1, 2, 3, 4]

# Using List Comprehension
# List comprehension combined with a enumerate() allows
# removing duplicates while preserving the original order.
# To remove duplicates while maintaining the original order
# we use a set to track seen elements to preserve order.

a = [1, 2, 2, 3, 4, 4, 5]

# Using list comprehension to remove duplicates
unique_list = [item for index, item in enumerate(a) if item not in a[:index]]
print(unique_list)

# Using dict.fromkeys()
# Dictionaries in Python 3.7+ maintain insertion order
# making this method efficient way to remove duplicates
# while preserving order.

a = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(dict.fromkeys(a))
print(unique_list)

# Using a Loop for Explicit Control
# Using loop is useful for beginners as it follows
# step-by-step logic to remove duplicates. This method
# will remove the original order of elements.

a = [1, 2, 2, 3, 4, 4, 5]

unique_list = []

for x in a:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)




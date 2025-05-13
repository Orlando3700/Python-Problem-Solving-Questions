# Write a Python code to implement a function
# to flatten a nested list

# This defines a function called flatten that
# takes one argument: nested_list. This is
# expected to be a list that might contain
# other lists (nested lists)
def flatten(nested_list):
    # Creates an empty list called flat_list.
    # This will store the flattened elements
    # (i.e., all individual elements from all
    # levels of nesting)
    flat_list = []
    # Starts a loop that goes through each
    # element (item) in the input nested_list
    for item in nested_list:
        # Checks if the current item is a list.
        # If it is, that means it's a nested
        # list and needs to be flattened further.
        if isinstance(item, list):
            # Recursively calls the flatten
            # function on the nested item. This
            # call returns a flat list of that
            # nested part, which is then added
            # to flat_list using .extend()
            # (which appends elements of one
            # list into another).
            flat_list.extend(flatten(item))
        # If item is not a list (i.e., it's a
        # basic element like a number), it is
        # directly added to flat_list using
        # .append().
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]


# Write a Python code to find the maximum subarray sum

# This Python function implements Kadane’s
# Algorithm, which efficiently finds the
# maximum sum of a contiguous subarray within
# a one-dimensional array of numbers.

# This defines a function named max_subarray_sum
# that takes a single parameter arr, which is a
# list of integers.
def max_subarray_sum(arr):
    # This initializes two variables:
    # current_sum: the sum of the current subarray we're examining.
    # max_sum: the highest sum we’ve found so far.
    # Both are initialized to the first element
    # of the array (arr[0]) to handle arrays
    # that contain only negative numbers correctly.
    max_sum = current_sum = arr[0]
    # This starts a loop over the array,
    # beginning from the second element (i.e., arr[1:])
    # because the first element was already used in initialization.
    for num in arr[1:]:
        # For each number num, this line decides:
        # Either start a new subarray from the current number (num),
        # Or extend the current subarray by
        # adding the current number to current_sum.
        current_sum = max(num, current_sum + num)
        # This updates max_sum to be the maximum
        # between the current max_sum and the current_sum.
        # This ensures that max_sum always holds
        # the largest subarray sum seen so far.
        max_sum = max(max_sum, current_sum)
    # After looping through the array, return the max_sum as the result.
    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
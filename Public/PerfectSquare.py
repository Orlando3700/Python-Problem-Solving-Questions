# Write a Python code to check if a number is a perfect square

# This defines a function named is_perfect_square
# that takes a single argument x.
def is_perfect_square(x):
    # x**0.5: This calculates the square root of x.
    # For example, 16**0.5 is 4.0, and 14**0.5 is about 3.741.
    # int(x**0.5): This converts the square root to an integer
    # by truncating the decimal part. For example:
    # int(4.0) is 4
    # int(3.741) is 3
    return int(x**0.5)**2 == x

print(is_perfect_square(16))  # True
print(is_perfect_square(14))  # False
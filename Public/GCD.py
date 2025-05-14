# Write a Python code to find the GCD of two numbers

# This function calculates the Greatest Common
# Divisor (GCD) of two numbers using the
# Euclidean Algorithm.

# This defines a function named gcd that takes
# two integers, a and b.
def gcd(a, b):
    # This line starts a while loop that continues as long as b is not zero.
    # In Python, while b: is the same as while b != 0:
    while b:
        # It updates a to the value of b, and b
        # to the remainder when a is divided by b (a % b).
        # This step reduces the problem to a
        # smaller one while preserving the GCD.
        # Eventually, b becomes 0, and a will
        # contain the GCD.
        a, b = b, a % b
    return a
print(gcd(48, 18))  # 6
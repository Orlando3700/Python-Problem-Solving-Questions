# How do you handle exceptions in Python?

# Using the try-except block:

# Simple Exception Handling Example
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
    
except ZeroDivisionError:
    print("Can't be divided by zero!")
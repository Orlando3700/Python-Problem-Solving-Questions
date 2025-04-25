# Write a Python code to check if a number is
# even or odd

# First Approach

def is_even(num):
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False

# Second Approach

# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
    
# Third Approach

x = 24
# Check the remainder dividing x by 2 is 0
if x % 2 == 0:
    print("Even")
else:
    print ("Odd")
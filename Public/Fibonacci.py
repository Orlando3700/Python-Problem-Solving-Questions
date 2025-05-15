# Writing Fibonacci Series

# Option 1

fib = [0,1]
# Range starts from 0 by default
for i in range(5):  
    fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))

# Option 2

# This approach uses a while loop to print the first n
# Fibonacci numbers by repeatedly summing the previous
# two numbers. It starts with 0 and 1, and calculates the
# next number in the sequence until n terms are printed.

n = 10
a = 0
b = 1
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()

# Option 3

# This approach iteratively calculates the nth Fibonacci
# number by updating two variables, a and b, without
# recursion, making it more efficient in terms of time and
# space.

def fibonacci(n):
    a = 0
    b = 1

    # Check if n is less than 0
    if n < 0:
        print("Incorrect input")
        
    # Check if n is equal to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(9))

# Option 4

# Using DP (Dynamic Programming)
# This approach uses dynamic programming by storing
# previously computed Fibonacci numbers in a list
# (FibArray). It avoids redundant calculations by checking
# if the result is already available, making it more
# efficient than the naive recursive approach.

FibArray = [0, 1]

def fibonacci2(n):

    # Check is n is less than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is less than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacci2(n - 1) + fibonacci2(n - 2))
        return FibArray[n]

print(fibonacci2(9))

# Option 5

# Using Cache  
# This approach uses Python’s lru_cache decorator from
# the functools module to cache the results of the
# Fibonacci function. It stores the results of expensive
# recursive calls, improving efficiency by avoiding
# redundant calculations, especially for larger values
# of n.

from functools import lru_cache

@lru_cache(None)
def fibonacci3(num: int) -> int:

    # check if num is less than 0 it will return none
    if num < 0:
        print("Incorrect input")
        return

    # check if num between 1, 0 it will return num
    elif num < 2:
        return num

    # return the fibonacci of num - 1 & num - 2
    return fibonacci3(num - 1) + fibonacci3(num - 2)
print(fibonacci3(9))

# Option 6

# Using Backtracking
# This approach uses backtracking with memoization to
# optimize the Fibonacci calculation. It stores previously
# computed values in a dictionary (memo), ensuring that
# each Fibonacci number is computed only once. This
# reduces the time complexity significantly compared to
# the naive recursive method.

def fibonacci4(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci4(n-1) + fibonacci4(n-2)
        return memo[n]

print(fibonacci4(9))

# Option 7

# Using Recursion   
# This approach uses recursion to calculate the Fibonacci
# sequence. The base cases handle inputs of 0 and 1
# (returning 0 and 1). For values greater than 1, it
# recursively calls the function to sum the previous two
# Fibonacci numbers. While this method is straightforward,
# it is inefficient for larger inputs due to redundant
# calculations.

def Fibonacci(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))



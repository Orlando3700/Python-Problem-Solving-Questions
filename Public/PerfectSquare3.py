import math

def is_perfect_square(n):
    # If ceil and floor are equal
    # the number is a perfect
    # square
    if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
        return True
    else:
        return False

x = 49
if is_perfect_square(x):
    print("Yes")
else:
    print("No")
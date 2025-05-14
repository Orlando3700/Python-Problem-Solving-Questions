# Python program to find if x is a
# perfect square.
def is_perfect_square(x):
    # Find floating point value of
    # square root of x.
    if x >= 0:
        sr = int(x ** 0.5)

        # if product of square root
        # is equal, then
        # return T/F
        return (sr * sr == x)
    # else return false if n<0
    return False

x = 49
if is_perfect_square(x):
    print("Yes")
else:
    print("No")
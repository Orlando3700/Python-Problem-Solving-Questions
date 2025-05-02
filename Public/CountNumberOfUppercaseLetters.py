#  Write a Python code to count the number of uppercase letters in a string

def count_uppercase(s):
    return sum(1 for char in s if char.isupper())

print(count_uppercase("Nxtwave"))  # 1
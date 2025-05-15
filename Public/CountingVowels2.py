# Using a Set for Fast Lookup
# A set allows quick membership testing, making it an
# efficient way to count vowels. We iterate through the
# string and check if each character is in the set of vowels.


s = "Python Programming"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(1 for ch in s if ch in vowels)

print("Number of vowels:", c)
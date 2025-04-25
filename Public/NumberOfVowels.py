# Write a Python program to count the number of vowels in a string

# First Approach

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels("Hello World"))

# Second Approach

# We are given a string and our task is to count the number
# of vowels present in it. Vowels in English include ‘a’,
# ‘e’, ‘i’, ‘o’, and ‘u’ (both uppercase and lowercase).
# Using sets, we can efficiently check for vowel presence
# due to their fast membership lookup.

# A set allows quick membership testing, making it an
# efficient way to count vowels. We iterate through the
# string and check if each character is in the set of
# vowels.

s = "Orlando Fernand"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(1 for ch in s if ch in vowels)

print("Number of vowels:", c)

# Third Approach

# Using a Set and Intersection
# Instead of iterating through the string, we use set
# intersection to find common elements between the string
# and the vowel set.

s = "Amanda Fernand"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(s.count(v) for v in set(s) & vowels)

print("Number of vowels:", c)

# Fourth Approach

string=(input("Enter string:"))
# Set vowel count to 0
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1 # Increment vowel count
print("Number of vowels are:")
print(vowels)

#Fifth Approach

# Utilize a Dictionary to Simplify Counting

# Initialize a dictionary to store vowel keys and their counts.
# Iterate through each character and increment the count
# in the dictionary if the character is a vowel.

text = "Explore Python with practical examples."
vowels = 'aeiou'
vowel_count = {vowel: 0 for vowel in vowels}

for char in text.lower():
    if char in vowel_count:
        vowel_count[char] += 1

print(vowel_count)
# Here, vowel_count is a dictionary that maintains a count
# of each vowel encountered in the string. The dictionary
# comprehension sets initial counts to zero. The loop
# increases these counts appropriately when vowels are found.

# Sixth Approach

#Using List Comprehensions and the collections.Counter

# Count Vowels Using Python's Built-In Tools

#Utilize collections.Counter from the Python standard
# library to count characters efficiently.
# Filter the counts using a list comprehension to include
# only vowels.

from collections import Counter

text = "Hello my name is Orlando Fernand."
counter = Counter(text.lower())
vowels = 'aeiou'
vowel_count = {vowel: counter[vowel] for vowel in vowels if vowel in counter}

print(vowel_count)
# Counter automatically tallies the frequency of each
# character in the string. The list comprehension then
# extracts the counts for vowels. This method is very
# efficient for long strings.



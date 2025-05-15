# Counting the Number of Occurrences of a Character in a String

# Option 1

# Using a Loop
# If we want more control over the counting process then we
# can use a loop (for loop) to iterate through each
# character in the string.

word = "python"
character = "p"
count = 0
for letter in word:
    if letter == character:
        count += 1
print(count)

# Option 2

# Using count()
# The built-in count() method in the string class makes it
# easy to count how many times a character appears in a
# string.

s = "Fernand"
cnt = s.count('n')
print(cnt)
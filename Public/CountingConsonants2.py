# Counting Consonants in a given word

# Initialize a variable to store the count of consonants.
# Iterate through each character in the word.
# Check if the character is a consonant (not a vowel).
# If it is a consonant, increment the count.
# Print the final count.

def is_lower_case_alphabet(ch):
    return 'a' <= ch <= 'z'

def is_vowel(ch):
    return ch in {'a', 'e', 'i', 'o', 'u'}

word = "programming"
consonant_count = 0

for i in range(len(word)):
    # Convert to lowercase for case-insensitivity
    ch = word[i].lower()
    if is_lower_case_alphabet(ch) and not is_vowel(ch):
        consonant_count += 1

print("Number of consonants:", consonant_count)
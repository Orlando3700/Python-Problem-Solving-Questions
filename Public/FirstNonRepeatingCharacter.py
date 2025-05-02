# Write a Python code to find the first non-repeating character in a string

def first_non_repeating_char(s):
    # This creates an empty dictionary named char_count to
    # store the count of each character in the string.
    char_count = {}
    # This loop goes through each character char in the string s.
    # char_count.get(char, 0) looks up the current count of
    # char; if it doesn't exist, it defaults to 0.
    # Then, it adds 1 to the count and updates char_count[char].
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    # This loop again goes through the string in the original order.
    # It checks for the first character that has a count of
    # 1 (i.e., appears only once).
    # As soon as it finds such a character, it returns it.
    for char in s:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeating_char("nxtwave"))  # n
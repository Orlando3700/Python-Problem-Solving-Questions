# Using array
# The strings contain only lowercase English letters
# we can use an array of size 26 to track the frequency
# of each character instead of using a hashmap. Each
# character is mapped to an index between 0 and 25 using
# the ord() function.

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):  # check length
    print("No")
else:
    count = [0] * 26  # array to track character frequencies (a-z)

    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1  # increment for s1
        count[ord(s2[i]) - ord('a')] -= 1  # decrement for s2

    if all(x == 0 for x in count):  # check if all frequencies are zero
        print("Yes")
    else:
        print("No")
# Using collections.Counter
# The Counter class from collections module is a simple and
# efficient way to count how many times each character
# appears in a string. It automatically creates a count
# for each character and making it easy to see how many
# of each character are present in the string.

from collections import Counter 

s = "OrlandoFernand"

cnt = Counter(s)
print(cnt['n'])
# Importing Regular Expressions Library
import re
spChar = "!@#$%^&*()"

count = re.sub('[\w]+', '', spChar)
print(len(count))
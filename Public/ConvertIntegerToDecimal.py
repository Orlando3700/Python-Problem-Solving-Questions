# Converting an Integer into Decimals

from decimal import Decimal

# Integer value
num = 42

# Convert to decimal
decimal_num = Decimal(num)

print(decimal_num)         # Output: 42
print(type(decimal_num))   # Output: <class 'decimal.Decimal'>
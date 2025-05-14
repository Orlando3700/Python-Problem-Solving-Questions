# Write a Python code to convert a list of temperatures from Celsius to Fahrenheit

def celsius_to_fahrenheit(temps):
    return [(temp * 9/5) + 32 for temp in temps]
print(celsius_to_fahrenheit([0, 20, 37]))  # [32.0, 68.0, 98.6]


c = 47

# Converting the temperature to Fahrenheit using the formula
f = (c * 1.8) + 32

print(str(c))
print(str(f))


x = float(input("Enter temperature in celsius: "))

y = (x * 1.8) + 32

print(str(x))
print(str(y))
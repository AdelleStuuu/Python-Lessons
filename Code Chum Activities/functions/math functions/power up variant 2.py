import math
# prompt the user to input two values
# base and exponent
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
# use the pow function to raise the base 
# by the expoenent
power = math.pow(base,exponent)
# print the result
print(f"Result: {power:.2f}")
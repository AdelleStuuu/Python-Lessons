import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

absoluteDifference = abs(num1 - num2)
cubed = math.pow(absoluteDifference,3)
result = math.sqrt(cubed)

print(f"Result: {result:.2f}")
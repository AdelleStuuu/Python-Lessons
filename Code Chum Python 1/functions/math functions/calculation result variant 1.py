import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = math.sqrt(math.pow(abs(num1 - num2),3))
print(f"Result: {result:.2f}")
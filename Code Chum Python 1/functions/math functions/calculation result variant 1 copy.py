import math
# prompt the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# take the absolute differents of the two numbers 
# raise the answer to 3 
# square root the result of the cubed power
absoluteDifference = abs(num1 - num2)
cubed = math.pow(absoluteDifference,3)
result = math.sqrt(cubed)
# print the result of the equation
print(f"Result: {result:.2f}")
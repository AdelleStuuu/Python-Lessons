import math
# prompt user to input the value of the sides
side = float(input("Enter side: "))
# break down the equation for readability
sqrtOf5 = math.sqrt(5)
innerEquation = 5*(5+2*sqrtOf5)
sideSquared = math.pow(side,2)
# take the 1/4 of the sqrt of the inner equation and
# multiply it by side squared
area = 1/4*(math.sqrt(innerEquation)*sideSquared)
# print the area of the pentagon 
print(f"Area of Pentagon: {area:.2f}")
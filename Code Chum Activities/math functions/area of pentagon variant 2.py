import math
side = float(input("Enter side: "))

sqrtOf5 = math.sqrt(5)
innerEquation = 5*(5+2*sqrtOf5)
sideSquared = math.pow(side,2)

area = 1/4*(math.sqrt(innerEquation)*sideSquared)
print(f"Area of Pentagon: {area:.2f}")
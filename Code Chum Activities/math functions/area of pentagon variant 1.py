import math
side = float(input("Enter side: "))
area = 1/4*(math.sqrt(5*(5+2*math.sqrt(5)))*math.pow(side,2))
print(f"Area of Pentagon: {area:.2f}")
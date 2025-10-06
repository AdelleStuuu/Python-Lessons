import math
side = float(input("Enter side: "))
print(f"Area of Pentagon: {(1/4*(math.sqrt(5*(5+2*math.sqrt(5)))*math.pow(side,2))):.2f}")
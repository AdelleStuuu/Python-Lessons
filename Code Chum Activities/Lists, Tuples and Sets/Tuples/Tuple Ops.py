num1 = input("Enter first set of numbers separated by spaces: ")
listed = num1.split()
set1 = set()
for i in listed:
    set1.add(int(i))
num2 = input("Enter second set of numbers separated by spaces: ")
listed = num2.split()
set2 = set()
for i in listed:
    set2.add(int(i))
num3 = input("Enter third set of numbers separated by spaces: ")
listed = num3.split()
set3 = set()
for i in listed:
    set3.add(int(i))


union = set1 | set2 | set3 
print(f"Union of all three tuples: {union}")
intersection = set1 & set2 & set3 
print(f"Intersection of all three tuples: {intersection}")
list1 = input("Enter elements of the first set: ")
list2 = input("Enter elements of the second set: ")

set1 = set()
set2 = set()
separated = list1.split(" ")
for i in separated: 
    set1.add(int(i))
separated = list2.split(" ")
for i in separated: 
    set2.add(int(i))

union = set1 | set2
intersection = set1 & set2
print(f"Union: {union}")
print(f"Intersection: {intersection}")
unionSum = 0
intersectionSum = 0

for i in union: 
    unionSum += i

for i in intersection: 
    intersectionSum += i
print(f"Sum of Union: {unionSum}")
print(f"Sum of Intersection: {intersectionSum}")
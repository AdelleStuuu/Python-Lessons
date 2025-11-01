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

print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
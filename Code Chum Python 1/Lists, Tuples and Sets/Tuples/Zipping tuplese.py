set1 = input("Enter first set of numbers separated by spaces: ")
set2 = input("Enter second set of numbers separated by spaces: ")
list1 = set1.split(" ")
list2 = set2.split(" ")
intList1 = []
intList2 = []
for i in list1:
    if i != "":
        intList1.append(int(i))
for i in list2:
    intList2.append(int(i))

zipped = zip(intList1,intList2)
tupled = tuple(zipped)
print(f"Zipped Tuple: {tupled}")
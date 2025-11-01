listOfInt = input("Enter list of integers: ")
firstList = listOfInt.split(" ")
newList = []
for i in firstList:
    if i == " ":
        continue 
    else:
        if int(i) in newList:
            continue
        else:
            newList.append(int(i)) 

print(f"List with consecutive duplicates removed: {newList}")
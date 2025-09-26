string = input("Enter a string: ")
aCount = bCount = 0
for i in string:
    if i.lower() == 'a':
        aCount += 1
    elif i.lower() == 'b':
        bCount += 1
print(f"Number of 'a' occurrences: {aCount}")
print(f"Number of 'b' occurrences: {bCount}")
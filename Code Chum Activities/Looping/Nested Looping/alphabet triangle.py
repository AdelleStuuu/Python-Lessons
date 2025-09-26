asciiValue = 65 
rows = int(input("Enter the number of rows: "))
for i in range(rows + 1):
    
    
    for j in range(i):
        print(chr(asciiValue), end=" ")
        asciiValue += 1
    if i != 0:
        print()
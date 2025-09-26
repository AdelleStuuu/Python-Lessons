number = int(input("Enter a number: "))
for i in range(1,number+1):
    if i == 4:
        continue
    print(i, end=" ")
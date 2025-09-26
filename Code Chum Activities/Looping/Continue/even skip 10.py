number = int(input("Enter a number: "))
for i in range(number+1):
    if i % 2 != 0 or i == 10:
        continue
    print(i, end=" ")
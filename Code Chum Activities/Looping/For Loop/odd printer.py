number = int(input("Enter a positive integer: "))
for i in range(number):
    if (i + 1) % 2 != 0:
        print(i + 1)
    else:
        continue
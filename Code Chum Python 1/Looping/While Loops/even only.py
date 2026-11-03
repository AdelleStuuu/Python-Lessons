number = int(input("Enter a positive integer: "))
iterrable = 1
while iterrable != (number + 1):
    if iterrable % 2 == 0:
        print(iterrable)
    iterrable += 1
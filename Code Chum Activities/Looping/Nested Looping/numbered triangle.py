number = int(input("Enter an integer: "))
for i in range(number+1):
    k = 0
    for j in range(i):
        print(k+1, end= " ")
        k += 1
    if i != 0:
        print()
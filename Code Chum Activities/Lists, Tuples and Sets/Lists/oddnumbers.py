integer = int(input("Enter an integer: "))
List = []
for i in range(integer+1):
    if i % 2 != 0:
        List.append(i)
print(List)
firstCharacter = input("Enter First Character: ")
secondCharacter = input("Enter Second Character: ")
size = int(input("Enter Size: "))
Number = 0
Nember = 0
for i in range(size):
    for k in range(Number):
        print("-",end="")
    Number += 1
    if (i+1) % 2 != 0:
        print(firstCharacter, end="")
    else:    
        print(secondCharacter, end="")
    print()
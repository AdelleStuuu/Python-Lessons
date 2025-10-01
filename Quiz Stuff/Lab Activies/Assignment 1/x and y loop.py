x = 1

while x <= 5:
    y = 1
    while y <= 5:
        if x >= y:
            print(x,end="\t")
        else:
            print(y,end="\t")
        y+=1
    print()
    x += 1
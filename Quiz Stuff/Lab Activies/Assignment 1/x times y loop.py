x = 1

while x <= 5:
    y = 1
    while y <= 5:
        if (x + y) % 2 == 0 :
            print(x+y,end="\t")
        else:
            print(y*x,end="\t")
        y+=1
    print()
    x += 1
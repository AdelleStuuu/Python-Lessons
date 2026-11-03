num = int(input("Enter a number: "))
evenodd = []
for i in range(num):
    if (i + 1) % 2 == 0:
        evenodd.append("even")
    else:
        evenodd.append("odd")

print(evenodd)
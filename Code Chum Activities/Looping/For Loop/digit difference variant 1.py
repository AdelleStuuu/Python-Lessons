number = input("Enter a positive integer: ")
iterrable = diff = 0
numberList = [int(digit) for digit in number]
numberList.reverse()
for i in numberList: 
    if iterrable == 0:
        diff = i
    else:
        diff -= i 
    iterrable += 1
print(f"Result of subtracting digits: {diff}")
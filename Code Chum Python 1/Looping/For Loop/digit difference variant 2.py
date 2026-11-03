number = input("Enter a positive integer: ")
iterrable = diff = j = 0
numberList = list(number)

for i in numberList:
    numberList[j] = int(i)
    j+=1
    
numberList.reverse()

for i in numberList: 
    if iterrable == 0:
        diff = i
    else:
        diff -= i 
    iterrable += 1
print(f"Result of subtracting digits: {diff}")
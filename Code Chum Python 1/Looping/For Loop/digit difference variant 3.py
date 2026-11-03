number = input("Enter a positive integer: ")
iterrable = diff = 0
numberList = []
j = len(number)-1

for i in number:
    numberList += [int(i)]
    
for i in range(len(number)): 
    temp1 = numberList[i]
    temp2 = numberList[j]
    numberList[i] = temp2
    numberList[j] = temp1
    j-=1
    if i >= (len(number)//2):
        break

for i in numberList: 
    if iterrable == 0:
        diff = i
    else:
        diff -= i 
    iterrable += 1
print(f"Result of subtracting digits: {diff}")
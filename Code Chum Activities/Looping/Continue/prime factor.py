import math 
number = int(input("Enter a number: "))
listOfPrime = ""
for i in range(2, number + 1):
    if number % i == 0:
        isPrime = True
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            if i % 3 == 0:
                continue
            listOfPrime += (f" {i}")
print(f"Prime factors of {number} (excluding multiples of 3):{listOfPrime}")
number = int(input("Enter a positive integer: "))

for i in range(number): 
    if i % number != 0:
        print(f"{number} is not a prime number")
        break
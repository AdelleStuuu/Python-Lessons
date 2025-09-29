digits = input("Enter a positive integer: ")
digitCount = 0
while True:
    for i in digits:
        digitCount +=1
    break
print(f"Number of digits: {digitCount}")
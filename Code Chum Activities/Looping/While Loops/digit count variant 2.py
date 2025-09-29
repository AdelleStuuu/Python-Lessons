digits = input("Enter a positive integer: ")
digitCount = i = 0
while i < len(digits):
    digitCount += 1 
    i = digitCount 
print(f"Number of digits: {digitCount}")
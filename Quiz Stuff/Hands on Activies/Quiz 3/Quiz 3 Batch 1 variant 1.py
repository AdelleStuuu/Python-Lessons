number = 1;
add = numberEntered = oddNumber = evenNumber = positiveNumber = negativeNumber = 0 

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    numberEntered  += 1
    add += number
    
    if number % 2 == 0:
        evenNumber += 1
    else:
        oddNumber += 1
    
    if number >= 0:
        positiveNumber += 1
    else: 
        negativeNumber += 1

average = add / numberEntered


print("\nResults:")
print(f"How many numbers were entered: {numberEntered}")
print(f"Sum of all numbers entered: {add}")
print(f"Average of all numbers entered: {average:.2f}")
print(f"How many numbers were positive: {positiveNumber}")
print(f"How many numbers were negative: {negativeNumber}")
print(f"How many numbers are odd: {oddNumber}")
print(f"How many numbers are even: {evenNumber}")
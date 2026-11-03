numberEntered = add = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number > 0 :
        add += number
        numberEntered += 1
    else:
        continue
average = add / numberEntered
print(f"Average: {average:.2f}")
numberEntered = add = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number > 0 :
        add += number
    else:
        continue
print(f"Sum: {add}")
add = 0
while True:
    number = int(input("Enter a number: "))
    if number >= 0:
        add += number
    else:
        break
print(f"Sum of positive numbers: {add}")
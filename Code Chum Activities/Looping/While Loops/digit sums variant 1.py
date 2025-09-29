digits = input("Enter an integer: ")
add = 0
while True:
    for i in digits:
        add += int(i)
    break
print(f"Sum of digits: {add}")
digits = input("Enter an integer: ")
add = i = 0
while i < len(digits):
    add += int(digits[i])
    i+=1
print(f"Sum of digits: {add}")
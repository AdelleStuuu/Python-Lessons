integer = int(input("Enter an integer: "))
number = 1
row = 1
print("\nMultiplication Table")
for i in range(integer):
    number = 1
    for j in range(integer):
        product = number * row
        print(product, end="\t")
        number += 1
    print()
    row += 1
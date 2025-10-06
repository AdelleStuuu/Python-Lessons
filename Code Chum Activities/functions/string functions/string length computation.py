first = input("Enter the first string: ")
second = input("Enter the second string: ")
third = input("Enter the third string: ")
fourth = input("Enter the fourth string: ")
fifth = input("Enter the fifth string: ")

print("Length of the first string:", len(first))
print("Length of the second string:", len(second))
print("Length of the third string:", len(third))
print("Length of the fourth string:", len(fourth))
print("Length of the fifth string:", len(fifth))

intThird = int(len(third))
intFourth = int(len(fourth))

result = len(first+second) / (intThird-intFourth)

print(f"Result: {int(result)}")
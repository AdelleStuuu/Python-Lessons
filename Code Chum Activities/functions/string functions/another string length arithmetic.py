# prompt user to input 3 string values
first = input("Enter the first string: ")
second = input("Enter the second string: ")
third = input("Enter the third string: ")
# print the length of alll 3string values
print(f"Length of the first string: {len(first)}")
print(f"Length of the second string: {len(second)}")
print(f"Length of the third string: {len(third)}")
# turn to integet first and add the first and second string
# before diving the result to the third string
result = int(len(first+second)/len(third))
# print the result
print(f"Result: {result}")
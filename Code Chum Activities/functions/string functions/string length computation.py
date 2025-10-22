# prompt the user to enter strings by a set of 5
first = input("Enter the first string: ")
second = input("Enter the second string: ")
third = input("Enter the third string: ")
fourth = input("Enter the fourth string: ")
fifth = input("Enter the fifth string: ")
# take the length of each string and provide an output
print("Length of the first string:", len(first))
print("Length of the second string:", len(second))
print("Length of the third string:", len(third))
print("Length of the fourth string:", len(fourth))
print("Length of the fifth string:", len(fifth))
# turn the third and fourth string into an integger value
intThird = int(len(third))
intFourth = int(len(fourth))
# add the first and second string length 
# subtract the third and fourth string length
# divide the to answers to each other 
result = len(first+second) / (intThird-intFourth)
# print the integer results
print(f"Result: {int(result)}")
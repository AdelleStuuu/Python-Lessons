string = input("Enter a string: ")
vowels = []
for i in string:
    if i.lower() in "aeoiu":
        vowels.append(i)

print(vowels)
vowels = ['a','e','i','o','u']

phrase = input('Enter a phrase: ')
aLetter = 0
eLetter = 0
iLetter = 0
oLetter = 0
uLetter = 0

for i in phrase:
    iConverted = i.lower()
    if iConverted in vowels:
        if iConverted == 'a':
            aLetter += 1
        elif iConverted == 'e':
            eLetter += 1
        elif iConverted == 'i':
            iLetter += 1
        elif iConverted == 'o':
            oLetter += 1
        elif iConverted == 'u':
            uLetter += 1

print(f"A =  {aLetter}")
print(f"E =  {eLetter}")
print(f"I =  {iLetter}")
print(f"O =  {oLetter}")
print(f"U =  {uLetter}")
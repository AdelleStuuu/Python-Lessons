isLower =['a','b','c','d','e','f','q','w','e','r','t','y','u','i','o','p','s','g','h','j','k','l','z','x','v','n','m']
isNumber = ['1','2','3','4','5','6','7','8','9','0']
isVowel = ['a','e','i','o','u']
consonants = 0
vowel = 0
number = 0
lower = 0
upper = 0
isUpper = []
special = 0
space = 0

phrase = input('Enter a phrase: ')
splitPhrase = phrase

for i in isLower:
    isUpper.append(i.upper())

for i in phrase:
    if i in isLower:
        lower += 1
    elif i in isNumber:
        number += 1
    elif i in isUpper:
        upper += 1
    elif i == " ":
        space += 1
    else:
        special += 1
        
    if i.lower() in isVowel and (i in isLower or i in isUpper):
        vowel += 1
    
    if i.lower() not in isVowel and (i in isLower or i in isUpper):
        consonants += 1 

print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")
print(f"Vowels: {vowel}")
print(f"Consonants: {consonants}")
print(f"Special characters: {special}")
print(f"Spaces: {space}")
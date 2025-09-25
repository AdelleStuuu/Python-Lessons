isVowel = ['a','e','i','o','u']
consonants = vowel = number = lower = upper = special = space = 0

phrase = input('Enter a phrase: ')

for i in phrase:
    if i.islower():
        lower += 1
    elif i.isdigit():
        number += 1
    elif i.isupper():
        upper += 1
    elif i == " ":
        space += 1
    else:
        special += 1
        
    if i.lower() in isVowel and i.isalpha():
        vowel += 1
    
    if i.lower() not in isVowel and i.isalpha():
        consonants += 1 

print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")
print(f"Vowels: {vowel}")
print(f"Consonants: {consonants}")
print(f"Special characters: {special}")
print(f"Spaces: {space}")
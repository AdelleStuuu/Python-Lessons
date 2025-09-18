vowels = {
    'A' : 0,
    'E' : 0,
    'I' : 0,
    'O' : 0,
    'U' : 0,
}

phrase = input('Enter a phrase: ')
convertedPhrase = phrase.upper()

for i in convertedPhrase:
    if i in vowels: 
        vowels[i] += 1
    elif i not in vowels:
        continue 
    
for letter,amount in vowels.items():
    print(f"{letter} =  {amount}")



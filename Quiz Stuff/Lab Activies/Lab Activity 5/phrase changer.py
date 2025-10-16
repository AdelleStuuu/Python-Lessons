vowel = "aeiou"

phrase = input("Enter a sentence or phrase: ")
print(f"Original string: {phrase}")

for i in phrase: 
    if i == " ":
        phrase = phrase.replace(" ", "x")
        
    if i.lower() in vowel:
        phrase = phrase.replace(i,i.upper())
    else:
        phrase = phrase.replace(i,i.lower())
         
print(f"Processed string: {phrase}")
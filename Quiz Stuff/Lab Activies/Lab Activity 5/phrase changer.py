# initialize the vowels
vowel = "aeiou"

# provide an input for the phrase
phrase = input("Enter a sentence or phrase: ")
# print the original string first 
print(f"Original string: {phrase}")

# for loop to loop through the phrase
for i in phrase: 
    # check if spaces are present
    # replace the spaces with the letter x
    if i == " ":
        phrase = phrase.replace(" ", "x") 
    # lower the letter first before checking if its in the vowel
    # use membership in instead of doing another for loop   
    if i.lower() in vowel:
        #make them uppercase if its a vowel
        phrase = phrase.replace(i,i.upper())
    else:
        #make them lowercase if its a consonant
        phrase = phrase.replace(i,i.lower())
# print the entire string 
print(f"Processed string: {phrase}")
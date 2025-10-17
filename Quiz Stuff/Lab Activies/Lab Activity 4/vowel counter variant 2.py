# initialize them using a dictionary for ease of use
vowels = {
    'A' : 0,
    'E' : 0,
    'I' : 0,
    'O' : 0,
    'U' : 0,
}

# prompt user to enter a phrase
phrase = input('Enter a phrase: ')
# turn the entire phrase intp upper case
convertedPhrase = phrase.upper()

# start a for loop that checks through the entire upper case phrase
for i in convertedPhrase:
    # if the letter is inside the key of vowels
    # increment key's value by 1
    if i in vowels: 
        vowels[i] += 1
    # ignore if not since an else is required in code chum
    elif i not in vowels:
        continue 
# use a for loop print out the keys and the values of the dictionary 
for letter,amount in vowels.items():
    print(f"{letter} =  {amount}")
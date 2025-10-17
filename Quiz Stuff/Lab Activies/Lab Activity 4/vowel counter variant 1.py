# initialize vowels within a list
vowels = ['a','e','i','o','u']

# prompt user to enter a phrase
phrase = input('Enter a phrase: ')
# start a counter with all of them at zero
aLetter = 0
eLetter = 0
iLetter = 0
oLetter = 0
uLetter = 0

# start a loop that goes through the string phrase
for i in phrase:
    # convert i to lower case first 
    # not necessary as shown in lab act 5
    iConverted = i.lower()
    # conditional checking if theres a vowel
    # check what specific vowel before adding corresponding 
    # vowel by 1
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

# print all total vowels that were seen 
print(f"A =  {aLetter}")
print(f"E =  {eLetter}")
print(f"I =  {iLetter}")
print(f"O =  {oLetter}")
print(f"U =  {uLetter}")
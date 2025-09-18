vowels = ['a','e','i','o','u']

phrase = input('Enter a phrase: ')
a = 0
e = 0
iL = 0
o = 0
u = 0

for i in phrase:
    iCon = i.lower()
    if iCon in vowels:
        if iCon == 'a':
            a += 1
        elif iCon == 'e':
            e += 1
        elif iCon == 'i':
            iL += 1
        elif iCon == 'o':
            o += 1
        elif iCon == 'u':
            u += 1

print(f"A =  {a}")
print(f"E =  {e}")
print(f"I =  {iL}")
print(f"O =  {o}")
print(f"U =  {u}")
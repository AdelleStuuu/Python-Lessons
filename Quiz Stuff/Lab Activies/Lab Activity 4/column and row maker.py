character = input('Enter a character: ')
rows = int(input('Enter number of rows: '))
column = int(input('Enter number of columns: '))

for i in range(rows):
    for j in range(column):
        print(character, end="\t")
    print()
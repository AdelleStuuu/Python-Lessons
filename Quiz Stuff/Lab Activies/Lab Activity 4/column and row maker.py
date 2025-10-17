# prompt the user to input the needed character
# the amount od rows, and the column count
character = input('Enter a character: ')
rows = int(input('Enter number of rows: '))
column = int(input('Enter number of columns: '))

# start a for loop that goes per amount of rows
for i in range(rows):
    # start another one per column
    for j in range(column):
        # print the character by column and tab it
        print(character, end="\t")
    # finish the row by closing it with an empty print
    print()
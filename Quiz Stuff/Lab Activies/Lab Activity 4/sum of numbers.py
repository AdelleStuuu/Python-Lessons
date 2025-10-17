# initialize values num and add with 
# values none and zero in that order
num = None
add = 0
# start a while loop that checks if 
# the num variable is not 0
while num != 0:
    # prompt user to add a number and add it to the add variable
    num = int(input('Enter a number (0 to stop): '))
    add += num
# prin out the sum of the numbers
print(f'The sum of all numbers is: {add}')

# promp the user to enter necessary information 
# for the rental information
age = float(input('Enter driver\'s age: '))
carDailyRate = float(input('Enter the car\'s daily rate: '))
rentalDays  = float(input('Enter rental days: '))
# initialize variables for the fee, discount and price
discount = .80
fee = 1000
# multiply the rate and rental days to get the initial price
price = carDailyRate * rentalDays
# check if the user is in the appropriate age to rent
if age < 21: 
    # tell the user theyre not allowed to rent 
    # if they dont reach the required age 
    print('Only drivers aged 21 years old or above can rent.')
else: 
    # if the user is legal, check if theyre of senior age to apply discount
    if age >= 60:
        price *= discount
    # add a fee if the rental days exceed or reach 30
    if rentalDays >= 30: 
        price += fee
    # give the user the total cost
    print(f'Your total cost is ${price:.2f}.')
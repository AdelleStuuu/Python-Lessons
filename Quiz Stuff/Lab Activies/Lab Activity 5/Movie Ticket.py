print("==============================")
print("   MOVIE TICKETING SYSTEM")
print("==============================")
print("Movies: \n  [W] Wall-E       - P150   \n  [X] X-Men        - P200\n  [Y] Yogi Bear    - P250\n  [Z] Zombieland   - P300")
print("------------------------------")
print("Discounts:\n  [R] Regular      - 0%\n  [V] VIP          - 10%\n  [S] Senior       - 20%")
print("==============================")

#initialize the code and use inputs
movie_code = input("Enter Movie Code (W, X, Y, Z): ")
discount_code = input("Enter Discount Code (R, V, S): ")
quantity = float(input("Enter how many tickets: "))

# Match case converting the code to its price equivalent
match movie_code:
    case "W":
        price = 150
    case "X": 
        price = 200
    case "Y":
        price = 250
    case "Z":
        price = 300

# Match case converting the code to its discount amount equivalent        
match discount_code:
    case "R":
        discount = 1
    case "V":
        discount = .9
    case "S":
        discount = .8

# multiply the price and and discount before multiplying quantity
def compute(movie_code,discount_code,quantity):
    return (movie_code * discount_code) * quantity
# print the result
print(f"The total is P{compute(price,discount,quantity):.2f}")
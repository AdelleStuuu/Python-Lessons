print("=== Coffee Shop Ordering System ===")
CoffeeCode = input("Enter Coffee Code (E, L, C, M): ")
CustomerCode = input("Enter Customer Type Code (R, M, S): ")
AddonCode = input("Enter Add-on Code (X, W, N): ")
Quantity = input("Enter Quantity: ")

print()


match CoffeeCode:
    case "E":
        CoffeeCodePrice = 100
    case "L":
        CoffeeCodePrice = 120
    case "C":
        CoffeeCodePrice = 150
    case "M":
        CoffeeCodePrice = 180

match CustomerCode:
    case "R":
        CustomerCodePrice = 1
    case "M":
        CustomerCodePrice = .9
    case "S":
        CustomerCodePrice = .8

match AddonCode:
    case "X":
        AddonCodePrice = 30
    case "W":
        AddonCodePrice = 20
    case "N":
        AddonCodePrice = 0

def compute_total(coffee_code, customer_code, addon_code, quantity):
    return ((float(coffee_code + addon_code) * customer_code) ) * float(quantity)

print(f"Total Bill: {compute_total(CoffeeCodePrice,CustomerCodePrice,AddonCodePrice,Quantity):.2f}")
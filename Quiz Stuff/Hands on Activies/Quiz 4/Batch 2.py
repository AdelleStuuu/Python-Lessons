print("FAST FOOD ORDERING SYSTEM")
print("--------------------------")

mealCode = input("Enter Meal Code [B/C/S/F]: ")
customerType = input("Enter Customer Type [R/T/S]: ")
sideItem = input("Enter Side Item [D/U/N]: ")
quantity = float(input("Enter Quantity: "))

meal = {
    "B": 85,
    "C": 100,
    "S": 95,
    "F": 60
}

cus = {
    "R": 1.0,
    "T": .85,
    "S": .8
} 

side = {
    "D": 25,
    "U": 30,
    "N": 0
}

def compute_bill(meal_code, customer_code, side_code, quantity):
    return ((meal_code + side_code) * customer_code) * quantity

print(f"Total Bill: P{compute_bill(meal[mealCode],cus[customerType],side[sideItem],quantity):.2f}")

class item:
    def __init__(self, itemId, name, rarity):
        self._itemId = itemId
        self._name = name
        self._rarity = rarity

    def getDetails(self):
        print(f"Item: {self._name}")
        print(f"Rarity: {self._rarity}")

class weapon(item):
    def __init__(self, itemId, name, rarity, damage):
        super().__init__(itemId, name, rarity)
        self._damage = damage

    def getDetails(self):
        super().getDetails()
        print(f"Damage: {self._damage}")


class armor(item):
    def __init__(self, itemId, name, rarity, defense):
        super().__init__(itemId, name, rarity)
        self._defense = defense

    def getDetails(self):
        super().getDetails()
        print(f"Defense: {self._defense}")


class potion(item):
    def __init__(self, itemId, name, rarity, effect):
        super().__init__(itemId, name, rarity)
        self.__effect = effect

    def use(self):
        print(f"You used {self._name}!")
        print(f"Effect: {self.__effect}")

    def getDetails(self):
        super().getDetails()
        print(f"Effect: {self.__effect}")

class inventorySlot:
    def __init__(self, item, quantity):
        self._item = item
        self._quantity = quantity


class inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self._slots = []

    def addItem(self, item, quantity=1):
        for slot in self._slots:
            if slot._item._itemId == item._itemId:
                slot._quantity += quantity
                print("Item quantity updated!")
                return

        if len(self._slots) < self.__capacity:
            self._slots.append(inventorySlot(item, quantity))
            print(f"{item._name} added to inventory!")
        else:
            print("Inventory is full!")

    def removeItem(self, itemId):
        for slot in self._slots:
            if slot._item._itemId == itemId:
                self._slots.remove(slot)
                print("Item removed!")
                return

        print("Item not found!")

    def viewInventory(self):
        if not self._slots:
            print("\nYour inventory is empty!")
            return

        print("\n===== INVENTORY =====")
        for slot in self._slots:
            print(f"ID: {slot._item._itemId} | "
                  f"{slot._item._name} | "
                  f"Quantity: {slot._quantity}")

    def getSlots(self):
        return self._slots

class player:
    def __init__(self, playerId, username, inventory):
        self.__playerId = playerId
        self.__username = username
        self.__inventory = inventory

    def getInventory(self):
        return self.__inventory

    def viewInventory(self):
        print(f"\nPlayer: {self.__username}")
        self.__inventory.viewInventory()

    def equipItem(self, itemId):
        for slot in self.__inventory.getSlots():
            if slot._item._itemId == itemId:
                if isinstance(slot._item, weapon):
                    print(f"{slot._item._name} equipped as weapon!")
                    return
                elif isinstance(slot._item, armor):
                    print(f"{slot._item._name} equipped as armor!")
                    return

        print("Weapon or armor not found!")

    def usePotion(self, itemId):
        for slot in self.__inventory.getSlots():
            if slot._item._itemId == itemId:
                if isinstance(slot._item, potion):
                    slot._item.use()
                    slot._quantity -= 1

                    if slot._quantity == 0:
                        self.__inventory.removeItem(itemId)
                    return

        print("Potion not found!")


def testRelationships(gamePlayer, playerInventory):

    print("\n===== OOP RELATIONSHIP TESTS =====")

    print("\n[TEST 1: INHERITANCE !!!]")

    if (issubclass(weapon, item) and
        issubclass(armor, item) and
        issubclass(potion, item)):
        print("PASS: Weapon, Armor, and Potion inherit from Item.")
    else:
        print("FAIL: Inheritance relationship not implemented properly.")

    print("\n[TEST 2: COMPOSITION !!!]")

    if all(isinstance(slot, inventorySlot)
           for slot in playerInventory.getSlots()):
        print("PASS: Inventory contains InventorySlot objects.")
    else:
        print("FAIL: Composition relationship not implemented properly.")

    print("\n[TEST 3: ASSOCIATION !!!]")

    if gamePlayer.getInventory() is playerInventory:
        print("PASS: Player is associated with its Inventory.")
    else:
        print("FAIL: Association relationship not implemented properly.")

    print("\n===== TESTING COMPLETED =====")


sword = weapon(101, "Iron Sword", "Common", 25)
shield = armor(202, "Steel Armor", "Rare", 40)
healthPotion = potion(301, "Health Potion", "Common", "Restore HP")

playerInventory = inventory(5)
gamePlayer = player(1, "Adelle", playerInventory)

playerInventory.addItem(sword)
playerInventory.addItem(shield)
playerInventory.addItem(healthPotion, 3)


while True:
    print("\n===== GAME INVENTORY SYSTEM =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Equip Weapon/Armor")
    print("5. Use Potion")
    print("6. Test OOP Relationships")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        gamePlayer.viewInventory()

    elif choice == "2":
        print("\n1. Weapon")
        print("2. Armor")
        print("3. Potion")

        itemType = input("Choose item type: ")
        itemId = int(input("Enter item ID: "))
        name = input("Enter item name: ")
        rarity = input("Enter rarity: ")

        if itemType == "1":
            damage = int(input("Enter damage: "))
            newItem = weapon(itemId, name, rarity, damage)

        elif itemType == "2":
            defense = int(input("Enter defense: "))
            newItem = armor(itemId, name, rarity, defense)

        elif itemType == "3":
            effect = input("Enter potion effect: ")
            newItem = potion(itemId, name, rarity, effect)

        else:
            print("Invalid item type!")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            playerInventory.addItem(newItem, quantity)
        else:
            print("Quantity must be greater than zero!")

    elif choice == "3":
        itemId = int(input("Enter item ID to remove: "))
        playerInventory.removeItem(itemId)

    elif choice == "4":
        itemId = int(input("Enter item ID to equip: "))
        gamePlayer.equipItem(itemId)

    elif choice == "5":
        itemId = int(input("Enter potion ID to use: "))
        gamePlayer.usePotion(itemId)

    elif choice == "6":
        testRelationships(gamePlayer, playerInventory)

    elif choice == "7":
        print("Exiting Game Inventory System...")
        break

    else:
        print("Invalid choice! Please try again.")

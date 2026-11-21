
class Fighter:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def performAction(self):
        print(f"{self.name} swings a sword and deals physical damage!")


class Wizard:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def performAction(self):
        print(f"{self.name} casts a powerful fireball spell!")


class Ranger:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def performAction(self):
        print(f"{self.name} shoots an arrow at the enemy!")


class Artificer:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def performAction(self):
        print(f"{self.name} uses a magical invention to attack!")


class Cleric:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def performAction(self):
        print(f"{self.name} casts a healing spell on the party!")


def characterTurn(character, turnNumber):
    print(f"\n{turnNumber}. {character.name} (Initiative: {character.speed})")
    character.performAction()


def addCharacter(characters):
    print("\n=== SELECT CHARACTER TYPE ===")
    print("1 - Fighter")
    print("2 - Wizard")
    print("3 - Ranger")
    print("4 - Artificer")
    print("5 - Cleric")

    choice = input("\nEnter your choice (1-5): ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid character selection!")
        return

    name = input("Enter character name: ")

    while True:
        try:
            speed = int(input("Enter initiative/speed: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if choice == "1":
        character = Fighter(name, speed)
    elif choice == "2":
        character = Wizard(name, speed)
    elif choice == "3":
        character = Ranger(name, speed)
    elif choice == "4":
        character = Artificer(name, speed)
    else:
        character = Cleric(name, speed)

    characters.append(character)
    print(f"\n{name} has joined the party!")


def startCombat(characters):
    if not characters:
        print("\nThere are no characters in combat!")
        return

    sortedCharacters = sorted(
        characters,
        key=lambda character: character.speed,
        reverse=True
    )

    print("\n========== COMBAT ROUND ==========")
    print("INITIATIVE ORDER:")

    for index, character in enumerate(sortedCharacters, start=1):
        print(f"{index}. {character.name} - {character.speed}")

    print("\n========== EVERYONE'S TURN ==========")

    for index, character in enumerate(sortedCharacters, start=1):
        characterTurn(character, index)

    print("\n========== END OF ROUND ==========")


characters = []
roundNumber = 1

while True:
    print("\n====== D&D COMBAT SYSTEM ======")
    print("1 - Add Character")
    print("2 - Start Next Combat Round")
    print("3 - View Initiative Order")
    print("4 - Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        addCharacter(characters)

    elif choice == "2":
        if characters:
            print(f"\n========== ROUND {roundNumber} ==========")
            startCombat(characters)
            roundNumber += 1
        else:
            print("\nAdd characters before starting combat!")

    elif choice == "3":
        sortedCharacters = sorted(
            characters,
            key=lambda character: character.speed,
            reverse=True
        )

        print("\n========== INITIATIVE ORDER ==========")

        if not sortedCharacters:
            print("No characters have been added.")
        else:
            for index, character in enumerate(sortedCharacters, start=1):
                print(f"{index}. {character.name} - {character.speed}")

    elif choice == "4":
        print("\nLeaving combat system...")
        break

    else:
        print("\nInvalid choice. Please try again.")

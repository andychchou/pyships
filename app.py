destroyer = {
    "hp": 100,
    "damage": 20,
    "rof": 80,
    "accuracy": 30,
    "range": 30,
    "speed": 100,
    "evasion": 80
}

cruiser = {
    "hp": 200,
    "damage": 30,
    "rof": 50,
    "accuracy": 30,
    "range": 50,
    "speed": 80,
    "evasion": 60
}

battleship = {
    "hp": 400,
    "damage": 60,
    "rof": 20,
    "accuracy": 30,
    "range": 70,
    "speed": 50,
    "evasion": 30
}

carrier = {
    "hp": 100,
    "damage": 40,
    "rof": 10,
    "accuracy": 80,
    "range": 100,
    "speed": 80,
    "evasion": 60
}

# game setup
selection = input("Select")
p1_ship = {}
p2_ship = {}

while True:
    if selection == "1":
        p1_ship = destroyer.copy()
    elif selection == "2":
        p1_ship = cruiser.copy()
    elif selection == "3":
        p1_ship = battleship.copy()
    elif selection == "4":
        p1_ship = cruiser.copy()

    print("Unknown ship")

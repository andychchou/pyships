class Warship:
    def __init__(self, hp, damage, rof, accuracy, range, speed, evasion):
        self.hp = hp
        self.damage = damage
        self.rof = rof
        self.accuracy = accuracy
        self.range = range
        self.speed = speed
        self.evasion = evasion

    def move_forward(self):
        print("Moved forward")


class Destroyer(Warship):
    def __init__(self):
        hp = 100
        damage = 20
        rof = 80
        accuracy = 30
        range = 30
        speed = 100
        evasion = 80
        super().__init__(hp, damage, rof, accuracy, range, speed, evasion)


class Cruiser(Warship):
    def __init__(self):
        hp = 200
        damage = 30
        rof = 50
        accuracy = 30
        range = 50
        speed = 80
        evasion = 60
        super().__init__(hp, damage, rof, accuracy, range, speed, evasion)


class Battleship(Warship):
    def __init__(self):
        hp = 400
        damage = 60
        rof = 20
        accuracy = 30
        range = 70
        speed = 50
        evasion = 30
        super().__init__(hp, damage, rof, accuracy, range, speed, evasion)


class Carrier(Warship):
    def __init__(self):
        hp = 100
        damage = 40
        rof = 10
        accuracy = 80
        range = 100
        speed = 80
        evasion = 60
        super().__init__(hp, damage, rof, accuracy, range, speed, evasion)


ship1 = Destroyer()
print(ship1.hp)
ship1.move_forward()

# game setup
# selection = input("Select")
# p1_ship = {}
# p2_ship = {}

# while True:
#     if selection == "1":
#         p1_ship = destroyer.copy()
#     elif selection == "2":
#         p1_ship = cruiser.copy()
#     elif selection == "3":
#         p1_ship = battleship.copy()
#     elif selection == "4":
#         p1_ship = cruiser.copy()

#     print("Unknown ship")

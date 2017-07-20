import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level

class Wizard(Creature):
    pass

class SmallAnimal(Creature):
    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level / 2

class Dragon(Creature):
    pass
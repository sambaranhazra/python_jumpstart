import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        print("The wizard {} attacks {}".format(self.name, creature.name))
        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()
        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))
        if my_roll >= creature_roll:
            return True
        else:
            print("The Wizard has been defeated!!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness, breathe_fire=False):
        super().__init__(name, level)
        self.breathe_fire = breathe_fire
        self.scale_thickness = scale_thickness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathe_fire else 1
        scale_modifier = self.scale_thickness / 10
        return base_roll * fire_modifier * scale_modifier

    # def breathe_fire(self):

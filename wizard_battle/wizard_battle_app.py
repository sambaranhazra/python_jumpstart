import random

import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print("-------------------")
    print("  WIZARD GAME APP")
    print("-------------------")
    print()


def game_loop():
    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, scale_thickness=20),
        Wizard("Evil wizard", 1000),
    ]
    print(creatures)
    hero = Wizard("Gandalf", 75)
    while True:
        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared from a dark and foggy forest.".format(active_creature.name,
                                                                                   active_creature.level))
        cmd = input("Do you [a]ttack, [r]un away, or [l]ook around?")
        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Wizard runs and hides taking time to recover!!!")
                time.sleep(5)
                print("Wizard returns revitalized!!!")
        elif cmd == "r":
            print("{} ran away to take shelter.".format(hero.name))
        elif cmd == "l":
            print("{} looking around for creatures".format(hero.name))
            for creature in creatures:
                print("* {} of level {} near.".format(creature.name, creature.level))
        else:
            print("OK, exiting game.")
            break


if __name__ == '__main__':
    main()

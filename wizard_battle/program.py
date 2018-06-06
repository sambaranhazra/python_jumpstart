import random

import time

from actors import Wizard, Creature


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
        Creature("Toad", 1),
        Creature("Tiger", 12),
        Creature("Bat", 3),
        Creature("Dragon", 50),
        Creature("Evil wizard", 1000),
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
            print("Run away")
        elif cmd == "l":
            print("Look around")
        else:
            print("OK, exiting game.")
            break


if __name__ == '__main__':
    main()

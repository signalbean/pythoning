from character import Hero, Enemy
from weapon import iron_sword, short_bow, war_hammer
import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    hero = Hero("Hero", 100)
    enemy = Enemy("Enemy", 100)

    hero.equip(iron_sword)

    print("---- Choose weapon for hero ----")
    print("1. Fists\n2. Iron Sword\n3. Short Bow\n4. War Hammer")

    try:
        choice = int(input("> "))

        if choice == 1:
            hero.drop()
        elif choice == 2:
            hero.equip(iron_sword)
        elif choice == 3:
            hero.equip(short_bow)
        elif choice == 4:
            hero.equip(war_hammer)
        else:
            print("Invalid choice, using default.")
    except ValueError:
        print("Not a valid number.")
        sys.exit(1)

    while True:
        clear_screen()

        hero.attack(enemy)
        if enemy.has_fallen():
            break

        enemy.attack(hero)
        if hero.has_fallen():
            break

        hero.healthbar.draw()
        enemy.healthbar.draw()

        print("\nPress Enter to fight or Ctrl+C to exit.")
        try:
            input()
        except KeyboardInterrupt:
            print("\nExiting.")
            sys.exit(0)

if __name__ == "__main__":
    main()

from character import Hero, Enemy
from weapon import WEAPONS
import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def choose_weapon():
    print("---- Choose weapon for hero ----")
    for idx, weapon in enumerate(WEAPONS, start=1):
        print(f"{idx}. {getattr(weapon, 'name', str(weapon))}")

    try:
        choice = int(input("> "))
        return WEAPONS[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice, using default.")
        return WEAPONS[0]

def main():
    hero = Hero("Hero", 100)
    enemy = Enemy("Enemy", 100)

    hero.equip(choose_weapon())

    while True:
        clear_screen()

        hero.attack(enemy)
        enemy.attack(hero)

        hero.healthbar.draw()
        enemy.healthbar.draw()

        if enemy.has_fallen() or hero.has_fallen():
            import time
            time.sleep(2)
            break

        print("\nPress Enter to fight or Ctrl+C to exit.")
        try:
            input()
        except KeyboardInterrupt:
            print("\nExiting.")
            sys.exit(0)

if __name__ == "__main__":
    main()

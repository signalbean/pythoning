from character import Hero, Enemy
from weapon import iron_sword
import os
import sys

hero = Hero("Hero", 100)
hero.equip(iron_sword)
# uncomment the below line to make the hero use fists
# hero.drop()

enemy = Enemy("Enemy", 100)

while True:
    os.system("clear") # or 'cls' instead of 'clear' on Windows

    hero.attack(enemy) # attack loop starts with hero

    enemy.attack(hero) # enemy immediately counter-attacks

    # redraw updated healthbars after each exchange
    hero.healthbar.draw()
    enemy.healthbar.draw()

    print("\nPress Enter key to fight or Ctrl+C to exit.")

    try:
        input()
    except KeyboardInterrupt:
        print("\nSIGINT received. Exiting.")
        sys.exit(0)

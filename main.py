from character import Hero, Enemy
from weapon import iron_sword
import os
import sys

hero = Hero("Hero", 100)
hero.equip(iron_sword)
enemy = Enemy("Enemy", 100)

while True:
    os.system("clear")
        
    hero.attack(enemy)
    enemy.attack(hero)
        
    hero.healthbar.draw()
    enemy.healthbar.draw()
        
    print("\nPress Enter to fight or Ctrl+C to exit.")
        
    try:
        input()
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit(0)

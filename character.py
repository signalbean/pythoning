from weapon import fists
from healthbar import HealthBar

class Character:
    def __init__(self, name: str, hp: int, weapon=fists) -> None:
        # basic shared fields for all character types
        self.name = name
        self.hp = hp
        self.max_hp = hp
        # starting weapon, default is fists
        self.weapon = weapon

    def attack(self, target) -> None:
        # simple damage application with floor at zero
        target.hp = max(target.hp - self.weapon.dmg, 0)

class Hero(Character):
    def __init__(self, name: str, hp: int, weapon=fists) -> None:
        super().__init__(name, hp, weapon)
        # store original weapon so drop() can revert to it
        self.default_weapon = weapon
        # hero healthbar uses green
        self.healthbar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:

        self.weapon = weapon # change current weapon

    def drop(self) -> None:

        self.weapon = self.default_weapon # go back to default weapon

class Enemy(Character):
    def __init__(self, name: str, hp: int, weapon=fists) -> None:
        super().__init__(name, hp, weapon)
        # enemy healthbar marked in red
        self.healthbar = HealthBar(self, color="red")

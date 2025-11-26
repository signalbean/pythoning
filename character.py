from weapon import fists, Weapon
from healthbar import HealthBar

class Character:
    def __init__(self, name: str, hp: int) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = fists

    def attack(self, target: "Character") -> None:
        target.hp = max(target.hp - self.weapon.dmg, 0)

class Hero(Character):
    def __init__(self, name: str, hp: int) -> None:
        super().__init__(name, hp)
        self.healthbar = HealthBar(self, color="green")

    def equip(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def drop(self) -> None:
        self.weapon = fists

class Enemy(Character):
    def __init__(self, name: str, hp: int) -> None:
        super().__init__(name, hp)
        self.healthbar = HealthBar(self, color="red")

from weapon import fists, Weapon
from healthbar import HealthBar

class Character:
    def __init__(self, name: str, hp: int) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = fists

    def has_fallen(self) -> bool:
        return self.hp <= 0

    def rip(self) -> None:
        print(f"{self.__class__.__name__} has fallen!")

    def attack(self, target: "Character") -> bool:
        target.hp = max(target.hp - self.weapon.dmg, 0)
        if target.has_fallen():
            target.rip()
            return True
        return False

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

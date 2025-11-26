class Weapon:
    def __init__(self, name: str, dmg: int) -> None:
        self.name = name
        self.dmg = dmg

fists = Weapon("Fists", 2)
iron_sword = Weapon("Iron Sword", 5)
short_bow = Weapon("Short Bow", 4)
war_hammer = Weapon("War Hammer", 7)

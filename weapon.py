class Weapon:
    def __init__(self, name: str, wtype: str, dmg: int, val: int) -> None:
        # weapon data container
        self.name = name
        self.wtype = wtype
        self.dmg = dmg
        self.val = val

# default option
fists = Weapon("Fists", "blunt", 2, 0)

# melee weapon
iron_sword = Weapon("Iron Sword", "sharp", 5, 10)

# ranged weapon with moderate damage
short_bow = Weapon("Short Bow", "ranged", 4, 8)

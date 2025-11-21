class HealthBar:
    remaining = "#"
    lost = "_"
    barrier = "|"

    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[34m",
        "purple": "\033[95m",
        "brown": "\033[33m",
        "yellow": "\033[93m",
        "grey": "\033[37m",
        "default": "\033[0m"
    }

    def __init__(self, entity, length=20, colored=True, color="") -> None:
        self.entity = entity
        self.length = length
        self.colored = colored
        self.color = self.colors.get(color, self.colors["default"])

    def draw(self) -> None:
        max_val = self.entity.max_hp
        cur_val = self.entity.hp

        remaining_bars = round(cur_val / max_val * self.length)
        lost_bars = self.length - remaining_bars

        print(f"{self.entity.name}'s HEALTH: {cur_val}/{max_val}")

        color = self.color if self.colored else ""
        reset = self.colors["default"] if self.colored else ""

        print(f"{self.barrier}{color}"
              f"{self.remaining * remaining_bars}"
              f"{self.lost * lost_bars}"
              f"{reset}{self.barrier}")

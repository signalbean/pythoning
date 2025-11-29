class HealthBar:
    remaining = "="
    lost = "_"
    barrier = "|"

    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[34m",
        "purple": "\033[95m",
        "brown": "\033[33m",
        "yellow": "\033[93m",
        "default": "\033[0m"
    }

    def __init__(self, entity, length: int = 20, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.color = self.colors.get(color, self.colors["default"])

    def draw(self) -> None:
        remaining_bars = round(self.entity.hp / self.entity.max_hp * self.length)
        lost_bars = self.length - remaining_bars

        print(f"{self.entity.name}'s health: {self.entity.hp}/{self.entity.max_hp}")
        print(f"{self.barrier}{self.color}{self.remaining * remaining_bars}"
              f"{self.lost * lost_bars}{self.colors['default']}{self.barrier}")

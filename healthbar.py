class HealthBar:
    # characters used to show health segments
    remaining = "#"
    lost = "_"
    barrier = "|"

    # ANSI color codes for colored output
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
        # attach to the entity whose health is displayed
        self.entity = entity

        self.length = length # total visual segments

        self.colored = colored # toggle color output

        # final color code selected from mapping
        self.color = self.colors.get(color, self.colors["default"])

    def draw(self) -> None:
        # get max and current values from the entity
        max_val = self.entity.max_hp
        cur_val = self.entity.hp

        # finding filled and empty portions of the bar
        remaining_bars = round(cur_val / max_val * self.length)
        lost_bars = self.length - remaining_bars

        # show health state first
        print(f"{self.entity.name}'s health: {cur_val}/{max_val}")

        # choose color codes if enabled
        color = self.color if self.colored else ""
        reset = self.colors["default"] if self.colored else ""

        # print the framed bar with coloring and proportions
        print(f"{self.barrier}{color}"
              f"{self.remaining * remaining_bars}"
              f"{self.lost * lost_bars}"
              f"{reset}{self.barrier}")

# Terminal Battle Sim

A tiny Python OOP demo where two characters fight each other in the terminal. Characters,
weapons, and a colored health bar each get their own class. The health bar uses ANSI colors and 
fills with `#` and `_` as HP changes. Weapons define damage, the hero can swap them, and `main.py`
runs a loop that clears the screen, shows both bars, applies attacks, and waits for you to 
hit Enter for the next iteration.

## File Overview

| File           | Purpose                                                  |
| -------------- | -------------------------------------------------------- |
| `main.py`      | Starts the program and runs the battle loop.             |
| `character.py` | Base character logic plus `Hero` and `Enemy` subclasses. |
| `weapon.py`    | Weapon definitions and preset weapons.                   |
| `healthbar.py` | Handles drawing and coloring the health bars.            |

## How to Run It

1. Clone this repo
2. Open a terminal and navigate to that folder.
3. Run:

   ```bash
   python3 main.py
   # or
   python main.py
   ```
4. Hit Enter to step through each round.
5. Use `Ctrl+D` to exit.

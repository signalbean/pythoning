# Terminal Battle Sim

A small Python OOP demo where two characters fight each other in the terminal. Characters, weapons, and a colored health bar each use their own class. The health bar uses ANSI colors and fills with `[]` and `_` as HP moves. Weapons define damage, the hero can change them, and `main.py` runs a loop that clears the screen, shows the bars, applies attacks, and waits for Enter along with weapon switching for the Hero character.

## Files

* `main.py`: runs the battle loop
* `character.py`: character logic plus `Hero` and `Enemy`
* `weapon.py`: weapon classes and presets
* `healthbar.py`: draws colored health bars

## Run

```bash
python main.py
```

Press Enter for each round. `Ctrl+C` to quit.

## License

WTFPL

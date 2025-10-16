# Daggerheart Dice Roller

This repository contains a Python-based dice roller designed to automate attack and damage rolls for the tabletop game Daggerheart. This tool is intended for casual use and does not replace official game mechanics or rules.

---

## Features

- Attack Roll System: Uses the Daggerheart mechanics of rolling two separate d12s for Hope and Fear, combining them with character modifiers to calculate total attack rolls.
- Damage Calculation:
  - Sword: 3d10 + 15 base, including Persona and Bloody Charge modifiers.
  - Shield: 3d6 + 10 base, including Persona and Bloody Charge modifiers.
- Persona Mode: Adds additional dice and bonuses to both attack and damage rolls.
- Bloody Charge: Adds additional dice and bonuses, can be toggled independently.
- Massive Effect: Rolls one extra damage die and drops the lowest.
- Reroll Mechanic: Rerolls 1s and 2s on damage dice to reflect the "Not Good Enough" mechanic.
- Interactive Menu: Easily select attacks, toggle Persona and Bloody Charge, or exit the program.

---

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone the repository:
git clone https://github.com/yourusername/daggerheart-dice-roller.git
cd daggerheart-dice-roller

3. Run the program:
python daggerheart_roller.py


---

## Usage

- Menu Options:
  1. Sword Attack  
  2. Shield Attack  
  3. Toggle Persona Mode  
  4. Toggle Bloody Charge  
  5. Quit  

- Persona Mode and Bloody Charge toggles affect all subsequent attacks until changed.
- Attack rolls are calculated as Hope + Fear + modifiers.
- Damage rolls follow the weapon-specific rules described above.

---

## Credits

- Daggerheart: The dice roller is based on mechanics from the tabletop game Daggerheart.
- ChatGPT: Code generation and structuring assistance was provided by OpenAI's ChatGPT.

---

## Disclaimer

This tool is for casual automation and personal use only. It is not affiliated with or endorsed by the creators of Daggerheart. It does not replace the official rules of the game.

---

## License

This project is open-source and available under the MIT License.

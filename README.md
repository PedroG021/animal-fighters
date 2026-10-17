# Animal Fighters

#### Video Demo: <https://youtu.be/HC67CvCWaks?si=LUa3g9nLADjX3Ni3>

## Description
A 1v1 old-school RPG turn-based game, which runs directly in the terminal (CLI). The game is based on text features, text formats, and text effects via `sys` and `time` libraries, using object-oriented programming. Each animal fighter is an object with its own skills, damage, health, name, and figure. The champions are only created when the player chooses them; the program uses randomization with the `random` library to choose the CPU animal fighter and who will start the fight. Whoever gets their health to 0 first loses the fight. The user and CPU have one turn each. When a fight is over, the winner is shown and the program restarts to the menu option. Finally, the project includes tests in `test_project.py` that cover each important function, using monkeypatch to make it easier and capsys to see function side-effects.

This project was developed as the Final Project for **CS50's Introduction to Programming with Python (CS50P)**, from Harvard University.

---

## Features
- **Text Effects**: All the fight effects and battle design were made using literal strings and helpful libraries like `sys` and `time`.
- **CLI Validation**: The project includes custom validation routines to handle empty answers, numeric option boundaries, and non-positive quantities, so the program does not crash on invalid input.
- **Robust Unit Testing**: Includes pytest tests for the main game logic, using monkeypatch and capsys.
---

## File Structure & System Architecture
- **`project.py`**: The entry point of the project. Contains the main CLI loop (`main()`), menu options selection (`get_menu_choice()`), champion choice (`choose_your_champion()`), and all the battle flow with (`start_battle()`), (`user_action_sequence()`), and (`cpu_action_sequence()`).
- **`champions.py`**: Handles the champions/fighters structures, with representational dicts like (`animals`) and (`animals_play_number`), such as the (`__init__()`) special method that generates the fighters, the (`create_champions()`) class method which returns the champions to be created, (`get_cpu_champion()`) and (`get_user_champion()`) to access the corresponding values inside the dicts, fight options with (`fight_options()`), the damage count for each round with (`damage_count()`), and the winner message with (`display_winner()`).
- **`helper.py`**: This module keeps functions that help the project run more smoothly, like getting a valid number with (`get_number()`), the RPG text effect of the game with (`rpg_text_effect()`), and all the functions that represent the visual battle flow of what's happening and how it is shown to the user, with (`battle_text_round_begin()`), (`battle_text_round_end()`), (`battle_formatter()`), and (`visual_action_to_do()`).
- **`test_project.py`**: The function tester module. Includes tests for logical functions, creational functions, input validation, side-effects, `monkeypatch`, and `capsys`.
---

## Design Decisions
1. **Separation of Concerns (SoC)**: The project was designed with the goal of separating code as much as possible; because of this, each function has a specific 'job', making it easier to test. For instance: The project doesn't ask for a number every time in each function; instead, I use `helper` functions like (`get_number()`) whose purpose in life is to get a valid number despite errors and return it.
2. **Project Defensiveness**: The project handles user mistakes when typing, making sure the game doesn't crash when running because of the user, and doesn't crash when getting information like in (`get_menu_choice()`).
3. **Type Hints**: Every function counts with type hints, which makes it easier to understand the purpose of the functions.

---

## Step-by-Step Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/PedroG021/animal-fighters.git
   cd animal-fighters
   ```
2. **Create a virtual environment** (keeps the project's libraries isolated)
   ```bash
   python -m venv .venv
   ```
3. **Activate the virtual environment**
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (CMD): `.venv\Scripts\activate.bat`
   - Linux / macOS: `source .venv/bin/activate`
4. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the tests** (optional, but recommended)
   ```bash
   pytest test_project.py
   ```
6. **Start the game**
   ```bash
   python project.py
   ```
7. **Play**: choose `3` in the menu, pick your animal by its playable number (1-5), and on each turn type `1` (basic attack), `2` (skill) or `3` (run away). Whoever reaches 0 health first loses.

---

## Setup & Execution

### Prerequisites
- Python 3.12+

### Installation

 Install necessary libraries:
```bash
pip install -r requirements.txt
```

---

### Running the Application

```bash
python project.py
```

---

### Running Tests

```bash
pytest test_project.py
```

---

## Usage

When you run `python project.py`, a menu is shown:

```text
Type 0 to close the program.
Type 1 to understand the game.
Type 2 to read the rules.
Type 3 to start playing the game.
```

Type the corresponding number of what you want to do.

---

## Important Links Received via Duck AI For Functions Throughout The Project

For RPG Text Effect:
https://docs.python.org/3/library/sys.html |
https://docs.python.org/3/library/time.html

For Randomization In The Game:
https://docs.python.org/3/library/random.html

To Enable Testing Of Complex Functions In Simpler Ways:
https://docs.pytest.org/en/stable/how-to/monkeypatch.html

To Ensure That Side Effects From Functions Like `print` Or `Error Messages` Are Being Displayed:
https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html

To Understand How To Pass A Sequence Of Inputs On The Same MonkeyPatch line:
https://docs.python.org/3/library/functions.html#iter |
https://docs.python.org/3/library/functions.html#next

To Be Able To Use Type Hints Like `ANY`:
https://docs.python.org/3/library/typing.html

Basic Help For The README Template File:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax |
https://www.freecodecamp.org/news/how-to-structure-your-readme-file/


---

## Known Limitations

- There's no persistence for the user, like tracking how many battles they have fought already, nor a space for users to have their own accounts with their names to store that data.
- No sound effects or background music.

---

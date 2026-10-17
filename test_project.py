from project import main, get_menu_choice, choose_your_champion, start_battle
from champions import Champions
import helper

# ===================================================================================================

# MAIN MODULE FUNCTION TESTS (project.py)

# ===================================================================================================


def test_main_case_0(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: 0)
    result = main()
    captured = capsys.readouterr()
    assert result is None
    assert "Goodbye, fighter!" in captured.out


def test_main_case_1(monkeypatch, capsys):
    entries = iter([1, 0])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))
    result = main()
    captured = capsys.readouterr()
    assert result is None
    assert "Game Description:\nIts a simple 1v1 game" in captured.out


def test_main_case_2(monkeypatch, capsys):
    entries = iter([2, 0])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))
    result = main()
    captured = capsys.readouterr()
    assert result is None
    assert "\nGame Rules:\nThere are no rules" in captured.out


def test_main_case_3(monkeypatch, capsys):
    entries = iter([3, 0])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))

    monkeypatch.setattr("project.choose_your_champion", lambda: 4)

    user_champion = (
        "🦅",
        "Ghost Eagle",
        90,
        "Ultra-Fast Slicing Blade",
        45,
        "Prominent Beak",
        10,
    )
    cpu_champion = (
        "🕷 ",
        "White Spider",
        110,
        "Spider-Web Machine Gun",
        35,
        "Mega Spider Bite",
        15,
    )

    monkeypatch.setattr(
        "champions.Champions.create_champions",
        lambda n: (Champions(*user_champion), Champions(*cpu_champion)),
    )

    monkeypatch.setattr(helper, "rpg_text_effect", lambda text, delay: print("Working"))

    monkeypatch.setattr(
        "project.start_battle", lambda champ1, champ2: "Champion won the battle"
    )

    result = main()
    captured = capsys.readouterr()
    assert result is None
    assert "Working" in captured.out
    assert "Champion won the battle" in captured.out


def test_main_case_no_match(monkeypatch, capsys):
    entries = iter([4, 0])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))
    result = main()
    captured = capsys.readouterr()
    assert result is None
    assert "\nError: Type a number in range." in captured.out


def test_get_menu_choice(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: 3)

    result = get_menu_choice()
    captured = capsys.readouterr()
    assert result == 3
    assert "Type 0 to close the program." in captured.out


def test_choose_your_champion(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: 4)

    result = choose_your_champion()
    captured = capsys.readouterr()
    assert result == 4
    assert (
        "| 🦅 Ghost Eagle | Health: 90 | Skill: Ultra-Fast Slicing Blade | Damage: 45 | Basic Attack: Prominent Beak | Basic Attack Damage: 10 | Playable number: 4"
        in captured.out
    )


def test_start_battle(monkeypatch):
    user_champion = Champions(
        "🦅", "Ghost Eagle", 90, "Ultra-Fast Slicing Blade", 45, "Prominent Beak", 10
    )
    cpu_champion = Champions(
        "🕷 ", "White Spider", 110, "Spider-Web Machine Gun", 35, "Mega Spider Bite", 15
    )
    cpu_champion.health = 0

    monkeypatch.setattr("project.random.choice", lambda *args: user_champion)

    monkeypatch.setattr("helper.rpg_text_effect", lambda *args: ("Ok", 0.2))

    monkeypatch.setattr(
        "project.user_action_sequence", lambda *args: user_champion.health
    )

    monkeypatch.setattr(
        "project.cpu_action_sequence", lambda *args: cpu_champion.health
    )

    result = start_battle(user_champion, cpu_champion)
    assert result == "🦅 Ghost Eagle won the battle.\n"


# ===================================================================================================

# HELPER MODULE FUNCTION TEST (helper.py)

# ===================================================================================================


def test_get_number(monkeypatch, capsys):
    entries = iter([6, "two", "", 3])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))

    result = helper.get_number("anything")
    captured = capsys.readouterr()
    assert result == 3
    assert "Error: Type a number in range." in captured.out
    assert "Error: Type a literal number like '1' or '2'." in captured.out


# ===================================================================================================

# CHAMPIONS MODULE FUNCTION TESTS (champions.py)

# ===================================================================================================


def test_create_champions(monkeypatch):
    user_champion = Champions(
        "🦅", "Ghost Eagle", 90, "Ultra-Fast Slicing Blade", 45, "Prominent Beak", 10
    )
    cpu_champion = Champions(
        "🕷 ", "White Spider", 110, "Spider-Web Machine Gun", 35, "Mega Spider Bite", 15
    )

    monkeypatch.setattr(
        "champions.Champions.get_user_champion", lambda n: user_champion
    )
    monkeypatch.setattr("champions.Champions.get_cpu_champion", lambda: cpu_champion)

    result = Champions.create_champions("Any")
    assert result == (user_champion, cpu_champion)


def test_get_user_champion(monkeypatch):
    monkey_animals_play_number_dict = {1: "spider"}

    monkey_animals_dict = {
        "spider": {
            "name": "White Spider",
            "figure": "🕷 ",
            "health": 110,
            "skill": "Spider-Web Machine Gun",
            "skill_damage": 35,
            "basic_attack": "Mega Spider Bite",
            "basic_attack_damage": 15,
            "play_number": 1,
        }
    }

    monkeypatch.setattr(
        "champions.Champions.animals_play_number", monkey_animals_play_number_dict
    )
    monkeypatch.setattr("champions.Champions.animals", monkey_animals_dict)

    result = Champions.get_user_champion(1)
    assert result.name == "White Spider"
    assert result.figure == "🕷 "
    assert result.health == 110


def test_get_cpu_champion(monkeypatch):
    monkey_animals_play_number_dict = {1: "spider"}

    monkey_animals_dict = {
        "spider": {
            "name": "White Spider",
            "figure": "🕷 ",
            "health": 110,
            "skill": "Spider-Web Machine Gun",
            "skill_damage": 35,
            "basic_attack": "Mega Spider Bite",
            "basic_attack_damage": 15,
            "play_number": 1,
        }
    }

    monkeypatch.setattr("champions.random.randint", lambda *args: 1)
    monkeypatch.setattr(
        "champions.Champions.animals_play_number", monkey_animals_play_number_dict
    )
    monkeypatch.setattr("champions.Champions.animals", monkey_animals_dict)

    result = Champions.get_cpu_champion()
    assert result.name == "White Spider"
    assert result.figure == "🕷 "
    assert result.health == 110


def test_damage_count():
    user_champion1 = Champions(
        "🦅", "Ghost Eagle", 90, "Ultra-Fast Slicing Blade", 45, "Prominent Beak", 10
    )
    cpu_champion1 = Champions(
        "🕷 ", "White Spider", 110, "Spider-Web Machine Gun", 35, "Mega Spider Bite", 15
    )

    result1 = Champions.damage_count(user_champion1, cpu_champion1, 2)
    assert result1 == 65

    user_champion2 = Champions(
        "🦅", "Ghost Eagle", 90, "Ultra-Fast Slicing Blade", 45, "Prominent Beak", 10
    )
    cpu_champion2 = Champions(
        "🕷 ", "White Spider", 110, "Spider-Web Machine Gun", 35, "Mega Spider Bite", 15
    )

    result2 = Champions.damage_count(user_champion2, cpu_champion2, 1)
    assert result2 == 100


# ===================================================================================================

# END OF FUNCTION TESTS (champions.py)

# ===================================================================================================

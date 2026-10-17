import time
import sys
from champions import Champions


def get_number(s: str) -> int:
    while True:
        try:
            number_choice = int(input(s))
            if 0 <= number_choice <= 5:
                return number_choice

            print("\nError: Type a number in range.\n")

        except ValueError:
            print("\nError: Type a literal number like '1' or '2'.\n")
            continue


def rpg_text_effect(text: str, delay: float) -> None:
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)


def battle_text_round_begin(champion: Champions) -> str:
    rpg_text_effect(
        "\n===================================================================================\n",
        0.01,
    )
    rpg_text_effect(
        f"|--------------------------------Start of {champion.figure} round--------------------------------|\n",
        0.01,
    )
    return ""


def battle_text_round_end(champion: Champions) -> str:
    rpg_text_effect(
        f"\n\n|--------------------------------End of {champion.figure} round----------------------------------|\n",
        0.01,
    )
    rpg_text_effect(
        "===================================================================================\n\n\n",
        0.01,
    )
    return ""


def battle_formatter(user: Champions, cpu: Champions) -> str:
    rpg_text_effect(
        f"\n                      | {user.figure} {user.name} Current Health: {user.health} |\n",
        0.01,
    )
    rpg_text_effect(
        f"                      | {cpu.figure} {cpu.name} Current Health: {cpu.health} |\n",
        0.01,
    )
    return ""


def visual_action_to_do(champion: Champions, action: int) -> None:
    match action:
        case 1:
            battle_text_round_begin(champion)
            rpg_text_effect(
                f'\n {champion.figure} {champion.name} used "{champion.basic_attack}" and caused {champion.basic_attack_damage} damage...\n\n',
                0.05,
            )

        case 2:
            battle_text_round_begin(champion)
            rpg_text_effect(
                f'\n {champion.figure} {champion.name} used "{champion.skill}" and caused {champion.skill_damage} damage...\n\n',
                0.05,
            )

        case 3:
            rpg_text_effect(
                f"\n {champion.figure} {champion.name} runned away from the battle... like a coward.\n\n",
                0.05,
            )
            sys.exit(0)

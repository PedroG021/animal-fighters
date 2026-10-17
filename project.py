from champions import Champions
import random
import helper


def main() -> None:
    print("\nWelcome to the Animals battle.\n")

    while True:
        try:
            choice = get_menu_choice()
            match choice:
                case 0:
                    print("\nGoodbye, fighter!\n")
                    return

                case 1:
                    print(
                        "\nGame Description:\nIts a simple 1v1 game, Choose your champion, the game will automatically choose your oponnent, then fight using it skills.\n"
                    )

                case 2:
                    print("\nGame Rules:\nThere are no rules, only battle to death.\n")

                case 3:
                    user_champion_number = choose_your_champion()
                    user_champion, cpu_champion = Champions.create_champions(
                        user_champion_number
                    )
                    helper.rpg_text_effect(
                        f"\n\n\n\n| User Champion: {user_champion}\n\n                                                                          VERSUS\n\n| Cpu Champion: {cpu_champion}\n\n",
                        0.01,
                    )
                    print(start_battle(user_champion, cpu_champion))

                case _:
                    print("\nError: Type a number in range.\n")

        except (KeyboardInterrupt, EOFError):
            print("\n\nSession closed\n")
            return


def get_menu_choice() -> int:
    choice = None
    while choice is None:
        print("Type 0 to close the program.")
        print("Type 1 to understand the game.")
        print("Type 2 to read the rules.")
        print("Type 3 to start playing the game.")
        choice = helper.get_number("\nWhat do you want to do? ")
        if choice == 0:
            return choice
    return choice


def choose_your_champion() -> int:
    carachter_number = 0
    while carachter_number == 0:
        print("\nPlayable Animals:\n")

        for animal in Champions.animals.values():
            print(
                f"| {animal["figure"]} {animal["name"]} | Health: {animal["health"]} | Skill: {animal["skill"]} | Damage: {animal["skill_damage"]} | Basic Attack: {animal["basic_attack"]} | Basic Attack Damage: {animal["basic_attack_damage"]} | Playable number: {animal["play_number"]}\n"
            )

        carachter_number = helper.get_number(
            "Type the playable number of the champion you want: "
        )

        if carachter_number == 0:
            print("\nError: Type a number in range.")

    return carachter_number


def start_battle(user_champ: Champions, cpu_champ: Champions) -> str:
    first_attacker = random.choice([user_champ, cpu_champ])
    helper.rpg_text_effect(f"\n {first_attacker.name} will start the battle.\n\n", 0.07)

    while user_champ.health > 0 and cpu_champ.health > 0:
        if first_attacker is user_champ:
            user_action_sequence(user_champ, cpu_champ)

            if user_champ.health == 0 or cpu_champ.health == 0:
                break

            cpu_action_sequence(cpu_champ, user_champ)

        else:
            cpu_action_sequence(cpu_champ, user_champ)

            if user_champ.health == 0 or cpu_champ.health == 0:
                break

            user_action_sequence(user_champ, cpu_champ)

    return Champions.display_winner(user_champ, cpu_champ)


def user_action_sequence(user_champ: Champions, cpu_champ: Champions) -> str:
    Champions.fight_options(user_champ)
    user_action = helper.get_number("What will you do? ")

    while user_action == 0 or user_action > 3:
        print("\nError: Type a number in range.\n")
        user_action = helper.get_number("What will you do? ")

    helper.visual_action_to_do(user_champ, user_action)
    Champions.damage_count(user_champ, cpu_champ, user_action)
    helper.battle_formatter(user_champ, cpu_champ)
    return helper.battle_text_round_end(user_champ)


def cpu_action_sequence(cpu_champ: Champions, user_champ: Champions) -> str:
    cpu_action = random.randint(1, 2)
    helper.visual_action_to_do(cpu_champ, cpu_action)
    Champions.damage_count(cpu_champ, user_champ, cpu_action)
    helper.battle_formatter(user_champ, cpu_champ)
    return helper.battle_text_round_end(cpu_champ)


if __name__ == "__main__":
    main()

import random
from typing import Any


class Champions:
    animals: dict[str, dict[str, Any]] = {
        "spider": {
            "name": "White Spider",
            "figure": "🕷 ",
            "health": 110,
            "skill": "Spider-Web Machine Gun",
            "skill_damage": 35,
            "basic_attack": "Mega Spider Bite",
            "basic_attack_damage": 15,
            "play_number": 1,
        },
        "turtle": {
            "name": "King Turtle",
            "figure": "🐢",
            "health": 150,
            "skill": "Colossal King Turtle Bite",
            "skill_damage": 25,
            "basic_attack": "Hoof Beat",
            "basic_attack_damage": 20,
            "play_number": 2,
        },
        "ram": {
            "name": "Mad Ram",
            "figure": "🐏",
            "health": 120,
            "skill": "Furious Headbutt",
            "skill_damage": 30,
            "basic_attack": "Intimidating Stance",
            "basic_attack_damage": 20,
            "play_number": 3,
        },
        "eagle": {
            "name": "Ghost Eagle",
            "figure": "🦅",
            "health": 90,
            "skill": "Ultra-Fast Slicing Blade",
            "skill_damage": 45,
            "basic_attack": "Prominent Beak",
            "basic_attack_damage": 10,
            "play_number": 4,
        },
        "fish": {
            "name": "Wild Fish",
            "figure": "🐡",
            "health": 100,
            "skill": "Venomous Bite",
            "skill_damage": 40,
            "basic_attack": "Fin Strike",
            "basic_attack_damage": 12,
            "play_number": 5,
        },
    }

    animals_play_number: dict[int, str] = {
        1: "spider",
        2: "turtle",
        3: "ram",
        4: "eagle",
        5: "fish",
    }

    def __init__(
        self,
        figure: str,
        name: str,
        health: int,
        skill: str,
        skill_damage: int,
        basic_attack: str,
        basic_attack_damage: int,
    ) -> None:
        self.name = name
        self.health = health
        self.skill = skill
        self.skill_damage = skill_damage
        self.figure = figure
        self.basic_attack = basic_attack
        self.basic_attack_damage = basic_attack_damage

    def __str__(self) -> str:
        return f"{self.figure} {self.name} | Health: {self.health} | Skill: {self.skill} | Skill Damage: {self.skill_damage} | Basic Attack: {self.basic_attack} | Basic Attack Damage: {self.basic_attack_damage} |"

    @classmethod
    def create_champions(cls, n: int) -> tuple["Champions", "Champions"]:
        user_champion = Champions.get_user_champion(n)
        cpu_champion = Champions.get_cpu_champion()
        while user_champion.name == cpu_champion.name:
            cpu_champion = Champions.get_cpu_champion()

        return user_champion, cpu_champion

    @staticmethod
    def get_cpu_champion() -> "Champions":
        cpu_champion_number = random.randint(1, 5)
        return Champions.get_champion(cpu_champion_number)

    @staticmethod
    def get_champion(champion: int) -> "Champions":
        champion = Champions.animals_play_number.get(champion, "")
        champion = Champions.animals[champion]
        champion = Champions(
            champion["figure"],
            champion["name"],
            champion["health"],
            champion["skill"],
            champion["skill_damage"],
            champion["basic_attack"],
            champion["basic_attack_damage"],
        )
        return champion

    @staticmethod
    def get_user_champion(n: int) -> "Champions":
        return Champions.get_champion(n)

    def fight_options(self) -> None:
        print(
            f"Type 1 to basic attack the enemy, causes {self.basic_attack_damage} damage."
        )
        print(f"Type 2 to use your skill, causes {self.skill_damage} damage.")
        print("Type 3 to run away the battle as a coward, causes shame to everyone.\n")
        return

    @staticmethod
    def damage_count(
        champ1: "Champions", champ2: "Champions", champ_action: int
    ) -> int | None:
        match champ_action:
            case 1:
                champ2.health -= champ1.basic_attack_damage
                if champ2.health < 0:
                    champ2.health = 0
                return champ2.health

            case 2:
                champ2.health -= champ1.skill_damage
                if champ2.health < 0:
                    champ2.health = 0
                return champ2.health

            case _:
                return None

    @staticmethod
    def display_winner(champ1: "Champions", champ2: "Champions") -> str:
        if champ1.health == 0:
            return f"{champ2.figure} {champ2.name} won the battle.\n"

        return f"{champ1.figure} {champ1.name} won the battle.\n"

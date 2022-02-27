"""File containing code defining game content such as characters, items etc...."""
from items import *
import random
import validators


class Creature:
    """Defines basic statistics of every creature and person in game.;
     _init__(self, name="John Doe", hp=100, mp=100, m_spd=1)"""

    def __init__(self, name="John Doe", hp=100, mp=100, evasion=1):
        self._health_points = validators.validate_int_value(hp)
        self._mana_points = validators.validate_int_value(mp)
        self.evasion = validators.validate_int_value(evasion)
        self._name = validators.validate_str_value(name)
        self.weapon_in_hand = None
        self.alive = True
        self.experience = 0
        self.level = 1
        self.strength = 10
        self.player_basic_attack = self.strength

    def __repr__(self):
        return f"This is Creature class object. ID:{id(self)}"

    def needed_experience(self):
        exp_constant = 800
        exp_constant_multiplayer = 200
        experience_needed = 0
        for i in range(self.level):
            experience_needed += exp_constant + (i + 1) * exp_constant_multiplayer
        return experience_needed

    def leveling_method(self):
        experience_needed = self.needed_experience()
        str_lvl_bonus = 2
        if self.experience >= experience_needed:
            self.level += 1
            self.strength += str_lvl_bonus

    # show instance: health points, mana points and speed
    def show_creature_stats(self):
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self.evasion} "
              f"evasion")

    def show_stats(self):
        experience_needed = self.needed_experience()
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self.evasion} "
              f"evasion \n{self.level} level \n{self.experience}/{experience_needed}\n{self.strength} strength")
        print(f"You are holding {self.weapon_in_hand}")


class EasyMonster(Creature):
    gained_experience = 100
    EasyMonster_weapon = Weapons(6, 1)
    gold_drop = random.randint(10, 20)
    chest_drop = None

    def __init__(self, name="Orc", hp=random.randint(100, 200), mp=100, evasion=1):
        Creature.__init__(self, name, hp, mp, evasion)
        self.weapon_in_hand = EasyMonster.EasyMonster_weapon
        self.player_basic_attack = 2


class MediumMonster(Creature):
    gained_experience = 2000
    MediumMonster_weapon = Weapons(15, 1)
    gold_drop = random.randint(10, 30)
    chest_drop = Chest(1)  # drops wooden chest

    def __init__(self, name="Orc Warrior", hp=random.randint(200, 300), mp=100, evasion=1):
        Creature.__init__(self, name, hp, mp, evasion)
        self.weapon_in_hand = MediumMonster.MediumMonster_weapon
        self.player_basic_attack = 5


class HardMonster(Creature):
    gained_experience = 400
    HardMonster_weapon = Weapons(20, 2)
    gold_drop = random.randint(20, 40)
    chest_drop = Chest()

    def __init__(self, name="Orc Captain", hp=random.randint(300, 400), mp=100, evasion=1):
        Creature.__init__(self, name, hp, mp, evasion)
        self.weapon_in_hand = HardMonster.HardMonster_weapon
        self.player_basic_attack = 10


class LegendaryMonster(Creature):
    gained_experience = 1000
    LegendaryMonster_weapon = Weapons(35, 2)
    gold_drop = random.randint(50, 120)
    chest_drop = Chest()

    def __init__(self, name="Orc Leader", hp=random.randint(500, 600), mp=100, evasion=1):
        Creature.__init__(self, name, hp, mp, evasion)
        self.weapon_in_hand = LegendaryMonster.LegendaryMonster_weapon
        self.player_basic_attack = 20

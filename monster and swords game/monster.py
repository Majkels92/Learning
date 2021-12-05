import random
import validators


class Creature:
    """Defines basic statistics of every creature and person in game."""

    def __init__(self, hp=100, mp=100, spd=1, name="John Doe"):
        self._health_points = validators.validate_int_value(hp)
        self._mana_points = validators.validate_int_value(mp)
        self._speed = validators.validate_int_value(spd)
        self._name = validators.validate_str_value(name)

    # show instance: health points, mana points and speed
    def show_creature_stats(self):
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self._speed} speed")


class Weapons:
    """Defines damage and attack speed of weapon"""

    def __init__(self):
        self._basic_damage = random.randint(1, 100)
        self._basic_attack_speed = Weapons.setting_att_speed()

    # draw value of attack speed with weighted possibility (common = 60%, rare = 30%, legendary=10%)
    # att_spd_range - attribute used for increasing possibility of better attack speed draw, used in Chest class
    @staticmethod
    def setting_att_speed(att_spd_range=1):
        """ Draw value of attack speed with weighted possibility (common = 60%, rare = 30%, legendary=10%);
        att_spd_range - attribute used for increasing possibility of better attack speed draw, used in Chest class"""
        possibility = random.randint(att_spd_range, 10)
        if possibility <= 6:
            return (random.randrange(10, 51))/10
        elif possibility <= 9:
            return (random.randrange(50, 81))/10
        else:
            return (random.randrange(80, 101))/10

    # show instance: basic damage and attack speed
    def show_weapon_stats(self):
        print(f"This weapon has: \n{self._basic_damage} dmg\n{self._basic_attack_speed} att spd")


a = Creature(200, 300, 4)
a.show_creature_stats()
w = Weapons()
w.show_weapon_stats()

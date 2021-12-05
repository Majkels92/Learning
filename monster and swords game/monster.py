import random
import validators


class Creature:
    """Defines basic statistics of every creature and person in game."""

    def __init__(self, hp=100, mp=100, spd=1, name="John Doe"):
        self._health_points = validators.validate_int_value(hp)
        self._mana_points = validators.validate_int_value(mp)
        self._speed = validators.validate_int_value(spd)
        self._name = validators.validate_str_value(name)

    # show objects: health points, mana points and speed
    def show_creature_stats(self):
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self._speed} speed")


class Weapons:
    """Defines damage and attack speed of weapon"""

    def __init__(self):
        self.set_damage()
        self.set_attack_speed()

    def set_damage(self):
        self.damage = random.randint(1, 100)

    def set_attack_speed(self):
        self.attack_speed = (random.randrange(10, 101))/10

    def show_weapon_stats(self):
        print(f"This weapon has: \n{self.damage} dmg\n{self.attack_speed} att spd")


a = Creature(200, 300, 4)
a.show_creature_stats()

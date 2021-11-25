import random

class Creature:
    """Defines basic statistics of every creature and person in game."""

    def __init__(self, hp = 100, mp = 100, spd = 1):
        self.set_hp(hp)
        self.set_mp(mp)
        self.set_spd(spd)

    def set_hp(self, hp):
        if isinstance(hp, int) and hp > 0:
            self.health_points = hp
        else:
            raise TypeError("Attribute must be integer and greater than 0.")

    def set_mp(self, mp):
        if isinstance(mp, int) and mp > 0:
            self.mana_points = mp
        else:
            raise TypeError("Attribute must be integer and greater than 0.")

    def set_spd(self, spd):
        if isinstance(spd, int) and spd > 0:
            self.speed = spd
        else:
            raise TypeError("Attribute must be integer and greater than 0.")

    def show_creature_stats(self):
        print(f"This subject has: \n{self.health_points} hp \n{self.mana_points} mp \n{self.speed} speed")

class Weapons:

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
b = Weapons()
b.show_weapon_stats()





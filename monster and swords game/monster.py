class Creature:

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

    def show_stats(self):
        print(f"This subject has: \n{self.health_points} hp \n{self.mana_points} mp \n{self.speed} speed")


a = Creature(200, 300, 4)
a.show_stats()


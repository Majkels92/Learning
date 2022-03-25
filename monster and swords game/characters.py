"""File containing code defining game content such as characters, items etc...."""
import validators
import items


class Creature:
    """Defines basic statistics of every creature and person in game.;
     _init__(self, name="John Doe", hp=100, mp=100, m_spd=1)"""

    gold_drop = None
    gained_experience = None
    chest_drop = None

    def __init__(self, name="John Doe", hp=100, mp=100, evasion=1, strength=10):
        self._health_points = validators.validate_int_value(hp)
        self._mana_points = validators.validate_int_value(mp)
        self.evasion = validators.validate_int_value(evasion)
        self._name = validators.validate_str_value(name)
        self.weapon_in_hand = None
        self.alive = True
        self.experience = 0
        self.level = 1
        self.strength = validators.validate_int_value(strength)
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
            self._health_points += 30


    # show instance: health points, mana points and speed
    def show_creature_stats(self):
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self.evasion} "
              f"evasion")

    def show_stats(self):
        experience_needed = self.needed_experience()
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self.evasion} "
              f"evasion \n{self.level} level \n{self.experience}/{experience_needed}\n{self.strength} strength")
        print(f"You are holding {self.weapon_in_hand}")


class Monster(Creature):

    def __init__(self, name, w_att, w_speed, gold_drop, gained_experience, chest_drop, hp, strength, evasion=1):
        Creature.__init__(self)
        self.name = name
        self.weapon_in_hand = items.Weapons(w_att, w_speed)
        self.gold_drop = gold_drop
        self.gained_experience = gained_experience
        self.chest_drop = chest_drop
        self.hp = hp
        self.player_basic_attack = strength
        self.evasion = evasion

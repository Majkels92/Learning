"""File containing code defining game content such as characters, items etc...."""
import random
import validators


class Creature:
    """Defines basic statistics of every creature and person in game.;
     _init__(self, hp=100, mp=100, m_spd=1, name="John Doe")"""

    def __init__(self, hp=100, mp=100, m_spd=1, name="John Doe"):
        self._health_points = validators.validate_int_value(hp)
        self._mana_points = validators.validate_int_value(mp)
        self._movement_speed = validators.validate_int_value(m_spd)
        self._name = validators.validate_str_value(name)

    def __repr__(self):
        return f"This is Creature class object. ID:{id(self)}"

    # show instance: health points, mana points and speed
    def show_creature_stats(self):
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self._movement_speed} "
              f"movement speed")


class Weapons:
    """Defines damage and attack speed of weapon"""

    def __init__(self):
        self._basic_damage = Weapons.setting_dmg()
        self._basic_attack_speed = Weapons.setting_att_speed()

    def __repr__(self):
        return f"This is Weapon class object. ID:{id(self)}"

    # draw value of basic attack speed with weighted possibility
    @staticmethod
    def setting_att_speed(att_spd_range=1):
        """ Draw value of basic attack speed with weighted possibility (common = 60%, rare = 30%, legendary=10%)
        att_spd_range - attribute used for increasing possibility of better attack speed draw, used in Chest class"""
        possibility = random.randint(att_spd_range, 10)
        if possibility <= 6:
            return (random.randrange(10, 50))/10
        elif possibility <= 9:
            return (random.randrange(50, 80))/10
        else:
            return (random.randrange(80, 101))/10

    # draw value of basic attack damage with weighted possibility
    @staticmethod
    def setting_dmg(dmg_range=1):
        """ Draw value of basic damage with weighted possibility (common = 60%, rare = 30%, legendary=10%);

        setting_dmg(dmg_range)
        dmg_range: default value = 1

        dmg_range - attribute used for increasing possibility of better attack speed draw, used in Chest class"""
        possibility = random.randint(dmg_range, 10)
        if possibility <= 6:
            return random.randint(1, 50)
        elif possibility <= 9:
            return random.randint(51, 85)
        else:
            return random.randint(86, 100)

    # show instance: basic damage and attack speed
    def show_weapon_stats(self):
        print(f"This weapon has: \n{self._basic_damage} dmg\n{self._basic_attack_speed} att spd")


class Chest:
    """Creates Chest instance and defining its type and content"""

    def __init__(self):
        self.rarity = Chest.draw_rarity()
        self.drop = self.chest_gold_drop()

    # draws and set rarity of chest
    @staticmethod
    def draw_rarity():
        chest_rarity = random.randint(1, 10)
        if chest_rarity <= 6:
            return "wooden"
        elif chest_rarity <= 9:
            return "iron"
        else:
            return "golden"

    # draws amount of gold dropped from chest
    def chest_gold_drop(self):
        if self.rarity == "golden":
            drop = 100
        elif self.rarity == "iron":
            drop = 50
        elif self.rarity == "wooden":
            drop = 10
        return drop


class Backpack:
    """Defines backpack and number of available slots; __init__(self, slots=15)"""

    def __init__(self, owner, slots=15):
        self._owner = owner._name
        self.backpack_slots = []
        self._basic_slots = validators.validate_int_value(slots)
        for slot in range(self._basic_slots):
            slot = "Empty slot"
            self.backpack_slots.append(slot)

    def __repr__(self):
        return f"This is PlayerBackPack class object. ID:{id(self)}"

    @property
    def slots(self):
        return self._basic_slots

    # extends number of slots in players backpack
    def slot_extender(self, additional_slot):
        for new_slot in range(additional_slot):
            self.backpack_slots.append("Empty slot")


class GoldSack:
    """Creates sack for gold for chosen player, necessary name of owner as first argument.
    _-init__(self, owner, gold_amount=0) """

    def __init__(self, owner, gold_amount=0):
        self._owner = owner._name
        self.gold_amount = validators.validate_sack_value(gold_amount)

    def __repr__(self):
        return f"This is gold sack of {self._owner}"

    # shows amount of gold
    def check_gold_in_sack(self):
        return f"In {self._owner} sack is {self.gold_amount} gold"


player = Creature(name="Jacek Kopacz")
player2 = Creature(name="Daro Wariat")
sack = GoldSack(player2)
print(sack)
print(sack.check_gold_in_sack())

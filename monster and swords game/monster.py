"""File containing code defining game content such as characters, items etc...."""
import random
import validators


class Creature:
    """Defines basic statistics of every creature and person in game.;
     _init__(self, hp=100, mp=100, m_spd=1, name="John Doe")"""

    def __init__(self, hp=100, mp=100, evasion=1, name="John Doe"):
        self._health_points = validators.validate_int_value(hp)
        self._mana_points = validators.validate_int_value(mp)
        self._evasion = validators.validate_int_value(evasion)
        self._name = validators.validate_str_value(name)

    def __repr__(self):
        return f"This is Creature class object. ID:{id(self)}"

    # show instance: health points, mana points and speed
    def show_creature_stats(self):
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self._evasion} "
              f"evasion")


# inherited classes of monsters
class EasyMonster(Creature):

    gained_experience = 100
    EasyMonster_weapon = None

    def __init__(self, hp=random.randint(100, 200), mp=100, evasion=1, name="Orc"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.attack = 5

    def damage_output(self):
        damage_output = random.randint(self.attack, self.attack*2)
        return damage_output


class MediumMonster(Creature):

    gained_experience = 200
    MediumMonster_weapon = None

    def __init__(self, hp=random.randint(200, 300), mp=100, evasion=1, name="Orc Warrior"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.attack = 10

    def damage_output(self):
        damage_output = random.randint(self.attack, self.attack*2)
        return damage_output


class HardMonster(Creature):

    gained_experience = 400
    HardMonster_weapon = None

    def __init__(self, hp=random.randint(300, 400), mp=100, evasion=1, name="Orc Captain"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.attack = 20

    def damage_output(self):
        damage_output = random.randint(self.attack, self.attack*2)
        return damage_output


class LegendaryMonster(Creature):

    gained_experience = 1000
    LegendaryMonster_weapon = None

    def __init__(self, hp=random.randint(500, 600), mp=100, evasion=1, name="Orc Leader"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.attack = 40

    def damage_output(self):
        damage_output = random.randint(self.attack, self.attack*2)
        return damage_output


# ITEMS
class Weapons:
    """Defines damage and attack speed of weapon"""

    def __init__(self, damage, attack_speed):
        self._basic_damage = damage
        self._basic_attack_speed = attack_speed

    def __repr__(self):
        return f"This is Weapon class object. ID:{id(self)}"

    @property
    def basic_damage(self):
        return self._basic_damage

    @basic_damage.setter
    def basic_damage(self, value):
        self._basic_damage = value

    @property
    def basic_attack_speed(self):
        return self._basic_attack_speed

    @basic_attack_speed.setter
    def basic_attack_speed(self, value):
        self._basic_attack_speed = value

    # draw value of basic attack speed with weighted possibility
    @staticmethod
    def drawing_att_speed_value(att_spd_range_min=1, att_spd_range_max=10):
        """ Draw value of basic attack speed with weighted possibility (common = 60%, rare = 30%, legendary=10%)
        att_spd_range - attribute used for increasing possibility of better attack speed draw, used in Chest class"""
        possibility = random.randint(att_spd_range_min, att_spd_range_max)
        if possibility <= 6:
            return (random.randrange(10, 50))/10
        elif possibility <= 9:
            return (random.randrange(50, 80))/10
        else:
            return (random.randrange(80, 101))/10

    # draw value of basic attack damage with weighted possibility
    @staticmethod
    def drawing_dmg_value(dmg_range_min=1, dmg_range_max=10):
        """ Draw value of basic damage with weighted possibility (common = 60%, rare = 30%, legendary=10%);

        setting_dmg(dmg_range)
        dmg_range: default value = 1

        dmg_range - attribute used for increasing possibility of better attack speed draw, used in Chest class"""
        possibility = random.randint(dmg_range_min, dmg_range_max)
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

    def open_chest(self, sack):
        gold_received = self.drop
        sack.put_gold_into_sack(gold_received)


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

    # put item in first empty slot in backpack
    def put_item_into_backpack(self, item):
        for item_slot in range(len(self.backpack_slots)):
            if item_slot == "Empty slot":
                self.backpack_slots[item_slot] = item
            else:
                print("No room in inventory")

    # withdraws from backpack item chosen by slot number
    def withdraw_item_from_backpack(self, slot_index):
        validators.validate_int_value_2(slot_index)
        for item_slot in range(len(self.backpack_slots)):
            if (item_slot + 1) == slot_index:
                self.backpack_slots[item_slot] = "Empty slot"

    # extends number of slots in players backpack
    def slot_extender(self, additional_slot):
        for new_slot in range(additional_slot):
            self.backpack_slots.append("Empty slot")


class GoldSack:
    """Creates sack for gold for chosen player, necessary name of owner as first argument.
    _-init__(self, owner, gold_amount=0) """

    def __init__(self, owner, gold_amount=0):
        self._owner = owner._name
        self.gold_amount = validators.validate_int_value_2(gold_amount)

    def __repr__(self):
        return f"Sack of {self._owner} with {self.gold_amount} gold"

    # add gold to sack
    def put_gold_into_sack(self, value):
        self.gold_amount = self.gold_amount + value

    # withdraw gold from sack
    def withdraw_gold_from_sack(self, value):
        self.gold_amount = self.gold_amount - value
        if self.gold_amount < 0:
            self.gold_amount = 0

    # shows amount of gold
    def check_gold_in_sack(self):
        return f"In {self._owner} sack is {self.gold_amount} gold"


class ActionsFight:
    """Actions connected with fight"""

    def attack(self):
        pass

    def evade_attack(self):
        pass

    def escape(self):
        pass


"""michal = Creature(name = "Michal Skowronski")
sack = GoldSack(michal)
sack.put_gold_into_sack(20)
print(sack.check_gold_in_sack())"""

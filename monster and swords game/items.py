import random
import validators
import enum


class Weapons:
    """Defines damage and attack speed of weapon __init__(self, damage, attack_speed)"""

    def __init__(self, damage, attack_speed):
        self._basic_damage = validators.validate_int_weapon_dmg_value(damage)
        self._attack_speed = validators.validate_float_weapon_att_spd_value(attack_speed)
        self.additional_damage = 0

    def __repr__(self):
        return f"This is Weapon class object. ID:{id(self)} with {self._basic_damage} dmg and {self._attack_speed} spd"

    @property
    def basic_damage(self):
        return self._basic_damage

    @basic_damage.setter
    def basic_damage(self, value):
        self._basic_damage = value

    @property
    def basic_attack_speed(self):
        return self._attack_speed

    @basic_attack_speed.setter
    def basic_attack_speed(self, value):
        self._attack_speed = value

    # draw value of basic attack speed with weighted possibility
    @staticmethod
    def drawing_att_speed_value(att_spd_possibility_min=1, att_spd_possibility_max=10):
        """ Draw value of basic attack speed with weighted possibility (common = 60%, rare = 30%, legendary=10%)
        att_spd_range - attribute used for increasing possibility of better attack speed draw, used in Chest class
        """
        possibility = random.randint(att_spd_possibility_min, att_spd_possibility_max)
        if possibility <= 6:
            return round(random.uniform(1, 2.5), 1)
        elif possibility <= 9:
            return round(random.uniform(2.5, 3.5), 1)
        else:
            return round(random.uniform(3.5, 4), 1)

    # draw value of basic attack damage with weighted possibility
    @staticmethod
    def drawing_dmg_value(damage_possibility_min=1, damage_possibility_max=10):
        """ Draw value of basic damage with weighted possibility (common = 60%, rare = 30%, legendary=10%);

        setting_dmg(dmg_range)
        dmg_range: default value = 1

        dmg_range - attribute used for increasing possibility of better attack speed draw, used in Chest class"""
        possibility = random.randint(damage_possibility_min, damage_possibility_max)
        if possibility <= 6:
            return random.randint(1, 50)
        elif possibility <= 9:
            return random.randint(51, 85)
        else:
            return random.randint(86, 100)

    def weapon_damage_output(self):
        weapon_damage = self._basic_damage + self.additional_damage
        attack = weapon_damage + weapon_damage * round(random.uniform(-0.4, 0.4), 1)
        return attack

    # show instance: basic damage and attack speed
    def show_weapon_stats(self):
        print(f"This weapon has: \n{self._basic_damage} dmg\n{self._attack_speed} att spd")


class ChestTypes(enum.IntEnum):

    wooden = 1
    iron = 2
    golden = 3


class Chest:
    """Creates Chest instance and defining its type and content, __init__(self, rarity=None) if None draws rarity"""

    def __init__(self, rarity=None):
        if rarity is None:
            self.rarity = Chest.draw_rarity()
        else:
            self.rarity = rarity
        self.gold_drop = self.chest_gold_drop()
        self.weapon_drop = self.chest_weapon_drop()

    def __repr__(self):
        return f"This is {self.rarity.name} chest with {self.gold_drop} gold and {self.weapon_drop}"

    # draws and set rarity of chest
    @staticmethod
    def draw_rarity():
        chest_list = [c_type for c_type in ChestTypes]
        draw_chest_type = random.choices(chest_list, [70, 25, 5])
        drawn_chest = draw_chest_type[0]  # gives string type variable
        return drawn_chest

    # draws amount of gold dropped from chest
    def chest_gold_drop(self):
        if self.rarity == ChestTypes.wooden:
            gold_drop = 10
        elif self.rarity == ChestTypes.iron:
            gold_drop = 50
        elif self.rarity == ChestTypes.golden:
            gold_drop = 100
        return gold_drop

    def chest_weapon_drop(self):
        if self.rarity == ChestTypes.wooden:
            weapon_drop = Weapons(Weapons.drawing_dmg_value(1, 6), Weapons.drawing_att_speed_value(1, 6))
        elif self.rarity == ChestTypes.iron:
            weapon_drop = Weapons(Weapons.drawing_dmg_value(1, 9), Weapons.drawing_att_speed_value(1, 9))
        elif self.rarity == ChestTypes.golden:
            weapon_drop = Weapons(Weapons.drawing_dmg_value(7, 10), Weapons.drawing_att_speed_value(7, 10))
        return weapon_drop

    def open_chest(self, sack, backpack):
        gold_received = self.gold_drop
        sack.put_gold_into_sack(gold_received)
        weapon_received = self.weapon_drop
        backpack.put_item_into_backpack(weapon_received)

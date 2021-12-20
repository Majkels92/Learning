"""File containing code defining game content such as characters, items etc...."""
import random
import validators
import time


class Creature:
    """Defines basic statistics of every creature and person in game.;
     _init__(self, hp=100, mp=100, m_spd=1, name="John Doe")"""

    def __init__(self, hp=100, mp=100, evasion=1, name="John Doe"):
        self._health_points = validators.validate_int_value(hp)
        self._mana_points = validators.validate_int_value(mp)
        self.evasion = validators.validate_int_value(evasion)
        self._name = validators.validate_str_value(name)
        self.weapon = None
        self.alive = True

    def __repr__(self):
        return f"This is Creature class object. ID:{id(self)}"

    # show instance: health points, mana points and speed
    def show_creature_stats(self):
        print(f"{self._name} has: \n{self._health_points} hp \n{self._mana_points} mp \n{self.evasion} "
              f"evasion")


class Weapons:
    """Defines damage and attack speed of weapon __init__(self, damage, attack_speed)"""

    def __init__(self, damage, attack_speed):
        self._basic_damage = validators.validate_int_weapon_dmg_value(damage)
        self._attack_speed = validators.validate_float_weapon_att_spd_value(attack_speed)
        self.additional_damage = 0

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
        return self._attack_speed

    @basic_attack_speed.setter
    def basic_attack_speed(self, value):
        self._attack_speed = value

    # draw value of basic attack speed with weighted possibility
    @staticmethod
    def drawing_att_speed_value(att_spd_possibility_min=1, att_spd_possibility_max=10):
        """ Draw value of basic attack speed with weighted possibility (common = 60%, rare = 30%, legendary=10%)
        att_spd_range - attribute used for increasing possibility of better attack speed draw, used in Chest class"""
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

    def damage_output(self):
        weapon_damage = self._basic_damage + self.additional_damage
        attack = weapon_damage + weapon_damage * round(random.uniform(-0.4, 0.4), 1)
        return attack

    # show instance: basic damage and attack speed
    def show_weapon_stats(self):
        print(f"This weapon has: \n{self._basic_damage} dmg\n{self._attack_speed} att spd")


class EasyMonster(Creature):

    gained_experience = 100
    EasyMonster_weapon = Weapons(6, 1)
    gold_drop = random.randint(10, 20)

    def __init__(self, hp=random.randint(100, 200), mp=100, evasion=1, name="Orc"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.weapon = EasyMonster.EasyMonster_weapon


class MediumMonster(Creature):

    gained_experience = 200
    MediumMonster_weapon = Weapons(15, 1)
    gold_drop = random.randint(10, 30)

    def __init__(self, hp=random.randint(200, 300), mp=100, evasion=1, name="Orc Warrior"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.weapon = MediumMonster.MediumMonster_weapon


class HardMonster(Creature):

    gained_experience = 400
    HardMonster_weapon = Weapons(20, 2)
    gold_drop = random.randint(20, 40)

    def __init__(self, hp=random.randint(300, 400), mp=100, evasion=1, name="Orc Captain"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.weapon = HardMonster.HardMonster_weapon


class LegendaryMonster(Creature):

    gained_experience = 1000
    LegendaryMonster_weapon = Weapons(35, 2)
    gold_drop = random.randint(50, 120)

    def __init__(self, hp=random.randint(500, 600), mp=100, evasion=1, name="Orc Leader"):
        Creature.__init__(self, hp, mp, evasion, name)
        self.weapon = LegendaryMonster.LegendaryMonster_weapon


class Chest:
    """Creates Chest instance and defining its type and content"""

    def __init__(self):
        self.rarity = Chest.draw_rarity()
        self.drop = self.chest_gold_drop()

    # draws and set rarity of chest
    @staticmethod
    def draw_rarity():
        chest_type = ["wooden", "iron", "golden"]
        draw_chest_type = random.choices(chest_type, [70, 25, 5])
        return draw_chest_type

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

    @staticmethod
    def attack(weapon):
        hit = weapon.damage_output()
        multiplier = weapon._attack_speed
        hp_loss = hit*multiplier  # damage from attack
        return hp_loss

    @staticmethod
    def evade_attack(character):
        chance_to_evade = character.evasion/100
        result = round(random.uniform(0, 1), 2)
        if chance_to_evade >= result:
            evade = True
        else:
            evade = False
        return evade


class Actions:

    # method transferring dropped gold from beaten enemy or opened chest to chosen sack (usually player's)
    @staticmethod
    def loot_gold(looted_obj, profit_sack):
        profit_sack.put_gold_into_sack(looted_obj.gold_drop)


class Fight:

    @staticmethod
    def evading_attack(player, enemy):
        pass

    # method simulating fight, if player win fight, gives him dropped gold from nemesis
    @staticmethod
    def fight(player, enemy, player_sack):
        player_hp = player._health_points
        enemy_hp = enemy._health_points
        print("FIGHT BEGINS:")
        time.sleep(1)
        while player.alive is True or enemy.alive is True:
            hit = ActionsFight.attack(player.weapon)
            print(f"You hit for {hit} hp")
            enemy_hp = enemy_hp - hit
            time.sleep(0.3)
            print(f"ENEMY has {enemy_hp} left.")
            time.sleep(1)
            if enemy_hp <= 0:
                enemy.alive = False
                break
            hit = ActionsFight.attack(enemy.weapon)
            print(f"Enemy hit for {hit} hp")
            player_hp = player_hp - hit
            time.sleep(0.3)
            print(f"YOU have {player_hp} left.")
            time.sleep(1)
            if player_hp <= 0:
                player.alive = False
                break
        if player.alive is False:
            print("You died")
        else:
            print("You won fight!")
            Actions.loot_gold(enemy, player_sack)

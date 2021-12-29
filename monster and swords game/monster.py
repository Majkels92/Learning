"""File containing code defining game content such as characters, items etc...."""
import random
import validators
import time
import enum


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

    def leveling_method(self):
        experience_needed = 0
        for i in range(self.level):
            experience_needed += (i+1) * 200 + 800
        if self.experience >= experience_needed:
            self.level += 1
            self.strength += 2

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

    def __repr__(self):
        return f"This is {self.rarity} chest with {self.gold_drop} gold"

    # draws and set rarity of chest
    @staticmethod
    def draw_rarity():
        draw_chest_type = random.choices([1, 2, 3], [70, 25, 5])
        chest_type = draw_chest_type[0]  # gives string type variable
        return chest_type

    # draws amount of gold dropped from chest
    def chest_gold_drop(self):
        if self.rarity == ChestTypes.wooden:
            self.rarity = ChestTypes.wooden.name
            gold_drop = 10
        elif self.rarity == ChestTypes.iron:
            self.rarity = ChestTypes.iron.name
            gold_drop = 50
        elif self.rarity == ChestTypes.golden:
            self.rarity = ChestTypes.golden.name
            gold_drop = 100
        return gold_drop

    def open_chest(self, sack):
        gold_received = self.gold_drop
        sack.put_gold_into_sack(gold_received)


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
    chest_drop = Chest(1)

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


class Backpack:
    """Defines backpack and number of available slots; __init__(self, slots=15)"""

    def __init__(self, slots=15):
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
        validators.validate_sack_number_value(slot_index)
        for item_slot in range(len(self.backpack_slots)):
            if (item_slot + 1) == slot_index:
                self.backpack_slots[item_slot] = "Empty slot"

    # extends number of slots in players backpack
    def slot_extender(self, additional_slot):
        for new_slot in range(additional_slot):
            self.backpack_slots.append("Empty slot")


class GoldSack:
    """Creates sack for gold.
    _-init__(self, gold_amount=0) """

    def __init__(self, gold_amount=0):
        self.gold_amount = validators.validate_sack_number_value(gold_amount)

    def __repr__(self):
        return f"Sack with {self.gold_amount} gold"

    # add gold to sack
    def put_gold_into_sack(self, value):
        self.gold_amount = self.gold_amount + validators.validate_sack_number_value(value)

    # withdraw gold from sack
    def withdraw_gold_from_sack(self, value):
        self.gold_amount = self.gold_amount - validators.validate_sack_number_value(value)
        if self.gold_amount < 0:
            self.gold_amount = 0

    # shows amount of gold
    def check_gold_in_sack(self):
        return f"Sack has {self.gold_amount} gold"


class ActionsFight:
    """Actions connected with fight"""

    @staticmethod
    def attack(weapon, creature):
        hit = weapon.weapon_damage_output()
        multiplier = weapon._attack_speed
        hp_loss = hit*multiplier + creature.player_basic_attack  # damage from attack
        return int(hp_loss)

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
    def loot_gold(looted_obj, sack):
        sack.put_gold_into_sack(looted_obj.gold_drop)

    @staticmethod
    def loot_chest(chest_source, sack):
        chest_source.chest_drop.open_chest(sack)

    @staticmethod
    def gain_experience(player, experience_source):
        player.experience += experience_source.gained_experience
        player.leveling_method()


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
            hit = ActionsFight.attack(player.weapon_in_hand, player)
            print(f"You hit for {hit} hp")
            enemy_hp = validators.change_below_0(enemy_hp, hit)
            time.sleep(0.3)
            print(f"ENEMY has {enemy_hp} HP left.")
            time.sleep(1)
            if enemy_hp <= 0:
                enemy.alive = False
                break
            hit = ActionsFight.attack(enemy.weapon_in_hand, enemy)
            print(f"Enemy hit for {hit} hp")
            player_hp = validators.change_below_0(player_hp, hit)
            time.sleep(0.3)
            print(f"YOU have {player_hp} HP left.")
            time.sleep(1)
            if player_hp <= 0:
                player.alive = False
                break
        if player.alive is False:
            print("You died")
        else:
            print("You won fight!")
            if enemy.chest_drop is not None:
                Actions.loot_chest(enemy, player_sack)
            Actions.loot_gold(enemy, player_sack)
            Actions.gain_experience(player, enemy)

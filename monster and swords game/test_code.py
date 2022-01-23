from actions import *
from containers import *
from characters import *

michal = Creature("Michal Skowronski")  # creates player
michal.weapon_in_hand = Weapons(20, 2.0)  # adds weapon for player

# testing sack
print("TESTING SACK")
player_sack = GoldSack()
print(player_sack.check_gold_in_sack())
player_sack.put_gold_into_sack(20)
print(player_sack.check_gold_in_sack())
player_sack.withdraw_gold_from_sack(2)
print(player_sack.check_gold_in_sack())  # all passed
backpack = Backpack()

# testing chest
print("\n\nTESTING CHEST")
chest1 = Chest()
print(chest1)
print("before opening chest", player_sack.check_gold_in_sack())
chest1.open_chest(player_sack, backpack)
print("after opening chest", player_sack.check_gold_in_sack())

# testing fight
print("\n\nTESTING FIGHT")
print(michal.strength, "str")
print(michal.experience, "exp")
print(michal.level, "lvl")
orc = MediumMonster(evasion=50)  # creates monster
print(orc._health_points, " monster hp")
Fight.fight(michal, orc, player_sack, backpack)
print(player_sack.check_gold_in_sack())
print(michal.experience, "exp")
print(michal.level, "lvl")
print(michal.strength)  # all passed


# testing backpack 1
"""print("\nTESTING BACKPACK\n")
backpack = Backpack()
player_sack = GoldSack()
chest1 = Chest()
weapon1 = Weapons(20, 2.0)
print(backpack)
print(player_sack)
print(chest1)
backpack.show_slots()
print("now i put something for U")
for k in range(15):
    backpack.put_item_into_backpack(weapon1)
backpack.show_slots()
backpack.put_item_into_backpack(weapon1)
backpack.withdraw_item_from_slot(2)
backpack.show_slots()"""

# testing backpack 1
"""print("\nTESTING BACKPACK\n")
backpack = Backpack()
player_sack = GoldSack()
michal = Creature("Michal Skowronski")  # creates player
michal.weapon_in_hand = Weapons(20, 2.0)  # adds weapon for player
orc = MediumMonster(hp=10)  # creates monster
print(orc._health_points, " monster hp")
Fight.fight(michal, orc, player_sack, backpack)
backpack.show_slots()
"""

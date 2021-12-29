from monster import *

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

# testing chest
print("\n\nTESTING CHEST")
chest1 = Chest()
print(chest1)
print("before opening chest", player_sack.check_gold_in_sack())
chest1.open_chest(player_sack)
print("after opening chest", player_sack.check_gold_in_sack())

# testing backpack
print("\n\nTESTING BACKPACK")
backpack = Backpack()


# testing fight
print("\n\nTESTING FIGHT")
print(michal.strength, "str")
print(michal.experience, "exp")
print(michal.level, "lvl")
orc = MediumMonster(hp=10)  # creates monster
print(orc._health_points, " monster hp")
Fight.fight(michal, orc, player_sack)
print(player_sack.check_gold_in_sack())
print(michal.experience, "exp")
print(michal.level, "lvl")
print(michal.strength)  # all passed

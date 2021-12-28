from monster import *

michal = Creature(name="Michal Skowronski")  # creates player
michal.weapon = Weapons(20, 2.0)  # adds weapon for player

# testing sack + fight
player_sack = GoldSack(michal)
print(player_sack.check_gold_in_sack())
player_sack.put_gold_into_sack(20)
print(player_sack.check_gold_in_sack())
player_sack.withdraw_gold_from_sack(12.4)
print(player_sack.check_gold_in_sack())  # all passed

#  testing chest




#  testing fight
"""orc = EasyMonster()  # creates monster
Fight.fight(michal, orc, player_sack)
print(player_sack.check_gold_in_sack())"""

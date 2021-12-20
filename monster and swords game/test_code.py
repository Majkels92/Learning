from monster import *

michal = Creature(name="Michal Skowronski")  # creates player
michal.weapon = Weapons(20, 2.0)  # adds weapon for player
player_sack = GoldSack(michal)
orc = EasyMonster()  # creates monster
Fight.fight(michal, orc, player_sack)
print(player_sack.check_gold_in_sack())

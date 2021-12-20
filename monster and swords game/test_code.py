from monster import *

michal = Creature(name="Michal Skowronski")
michal.weapon = Weapons(20, 2.0)
orc = EasyMonster()
Fight.fight(michal, orc)

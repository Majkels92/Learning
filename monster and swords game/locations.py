import characters
import mysql.connector
import sys
sys.path.insert(0, './database_mysql')
from database_mysql import db_get_data, db_login_data


mydb = mysql.connector.connect(
    host=db_login_data.host,
    user=db_login_data.user,
    password=db_login_data.password,
    database=db_login_data.database
)


class MarhabaDesert:
    @staticmethod
    def entrance_description():
        print("""You enter area where You can only see sand and sand dunes, the sky is clear but it's terribly hot,
        you are sweating and thinking 'why would I ever come to this sandy hell'...""")


class Forest:
    @staticmethod
    def entrance_description():
        print("""Pleasant wind is blowing, You hear birds singing and trees cracking while moving from left to right,
        unfortunately despite of friendly atmosphere you can feel it in the air, that something is wrong with
        this forest...""")


class DarkCave:
    @staticmethod
    def entrance_description():
        print("""The cave with barely visible entrance, looks very interesting. Probably long time nobody seen what is
        inside. It's solid location to start searching some undiscovered treasures...but is it safe? You can sense 
        there is for sure a reason why nobody wants to explore this place. """)


class Camp:
    @staticmethod
    def entrance_description():
        print("""You have returned to safe camp where u can finally rest from everyday struggle of adventurer! """)


class LocationPaths:

    @staticmethod
    def easy_encounter():
        dr = db_get_data.draw_enemy(1)     # dr as draw result
        print(f"You enforced {dr[1]} let's KILL HIM!")
        mw = db_get_data.get_weapon_stats(dr[2])     # mw as monster weapon
        enemy = characters.Monster(dr[1], mw[1], float(mw[2]), dr[3], dr[4], dr[5], dr[6], dr[7])
        return enemy

    @staticmethod
    def medium_encounter():
        dr = db_get_data.draw_enemy(2)     # dr as draw result
        print(f"You enforced {dr[1]} let's KILL HIM!")
        mw = db_get_data.get_weapon_stats(dr[2])     # mw as monster weapon
        enemy = characters.Monster(dr[1], mw[1], float(mw[2]), dr[3], dr[4], dr[5], dr[6], dr[7])
        return enemy

    @staticmethod
    def hard_encounter():
        dr = db_get_data.draw_enemy(3)     # dr as draw result
        print(f"You enforced {dr[1]} let's KILL HIM!")
        mw = db_get_data.get_weapon_stats(dr[2])     # mw as monster weapon
        enemy = characters.Monster(dr[1], mw[1], float(mw[2]), dr[3], dr[4], dr[5], dr[6], dr[7])
        return enemy


import mysql.connector
import db_login_data
import random

mydb = mysql.connector.connect(
    host=db_login_data.host,
    user=db_login_data.user,
    password=db_login_data.password,
    database=db_login_data.database
)


def draw_enemy(difficulty):
    """Choose difficulty of monster 1 - easy, 2 - medium, 3 - hard and draw a monster from database"""
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM monsters WHERE difficulty={difficulty}")
    myresult = mycursor.fetchall()
    draw_result = random.choices(myresult)
    return draw_result[0]

def get_weapon_stats(id):
    myc = mydb.cursor()
    myc.execute(f"SELECT * FROM weapons WHERE id_weapon={id}")
    myresult = myc.fetchall()
    weapon = random.choices(myresult)
    return weapon[0]

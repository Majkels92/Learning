import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5699998",
    database="monsters_and_swords_game_db"
)

cursor = mydb.cursor()

# CREATING TABLE
try:
    cursor.execute("""CREATE TABLE monsters
    (id_monster INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(55) NOT NULL,
    id_weapon INT NOT NULL,
    CONSTRAINT weapons_id_weapon_fk
    FOREIGN KEY (id_weapon)
    REFERENCES weapons(id_weapon),
    gold_drop INT NOT NULL,
    gained_experience INT NOT NULL,
    chest_drop INT,
    hp INT NOT NULL,
    strength INT NOT NULL)""")
except:  # IF EXISTS SHOW TABLES IN DB
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)


import mysql.connector
import db_login_data

mydb = mysql.connector.connect(
    host=db_login_data.host,
    user=db_login_data.user,
    password=db_login_data.password,
    database=db_login_data.database
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

cursor.execute("SELECT * FROM monsters")
my_results = cursor.fetchall()

if my_results is None:
    # inserting data
    columns = "name, id_weapon, gold_drop, gained_experience, chest_drop, hp, strength, difficulty"
    sql = f"INSERT INTO monsters ({columns}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = [("Orc", 2, 30, 400, 1, 60, 4, 1),
           ("Goblin", 1, 30, 400, 1, 50, 4, 1),
           ("Wolf", 1, 30, 400, 1, 70, 4, 1),
           ("Cave Orc", 3, 500, 1, 100, 7, 2),
           ("Cave Troll", 5, 1000, 2, 200, 10, 3),
           ("Skeleton", 1, 30, 400, 1, 50, 4, 1),
           ("Orc Captain", 3, 100, 900, 2, 100, 7, 2),
           ("Orc Chef", 12, 1000, 4000, 3, 250, 12, 3),
           ("Black Goblin", 3, 100, 600, 2, 120, 7, 2),
           ("Mutant", 2, 30, 600, 2, 50, 5, 1),
           ("Ugly Mutant", 4, 50, 900, 2, 100, 10, 2),
           ("Mutant Alpha", 6, 100, 6000, 3, 150, 15, 3),
           ("Big Skeleton", 3, 100, 800, 2, 70, 6, 2),
           ("Wraith", 2, 30, 600, None, 50, 3, 1),
           ("Tiger", 2, 30, 600, None, 50, 3, 1),
           ("Eagle", 2, 30, 600, None, 50, 3, 1),
           ("Goblin Chef", 12, 6500, 3, 250, 12, 3),
           ("Bandit", 1, 40, 600, 2, 100, 4, 1),
           ("Bandit Captain", 3, 50, 1200, 3, 150, 8, 2)]
    cursor.executemany(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
else:
    for i in my_results:
        print(i)

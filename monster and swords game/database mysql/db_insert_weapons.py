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
    cursor.execute("""CREATE TABLE weapons
     (id_weapon INT AUTO_INCREMENT PRIMARY KEY,
     damage INT NOT NULL,
     attack_speed DEC(2,1) NOT NULL)""")
except:
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)

cursor.execute("SELECT * FROM weapons")
my_results = cursor.fetchall()

if my_results is None:
    # inserting data
    sql = "INSERT INTO weapons (damage, attack_speed) VALUES (%s, %s)"
    val = [(4, 1.0), (6, 1.0), (8, 1.0), (10, 1.0), (12, 1.0), (14, 1.0),
           (4, 1.5), (6, 1.5), (8, 1.5), (10, 1.5), (12, 1.5), (14, 1.5),
           (4, 2.0), (6, 2.0), (8, 2.0), (10, 2.0), (12, 2.0), (14, 2.0)]
    cursor.executemany(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
else:
    for i in my_results:
        print(i)


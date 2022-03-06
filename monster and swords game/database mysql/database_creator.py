import mysql.connector
import db_login_data

mydb = mysql.connector.connect(
    host=db_login_data.host,
    user=db_login_data.user,
    password=db_login_data.password
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE monsters_and_swords_game_db")
except mysql.connector.errors.DatabaseError:
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

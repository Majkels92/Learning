import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="5699998"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE monsters_and_swords_game_db")
except mysql.connector.errors.DatabaseError:
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

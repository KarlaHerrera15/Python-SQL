"""
PREP C: Stampa tutti gli animali presenti.
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="pythonuser", password="password123", database="Animali")
cursor = mydb.cursor()

cursor.execute("SELECT * FROM Mammiferi")
for animale in cursor.fetchall():
    print(animale)
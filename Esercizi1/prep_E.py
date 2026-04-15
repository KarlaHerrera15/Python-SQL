"""
PREP E: Visualizza solo animali con peso > 2.
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="pythonuser", password="password123", database="Animali")
cursor = mydb.cursor()

cursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2")
for x in cursor.fetchall():
    print(x)
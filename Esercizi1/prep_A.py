"""
PREP A: Creazione del database 'Animali' e della tabella 'Mammiferi'.
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="pythonuser", password="password123")
cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
cursor.execute("USE Animali")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Mammiferi (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Nome_Proprio VARCHAR(255),
        Razza VARCHAR(255),
        Peso INT,
        Eta INT
    )
""")
print("Database e Tabella creati correttamente.")
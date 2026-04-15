"""
PREP B: Inserimento di 5 record predefiniti.
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="pythonuser", password="password123", database="Animali")
cursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
valori = [
    ('Fido', 'Pastore Tedesco', 30, 5),
    ('Micia', 'Siamese', 4, 3),
    ('Dumbo', 'Elefante', 3000, 10),
    ('Jerry', 'Topo', 1, 1),
    ('Leo', 'Leone', 190, 7)
]

cursor.executemany(sql, valori)
mydb.commit()
print(f"Inseriti {cursor.rowcount} animali.")
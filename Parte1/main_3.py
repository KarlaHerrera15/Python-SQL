"""
ESERCIZIO 3: Inserimento Dati
Inseriamo un record specifico nella tabella 'customers'.
Viene utilizzato mydb.commit() per confermare la transazione.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

# Conferma l'inserimento nel database
mydb.commit()

print(f"Record inserito correttamente. ID assegnato: {mycursor.lastrowid}")

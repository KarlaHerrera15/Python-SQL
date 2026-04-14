"""
ESERCIZIO 2: Creazione della Tabella
Qui specifichiamo anche il database 'mydatabase' nella connessione.
Creiamo una tabella 'customers' con ID, nome e indirizzo.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Creazione tabella
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

print("Tabella 'customers' creata con successo!")
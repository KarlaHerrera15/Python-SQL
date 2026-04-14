"""
ESERCIZIO 4: Visualizzazione Dati
Eseguiamo una query SELECT per recuperare tutti i dati dalla tabella
e li stampiamo riga per riga nel terminale.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

print("Dati presenti nella tabella 'customers':")
for x in myresult:
  print(x)
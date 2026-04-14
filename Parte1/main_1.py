"""
ESERCIZIO 1: Creazione del Database
Questo script si connette al server locale MariaDB utilizzando le credenziali 
specificate e crea un nuovo database chiamato 'mydatabase'.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)

mycursor = mydb.cursor()

# Creazione del database
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

print("Database 'mydatabase' creato con successo!")
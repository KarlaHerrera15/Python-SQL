"""
PREP F - OPZIONE 1: 
Chiede all'inizio all'utente quanti animali vuole inserire.
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="pythonuser", 
    password="password123", 
    database="Animali"
)
cursor = mydb.cursor()

try:
    quanti = int(input("Quanti animali vuoi inserire? "))
    
    for i in range(quanti):
        print(f"\nInserimento animale n. {i+1}")
        nome = input("Nome Proprio: ")
        razza = input("Razza: ")
        
        try:
            peso = int(input("Peso (kg): "))
            eta = int(input("Età: "))
            
            sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nome, razza, peso, eta))
            mydb.commit()
            print("Animale salvato correttamente!")
            
        except ValueError:
            print("ERRORE: Peso ed Età devono essere numeri interi. Salto questo inserimento.")
            
except ValueError:
    print("ERRORE: Devi inserire un numero valido per la quantità.")


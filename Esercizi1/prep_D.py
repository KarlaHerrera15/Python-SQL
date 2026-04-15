"""
PREP D: Chiede all'utente di inserire 5 animali con verifica degli interi.
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="pythonuser", password="password123", database="Animali")
cursor = mydb.cursor()

for i in range(5):
    print(f"\nInserimento animale n. {i+1}")
    nome = input("Nome: ")
    razza = input("Razza: ")
    
    try:
        peso = int(input("Peso (int): "))
        eta = int(input("Età (int): "))
        
        sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, razza, peso, eta))
        mydb.commit()
        print("Animale salvato!")
    except ValueError:
        print("ERRORE: Peso ed Età devono essere numeri interi! Inserimento annullato.")
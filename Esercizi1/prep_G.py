import mysql.connector

def connetti():
    return mysql.connector.connect(host="localhost", user="pythonuser", password="password123", database="Animali")

def menu():
    while True:
        print("\n--- MENU ANIMALI ---")
        print("1. Inserisci nuovo animale")
        print("2. Visualizza tutti")
        print("3. Elimina animale (per ID)")
        print("4. Modifica animale (per ID)")
        print("0. Esci")
        
        scelta = input("Scegli: ")
        db = connetti()
        cursor = db.cursor()

        if scelta == "1":
            n = input("Nome: "); r = input("Razza: "); p = int(input("Peso: ")); e = int(input("Età: "))
            cursor.execute("INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)", (n, r, p, e))
            db.commit()
        
        elif scelta == "2":
            cursor.execute("SELECT * FROM Mammiferi")
            for x in cursor.fetchall(): print(x)
            
        elif scelta == "3":
            id_del = input("ID da eliminare: ")
            cursor.execute("DELETE FROM Mammiferi WHERE id = %s", (id_del,))
            db.commit()
            print("Eliminato.")

        elif scelta == "4":
            id_mod = input("ID da modificare: ")
            n = input("Nuovo Nome: "); r = input("Nuova Razza: "); p = int(input("Nuovo Peso: ")); e = int(input("Nuova Età: "))
            cursor.execute("UPDATE Mammiferi SET Nome_Proprio=%s, Razza=%s, Peso=%s, Eta=%s WHERE id=%s", (n, r, p, e, id_mod))
            db.commit()
            print("Modificato.")

        elif scelta == "0":
            break
        db.close()

if __name__ == "__main__":
    menu()
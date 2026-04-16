import mysql.connector # Importa la libreria per connettersi a MariaDB
import pandas as pd    # Importa pandas per la gestione dei file CSV

# Stabilisce la connessione con il server database locale
db = mysql.connector.connect(
    host="localhost",      # Indirizzo del server (locale)
    user="pythonuser",     # Nome utente creato in precedenza
    password="password123" # Password dell'utente
)
cursor = db.cursor() # Crea un cursore per inviare i comandi SQL al database

# Invia il comando SQL per creare il database se non esiste già
cursor.execute("CREATE DATABASE IF NOT EXISTS DisneyDB")
# Indica al cursore di operare all'interno del database DisneyDB
cursor.execute("USE DisneyDB")

# Crea la tabella 'Titles' definendo i nomi delle colonne e i tipi di dati (VARCHAR, INT)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Titles (
        id_db INT AUTO_INCREMENT PRIMARY KEY, -- ID numerico che aumenta da solo
        show_id VARCHAR(10),                 -- ID originale del catalogo
        tipo VARCHAR(50),                    -- Specifica se Movie o TV Show
        titolo VARCHAR(255),                 -- Titolo dell'opera
        regista VARCHAR(255),                -- Nome del regista
        anno_uscita INT,                     -- Anno di pubblicazione
        classificazione VARCHAR(20),         -- Rating (es. PG, TV-G)
        durata VARCHAR(50),                  -- Durata in minuti o stagioni
        genere VARCHAR(255)                  -- Categorie (es. Animation, Family)
    )
""")

# Legge il file CSV e lo carica in un oggetto DataFrame di Pandas
df = pd.read_csv('disney_plus_titles.csv')
# Sostituisce i valori vuoti (NaN) con la stringa "Non disponibile" per evitare errori SQL
df = df.fillna("Non disponibile")

# Ciclo for che attraversa ogni riga del file CSV caricato
for index, row in df.iterrows():
    # Prepara la query SQL con i segnaposto %s per la sicurezza (evita SQL Injection)
    sql = """INSERT INTO Titles 
             (show_id, tipo, titolo, regista, anno_uscita, classificazione, durata, genere) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    # Crea una tupla con i valori della riga corrente presi dalle colonne del CSV
    val = (
        row['show_id'], 
        row['type'], 
        row['title'], 
        row['director'], 
        int(row['release_year']), 
        row['rating'], 
        row['duration'], 
        row['listed_in']
    )
    # Esegue l'inserimento nel database usando la query e i valori correnti
    cursor.execute(sql, val)

# Conferma definitivamente tutte le operazioni di inserimento (salvataggio)
db.commit()
# Stampa un messaggio di conferma nel terminale
print(f"✅ Successo! Caricati {len(df)} titoli Disney+.")
# Chiude la connessione al database per liberare risorse
db.close()
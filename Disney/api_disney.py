from flask import Flask, jsonify # Importa il framework Flask e la funzione per i JSON
from flask_cors import CORS      # Importa l'estensione per gestire i permessi Cross-Origin
import mysql.connector           # Importa il connettore per il database

app = Flask(__name__) # Crea l'istanza dell'applicazione Flask
CORS(app)             # Abilita CORS per permettere a frontend (Angular) di chiamare l'API

# Funzione riutilizzabile per connettersi al database ad ogni richiesta
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",      # Indirizzo server
        user="pythonuser",     # Utente DB
        password="password123", # Password DB
        database="DisneyDB"    # Database specifico da usare
    )

# Definisce la rotta principale (Home Page)
@app.route("/")
def home():
    # Ritorna una semplice stringa di testo come benvenuto
    return "🏰 Disney+ Catalog API pronta!"

# Rotta per ottenere tutti i titoli (All)
@app.route("/all")
def get_all():
    conn = get_db_connection()            # Apre la connessione
    cursor = conn.cursor(dictionary=True) # Crea un cursore che restituisce dizionari (JSON ready)
    cursor.execute("SELECT * FROM Titles") # Esegue la query per prendere tutto
    risultato = cursor.fetchall()         # Recupera tutti i record trovati
    conn.close()                          # Chiude la connessione
    return jsonify(risultato)             # Trasforma la lista di dizionari in formato JSON

# Rotta filtrata solo per i Film
@app.route("/movies")
def get_movies():
    conn = get_db_connection()            # Apre la connessione
    cursor = conn.cursor(dictionary=True) # Crea il cursore dizionario
    # Filtra nel DB solo dove la colonna 'tipo' è uguale a 'Movie'
    cursor.execute("SELECT * FROM Titles WHERE tipo = 'Movie'")
    risultato = cursor.fetchall()         # Recupera i film
    conn.close()                          # Chiude la connessione
    return jsonify(risultato)             # Ritorna i film in JSON

# Rotta filtrata solo per le Serie TV
@app.route("/tv_shows")
def get_tv_shows():
    conn = get_db_connection()            # Apre la connessione
    cursor = conn.cursor(dictionary=True) 
    # Filtra nel DB solo dove la colonna 'tipo' è uguale a 'TV Show'
    cursor.execute("SELECT * FROM Titles WHERE tipo = 'TV Show'")
    risultato = cursor.fetchall()         # Recupera le serie
    conn.close()                          # Chiude la connessione
    return jsonify(risultato)             # Ritorna le serie in JSON

# Rotta per i titoli più recenti (dal 2021)
@app.route("/recent")
def get_recent():
    conn = get_db_connection()            # Apre la connessione
    cursor = conn.cursor(dictionary=True)
    # Filtra usando l'operatore matematico 'maggiore o uguale' sull'anno
    cursor.execute("SELECT * FROM Titles WHERE anno_uscita >= 2020")
    risultato = cursor.fetchall()         # Recupera i titoli recenti
    conn.close()                          # Chiude la connessione
    return jsonify(risultato)             # Ritorna i titoli recenti in JSON

# Punto di ingresso del programma
if __name__ == "__main__":
    # Avvia il server Flask con debug attivo (si riavvia da solo se modifichi il file)
    app.run(debug=True, port=5000)
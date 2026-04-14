from flask import Flask
from flask import send_file
import random
import json

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

with open('giocatori.json', 'r') as f:
    data = json.load(f)
    
# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"
    
# Annotation that allows the function to be hit at the specific URL (/books).
@app.route("/all")
# Generic Python functino that returns books.json
def all():
    return send_file('giocatori.json')

# Annotation that allows the function to be hit at the specific URL (/books).
@app.route("/random")
# Generic Python functino that returns books.json
def random_giocatori():
    random_giocatori = data['giocatori'][random.randrange(0, len(data['giocatori']))]
    print(random_giocatori)
    return random_giocatori
@app.route("/team/<string:abb>")
def get_by_team(abb):
    giocatori = carica_dati()
    
    # Cerchiamo tutti i giocatori che appartengono a quel team (es. HOU, WAS, LAL)
    # Trasformiamo tutto in maiuscolo per evitare errori di battitura
    risultati = [p for p in giocatori if p["team_abbreviation"].upper() == abb.upper()]
    
    if risultati:
        return jsonify(risultati)
    else:
        return jsonify({"errore": f"Nessun giocatore trovato per il team {abb}"}), 404
# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(debug=True)
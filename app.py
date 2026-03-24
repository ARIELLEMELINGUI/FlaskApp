from flask import Flask

app = Flask(__name__)

# --- CODE FONCTIONNEL (Mis en commentaire pour le test) ---
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
# ---------------------------------------------------------

# --- ERREUR VOLONTAIRE POUR LE TP ---
# On ajoute du texte n'importe où sans guillemets, 
# ce qui va causer une "SyntaxError" lors de l'étape 'Run tests'
Ceci est une erreur de syntaxe volontaire pour tester le blocage du pipeline !
import pytest
from app import app 

def test_index():
    # On crée un client de test pour simuler un navigateur
    tester = app.test_client()
    # On fait une requête vers la racine '/'
    response = tester.get('/')
    
    # On vérifie que le serveur répond 200 (OK)
    assert response.status_code == 200
    # On vérifie que le message "Hello, World!" est bien présent
    assert b"Hello, World!" in response.data
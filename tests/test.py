from flask import json
import pytest
from app import create_app


@pytest.fixture(scope="session", autouse=True)
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()



def test_transaction_sucess(client):
    data = {
        "amount": 1.0,
        "sender": 1,
        "recieve": 2
    }

    response = client.post('/transfer', json=data)
    assert response.status_code == 200
    result = json.loads(response.data.decode('utf-8'))
    assert result["message"] == 'Transação feita com sucesso'
    
def test_transaction_fail(client):

    data = {
        "amount": 10000000000000000000000000000000000000000.0,
        "sender": 1,
        "recieve": 2
    }

    response = client.post('/transfer', json=data)
    assert response.status_code == 400
    result = json.loads(response.data.decode('utf-8'))
    assert result["message"] == 'Saldo insuficiente para transação'
    

def test_user_erro(client):
    data = {
        "name": "Test",
        "cpf": "14725836903",
        "email": "test@example.com",
        "pass": "pass",
        "type": "COMMON",
        "balance": 0.20
    }

    response = client.post('/user', json=data)
    assert response.status_code == 500
    result = json.loads(response.data.decode('utf-8'))
    assert result["message"] == 'Erro ao criar usuário'


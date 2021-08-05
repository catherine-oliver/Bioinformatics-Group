import os
import pytest
from api import create_app
from flask import json
from dotenv import load_dotenv

@pytest.fixture
def client():
    load_dotenv('.env.test') 
    app = create_app()

    with app.test_client() as client:
        yield client

# Helper Functions
def getData(client, data):
    return client.get('/api/getVaccineData', query_string=data)

def login(client, data):
    return client.post('/api/login', data=data)

def getCard(client, data):
    return client.get('/api/getCard', query_string=data)


# Test cases
def test_get_state(client):
    data = {'state': 'NE', 'vaxType': 'All', 'ages': 'None'}
    response = getData(client, data)
    resdata = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert resdata[0] == 1892114

def test_get_state_age(client):
    data = {'state': 'NE', 'vaxType': 'All', 'ages': '12-17'}
    response = getData(client, data)
    resdata = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert resdata[0] == 1892114
    assert resdata[1] == 1891835

def test_get_state_age_vax(client):
    data = {'state': 'NE', 'vaxType': 'Moderna', 'ages': '12-17'}
    response = getData(client, data)
    resdata = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert resdata[0] == 1892114
    assert resdata[1] == 1891835
    assert resdata[2] == 748709
    
def test_valid_login(client):
    data = {'username': 'testUser', 'password': 'testPass'}
    response = login(client, data)

    assert response.status_code == 201

def test_invalid_username(client):
    data = {'username': 'invalid', 'password': 'testPass'}
    response = login(client, data)

    assert response.status_code == 401

def test_invalid_password(client):
    data = {'username': 'testUser', 'password': 'invalid'}
    response = login(client, data)

    assert response.status_code == 401

def test_getCard_noLogin(client):
    data = {'x-access-token': '', 'username': '', 'userId': ''}
    response = getCard(client, data)

    assert response.status_code == 400

def test_getCard_invalidToken(client):
    data = {'x-access-token': 'invalidToken', 'username': 'testPass', 'userId': '13'}
    response = getCard(client, data)

    assert response.status_code == 400
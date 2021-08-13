"""
@package API test

Tests the API.

Dependencies:
 - Flask
 - Pytest
 - Dotenv
"""
import os
import pytest
from api import create_app
from flask import json
from dotenv import load_dotenv

@pytest.fixture
def client():
    """Creates the API client to be used.

    @return the test_client() module of the API
    """
    load_dotenv('.env.test') 
    app = create_app()

    with app.test_client() as client:
        yield client

# Helper Functions
def getData(client, data):
    """A helper function for getVaccineData() tests

    @param client - the api client being tested
    @param data - the data to be passed as the query string
    @return the data retrieved
    """
    return client.get('/api/getVaccineData', query_string=data)

def login(client, data):
    """A helper function for the login() tests

    @param client - the api client being tested
    @param data - the username and password used to login
    @return the HTTP status and token
    """
    return client.post('/api/login', data=data)

def getCard(client, data):
    """A helper function for the getCard() tests

    @param client - the api client being tested
    @param data - the authenication header being tested
    @return the HTTP status of the authentication and the image data
    """
    return client.get('/api/getCard', query_string=data)


# Test cases
def test_get_state(client):
    """Tests whether the getVaccineData() API hook works when passed a state.
    @param client - the api client being tested
    """
    data = {'state': 'NE', 'vaxType': 'All', 'ages': 'None'}
    response = getData(client, data)
    resdata = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert resdata[0] == 1892114

def test_get_state_age(client):
    """Tests whether the getVaccineData() API hook works when passed a state and age group
    @param client - the api client being tested
    """
    data = {'state': 'NE', 'vaxType': 'All', 'ages': '12-17'}
    response = getData(client, data)
    resdata = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert resdata[0] == 1892114
    assert resdata[1] == 1891835

def test_get_state_age_vax(client):
    """Tests whether the getVaccineData() API hook works when passed a state, age group, and vaccine type.
    @param client - the api client being tested
    """
    data = {'state': 'NE', 'vaxType': 'Moderna', 'ages': '12-17'}
    response = getData(client, data)
    resdata = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert resdata[0] == 1892114
    assert resdata[1] == 1891835
    assert resdata[2] == 748709

def test_get_null_data(client):
    """Tests whether the getVaccineData() API converts Null data to "Unreported".
    @param client - the api client being tested
    """
    data = {'state': 'testNull', 'vaxType': 'All', 'ages': '12-17'}
    response = getData(client, data)
    resdata = json.loads(response.get_data(as_text = True))

    print(resdata)
    assert resdata[0] == "Unreported"
    
def test_valid_login(client):
    """Tests whether the login() API hook works given a valid user
    @param client - the api client being tested
    """
    data = {'username': 'testUser', 'password': 'testPass'}
    response = login(client, data)

    assert response.status_code == 201

def test_invalid_username(client):
    """Tests whether the login() API hook returns an error status when given an invalid username
    @param client - the api client being tested
    """
    data = {'username': 'invalid', 'password': 'testPass'}
    response = login(client, data)

    assert response.status_code == 401

def test_invalid_password(client):
    """Tests whether the login() API hook returns an error status when given a valid username and invalid password
    @param client - the api client being tested
    """
    data = {'username': 'testUser', 'password': 'invalid'}
    response = login(client, data)

    assert response.status_code == 401

def test_getCard_noLogin(client):
    """Tests whether the getCard() API hook returns an error status when given no authentication data
    @param client - the api client being tested
    """
    data = {'x-access-token': '', 'username': '', 'userId': ''}
    response = getCard(client, data)

    assert response.status_code == 400

def test_getCard_invalidToken(client):
    """Tests whether the getCard() API hook returns an error status when given an invalid token but valid user data
    @param client - the api client being tested
    """
    data = {'x-access-token': 'invalidToken', 'username': 'testPass', 'userId': '13'}
    response = getCard(client, data)

    assert response.status_code == 400
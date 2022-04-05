import os
import tempfile
import pytest

from api import app

@pytest.fixture
def client():

    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_index_get(client):

    response = client.get('/')

    assert response.status_code == 200
    assert response.json['greeting'] == 'Hello, DevGrid!'


def test_weather_list_empty_get(client):

    response = client.get('/temperature')

    assert response.status_code == 404
    assert response.json['message'] == 'Weather list not found'


def test_weather_get(client):

    response = client.get('/temperature/Sao Paulo') # without accents

    assert response.status_code == 200    
    assert type(response.json['min']) == float
    assert type(response.json['max']) == float
    assert type(response.json['avg']) == float
    assert type(response.json['feels_like']) == float
    assert response.json['city'] == 'São Paulo'
    assert response.json['country'] == 'BR'

    response = client.get('temperature/toronto') # with lowercase letters

    assert response.status_code == 200    
    assert type(response.json['min']) == float
    assert type(response.json['max']) == float
    assert type(response.json['avg']) == float
    assert type(response.json['feels_like']) == float
    assert response.json['city'] == 'Toronto'
    assert response.json['country'] == 'CA'

    response = client.get('temperature/lonfoodonbar') # with wrong city name

    assert response.status_code == 404
    assert response.json['message'] == 'Weather not found'


def test_weather_list_get(client):

    client.get('/temperature/Toronto')
    client.get('/temperature/Amsterdam')
    client.get('/temperature/Berlin')
    client.get('/temperature/Oslo')

    response = client.get('/temperature')

    assert response.status_code == 200
    assert len(response.json) == 5
    assert response.json[0]['city'] == 'Oslo'
    assert response.json[4]['city'] == 'London'

    response = client.get('/temperature?max=3')

    assert len(response.json) == 3


def test_weather_list_with_invalid_params_get(client):

    response = client.get('/temperature?max=-3')

    assert response.status_code == 400
    assert response.json['message'] == 'The \'max\' attribute must be a positive integer between 1 and 5. Example: 4'

    response = client.get('/temperature?max=0')

    assert response.status_code == 400
    assert response.json['message'] == 'The \'max\' attribute must be a positive integer between 1 and 5. Example: 4'

    response = client.get('/temperature?max=6')

    assert response.status_code == 400
    assert response.json['message'] == 'The \'max\' attribute must be a positive integer between 1 and 5. Example: 4'

    response = client.get('/temperature?max=foo')

    assert response.status_code == 400
    assert response.json['message'] == 'The \'max\' attribute must be a positive integer between 1 and 5. Example: 4'

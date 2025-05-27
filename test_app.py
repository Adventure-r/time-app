import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_time_endpoint_exists(client):
    """Тест проверяет, что endpoint /time существует"""
    response = client.get('/time')
    assert response.status_code == 200

def test_time_endpoint_returns_json(client):
    """Тест проверяет, что endpoint возвращает JSON"""
    response = client.get('/time')
    assert response.content_type == 'application/json'

def test_time_endpoint_structure(client):
    """Тест проверяет структуру ответа"""
    response = client.get('/time')
    data = json.loads(response.data)
    assert 'time' in data
    assert isinstance(data['time'], int)

def test_time_not_zero(client):
    """Тест проверяет, что время не равно 0"""
    response = client.get('/time')
    data = json.loads(response.data)
    assert data['time'] != 0
    assert data['time'] > 0

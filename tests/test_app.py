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

def test_metrics_endpoint_exists(client):
    """Тест проверяет, что endpoint /metrics существует"""
    response = client.get('/metrics')
    assert response.status_code == 200

def test_metrics_endpoint_returns_json(client):
    """Тест проверяет, что endpoint возвращает JSON"""
    response = client.get('/metrics')
    assert response.content_type == 'application/json'

def test_metrics_structure(client):
    """Тест проверяет структуру ответа /metrics"""
    response = client.get('/metrics')
    data = json.loads(response.data)
    assert 'count' in data
    assert isinstance(data['count'], int)

def test_metrics_counting(client):
    """Тест проверяет правильность подсчета запросов"""
    # Получаем начальное значение
    initial_response = client.get('/metrics')
    initial_data = json.loads(initial_response.data)
    initial_count = initial_data['count']

    # Делаем запрос к /time
    client.get('/time')

    # Проверяем, что счетчик увеличился
    final_response = client.get('/metrics')
    final_data = json.loads(final_response.data)
    assert final_data['count'] == initial_count + 1

def test_metrics_multiple_requests(client):
    """Тест проверяет подсчет множественных запросов"""
    initial_response = client.get('/metrics')
    initial_count = json.loads(initial_response.data)['count']

    # Делаем несколько запросов
    for _ in range(3):
        client.get('/time')

    final_response = client.get('/metrics')
    final_count = json.loads(final_response.data)['count']
    assert final_count == initial_count + 3

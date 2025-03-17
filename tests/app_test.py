from fastapi.testclient import TestClient
import sys
print(sys.path)
from src.app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")  # Добавлен запрос
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_calculate_endpoint_valid_input():
    response = client.get("/calculate/5/3")  # Добавлен запрос
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_calculate_endpoint_invalid_input():
    response = client.get("/calculate/5/abc")
    assert response.status_code == 422


def test_calculate_endpoint_with_zero():
    response = client.get("/calculate/5/0")  # Добавлен запрос
    assert response.status_code == 200
    assert response.json() == {"result": 5}
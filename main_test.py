import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/roleUsers/ybFpVWSJpDi9IWO')
    assert response.status_code == 200

def test_204():
    response = client.get('/roleUsers/error')
    assert response.status_code == 204
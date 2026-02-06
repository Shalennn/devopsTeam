import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test que /health retourne 200 [cite: 55]
def test_health_check(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    assert response.json == {"status": "OK", "version": "1.0"}

# Test que /servers retourne la liste [cite: 56]
def test_get_servers(client):
    response = client.get('/api/v1/servers')
    assert response.status_code == 200
    assert "servers" in response.json
    assert response.json["count"] == 2

# Test que /servers/1 retourne le bon serveur [cite: 57]
def test_get_server_by_id(client):
    response = client.get('/api/v1/servers/1')
    assert response.status_code == 200
    assert response.json["hostname"] == "web-prod-01"

# Test que /servers/999 retourne 404 [cite: 58]
def test_get_server_not_found(client):
    response = client.get('/api/v1/servers/999')
    assert response.status_code == 404
    assert response.json["error"] == "Server not found"
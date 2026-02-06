import pytest
from app.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_servers_list():
    client = app.test_client()
    response = client.get("/api/v1/servers")
    assert response.status_code == 200
    assert response.json["count"] == 2


def test_server_by_id_ok():
    client = app.test_client()
    response = client.get("/api/v1/servers/1")
    assert response.status_code == 200
    assert response.json["hostname"] == "web-prod-01"


def test_server_by_id_not_found():
    client = app.test_client()
    response = client.get("/api/v1/servers/999")
    assert response.status_code == 404

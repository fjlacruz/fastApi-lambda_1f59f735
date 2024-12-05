from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser", "email": "test@example.com"}

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "sample_user", "email": "sample@example.com"}

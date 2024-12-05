from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Item", "description": "Test Description"}

def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Sample Item", "description": "This is a sample item."}

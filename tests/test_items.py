from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Item1", "description": "Description1"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item1", "description": "Description1"}

def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Sample Item", "description": "This is a sample item."}

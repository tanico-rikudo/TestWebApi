from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_item():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query": "test"}

def test_create_item():
    response = client.post("/items/", params={"name": "apple", "price": 10.5})
    assert response.status_code == 200
    assert response.json() == {"name": "apple", "price": 10.5}

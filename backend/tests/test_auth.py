from fastapi.testclient import TestClient
from main import app
from database import get_db
from models import User
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def cleanup_db(db: Session = next(get_db())):
    db.query(User).delete()
    db.commit()

def test_user_registration():
    response = client.post(
        "/auth/signup",
        json={"email": "test@example.com", "password": "secure123"}
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["email"] == "test@example.com"

def test_duplicate_registration():
    client.post("/auth/signup", json={"email": "dup@test.com", "password": "pass"})
    response = client.post("/auth/signup", json={"email": "dup@test.com", "password": "pass"})
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"]

def test_protected_endpoint_access():
    # Test without token
    response = client.get("/researchers/")
    assert response.status_code == 401

    # Get valid token
    client.post("/auth/signup", json={"email": "auth_test@ex.com", "password": "pass"})
    login = client.post("/auth/login", data={"username": "auth_test@ex.com", "password": "pass"})
    token = login.json()["access_token"]
    
    # Test with token
    response = client.get("/researchers/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

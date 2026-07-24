import pytest
from fastapi.testclient import TestClient
from main import app
from database import get_db
from models import User, Researcher, Prediction
import joblib
import numpy as np

client = TestClient(app)

@pytest.fixture(autouse=True)
def override_dependencies():
    # Mock ML model and preprocessor
    mock_model = joblib.load('ml_model/model.joblib')
    mock_preprocessor = joblibPreprocessor()
    
    app.dependency_overrides[get_db] = lambda: next(get_db())
    app.state.model = mock_model
    app.state.preprocessor = mock_preprocessor
    yield
    app.dependency_overrides.clear()

@pytest.fixture
def auth_header():
    # Create test user and get token
    client.post("/auth/signup", json={"email": "test@example.com", "password": "test123"})
    response = client.post("/auth/login", data={"username": "test@example.com", "password": "test123"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_full_prediction_flow(auth_header):
    # Create researcher
    researcher_data = {
        "name": "Dr. Alice Smith",
        "institution": "MIT",
        "start_year": 2020,
        "research_area": "NLP"
    }
    create_res = client.post("/researchers/", json=researcher_data, headers=auth_header)
    assert create_res.status_code == 200
    researcher_id = create_res.json()["id"]

    # Make prediction
    prediction_data = {
        "researcher_id": researcher_id,
        "citation_count": 150,
        "h_index": 7,
        "years_since_first_pub": 3,
        "top_tier_conferences": 4,
        "grants_received": 2
    }
    pred_res = client.post("/predict/", json=prediction_data, headers=auth_header)
    assert pred_res.status_code == 200
    assert "probability" in pred_res.json()
    assert "feature_importances" in pred_res.json()

    # Verify prediction storage
    db = next(get_db())
    db_pred = db.query(Prediction).filter(Prediction.researcher_id == researcher_id).first()
    assert db_pred is not None
    assert 0 <= db_pred.probability <= 1

    # Check insights
    insights_res = client.get("/api/insights/diversity-metrics", headers=auth_header)
    assert insights_res.status_code == 200
    assert any(metric["metric"] == "Collaboration" for metric in insights_res.json())


def test_invalid_data_handling(auth_header):
    # Test missing required field
    invalid_data = {
        "citation_count": "invalid",
        "h_index": -5,
        "years_since_first_pub": 3
    }
    response = client.post("/predict/", json=invalid_data, headers=auth_header)
    assert response.status_code == 422
    errors = response.json()["detail"]
    assert any(e["loc"] == ["body", "citation_count"] for e in errors)
    assert any(e["msg"] == "ensure this value is greater than or equal to 0" for e in errors)


def test_unauthorized_access():
    # Attempt prediction without auth
    response = client.post("/predict/", json={"citation_count": 100})
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]

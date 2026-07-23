from fastapi.testclient import TestClient
from main import app
import joblib
import numpy as np

client = TestClient(app)

def test_prediction_endpoint(mocker):
    mock_model = mocker.Mock()
    mock_model.predict_proba.return_value = np.array([[0.2, 0.8]])
    mock_preprocessor = mocker.Mock()
    mock_preprocessor.transform.return_value = np.array([[1, 2, 3, 4, 5]])
    
    app.state.model = mock_model
    app.state.preprocessor = mock_preprocessor
    
    payload = {
        "citation_count": 150,
        "h_index": 7,
        "years_since_first_pub": 6,
        "top_tier_conferences": 3,
        "grants_received": 2
    }
    
    response = client.post("/predict/", json=payload)
    
    assert response.status_code == 200
    assert 0 <= response.json()["probability"] <= 1
    assert len(response.json()["feature_importances"]) == 5
    mock_preprocessor.transform.assert_called_once()

def test_invalid_prediction_input():
    response = client.post("/predict/", json={"invalid": "data"})
    assert response.status_code == 422

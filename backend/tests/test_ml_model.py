import pytest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from preprocessing import DataPreprocessor

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'citation_count': [0, 100, 500],
        'h_index': [0, 5, 10],
        'years_since_first_pub': [1, 5, 10],
        'top_tier_conferences': [0, 2, 5],
        'grants_received': [0, 1, 3]
    })

@pytest.fixture
def trained_model():
    model = RandomForestClassifier(n_estimators=10)
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    model.fit(X, y)
    return model

def test_preprocessing_pipeline(sample_data):
    preprocessor = DataPreprocessor()
    transformed = preprocessor.pipeline.fit_transform(sample_data)
    
    assert not np.isnan(transformed).any()
    assert transformed.shape == sample_data.shape
    assert np.allclose(transformed.mean(axis=0), 0, atol=1e-2)

def test_model_prediction(trained_model, sample_data):
    preprocessor = DataPreprocessor()
    processed_data = preprocessor.pipeline.fit_transform(sample_data)
    
    predictions = trained_model.predict_proba(processed_data)
    
    assert predictions.shape == (3, 2)
    assert np.all((predictions >= 0) & (predictions <= 1))

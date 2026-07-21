import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump
from feature_engineering import get_features
from preprocessing import DataPreprocessor
import os

def train_model():
    db_uri = os.getenv('DATABASE_URI', 'postgresql://user:password@db:5432/dbname')
    
    data = get_features(db_uri)
    
    if data.empty:
        raise ValueError("No data found for training")
    
    X = data[['early_publications_count', 'early_discipline_diversity', 'early_citation_sum']]
    y = data['h_index'] >= 15  # Simplified star scientist criteria

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Preprocess data
    preprocessor = DataPreprocessor()
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Train model
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))

    # Save artifacts
    dump(model, 'model.joblib')
    dump(preprocessor, 'preprocessor.joblib')

if __name__ == '__main__':
    train_model()
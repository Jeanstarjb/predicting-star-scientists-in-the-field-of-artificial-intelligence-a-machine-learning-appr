import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump
from feature_engineering import get_features
import os

def train_model():
    db_uri = os.getenv('DATABASE_URI', 'postgresql://user:password@db:5432/dbname')
    
    data = get_features(db_uri)
    
    if data.empty:
        raise ValueError("No data found for training")
    
    X = data[['early_publications_count', 'early_discipline_diversity', 'early_citation_sum']]
    y = data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
    print(classification_report(y_test, y_pred))
    
    dump(model, 'model.joblib')
    print("Model saved as model.joblib")

if __name__ == '__main__':
    train_model()
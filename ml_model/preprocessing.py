import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class DataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.pipeline = Pipeline([
            ('validation', FunctionTransformer(validate_input_data)),
            ('imputation', SimpleImputer(strategy='median')),
            ('log_transform', FunctionTransformer(np.log1p)),
            ('scaling', StandardScaler())
        ])

    def fit(self, X, y=None):
        self.pipeline.fit(X)
        return self

    def transform(self, X):
        return self.pipeline.transform(X)

def validate_input_data(X):
    if not isinstance(X, pd.DataFrame):
        X = pd.DataFrame(X)
    
    required_features = ['early_publications_count', 
                        'early_discipline_diversity', 
                        'early_citation_sum']
    
    for feat in required_features:
        if feat not in X.columns:
            raise ValueError(f"Missing required feature: {feat}")
        if X[feat].dtype not in [np.int64, np.float64]:
            raise ValueError(f"Invalid dtype for {feat}. Expected numeric type")
        
    X = X[(X['early_publications_count'] >= 0) &
          (X['early_discipline_diversity'] >= 0) &
          (X['early_citation_sum'] >= 0)]
    
    return X.replace([np.inf, -np.inf], np.nan)

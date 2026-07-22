import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

class DataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.pipeline = Pipeline([
            ('imputation', SimpleImputer(strategy='median')),
            ('log_transform', FunctionTransformer(np.log1p)),
            ('scaling', StandardScaler())
        ])

    def fit(self, X, y=None):
        self.pipeline.fit(X)
        return self

    def transform(self, X):
        return self.pipeline.transform(X)
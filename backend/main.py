from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib
from sqlalchemy.orm import Session
import datetime
from . import models, schemas, preprocessing
from .database import get_db
from .routers import researchers, publications, predictions

app = FastAPI()

try:
    model = joblib.load('model.joblib')
    preprocessor = preprocessing.DataPreprocessor()
except Exception as e:
    raise RuntimeError(f"Error loading model or preprocessor: {e}")

app.state.model = model
app.state.preprocessor = preprocessor

app.include_router(researchers.router)
app.include_router(publications.router)
app.include_router(predictions.router)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}